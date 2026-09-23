# -*- coding: utf-8 -*-
"""
주간 알트코인 스크리너
- 바이낸스 USDT 페어 중 최소 조건을 통과한 후보를 점수화한다.
- 점수 = 펀더멘털 40 + 모멘텀 40 + 리스크 감점(−20~0), 0~100으로 자름.
- "오를 종목"이 아니라 "최소 조건을 통과한 후보"를 뽑는 도구다.
- 실행: python alt_screener.py   (결과: data/alts_latest.md, data/alts_history.csv)
소스: CoinGecko(시세·시총·FDV·바이낸스 상장), DefiLlama(TVL·수수료·언락)
"""
import csv
import datetime as dt
import json
import sys
import time
from pathlib import Path

from coin_daily import KST, UTC, get_json, num, rnd

BASE_DIR = Path(__file__).resolve().parent
CG = "https://api.coingecko.com/api/v3"
LLAMA = "https://api.llama.fi"
EXCLUDE_WORDS = ("wrapped", "staked", "usd", "tether", "dai", "bridged", "liquid-staked", "restaked")


def cg(path, params=None, key=""):
    time.sleep(2.5)  # 무료 등급 속도 제한 여유
    return get_json(CG + path, params, headers={"x-cg-demo-api-key": key} if key else None, timeout=40)


# ─────────────────────────── 수집 ───────────────────────────
def binance_usdt_ids(cfg, key, max_pages=12):
    """CoinGecko가 보는 바이낸스 USDT 페어의 코인 id 집합 (거래량 순)."""
    ids, notes = set(), []
    for page in range(1, max_pages + 1):
        try:
            j, _ = cg("/exchanges/binance/tickers", {"page": page, "order": "volume_desc"}, key)
        except Exception as e:
            notes.append(f"바이낸스 페어 {page}페이지 실패: {str(e)[:80]}")
            break
        tks = j.get("tickers", [])
        if not tks:
            break
        for t in tks:
            if t.get("target") == "USDT" and t.get("coin_id"):
                ids.add(t["coin_id"])
    return ids, notes


def markets(key, pages=2):
    out = []
    for page in range(1, pages + 1):
        j, _ = cg("/coins/markets", {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 250,
                                     "page": page, "price_change_percentage": "7d,30d"}, key)
        out += j
    return out


def llama_data():
    """gecko_id → TVL, 7일 TVL 변화, 30일 수수료."""
    tvl, chg, fees, notes = {}, {}, {}, []
    name2gid = {}
    try:
        prot, _ = get_json(LLAMA + "/protocols", timeout=60)
        for p in prot:
            gid = p.get("gecko_id")
            if not gid:
                continue
            name2gid[str(p.get("name", "")).lower()] = gid
            if num(p.get("tvl")):
                tvl[gid] = tvl.get(gid, 0) + num(p["tvl"])
                if p.get("change_7d") is not None:
                    chg.setdefault(gid, num(p["change_7d"]))
    except Exception as e:
        notes.append(f"DefiLlama 프로토콜 TVL 실패: {str(e)[:80]}")
    try:  # 체인 자체의 TVL (L1/L2는 여기에 잡힌다)
        chains, _ = get_json(LLAMA + "/v2/chains", timeout=60)
        for c in chains:
            gid, v = c.get("gecko_id"), num(c.get("tvl"))
            if gid and v:
                tvl[gid] = max(tvl.get(gid, 0), v)
    except Exception as e:
        notes.append(f"DefiLlama 체인 TVL 실패: {str(e)[:80]}")
    try:
        f, _ = get_json(LLAMA + "/overview/fees",
                        {"excludeTotalDataChart": "true", "excludeTotalDataChartBreakdown": "true"}, timeout=60)
        for p in f.get("protocols", []):
            gid = p.get("gecko_id") or name2gid.get(str(p.get("name", "")).lower())
            v = num(p.get("total30d"))
            if gid and v:
                fees[gid] = fees.get(gid, 0) + v
    except Exception as e:
        notes.append(f"DefiLlama 수수료 실패: {str(e)[:80]}")
    return tvl, chg, fees, notes


def llama_unlocks():
    """gecko_id → (일수, 시총 대비 비중%) 가장 가까운 언락."""
    out, notes = {}, []
    try:
        j, _ = get_json(LLAMA + "/emissions", timeout=60)
        items = j if isinstance(j, list) else j.get("protocols", [])
        now = dt.datetime.now(UTC).timestamp()
        for it in items:
            gid = it.get("gecko_id")
            ev = it.get("upcomingEvent") or []
            price, mcap = num(it.get("tPrice")), num(it.get("mcap"))
            if not (gid and ev and price and mcap):
                continue
            e = ev[0]
            ts, toks = num(e.get("timestamp")), sum(num(x) or 0 for x in (e.get("noOfTokens") or []))
            if not ts or not toks or ts < now:
                continue
            out[gid] = ((ts - now) / 86400, toks * price / mcap * 100)
    except Exception as e:
        notes.append(f"DefiLlama 언락 실패: {str(e)[:80]} (MC/FDV로 대체 판단)")
    return out, notes


