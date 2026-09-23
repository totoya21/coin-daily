# -*- coding: utf-8 -*-
"""
점수 계산 모듈
- 지표별 −2 ~ +2점 (+는 매수 우호)
- 그룹 점수 = 그룹 내 판정 가능 지표 평균 × 50 → −100 ~ +100
- 총점 = 그룹 점수 가중합 (판정 불가 그룹은 제외 후 가중치 재배분)
- 판정 = 3일 평균 총점의 구간, 같은 구간 2일 연속일 때만 변경
기준선을 바꾸려면 아래 각 함수의 숫자를, 가중치·구간은 config.json의 "scoring"을 수정한다.
"""
import datetime as dt

SRC = "점수 계산(coin_daily)"


def _num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


# ─────────── history.csv 헬퍼 ───────────
def _series(hist, key, today):
    """key의 날짜별 마지막 값 (오늘 제외)."""
    out = {}
    for h in hist:
        if h["key"] == key and h["status"] == "ok" and h["value"] not in ("", None):
            d = h["run_at"][:10]
            if d < today:
                out[d] = h["value"]
    return dict(sorted(out.items()))


def _days_ago(hist, key, today, n, slack=2):
    """n일 전(±slack일 이내 가장 가까운 과거) 값."""
    s = _series(hist, key, today)
    target = dt.date.fromisoformat(today) - dt.timedelta(days=n)
    for k in range(slack + 1):
        d = (target - dt.timedelta(days=k)).isoformat()
        if d in s:
            return _num(s[d])
    return None


def _pct(x, arr):
    arr = [a for a in arr if a is not None]
    return None if not arr or x is None else 100.0 * sum(a <= x for a in arr) / len(arr)


def _band_pct(p, high_is_bad=True):
    """분포 위치(백분위) → 점수."""
    if p is None:
        return None
    if not high_is_bad:
        p = 100 - p
    if p <= 10:
        return 2
    if p <= 30:
        return 1
    if p < 70:
        return 0
    if p < 90:
        return -1
    return -2


# ─────────── 지표별 채점 (점수, 근거) ───────────
def s_mvrv_z(v, h, t, cfg):
    x = v.get("mvrv_z")
    if x is None:
        return None, "값 없음"
    sc = 2 if x <= 0 else 1 if x < 1 else 0 if x < 3 else -1 if x < 5 else -2
    return sc, f"MVRV Z {x:.2f}"


def s_sth(v, h, t, cfg):
    x = v.get("sth_mvrv")  # = 가격 ÷ STH-RP
    if x is None:
        return None, "값 없음"
    sc = 2 if x < 0.85 else 1 if x < 1.0 else 0 if x < 1.15 else -1 if x < 1.3 else -2
    return sc, f"가격÷STH-RP {x:.3f}"


def s_etf(v, h, t, cfg):
    st, s5 = v.get("etf_streak"), v.get("etf_5d_sum")
    if st is None or s5 is None:
        return None, "값 없음"
    if st >= 3:
        return 2, f"{int(st)}거래일 연속 순유입"
    if st <= -3:
        return -2, f"{int(-st)}거래일 연속 순유출"
    sc = 1 if s5 > 0 else -1 if s5 < 0 else 0
    return sc, f"5일 합 {s5:+.0f}백만$"


def s_ex_net(v, h, t, cfg):
    p = v.get("ex_net_7d_pct")
    return (None, "값 없음") if p is None else (_band_pct(p, True), f"7일 순유입 분포 {p:.0f}백분위")


def s_ex_supply(v, h, t, cfg):
    x = v.get("ex_supply_30d_pct")
    if x is None:
        return None, "값 없음"
    sc = 1 if x <= -0.5 else -1 if x >= 0.5 else 0
    return sc, f"30일 {x:+.2f}% (±0.5% 미만은 0점)"


