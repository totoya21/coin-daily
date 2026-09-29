# -*- coding: utf-8 -*-
"""
섹터 순환 트래커
- 추적 섹터별로 시총 상위 코인을 모아 BTC 대비 상대강도, 대장주 vs 후발주, 확산도(breadth)를 계산하고
  섹터의 '순환 단계'를 판정한다.
- 추적 목록 밖에서 급등하는 카테고리(새 내러티브 레이더)와 체인별 스테이블코인 유입도 같이 본다.
- 매일 기록(data/sectors_history.csv)이 쌓이면 전일·1주 전 대비 순위 변화로 '순환이 옮겨가는 방향'을 잡는다.
- 이 표는 '오를 섹터'를 맞히는 도구가 아니라 '자금이 어디로 움직이는지'를 보는 도구다.
- 실행: python sector_rotation.py   (결과: data/sectors_latest.md, data/sectors_latest.json, data/sectors_history.csv)
소스: CoinGecko(카테고리·시세), DefiLlama(스테이블코인·언락)
"""
import csv
import datetime as dt
import json
import os
import statistics
import sys
import time
from pathlib import Path

from coin_daily import KST, get_json, num, rnd
from alt_screener import EXCLUDE_WORDS, cg, llama_unlocks, regime

BASE_DIR = Path(__file__).resolve().parent
STABLE = "https://stablecoins.llama.fi"

# config.json에 "sector_rotation"이 없으면 이 값을 쓴다. 카테고리 id는 CoinGecko 기준
# (https://www.coingecko.com/en/categories 에서 카테고리 페이지 주소 끝부분).
DEFAULTS = {
    "per_sector": 15,               # 섹터별로 볼 시총 상위 코인 수
    "min_mcap_usd": 20_000_000,     # 이보다 작은 코인은 섹터 계산에서 제외
    "radar_min_mcap_usd": 300_000_000,
    "sectors": [
        {"name": "AI", "category": "artificial-intelligence"},
        {"name": "AI 에이전트", "category": "ai-agents"},
        {"name": "RWA", "category": "real-world-assets-rwa"},
        {"name": "DeFi", "category": "decentralized-finance-defi"},
        {"name": "무기한 선물 DEX", "category": "perpetuals"},
        {"name": "Layer 1", "category": "layer-1"},
        {"name": "Layer 2", "category": "layer-2"},
        {"name": "밈", "category": "meme-token"},
        {"name": "게임", "category": "gaming"},
        {"name": "DePIN", "category": "depin"},
        {"name": "프라이버시", "category": "privacy-coins"},
        {"name": "거래소 토큰", "category": "exchange-based-tokens"},
    ],
    "stable_chains": ["Ethereum", "Solana", "Base", "Arbitrum", "BSC", "Tron", "Hyperliquid L1", "Sui"],
    "stage": {                       # 판정 기준 (%p는 BTC 대비 초과수익)
        "overheat_follower_rs7": 25,  # 후발주 중앙값이 BTC보다 이만큼 더 오르면 과열
        "overheat_rs30": 60,          # 섹터 30일 초과수익이 이 이상이면 과열
        "overheat_breadth": 0.8,      # 구성 코인 중 BTC를 이긴 비율
        "spread_breadth": 0.6,
        "leader_gap": 5,              # 대장이 후발주보다 이만큼 앞서면 '대장 주도'
    },
}


def settings(cfg):
    s = json.loads(json.dumps(DEFAULTS))
    user = cfg.get("sector_rotation") or {}
    for k, v in user.items():
        if isinstance(v, dict) and isinstance(s.get(k), dict):
            s[k].update(v)
        else:
            s[k] = v
    return s


# ─────────────────────────── 수집 ───────────────────────────
def category_overview(key):
    """카테고리 id → {name, mcap, chg24, vol}"""
    j, _ = cg("/coins/categories", {"order": "market_cap_desc"}, key)
    out = {}
    for c in j:
        out[c.get("id")] = {"name": c.get("name"), "mcap": num(c.get("market_cap")),
                            "chg24": num(c.get("market_cap_change_24h")), "vol": num(c.get("volume_24h"))}
    return out