# ─────────────────────────── 점수 ───────────────────────────
def score_one(m, tvl, tvlchg, fees, unlock, btc30, btc7):
    mc, vol = num(m.get("market_cap")), num(m.get("total_volume"))
    fdv = num(m.get("fully_diluted_valuation"))
    c30 = num(m.get("price_change_percentage_30d_in_currency"))
    c7 = num(m.get("price_change_percentage_7d_in_currency"))
    d = {"id": m["id"], "symbol": (m.get("symbol") or "").upper(), "name": m.get("name"),
         "mcap": mc, "vol": vol, "c30": c30, "c7": c7,
         "mc_fdv": (mc / fdv) if (mc and fdv) else None,
         "tvl": tvl.get(m["id"]), "tvl7": tvlchg.get(m["id"]), "fees30": fees.get(m["id"]),
         "unlock": unlock.get(m["id"])}
    warn = []

    # 펀더멘털 40
    f = 0
    if d["fees30"] and mc:
        y = d["fees30"] * 12 / mc  # 연환산 수수료 / 시총
        d["fee_yield"] = y * 100
        f += 15 if y >= 0.2 else 12 if y >= 0.1 else 9 if y >= 0.05 else 6 if y >= 0.02 else 3
    if d["tvl"] and mc:
        r = mc / d["tvl"]
        d["mc_tvl"] = r
        f += 15 if r <= 2 else 12 if r <= 5 else 9 if r <= 10 else 5 if r <= 20 else 2
        t7 = d["tvl7"]
        f += (10 if t7 >= 10 else 6 if t7 >= 0 else 3 if t7 >= -10 else 0) if t7 is not None else 0
    thin_tvl = (d["tvl"] or 0) < 2e7          # TVL 2천만 달러 미만
    thin_fee = (d["fees30"] or 0) < 1e5        # 30일 수수료 10만 달러 미만
    d["track"] = "펀더멘털" if (d["fees30"] or d["tvl"]) else "내러티브"
    if d["track"] == "펀더멘털" and thin_tvl and thin_fee:
        warn.append("펀더멘털 데이터 빈약(사실상 모멘텀 종목)")

    # 모멘텀 40
    mo = 0
    rs30 = (c30 - btc30) if (c30 is not None and btc30 is not None) else None
    rs7 = (c7 - btc7) if (c7 is not None and btc7 is not None) else None
    d["rs30"], d["rs7"] = rs30, rs7
    if rs30 is not None:  # BTC 대비 +30%p 부근이 최고점, 너무 안 오르거나 너무 오른 쪽 모두 감점
        mo += max(2.0, min(20.0, 20 - abs(rs30 - 30) / 4.5))
    if rs7 is not None:
        mo += max(0.0, min(10.0, 5 + rs7 / 2))
    vm = (vol / mc) if (vol and mc) else 0
    d["vol_mcap"] = vm * 100
    mo += max(0.0, min(10.0, vm * 60))
    mo = round(mo, 1)

    # 리스크 감점
    r = 0
    if d["mc_fdv"] is not None and d["mc_fdv"] > 1.05:
        warn.append(f"데이터 오류 의심: MC/FDV {d['mc_fdv']:.2f} (유통량이 총발행량보다 큼)")
        d["mc_fdv"] = None  # 희석 감점 판단에서 제외
    if d["mc_fdv"] is not None:
        if d["mc_fdv"] < 0.4:
            r -= 12
            warn.append(f"희석 위험: 유통 시총이 FDV의 {d['mc_fdv']*100:.0f}%")
        elif d["mc_fdv"] < 0.6:
            r -= 7
            warn.append(f"물량 부담: FDV 대비 {d['mc_fdv']*100:.0f}%")
        elif d["mc_fdv"] < 0.8:
            r -= 3
    if c30 is not None and c30 > 150:
        r -= 5
        warn.append(f"단기 과열: 30일 +{c30:.0f}%")
    if vol and vol < 30e6:
        r -= 3
        warn.append("거래량 얇음")
    if d["unlock"]:
        days, pct = d["unlock"]
        if days <= 30 and pct >= 1:
            r -= 8 if pct >= 3 else 4
            warn.append(f"언락 D-{days:.0f}, 시총의 {pct:.1f}%")

    d["f"], d["mo"], d["r"] = f, mo, r
    # 펀더멘털 데이터가 없는 코인(밈·신규 등)은 같은 잣대로 비교하지 않고,
    # 모멘텀+리스크만 100점으로 환산해 별도 트랙으로 본다.
    d["score"] = (round(max(0, min(100, f + mo + r)), 1) if d["track"] == "펀더멘털"
                  else round(max(0, min(40, mo + r)) / 40 * 100, 1))
    d["warn"] = warn
    return d