def s_whale(v, h, t, cfg):
    x = v.get("whale_ratio_proxy")
    if x is None:
        return None, "값 없음"
    past = [_num(y) for y in list(_series(h, "whale_ratio_proxy", t).values())[-89:]]
    need = cfg["scoring"].get("min_history_days", 30)
    if len(past) + 1 < need:
        return None, f"분포 기준선 수집 중 ({len(past) + 1}/{need}일)"
    p = _pct(x, past + [x])
    sc = _band_pct(p, True)
    sc = min(sc, 1)  # 고래비율은 낮다고 강한 매수 신호로 보지 않음 (최대 +1)
    return sc, f"{x:.3f}, 최근 {len(past) + 1}일 분포 {p:.0f}백분위"


def s_usdt_d(v, h, t, cfg):
    x, old = v.get("usdt_d"), _days_ago(h, "usdt_d", t, 7)
    if x is None or old is None:
        return None, "7일 전 값 없음" if x is not None else "값 없음"
    ch = (x / old - 1) * 100
    sc = 1 if ch <= -3 else -1 if ch >= 3 else 0
    return sc, f"7일 {ch:+.1f}% (±3% 미만은 0점)"


def s_funding(v, h, t, cfg):
    x = v.get("funding_avg3")
    if x is None:
        return None, "값 없음"
    sc = 2 if x < 0 else 1 if x < 0.01 else 0 if x < 0.03 else -1 if x < 0.05 else -2
    return sc, f"3회 평균 {x:.4f}%"


def s_rsi(v, h, t, cfg):
    x = v.get("rsi14")
    if x is None:
        return None, "값 없음"
    sc = 2 if x <= 30 else 1 if x < 40 else 0 if x <= 60 else -1 if x < 70 else -2
    return sc, f"RSI {x:.1f}"


def s_ls(v, h, t, cfg):
    p = v.get("ls_account_pct")
    return (None, "값 없음") if p is None else (_band_pct(p, True), f"롱/숏 분포 {p:.0f}백분위")


def s_oi(v, h, t, cfg):
    oi, pr = v.get("oi_7d_pct"), v.get("price_7d_pct")
    if oi is None or pr is None:
        return None, "값 없음"
    if oi >= 15 and abs(pr) <= 3:
        return -2, f"OI 7일 {oi:+.1f}% vs 가격 {pr:+.1f}% (레버리지 과열)"
    if oi <= -5 and pr < 0:
        return 1, f"OI 7일 {oi:+.1f}%, 가격 {pr:+.1f}% (레버리지 정리)"
    return 0, f"OI 7일 {oi:+.1f}%, 가격 {pr:+.1f}%"


def s_skew(v, h, t, cfg):
    x = v.get("skew25")
    if x is None:
        return None, "값 없음"
    s = _series(h, "skew25", t)
    prev = _num(list(s.values())[-1]) if s else None
    if x < 0:
        return 1, f"{x:+.2f} (콜 우위)"
    if prev is not None and x > 0 and x > prev:
        return -1, f"{x:+.2f} (풋 우위 확대, 전일 {prev:+.2f})"
    return 0, f"{x:+.2f}"


def s_nasdaq(v, h, t, cfg):
    x, ma, c5 = v.get("nasdaq"), v.get("nasdaq_ma50"), v.get("nasdaq_5d_pct")
    if x is None or ma is None:
        return None, "값 없음"
    if c5 is not None and c5 <= -5:
        return -2, f"5일 {c5:+.1f}% 급락"
    return (1, "50일선 위") if x > ma else (-1, "50일선 아래")


def s_dxy(v, h, t, cfg):
    x, c20 = v.get("dxy"), v.get("dxy_20d_pct")
    if x is None or c20 is None:
        return None, "값 없음"
    if c20 <= -2:
        return 2, f"{x:.2f}, 20일 {c20:+.1f}%"
    if x <= 99 and c20 < 0:
        return 1, f"{x:.2f} (99 이하 & 하락)"
    if c20 > 0:
        return -1, f"{x:.2f}, 20일 {c20:+.1f}% (상승)"
    return 0, f"{x:.2f}, 20일 {c20:+.1f}%"


def s_usdjpy(v, h, t, cfg):
    x, c5 = v.get("usdjpy"), v.get("usdjpy_5d_pct")
    if x is None or c5 is None:
        return None, "값 없음"
    if c5 <= -3:
        return -2, f"{x:.2f}, 5일 {c5:+.1f}% (엔 급강세)"
    return (1, f"{x:.2f} (156 이하)") if x <= 156 else (0, f"{x:.2f}")