def sector_coins(cat, s, key):
    j, _ = cg("/coins/markets", {"vs_currency": "usd", "category": cat, "order": "market_cap_desc",
                                 "per_page": 60, "page": 1, "price_change_percentage": "24h,7d,30d"}, key)
    out = []
    for m in j:
        i = str(m.get("id", ""))
        if i == "bitcoin" or any(w in i for w in EXCLUDE_WORDS):
            continue
        mc = num(m.get("market_cap"))
        if not mc or mc < s["min_mcap_usd"]:
            continue
        out.append({"id": i, "symbol": str(m.get("symbol", "")).upper(), "name": m.get("name"), "mcap": mc,
                    "vol": num(m.get("total_volume")) or 0,
                    "p7": num(m.get("price_change_percentage_7d_in_currency")),
                    "p30": num(m.get("price_change_percentage_30d_in_currency")),
                    "p24": num(m.get("price_change_percentage_24h_in_currency"))})
        if len(out) >= s["per_sector"]:
            break
    return out


def stable_flows(chains):
    rows, notes = [], []
    for ch in chains:
        try:
            j, _ = get_json(f"{STABLE}/stablecoincharts/{ch}", timeout=40)
            pts = [(int(p["date"]), num((p.get("totalCirculatingUSD") or {}).get("peggedUSD"))) for p in j]
            pts = [p for p in pts if p[1]]
            if len(pts) < 31:
                raise ValueError("기록 부족")
            now = pts[-1][1]
            rows.append({"chain": ch, "now": now,
                         "c7": (now / pts[-8][1] - 1) * 100, "c30": (now / pts[-31][1] - 1) * 100})
        except Exception as e:
            notes.append(f"스테이블코인 {ch} 실패: {str(e)[:80]}")
        time.sleep(0.5)
    rows.sort(key=lambda r: r["c7"], reverse=True)
    return rows, notes


# ─────────────────────────── 계산 ───────────────────────────
def wavg(coins, k):
    xs = [(c[k], c["mcap"]) for c in coins if c[k] is not None]
    w = sum(m for _, m in xs)
    return sum(v * m for v, m in xs) / w if w else None


def analyze(name, cat, coins, btc7, btc30, unlock, st):
    lead, fol = coins[0], coins[1:]
    s7, s30 = wavg(coins, "p7"), wavg(coins, "p30")
    rs7 = None if s7 is None else s7 - btc7
    rs30 = None if s30 is None else s30 - btc30
    lrs7 = None if lead["p7"] is None else lead["p7"] - btc7
    lrs30 = None if lead["p30"] is None else lead["p30"] - btc30
    f7 = [c["p7"] - btc7 for c in fol if c["p7"] is not None]
    frs7 = statistics.median(f7) if f7 else None
    valid = [c for c in coins if c["p7"] is not None]
    breadth = sum(1 for c in valid if c["p7"] > btc7) / len(valid) if valid else None
    mc, vol = sum(c["mcap"] for c in coins), sum(c["vol"] for c in coins)
    top_f = sorted([c for c in fol if c["p7"] is not None], key=lambda c: c["p7"], reverse=True)[:3]
    d = {"name": name, "category": cat, "n": len(coins), "mcap": mc, "vol_mcap": vol / mc * 100 if mc else None,
         "rs7": rs7, "rs30": rs30, "breadth": breadth, "leader": lead, "lrs7": lrs7, "lrs30": lrs30,
         "frs7": frs7, "top_followers": top_f, "unlock": unlock.get(lead["id"])}
    d["stage"] = stage(d, st)
    return d


def stage(d, st):
    rs7, rs30, fr, lr, br = d["rs7"], d["rs30"], d["frs7"], d["lrs7"], d["breadth"]
    if rs7 is None:
        return "데이터 부족"
    rs30, br = rs30 or 0, br or 0
    if rs7 > 0 and br >= st["overheat_breadth"] and ((fr or 0) > st["overheat_follower_rs7"]
                                                      or rs30 > st["overheat_rs30"]):
        return "과열 경고"
    if (rs7 > 0 and lr is not None and fr is not None and lr > fr + st["leader_gap"]
            and br < st["spread_breadth"]):
        return "초기 (대장 주도)"
    if rs7 > 0 and br >= st["spread_breadth"]:
        return "확산 (후발주 추격)"
    if rs7 > 0 and rs30 <= 0:
        return "반등 초입"
    if rs7 > 0:
        return "상대 강세"
    if rs30 > 20:
        return "조정 (순환 이탈 가능)"
    return "소외"