def regime(key):
    g, _ = cg("/global", None, key)
    g = g["data"]
    btc_d, usdt_d = g["market_cap_percentage"]["btc"], g["market_cap_percentage"].get("usdt")
    j, _ = cg("/coins/markets", {"vs_currency": "usd", "ids": "bitcoin,ethereum",
                                 "price_change_percentage": "7d,30d"}, key)
    m = {x["id"]: x for x in j}
    btc30 = num(m["bitcoin"].get("price_change_percentage_30d_in_currency"))
    btc7 = num(m["bitcoin"].get("price_change_percentage_7d_in_currency"))
    eth30 = num(m["ethereum"].get("price_change_percentage_30d_in_currency"))
    ethbtc30 = (eth30 - btc30) if (eth30 is not None and btc30 is not None) else None
    e = ethbtc30 or 0
    verdict = ("알트 우호 (ETH가 BTC를 뚜렷이 앞섬)" if e > 3 else
               "BTC 우위 — 알트 비중을 늘릴 국면은 아님" if e < -3 else
               "중립 — 알트 국면이라고 보기 어려움, 신규 진입은 보수적으로")
    ok = 1 if e > 3 else -1 if e < -3 else 0
    return {"btc_d": btc_d, "usdt_d": usdt_d, "btc30": btc30, "btc7": btc7,
            "ethbtc30": ethbtc30, "verdict": verdict, "ok": ok}