def s_infl(v, h, t, cfg):
    x = v.get("infl_signal")
    if x is None:
        return None, "발표 후 30일 이내 지표 없음"
    return (1 if x > 0 else -1 if x < 0 else 0), f"둔화−재가속 합계 {x:+.0f}"


def s_fomc(v, h, t, cfg):
    x, old = v.get("pm_fomc"), _days_ago(h, "pm_fomc", t, 7)
    if x is None:
        return None, "FOMC 마켓 미설정 또는 값 없음"
    if old is None:
        return None, "7일 전 값 없음"
    d = x - old
    return (1 if d >= 10 else -1 if d <= -10 else 0), f"인하 확률 {x:.0f}% (7일 {d:+.0f}%p)"


INDICATORS = [
    ("밸류에이션", "mvrv_z", "MVRV Z", s_mvrv_z),
    ("밸류에이션", "sth", "가격÷STH-RP", s_sth),
    ("수급", "etf", "현물 ETF 순유입", s_etf),
    ("수급", "ex_net", "거래소 순유입(7일)", s_ex_net),
    ("수급", "ex_supply", "거래소 보유량(30일)", s_ex_supply),
    ("수급", "whale", "고래비율(근사)", s_whale),
    ("수급", "usdt_d", "테더 도미넌스(7일)", s_usdt_d),
    ("파생·심리", "funding", "펀딩비", s_funding),
    ("파생·심리", "rsi", "RSI(14)", s_rsi),
    ("파생·심리", "ls", "롱/숏 비율", s_ls),
    ("파생·심리", "oi", "미결제약정(OI)", s_oi),
    ("파생·심리", "skew", "옵션 스큐", s_skew),
    ("매크로", "nasdaq", "나스닥", s_nasdaq),
    ("매크로", "dxy", "DXY", s_dxy),
    ("매크로", "usdjpy", "USD/JPY", s_usdjpy),
    ("매크로", "infl", "CPI·PCE", s_infl),
    ("매크로", "fomc", "폴리마켓 금리인하", s_fomc),
]


def _band(x, bands):
    for lo, label, target in bands:
        if x >= lo:
            return label, target
    return bands[-1][1], bands[-1][2]