def history_ranks(path, today):
    """(전일 순위, 약 1주 전 순위) — 섹터 이름 기준."""
    if not path.exists():
        return {}, {}
    by_date = {}
    with open(path, encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            by_date.setdefault(r["run_at"], {})[r["sector"]] = int(r["rank7"])
    dates = sorted(d for d in by_date if d < today)
    if not dates:
        return {}, {}
    prev = by_date[dates[-1]]
    cutoff = (dt.date.fromisoformat(today) - dt.timedelta(days=6)).isoformat()
    wk = [d for d in dates if d <= cutoff]
    return prev, (by_date[wk[-1]] if wk else {})


def next_candidates(rows):
    """데이터만으로 뽑은 '다음 순환 후보' — 최종 판단은 뉴스·촉매와 같이 볼 것."""
    out = []
    for d in rows:
        why = []
        if d["stage"] == "과열 경고" or d["rs7"] is None:
            continue
        if d["stage"] == "반등 초입":
            why.append("30일은 BTC보다 약했지만 최근 7일 반등")
        if d["stage"] == "초기 (대장 주도)":
            why.append("대장이 먼저 움직이고 후발주는 아직")
        if d.get("wk_move") is not None and d["wk_move"] >= 3 and d["rs7"] > 0:
            why.append(f"1주 새 순위 {d['wk_move']}계단 상승")
        if d["vol_mcap"] is not None and d["vol_mcap"] >= 15 and d["rs7"] > 0 and (d["rs30"] or 0) < 20:
            why.append("시총 대비 거래량 높음 (자금 유입 가능성)")
        if why:
            out.append((d, why))
    out.sort(key=lambda x: (len(x[1]), x[0]["rs7"]), reverse=True)
    return out[:4]


# ─────────────────────────── 실행 ───────────────────────────
def main():
    cfg = json.loads((BASE_DIR / "config.json").read_text(encoding="utf-8"))
    key = os.environ.get("COINGECKO_API_KEY", cfg["keys"].get("coingecko_demo", "")).strip()
    s = settings(cfg)
    out_dir = Path(cfg["output_dir"])
    if not out_dir.is_absolute():
        out_dir = BASE_DIR / out_dir
    now = dt.datetime.now(KST)
    today = f"{now:%Y-%m-%d}"
    notes = []

    print("[1/5] 시장 국면 ...", flush=True)
    reg = regime(key)
    btc7, btc30 = reg["btc7"] or 0, reg["btc30"] or 0

    print("[2/5] 카테고리 전체 ...", flush=True)
    try:
        cats = category_overview(key)
    except Exception as e:
        cats = {}
        notes.append(f"카테고리 목록 실패: {str(e)[:80]} (id 검증·레이더 생략)")

    print("[3/5] 섹터별 코인 ...", flush=True)
    unlock, n1 = llama_unlocks()
    notes += n1
    rows = []
    for sec in s["sectors"]:
        cat = sec["category"]
        if cats and cat not in cats:
            notes.append(f"'{sec['name']}' 카테고리 id '{cat}'가 CoinGecko에 없음 — config.json에서 id 확인 필요")
            continue
        try:
            coins = sector_coins(cat, s, key)
        except Exception as e:
            notes.append(f"'{sec['name']}' 수집 실패: {str(e)[:80]}")
            continue
        if len(coins) < 3:
            notes.append(f"'{sec['name']}' 조건 통과 코인 {len(coins)}개 — 계산 생략")
            continue
        d = analyze(sec["name"], cat, coins, btc7, btc30, unlock, s["stage"])
        d["chg24"] = (cats.get(cat) or {}).get("chg24")
        rows.append(d)
        print(f"       {sec['name']:<10} {d['stage']}", flush=True)

    rows.sort(key=lambda d: d["rs7"] if d["rs7"] is not None else -1e9, reverse=True)
    hp = out_dir / "sectors_history.csv"
    prev, wk = history_ranks(hp, today)
    for n, d in enumerate(rows, 1):
        d["rank7"] = n
        d["day_move"] = (prev[d["name"]] - n) if d["name"] in prev else None
        d["wk_move"] = (wk[d["name"]] - n) if d["name"] in wk else None

    print("[4/5] 레이더·스테이블코인 ...", flush=True)
    tracked = {x["category"] for x in s["sectors"]}
    radar = sorted([(i, c) for i, c in cats.items() if i not in tracked and c["chg24"] is not None
                    and (c["mcap"] or 0) >= s["radar_min_mcap_usd"]], key=lambda x: x[1]["chg24"], reverse=True)[:8]
    flows, n2 = stable_flows(s["stable_chains"])
    notes += n2

    print("[5/5] 저장 ...", flush=True)
    cands = next_candidates(rows)
    out_dir.mkdir(parents=True, exist_ok=True)
    f = lambda v, n=1: "—" if v is None else f"{v:+,.{n}f}"  # noqa: E731
    money = lambda v: ("—" if not v else f"${v/1e9:.1f}B" if v >= 1e9  # noqa: E731
                       else f"${v/1e6:.0f}M")
    pct = lambda v, k, n: "—" if v is None else f"{v * k:.{n}f}%"  # noqa: E731
    mv = lambda v: "—" if v is None else ("=" if v == 0 else f"▲{v}" if v > 0 else f"▼{-v}")  # noqa: E731

    L = ["# 섹터 순환 트래커", "",
         f"- 실행: {now:%Y-%m-%d %H:%M KST}",
         "- 수익률은 모두 **BTC 대비 초과수익(%p)**. 섹터 수익률은 구성 코인 시총 가중.",
         "- 이 표는 '오를 섹터'가 아니라 '자금이 움직이는 방향'을 보여준다. 최종 판단과 책임은 사용자에게 있다.", "",
         "## 시장 국면", "",
         f"- BTC 도미넌스 {rnd(reg['btc_d'], 2)}% / 테더 도미넌스 {rnd(reg['usdt_d'], 2)}%",
         f"- BTC 7일 {f(reg['btc7'])}% / 30일 {f(reg['btc30'])}% / ETH−BTC 30일 격차 {f(reg['ethbtc30'])}%p",
         f"- **판단: {reg['verdict']}**", "",
         "## 1. 섹터 순위 (7일 상대강도 순)", "",
         "| # | 섹터 | 단계 | 7일 | 30일 | 24h 시총 | 확산도 | 거래량/시총 | 순위 변화(전일/1주) |",
         "|---|---|---|---|---|---|---|---|---|"]
    for d in rows:
        L.append(f"| {d['rank7']} | {d['name']} | **{d['stage']}** | {f(d['rs7'])} | {f(d['rs30'])} | "
                 f"{f(d.get('chg24'))}% | {pct(d['breadth'], 100, 0)} | "
                 f"{pct(d['vol_mcap'], 1, 1)} | {mv(d['day_move'])} / {mv(d['wk_move'])} |")
    L += ["", "확산도 = 구성 코인 중 7일 수익률이 BTC를 이긴 비율. 순위 변화는 기록이 쌓여야 표시된다.", "",
          "## 2. 대장주 vs 후발주", "",
          "| 섹터 | 대장 (시총 1위) | 대장 7일 | 대장 30일 | 후발주 7일 중앙값 | 7일 강한 후발주 | 대장 언락 |",
          "|---|---|---|---|---|---|---|"]
    for d in rows:
        ld, u = d["leader"], d["unlock"]
        ul = "—" if not u else f"{u[0]:.0f}일 뒤 시총의 {u[1]:.1f}%" + (" ⚠" if u[0] <= 30 and u[1] >= 2 else "")
        tf = ", ".join(f"{c['symbol']} {f(c['p7'] - btc7, 0)}" for c in d["top_followers"]) or "—"
        L.append(f"| {d['name']} | {ld['symbol']} ({money(ld['mcap'])}) | {f(d['lrs7'])} | {f(d['lrs30'])} | "
                 f"{f(d['frs7'])} | {tf} | {ul} |")
    L += ["", "대장이 앞서고 후발주가 안 따라오면 초기, 후발주가 대장을 따라잡으면 확산, 소형주까지 급등하면 후반부로 본다.", "",
          "## 3. 다음 순환 후보 (데이터 기준)", ""]
    if cands:
        for d, why in cands:
            L.append(f"- **{d['name']}** ({d['stage']}, 7일 {f(d['rs7'])}%p): " + " / ".join(why))
    else:
        L.append("- 조건에 맞는 섹터 없음")
    L += ["", "이 목록은 가격·거래량만 본 것이다. 뉴스·촉매·관심도 확인 전에는 후보일 뿐이다.", "",
          "## 4. 레이더 — 추적 목록 밖에서 24시간 급등한 카테고리", "",
          f"(시총 {money(s['radar_min_mcap_usd'])} 이상만. 며칠 연속 뜨면 config.json 추적 목록에 추가 검토)", ""]
    L += [f"- {c['name']} (`{i}`): 24h {f(c['chg24'])}%, 시총 {money(c['mcap'])}" for i, c in radar] or ["- 없음"]
    L += ["", "## 5. 체인별 스테이블코인 유입", "",
          "| 체인 | 스테이블코인 잔액 | 7일 | 30일 |", "|---|---|---|---|"]
    L += [f"| {r['chain']} | {money(r['now'])} | {f(r['c7'])}% | {f(r['c30'])}% |" for r in flows]
    L += ["", "스테이블코인이 빠르게 늘어나는 체인은 그 생태계 코인에 자금이 들어올 여지가 있다는 뜻으로 본다.", "",
          "## 사람이 따로 확인할 것", "",
          "- 관심도(마인드셰어): https://yaps.kaito.ai , X 검색",
          "- 섹터 지수·펀더멘털: https://app.artemis.xyz , https://tokenterminal.com , https://defillama.com",
          "- 언락 상세: https://tokenomist.ai", "",
          "## 출처", "",
          "- 카테고리·시세: CoinGecko (https://www.coingecko.com/en/categories)",
          "- 스테이블코인·언락: DefiLlama (https://defillama.com/stablecoins)", ""]
    if notes:
        L += ["## 수집 경고", ""] + [f"- {x}" for x in notes] + [""]
    (out_dir / "sectors_latest.md").write_text("\n".join(L), encoding="utf-8")

    js = {"run_at": now.isoformat(), "regime": reg, "sectors": rows,
          "candidates": [{"sector": d["name"], "why": w} for d, w in cands],
          "radar": [{"id": i, **c} for i, c in radar], "stable_flows": flows, "notes": notes}
    (out_dir / "sectors_latest.json").write_text(json.dumps(js, ensure_ascii=False, indent=1, default=str),
                                                 encoding="utf-8")

    rows_hist = []
    if hp.exists():  # 같은 날 재실행이면 그날 기록을 덮어쓴다
        with open(hp, encoding="utf-8-sig") as fh:
            rows_hist = [r for r in csv.DictReader(fh) if r["run_at"] != today]
    fields = ["run_at", "rank7", "sector", "category", "stage", "rs7", "rs30", "breadth", "vol_mcap",
              "leader", "lrs7", "lrs30", "frs7", "btc7", "btc30"]
    for d in rows:
        rows_hist.append({"run_at": today, "rank7": d["rank7"], "sector": d["name"], "category": d["category"],
                          "stage": d["stage"], "rs7": rnd(d["rs7"], 2), "rs30": rnd(d["rs30"], 2),
                          "breadth": rnd(d["breadth"], 3), "vol_mcap": rnd(d["vol_mcap"], 2),
                          "leader": d["leader"]["symbol"], "lrs7": rnd(d["lrs7"], 2), "lrs30": rnd(d["lrs30"], 2),
                          "frs7": rnd(d["frs7"], 2), "btc7": rnd(btc7, 2), "btc30": rnd(btc30, 2)})
    with open(hp, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows_hist)

    print(f"\n국면: {reg['verdict']}")
    for d in rows:
        print(f"  {d['rank7']:>2}. {d['name']:<10} {f(d['rs7']):>7}%p  {d['stage']}")
    print(f"\n저장: {out_dir / 'sectors_latest.md'}")


if __name__ == "__main__":
    sys.exit(main())