# ─────────────────────────── 실행 ───────────────────────────
def main():
    cfg = json.loads((BASE_DIR / "config.json").read_text(encoding="utf-8"))
    import os
    key = os.environ.get("COINGECKO_API_KEY", cfg["keys"].get("coingecko_demo", "")).strip()
    a = cfg.get("alt_screener", {})
    min_mcap, min_vol, top_n = a.get("min_mcap_usd", 1e8), a.get("min_volume_usd", 1e7), a.get("top_n", 15)
    out_dir = Path(cfg["output_dir"])
    if not out_dir.is_absolute():
        out_dir = BASE_DIR / out_dir
    now = dt.datetime.now(KST)
    notes = []

    print("[1/5] 시장 국면 ...", flush=True)
    reg = regime(key)
    print("[2/5] 바이낸스 USDT 페어 ...", flush=True)
    bnb, n1 = binance_usdt_ids(cfg, key)
    notes += n1
    print(f"       {len(bnb)}개", flush=True)
    print("[3/5] 시세·시총 ...", flush=True)
    mk = markets(key)
    print("[4/5] DefiLlama ...", flush=True)
    tvl, tvlchg, fees, n2 = llama_data()
    unlock, n3 = llama_unlocks()
    notes += n2 + n3

    print("[5/5] 점수 계산 ...", flush=True)
    cand, dropped = [], {"바이낸스 USDT 없음": 0, "시총 미달": 0, "거래량 미달": 0, "제외 대상": 0}
    for m in mk:
        i = m["id"]
        if i in ("bitcoin", "ethereum") or any(w in i for w in EXCLUDE_WORDS):
            dropped["제외 대상"] += 1
            continue
        if i not in bnb:
            dropped["바이낸스 USDT 없음"] += 1
            continue
        if not num(m.get("market_cap")) or num(m["market_cap"]) < min_mcap:
            dropped["시총 미달"] += 1
            continue
        if not num(m.get("total_volume")) or num(m["total_volume"]) < min_vol:
            dropped["거래량 미달"] += 1
            continue
        cand.append(score_one(m, tvl, tvlchg, fees, unlock, reg["btc30"], reg["btc7"]))
    cand.sort(key=lambda x: x["score"], reverse=True)
    fund = [c for c in cand if c["track"] == "펀더멘털"][:top_n]
    narr = [c for c in cand if c["track"] == "내러티브"][:max(5, top_n // 3)]
    top = fund + narr

    out_dir.mkdir(parents=True, exist_ok=True)
    L = ["# 주간 알트 스크리너", "",
         f"- 실행: {now:%Y-%m-%d %H:%M KST}",
         f"- 후보 {len(cand)}개 (통과 기준: 바이낸스 USDT 상장, 시총 ${min_mcap/1e6:.0f}M↑, "
         f"24h 거래량 ${min_vol/1e6:.0f}M↑)",
         "- 이 표는 '오를 종목'이 아니라 '최소 조건을 통과한 후보'다. 최종 선택과 책임은 사용자에게 있다.", "",
         "## 시장 국면 (종목보다 먼저 볼 것)", "",
         f"- BTC 도미넌스 {rnd(reg['btc_d'],2)}% / 테더 도미넌스 {rnd(reg['usdt_d'],2)}%",
         f"- 30일 수익률: BTC {rnd(reg['btc30'],1)}% / ETH−BTC 격차 {rnd(reg['ethbtc30'],1)}%p",
         f"- **판단: {reg['verdict']}**", "",
         ]
    fmt = lambda v, d=1: "—" if v is None else f"{v:,.{d}f}"  # noqa: E731
    money = lambda v: ("—" if not v else f"${v/1e9:.2f}B" if v >= 1e9  # noqa: E731
                       else f"${v/1e6:.0f}M" if v >= 1e6 else f"${v/1e3:.0f}K")
    def table(rows, head):
        out = [head, "",
               "| # | 코인 | 점수 | 펀더 | 모멘텀 | 리스크 | 시총 | 30일 vs BTC | 거래량/시총 | MC/FDV | TVL | 30일 수수료 | 경고 |",
               "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for n, d in enumerate(rows, 1):
            out.append(f"| {n} | {d['name']} ({d['symbol']}) | **{d['score']}** | {d['f']} | {d['mo']} | {d['r']} | "
                       f"{money(d['mcap'])} | {fmt(d['rs30'])}%p | {fmt(d['vol_mcap'])}% | "
                       f"{fmt(d['mc_fdv'],2)} | {money(d['tvl'])} | {money(d['fees30'])} | "
                       f"{'; '.join(d['warn']) or '—'} |")
        return out + [""]
    L += table(fund, "## A. 펀더멘털형 (TVL·수수료 데이터 있는 프로젝트)")
    L += table(narr, "## B. 내러티브·모멘텀형 (펀더멘털 데이터 없음 — 모멘텀·리스크만 100점 환산)")
    L += ["두 표는 잣대가 달라 점수를 서로 비교하면 안 된다. B는 근거가 가격과 거래량뿐이므로 더 작게 담을 것.", ""]
    L += ["", "## 제외 사유", "", " / ".join(f"{k} {v}개" for k, v in dropped.items()), "",
          "## 출처", "",
          "- 시총·거래량·FDV·바이낸스 상장: CoinGecko (https://www.coingecko.com)",
          "- TVL·수수료·언락: DefiLlama (https://defillama.com)",
          "- 언락 상세 확인: https://token.unlocks.app", ""]
    if notes:
        L += ["## 수집 경고", ""] + [f"- {x}" for x in notes] + [""]
    L += ["## 점수 구성", "",
          "- 펀더멘털 40: 수수료 매출/시총, 시총/TVL, TVL 7일 변화 (데이터 없으면 0점)",
          "- 모멘텀 40: BTC 대비 30일·7일 상대강도, 거래량/시총",
          "- 리스크 −20~0: MC/FDV(희석), 30일 과열, 거래량 부족, 30일 내 언락", ""]
    (out_dir / "alts_latest.md").write_text("\n".join(L), encoding="utf-8")

    hp = out_dir / "alts_history.csv"
    new = not hp.exists()
    with open(hp, "a", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(["run_at", "rank", "id", "symbol", "score", "fund", "mom", "risk", "mcap", "vol",
                        "rs30", "rs7", "mc_fdv", "tvl", "fees30", "track", "warn"])
        for n, d in enumerate(top, 1):
            w.writerow([f"{now:%Y-%m-%d}", n, d["id"], d["symbol"], d["score"], d["f"], d["mo"], d["r"],
                        rnd(d["mcap"], 0), rnd(d["vol"], 0), rnd(d["rs30"], 1), rnd(d["rs7"], 1),
                        rnd(d["mc_fdv"], 3), rnd(d["tvl"], 0), rnd(d["fees30"], 0), d["track"],
                        "; ".join(d["warn"])])
    print(f"\n국면: {reg['verdict']}")
    for n, d in enumerate(top, 1):
        print(f"  {n:>2}. [{d['track']}] {d['symbol']:<8} {d['score']:>3}점  {'; '.join(d['warn'])}")
    print(f"\n저장: {out_dir/'alts_latest.md'}")


if __name__ == "__main__":
    sys.exit(main())