def compute(recs, hist, cfg, now_kst):
    sc_cfg = cfg["scoring"]
    today = now_kst.strftime("%Y-%m-%d")
    v = {r["key"]: _num(r["value"]) for r in recs if r["status"] == "ok" and _num(r["value"]) is not None}

    rows, groups = [], {}
    for g, key, name, fn in INDICATORS:
        try:
            sc, why = fn(v, hist, today, cfg)
        except Exception as e:
            sc, why = None, f"계산 오류: {e}"
        prev = _series(hist, f"score_ind_{key}", today)
        prev = _num(list(prev.values())[-1]) if prev else None
        rows.append({"group": g, "key": key, "name": name, "score": sc, "prev": prev, "why": why})
        if sc is not None:
            groups.setdefault(g, []).append(sc)

    gscore = {g: round(sum(s) / len(s) * 50, 1) for g, s in groups.items()}
    w = {g: sc_cfg["weights"][g] for g in gscore}
    total = round(sum(gscore[g] * w[g] for g in gscore) / sum(w.values()), 1) if w else None
    scored = sum(r["score"] is not None for r in rows)
    coverage = scored / len(rows)

    past_tot = [_num(x) for x in list(_series(hist, "score_total", today).values())[-2:]]
    avg3 = round(sum(past_tot + [total]) / (len(past_tot) + 1), 1) if total is not None else None

    prev_raw_s = _series(hist, "judgment_raw", today)
    prev_eff_s = _series(hist, "judgment", today)
    prev_raw = list(prev_raw_s.values())[-1] if prev_raw_s else None
    prev_eff = list(prev_eff_s.values())[-1] if prev_eff_s else None

    bands = sc_cfg["bands"]
    targets = {b[1]: b[2] for b in bands}
    notes = []
    raw = _band(avg3, bands)[0] if avg3 is not None else None
    if raw is None or coverage < sc_cfg["min_coverage"]:
        eff = prev_eff or "보류"
        notes.append(f"판정 가능 지표 {scored}/{len(rows)}개로 기준({sc_cfg['min_coverage']:.0%}) 미달 → 전일 판정 유지")
    elif prev_eff is None:
        eff = raw
    elif raw == prev_eff:
        eff = raw
    elif raw == prev_raw:
        eff = raw
        notes.append(f"'{raw}' 구간 2일 연속 → 판정 변경 ({prev_eff} → {raw})")
    else:
        eff = prev_eff
        notes.append(f"오늘 구간 '{raw}'는 첫날 → 내일도 같으면 변경, 오늘은 '{prev_eff}' 유지")

    target = targets.get(eff)
    guards = []
    mz, fund = v.get("mvrv_z"), next((r["score"] for r in rows if r["key"] == "funding"), None)
    if target is not None and mz is not None:
        fl, cp = sc_cfg["floor"], sc_cfg["cap"]
        if mz <= fl["mvrv_z_max"] and target < fl["target_min"]:
            target = fl["target_min"]
            guards.append(f"바닥권 보호: MVRV Z {mz:.2f} ≤ {fl['mvrv_z_max']} → 최소 {fl['target_min']}%")
        if mz >= cp["mvrv_z_min"] and fund == -2 and target > cp["target_max"]:
            target = cp["target_max"]
            guards.append(f"과열 차단: MVRV Z {mz:.2f} & 펀딩비 과열 → 최대 {cp['target_max']}%")

    as_of = today
    mk = lambda key, name, val, note="": {  # noqa: E731
        "group": "Z.점수", "key": key, "name": name, "value": val, "prev": None, "unit": "",
        "source": SRC, "api_url": "", "view_url": "", "data_as_of": as_of,
        "status": "ok" if val is not None else "fail", "note": note}
    records = [mk(f"score_ind_{r['key']}", f"점수: {r['name']}", r["score"], r["why"]) for r in rows]
    records += [mk(f"score_group_{g}", f"그룹 점수: {g}", s) for g, s in gscore.items()]
    records += [mk("score_total", "총점", total), mk("score_avg3", "3일 평균 총점", avg3),
                mk("score_coverage", "판정 가능 비율", round(coverage * 100, 1)),
                mk("judgment_raw", "오늘 구간", raw), mk("judgment", "판정", eff, " / ".join(notes)),
                mk("target", "BTC 목표 비중(%)", target, " / ".join(guards))]

    return {"rows": rows, "groups": gscore, "weights": sc_cfg["weights"], "total": total, "avg3": avg3,
            "coverage": coverage, "scored": scored, "n": len(rows), "raw": raw, "judgment": eff,
            "prev_judgment": prev_eff, "target": target, "notes": notes, "guards": guards,
            "records": records}


def render(s):
    f = lambda x: "—" if x is None else (f"{x:+.0f}" if isinstance(x, (int, float)) else x)  # noqa: E731
    L = ["## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)", "",
         f"- **판정: {s['judgment']}** → BTC 목표 비중 **{s['target'] if s['target'] is not None else '—'}%**"
         f" (전일 판정: {s['prev_judgment'] or '없음'})",
         f"- 오늘 총점 {s['total']} / 3일 평균 {s['avg3']} / 오늘 구간 '{s['raw']}'",
         f"- 판정 가능 지표 {s['scored']}/{s['n']}개 ({s['coverage']:.0%})"]
    L += [f"- {n}" for n in s["notes"]]
    L += [f"- 안전장치 적용: {g}" for g in s["guards"]]
    L += ["", "| 그룹 | 가중치 | 그룹 점수 |", "|---|---|---|"]
    for g, w in s["weights"].items():
        L.append(f"| {g} | {w}% | {s['groups'].get(g, '판정 불가')} |")
    L += ["", "| 그룹 | 지표 | 점수 | 어제 | 근거 |", "|---|---|---|---|---|"]
    for r in s["rows"]:
        L.append(f"| {r['group']} | {r['name']} | {f(r['score']) if r['score'] is not None else '제외'} | "
                 f"{f(r['prev'])} | {r['why']} |")
    return L + [""]
