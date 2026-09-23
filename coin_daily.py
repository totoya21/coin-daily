# -*- coding: utf-8 -*-
"""
코인 데일리 스냅샷 수집기
- 하루 한 번 실행해서 지표값 + 출처 + 지난밤 뉴스를 저장한다.
- 모든 지표는 항상 같은 소스에서 가져온다 (config.json 참고).
- 사용법:
    python coin_daily.py            # 정식 수집 (history.csv 누적 + latest.md 갱신)
    (GitHub Actions에서 매일 09:30 KST 자동 실행. API 키는 GitHub Secrets 환경변수로 전달)
    python coin_daily.py --check    # 소스 점검만 (기록 안 함, check_report.md 생성)
"""
import argparse
import csv
import datetime as dt
import io
import json
import os
import re
import sys
import time
import traceback
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

KST = ZoneInfo("Asia/Seoul")
UTC = dt.timezone.utc
BASE_DIR = Path(__file__).resolve().parent
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"}
HIST_FIELDS = ["run_at", "group", "key", "name", "value", "prev", "unit", "data_as_of",
               "status", "source", "api_url", "view_url", "note"]


# ─────────────────────────── 공통 유틸 ───────────────────────────
def redact(url: str) -> str:
    """저장되는 URL에서 API 키를 가린다."""
    return re.sub(r"(api_key|x_cg_demo_api_key|token)=[^&]+", r"\1=***", url or "")


def get_json(url, params=None, headers=None, timeout=25):
    r = requests.get(url, params=params, headers={**UA, **(headers or {})}, timeout=timeout)
    r.raise_for_status()
    return r.json(), redact(r.url)


def rec(group, key, name, value, unit, source, api_url, view_url, as_of,
        prev=None, status="ok", note=""):
    return {"group": group, "key": key, "name": name, "value": value, "prev": prev,
            "unit": unit, "source": source, "api_url": api_url, "view_url": view_url,
            "data_as_of": as_of, "status": status, "note": note}


def fail(group, key, name, source, view_url, err, status="fail"):
    return rec(group, key, name, None, "", source, "", view_url, "", status=status,
               note=str(err)[:200])


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def rnd(x, n=4):
    return None if x is None else round(x, n)


def pct_rank(x, arr):
    """arr 안에서 x 이하 값의 비율(0~100)."""
    arr = [a for a in arr if a is not None]
    return None if not arr or x is None else 100.0 * sum(a <= x for a in arr) / len(arr)


# ─────────────────────────── A. 매크로 ───────────────────────────
def c_yahoo(cfg):
    import yfinance as yf
    out = []
    items = [("nasdaq", "나스닥 종합지수", "^IXIC", "pt"),
             ("dxy", "달러인덱스(DXY)", "DX-Y.NYB", "pt"),
             ("usdjpy", "USD/JPY", "JPY=X", "엔")]
    for key, name, tk, unit in items:
        view = f"https://finance.yahoo.com/quote/{requests.utils.quote(tk)}"
        try:
            close = yf.Ticker(tk).history(period="6mo")["Close"].dropna()
            last, prev = float(close.iloc[-1]), float(close.iloc[-2])
            as_of = close.index[-1].strftime("%Y-%m-%d")
            out.append(rec("A.매크로", key, name, rnd(last, 3), unit, "Yahoo Finance",
                           f"yfinance:{tk}", view, as_of, prev=rnd(prev, 3)))
            chg = {"nasdaq": ("nasdaq_5d_pct", "나스닥 5거래일 변화율", 5),
                   "dxy": ("dxy_20d_pct", "DXY 20거래일 변화율", 20),
                   "usdjpy": ("usdjpy_5d_pct", "USD/JPY 5거래일 변화율", 5)}[key]
            pc = (last / float(close.iloc[-1 - chg[2]]) - 1) * 100
            out.append(rec("A.매크로", chg[0], chg[1], rnd(pc, 2), "%", "Yahoo Finance",
                           f"yfinance:{tk}", view, as_of))
            if key == "nasdaq":
                ma50 = float(close.tail(50).mean())
                out.append(rec("A.매크로", "nasdaq_ma50", "나스닥 50일 이평", rnd(ma50, 2), "pt",
                               "Yahoo Finance", f"yfinance:{tk}", view, as_of,
                               note="종가가 이평 위면 추세 양호"))
        except Exception as e:
            out.append(fail("A.매크로", key, name, "Yahoo Finance", view, e))
    return out


def c_fred(cfg):
    out, signs = [], []
    key = cfg["keys"].get("fred", "")
    series = [("cpi_yoy", "CPI 전년비", "CPIAUCSL"), ("core_cpi_yoy", "근원 CPI 전년비", "CPILFESL"),
              ("pce_yoy", "PCE 전년비", "PCEPI"), ("core_pce_yoy", "근원 PCE 전년비", "PCEPILFE")]
    for k, name, sid in series:
        view = f"https://fred.stlouisfed.org/series/{sid}"
        if not key:
            out.append(fail("A.매크로", k, name, "FRED", view, "FRED API 키 없음"))
            continue
        try:
            j, url = get_json("https://api.stlouisfed.org/fred/series/observations",
                              {"series_id": sid, "api_key": key, "file_type": "json",
                               "sort_order": "desc", "limit": 24})
            obs = [(o["date"], num(o["value"])) for o in j["observations"] if num(o["value"])]
            if len(obs) < 14:
                raise ValueError(f"관측치 부족 ({len(obs)}개) — 전년비 계산 불가")
            yoy = (obs[0][1] / obs[12][1] - 1) * 100
            yoy_prev = (obs[1][1] / obs[13][1] - 1) * 100
            info, _ = get_json("https://api.stlouisfed.org/fred/series",
                               {"series_id": sid, "api_key": key, "file_type": "json"})
            upd = info["seriess"][0]["last_updated"][:10]
            fresh = (dt.date.today() - dt.date.fromisoformat(upd)).days <= 30
            if fresh and abs(yoy - yoy_prev) >= 0.05:  # 0.05%p 미만 변화는 노이즈로 무시
                signs.append(1 if yoy < yoy_prev else -1)
            out.append(rec("A.매크로", k, name, rnd(yoy, 2), "%", "FRED", url, view, obs[0][0],
                           prev=rnd(yoy_prev, 2),
                           note=f"FRED 갱신일 {upd} ({'발표 후 30일 이내' if fresh else '점수 미반영: 발표 후 30일 경과'})"))
        except Exception as e:
            out.append(fail("A.매크로", k, name, "FRED", view, e))
    if signs:
        out.append(rec("A.매크로", "infl_signal", "인플레이션 방향 합계", sum(signs), "", "FRED", "",
                       "https://fred.stlouisfed.org/", dt.date.today().isoformat(),
                       note="최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합"))
    return out


# ─────────────────────────── C. 파생 / 가격 ───────────────────────────
def rsi_wilder(closes, n=14):
    d = [closes[i] - closes[i - 1] for i in range(1, len(closes))]
    g = [max(x, 0) for x in d]
    l = [max(-x, 0) for x in d]
    ag, al = sum(g[:n]) / n, sum(l[:n]) / n
    for i in range(n, len(d)):
        ag = (ag * (n - 1) + g[i]) / n
        al = (al * (n - 1) + l[i]) / n
    return 100.0 if al == 0 else 100 - 100 / (1 + ag / al)


def _spot_recs(closes, as_of, src, url, view):
    return [
        rec("C.파생·가격", "btc_close", "BTC 일봉 종가", rnd(closes[-1], 2), "USD", src, url, view, as_of,
            prev=rnd(closes[-2], 2)),
        rec("C.파생·가격", "rsi14", "RSI(14, 일봉)", rnd(rsi_wilder(closes), 2), "", src, url, view, as_of,
            prev=rnd(rsi_wilder(closes[:-1]), 2), note="70↑ 과매수 / 30↓ 과매도"),
        rec("C.파생·가격", "price_7d_pct", "BTC 7일 가격 변화율", rnd((closes[-1] / closes[-8] - 1) * 100, 2), "%",
            src, url, view, as_of),
    ]


def c_coinbase_spot(cfg):
    view = "https://www.coinbase.com/price/bitcoin"
    try:
        j, url = get_json("https://api.exchange.coinbase.com/products/BTC-USD/candles", {"granularity": 86400})
        rows = sorted(j, key=lambda k: k[0])[:-1]  # 오래된→최신, 진행 중인 오늘 봉 제외
        closes = [float(k[4]) for k in rows]
        as_of = dt.datetime.fromtimestamp(rows[-1][0], UTC).strftime("%Y-%m-%d")
        return _spot_recs(closes, as_of, "Coinbase 현물", url, view)
    except Exception as e:
        return [fail("C.파생·가격", "rsi14", "RSI(14, 일봉)", "Coinbase 현물", view, e)]


def c_spot(cfg):
    return c_coinbase_spot(cfg) if cfg.get("spot_source", "coinbase") == "coinbase" else c_binance_spot(cfg)


def c_binance_spot(cfg):
    view = "https://www.binance.com/en/trade/BTC_USDT"
    try:
        j, url = get_json("https://api.binance.com/api/v3/klines",
                          {"symbol": "BTCUSDT", "interval": "1d", "limit": 300})
        closed = j[:-1]  # 마지막 봉은 진행 중이라 제외
        closes = [float(k[4]) for k in closed]
        as_of = dt.datetime.fromtimestamp(closed[-1][0] / 1000, UTC).strftime("%Y-%m-%d")
        return [
            rec("C.파생·가격", "btc_close", "BTC 일봉 종가", rnd(closes[-1], 2), "USDT", "Binance 현물",
                url, view, as_of, prev=rnd(closes[-2], 2)),
            rec("C.파생·가격", "rsi14", "RSI(14, 일봉)", rnd(rsi_wilder(closes), 2), "", "Binance 현물",
                url, view, as_of, prev=rnd(rsi_wilder(closes[:-1]), 2), note="70↑ 과매수 / 30↓ 과매도"),
            rec("C.파생·가격", "price_7d_pct", "BTC 7일 가격 변화율", rnd((closes[-1] / closes[-8] - 1) * 100, 2), "%",
                "Binance 현물", url, view, as_of),
        ]
    except Exception as e:
        return [fail("C.파생·가격", "rsi14", "RSI(14, 일봉)", "Binance 현물", view, e)]


def c_binance_futures(cfg):
    out, base = [], "https://fapi.binance.com"
    view = "https://www.binance.com/en/futures/BTCUSDT"
    sym = {"symbol": "BTCUSDT", "period": "1d", "limit": 2}
    try:
        j, url = get_json(base + "/futures/data/openInterestHist", {**sym, "limit": 8})
        oi7 = (num(j[-1]["sumOpenInterest"]) / num(j[0]["sumOpenInterest"]) - 1) * 100
        j = j[-2:]
        as_of = dt.datetime.fromtimestamp(j[-1]["timestamp"] / 1000, UTC).strftime("%Y-%m-%d")
        out.append(rec("C.파생·가격", "oi", "선물 미결제약정(OI)", rnd(num(j[-1]["sumOpenInterest"]), 2),
                       "BTC", "Binance 선물", url, view, as_of, prev=rnd(num(j[0]["sumOpenInterest"]), 2)))
        out.append(rec("C.파생·가격", "oi_usd", "선물 OI (달러)", rnd(num(j[-1]["sumOpenInterestValue"]) / 1e9, 3),
                       "십억$", "Binance 선물", url, view, as_of,
                       prev=rnd(num(j[0]["sumOpenInterestValue"]) / 1e9, 3)))
        out.append(rec("C.파생·가격", "oi_7d_pct", "OI 7일 변화율", rnd(oi7, 2), "%", "Binance 선물", url, view, as_of))
    except Exception as e:
        out.append(fail("C.파생·가격", "oi_btc", "선물 미결제약정(OI)", "Binance 선물", view, e))
    for k, name, path in [("ls_account", "롱/숏 계정비율(전체)", "/futures/data/globalLongShortAccountRatio"),
                          ("ls_top_pos", "롱/숏 포지션비율(상위 트레이더)", "/futures/data/topLongShortPositionRatio")]:
        try:
            j, url = get_json(base + path, {**sym, "limit": 30})
            series = [num(x["longShortRatio"]) for x in j]
            j = j[-2:]
            as_of = dt.datetime.fromtimestamp(j[-1]["timestamp"] / 1000, UTC).strftime("%Y-%m-%d")
            if k == "ls_account":
                out.append(rec("C.파생·가격", "ls_account_pct", "롱/숏 계정비율 분포 위치", rnd(pct_rank(series[-1], series), 1),
                               "백분위", "Binance 선물", url, view, as_of,
                               note=f"바이낸스 제공 범위 {len(series)}일 분포 기준. 높을수록 롱 쏠림"))
            out.append(rec("C.파생·가격", k, name, rnd(num(j[-1]["longShortRatio"]), 3), "배", "Binance 선물",
                           url, view, as_of, prev=rnd(num(j[0]["longShortRatio"]), 3), note="1 초과면 롱 우위"))
        except Exception as e:
            out.append(fail("C.파생·가격", k, name, "Binance 선물", view, e))
    try:
        j, url = get_json(base + "/fapi/v1/fundingRate", {"symbol": "BTCUSDT", "limit": 6})
        rates = [num(x["fundingRate"]) * 100 for x in j]
        as_of = dt.datetime.fromtimestamp(j[-1]["fundingTime"] / 1000, UTC).strftime("%Y-%m-%d %H:%M UTC")
        out.append(rec("C.파생·가격", "funding", "펀딩비(최근 1회, 8시간)", rnd(rates[-1], 4), "%",
                       "Binance 선물", url, view, as_of, prev=rnd(rates[-2], 4),
                       note="0.05%↑ 과열"))
        out.append(rec("C.파생·가격", "funding_avg3", "펀딩비 최근 3회 평균", rnd(sum(rates[-3:]) / 3, 4), "%",
                       "Binance 선물", url, view, as_of))
    except Exception as e:
        out.append(fail("C.파생·가격", "funding", "펀딩비", "Binance 선물", view, e))
    return out


def _deriv_recs(src, view, url_oi, oi_series, oi_unit, url_ls, ls_series, url_f, rates, as_of, f_as_of):
    """oi_series·ls_series는 오래된→최신 순서, rates는 최근 펀딩비(%) 오래된→최신."""
    out = []
    if oi_series and oi_unit == "USD":
        oi_series, oi_unit = [x / 1e9 for x in oi_series], "십억$"
    if oi_series:
        oi7 = (oi_series[-1] / oi_series[-8] - 1) * 100 if len(oi_series) >= 8 else None
        out.append(rec("C.파생·가격", "oi", f"선물 미결제약정(OI)", rnd(oi_series[-1], 2), oi_unit, src, url_oi, view,
                       as_of, prev=rnd(oi_series[-2], 2)))
        if oi7 is not None:
            out.append(rec("C.파생·가격", "oi_7d_pct", "OI 7일 변화율", rnd(oi7, 2), "%", src, url_oi, view, as_of,
                           note="달러 기준 OI라 가격 변동이 섞여 있음" if oi_unit == "십억$" else ""))
    if ls_series:
        out.append(rec("C.파생·가격", "ls_account", "롱/숏 계정비율", rnd(ls_series[-1], 3), "배", src, url_ls, view,
                       as_of, prev=rnd(ls_series[-2], 3), note="1 초과면 롱 우위"))
        out.append(rec("C.파생·가격", "ls_account_pct", "롱/숏 계정비율 분포 위치",
                       rnd(pct_rank(ls_series[-1], ls_series[-30:]), 1), "백분위", src, url_ls, view, as_of,
                       note=f"{src} 최근 {len(ls_series[-30:])}일 분포 기준. 높을수록 롱 쏠림"))
    if rates:
        out.append(rec("C.파생·가격", "funding", "펀딩비(최근 1회)", rnd(rates[-1], 4), "%", src, url_f, view, f_as_of,
                       prev=rnd(rates[-2], 4), note="0.05%↑ 과열"))
        out.append(rec("C.파생·가격", "funding_avg3", "펀딩비 최근 3회 평균", rnd(sum(rates[-3:]) / 3, 4), "%", src,
                       url_f, view, f_as_of))
    return out


def c_okx_futures(cfg):
    src, view, base = "OKX 선물", "https://www.okx.com/trade-swap/btc-usdt-swap", "https://www.okx.com/api/v5"
    try:
        oi, u1 = get_json(base + "/rubik/stat/contracts/open-interest-volume", {"ccy": "BTC", "period": "1D"})
        ls, u2 = get_json(base + "/rubik/stat/contracts/long-short-account-ratio", {"ccy": "BTC", "period": "1D"})
        fr, u3 = get_json(base + "/public/funding-rate-history", {"instId": "BTC-USDT-SWAP", "limit": 6})
        for j in (oi, ls, fr):
            if str(j.get("code")) != "0":
                raise ValueError(f"OKX 오류 {j.get('code')}: {j.get('msg')}")
        oi_rows = sorted(oi["data"], key=lambda r: int(r[0]))
        ls_rows = sorted(ls["data"], key=lambda r: int(r[0]))
        fr_rows = sorted(fr["data"], key=lambda r: int(r["fundingTime"]))
        as_of = dt.datetime.fromtimestamp(int(oi_rows[-1][0]) / 1000, UTC).strftime("%Y-%m-%d")
        f_as_of = dt.datetime.fromtimestamp(int(fr_rows[-1]["fundingTime"]) / 1000, UTC).strftime("%Y-%m-%d %H:%M UTC")
        return _deriv_recs(src, view, u1, [num(r[1]) for r in oi_rows], "USD", u2, [num(r[1]) for r in ls_rows],
                           u3, [num(r["fundingRate"]) * 100 for r in fr_rows], as_of, f_as_of)
    except Exception as e:
        return [fail("C.파생·가격", "funding_avg3", "OI·롱숏·펀딩비", src, view, e)]


def c_bybit_futures(cfg):
    src, view, base = "Bybit 선물", "https://www.bybit.com/trade/usdt/BTCUSDT", "https://api.bybit.com/v5/market"
    q = {"category": "linear", "symbol": "BTCUSDT"}
    try:
        oi, u1 = get_json(base + "/open-interest", {**q, "intervalTime": "1d", "limit": 8})
        ls, u2 = get_json(base + "/account-ratio", {**q, "period": "1d", "limit": 30})
        fr, u3 = get_json(base + "/funding/history", {**q, "limit": 6})
        for j in (oi, ls, fr):
            if j.get("retCode") != 0:
                raise ValueError(f"Bybit 오류 {j.get('retCode')}: {j.get('retMsg')}")
        oi_rows = sorted(oi["result"]["list"], key=lambda r: int(r["timestamp"]))
        ls_rows = sorted(ls["result"]["list"], key=lambda r: int(r["timestamp"]))
        fr_rows = sorted(fr["result"]["list"], key=lambda r: int(r["fundingRateTimestamp"]))
        as_of = dt.datetime.fromtimestamp(int(oi_rows[-1]["timestamp"]) / 1000, UTC).strftime("%Y-%m-%d")
        f_as_of = dt.datetime.fromtimestamp(int(fr_rows[-1]["fundingRateTimestamp"]) / 1000, UTC).strftime(
            "%Y-%m-%d %H:%M UTC")
        return _deriv_recs(src, view, u1, [num(r["openInterest"]) for r in oi_rows], "BTC", u2,
                           [num(r["buyRatio"]) / num(r["sellRatio"]) for r in ls_rows], u3,
                           [num(r["fundingRate"]) * 100 for r in fr_rows], as_of, f_as_of)
    except Exception as e:
        return [fail("C.파생·가격", "funding_avg3", "OI·롱숏·펀딩비", src, view, e)]


def c_futures(cfg):
    return {"okx": c_okx_futures, "bybit": c_bybit_futures,
            "binance": c_binance_futures}[cfg.get("derivatives_source", "okx")](cfg)


def probe(cfg):
    """후보 소스 접속 가능 여부 (점검 모드 전용)."""
    tests = [("Binance 선물", "https://fapi.binance.com/fapi/v1/time"),
             ("Binance 현물", "https://api.binance.com/api/v3/time"),
             ("OKX", "https://www.okx.com/api/v5/public/time"),
             ("Bybit", "https://api.bybit.com/v5/market/time"),
             ("Coinbase", "https://api.exchange.coinbase.com/products/BTC-USD/ticker"),
             ("Deribit", "https://www.deribit.com/api/v2/public/get_time"),
             ("Farside", "https://farside.co.uk/btc/"),
             ("TFTC (ETF 대체 소스)", "https://www.tftc.io/bitcoin-etf-flows/data.json"),
             ("Coin Metrics", "https://community-api.coinmetrics.io/v4/catalog-v2/asset-metrics?assets=btc&page_size=1"),
             ("BGeometrics", "https://bitcoin-data.com/"),
             ("Yahoo", "https://query1.finance.yahoo.com/v8/finance/chart/%5EIXIC?range=5d&interval=1d")]
    out = []
    for name, url in tests:
        try:
            r = requests.get(url, headers=UA, timeout=15)
            out.append(f"| {name} | {'✅ 가능' if r.status_code < 400 else '❌ 차단/오류'} | HTTP {r.status_code} |")
        except Exception as e:
            out.append(f"| {name} | ❌ 실패 | {str(e)[:80]} |")
    return ["## 접속 가능 여부 (후보 소스)", "",
            f"- 현재 설정: 현물 {cfg.get('spot_source')}, 파생 {cfg.get('derivatives_source')}, "
            f"ETF {cfg.get('etf_source')}", "",
            "| 소스 | 결과 | 상세 |", "|---|---|---|"] + out + [""]


def c_deribit(cfg):
    out, base = [], "https://www.deribit.com/api/v2/public/"
    view = "https://www.deribit.com/statistics/BTC/volatility-index"
    now = int(time.time() * 1000)
    try:
        j, url = get_json(base + "get_volatility_index_data",
                          {"currency": "BTC", "start_timestamp": now - 3 * 86400000,
                           "end_timestamp": now, "resolution": "3600"})
        data = j["result"]["data"]
        last, day_ago = data[-1], data[max(0, len(data) - 25)]
        as_of = dt.datetime.fromtimestamp(last[0] / 1000, UTC).strftime("%Y-%m-%d %H:%M UTC")
        out.append(rec("C.파생·가격", "dvol", "DVOL(BTC 내재변동성)", rnd(last[4], 2), "", "Deribit",
                       url, view, as_of, prev=rnd(day_ago[4], 2)))
    except Exception as e:
        out.append(fail("C.파생·가격", "dvol", "DVOL", "Deribit", view, e))
    try:
        idx = get_json(base + "get_index_price", {"index_name": "btc_usd"})[0]["result"]["index_price"]
        inst, inst_url = get_json(base + "get_instruments",
                                  {"currency": "BTC", "kind": "option", "expired": "false"})
        inst = inst["result"]
        exps = sorted({i["expiration_timestamp"] for i in inst})
        exp = min(exps, key=lambda e: abs(e - (now + 30 * 86400000)))
        cands = [i for i in inst if i["expiration_timestamp"] == exp and 0.7 * idx <= i["strike"] <= 1.3 * idx]
        calls, puts = [], []
        for i in cands:
            t = get_json(base + "ticker", {"instrument_name": i["instrument_name"]})[0]["result"]
            d, iv = t.get("greeks", {}).get("delta"), t.get("mark_iv")
            if d is None or iv is None:
                continue
            (calls if i["option_type"] == "call" else puts).append((d, iv, i["instrument_name"]))
            time.sleep(0.05)
        c25 = min(calls, key=lambda x: abs(x[0] - 0.25))
        p25 = min(puts, key=lambda x: abs(x[0] + 0.25))
        exp_s = dt.datetime.fromtimestamp(exp / 1000, UTC).strftime("%Y-%m-%d")
        out.append(rec("C.파생·가격", "skew25", "옵션 25델타 스큐(풋IV−콜IV)", rnd(p25[1] - c25[1], 2), "vol pt",
                       "Deribit", inst_url, "https://www.deribit.com/options/BTC",
                       dt.datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC"),
                       note=f"만기 {exp_s}, 콜 {c25[2]} / 풋 {p25[2]}. 양수면 하방 헤지 수요 우위"))
    except Exception as e:
        out.append(fail("C.파생·가격", "skew25", "옵션 25델타 스큐", "Deribit", "https://www.deribit.com/options/BTC", e))
    return out


# ─────────────────────────── B. 자금 흐름 ───────────────────────────
def c_coingecko(cfg):
    view = "https://www.coingecko.com/en/global-charts"
    key = cfg["keys"].get("coingecko_demo", "")
    try:
        j, url = get_json("https://api.coingecko.com/api/v3/global",
                          headers={"x-cg-demo-api-key": key} if key else None)
        d = j["data"]
        as_of = dt.datetime.fromtimestamp(d["updated_at"], UTC).strftime("%Y-%m-%d %H:%M UTC")
        return [rec("B.자금흐름", "usdt_d", "테더 도미넌스", rnd(d["market_cap_percentage"]["usdt"], 3), "%",
                    "CoinGecko", url, view, as_of, note="상승=위험회피 / TradingView USDT.D와 계산 방식 다름"),
                rec("B.자금흐름", "total_mcap", "전체 시가총액(TOTAL)", rnd(d["total_market_cap"]["usd"] / 1e12, 4),
                    "조$", "CoinGecko", url, view, as_of)]
    except Exception as e:
        return [fail("B.자금흐름", "usdt_d", "테더 도미넌스/TOTAL", "CoinGecko", view, e)]


def _farside_num(s):
    s = str(s).strip().replace(",", "")
    if s in ("", "-", "nan", "None"):
        return None
    neg = s.startswith("(") and s.endswith(")")
    v = num(s.strip("()"))
    return None if v is None else (-v if neg else v)


def _etf_recs(rows, src, url, view, as_of):
    """rows: [(date, total_musd, ibit_musd)] 오래된→최신"""
    tot = [r[1] for r in rows]
    sign = tot[-1] > 0
    streak = 0
    for v in reversed(tot):
        if v != 0 and (v > 0) == sign:
            streak += 1
        else:
            break
    word = "순유입" if sign else "순유출"
    return [rec("B.자금흐름", "etf_total", "BTC 현물 ETF 순유입(전체)", rnd(tot[-1], 1), "백만$", src, url, view,
                as_of, prev=rnd(tot[-2], 1), note=f"{streak}거래일 연속 {word}"),
            rec("B.자금흐름", "etf_ibit", "IBIT(블랙록) 순유입", rnd(rows[-1][2], 1), "백만$", src, url, view, as_of,
                prev=rnd(rows[-2][2], 1)),
            rec("B.자금흐름", "etf_5d_sum", "ETF 5거래일 순유입 합계", rnd(sum(tot[-5:]), 1), "백만$", src, url, view, as_of),
            rec("B.자금흐름", "etf_streak", "ETF 연속일수(+유입/−유출)", streak if sign else -streak, "일", src, url,
                view, as_of)]


def c_etf_tftc(cfg):
    """TFTC 공개 JSON (SoSoValue + Farside 집계, CC BY 4.0). Farside 직접 접근이 막힌 환경용."""
    src = "TFTC (SoSoValue·Farside 집계)"
    view = "https://www.tftc.io/bitcoin-etf-flows"
    url = "https://www.tftc.io/bitcoin-etf-flows/data.json"
    try:
        j, u = get_json(url)
        days = [d for d in j["days"] if d.get("netFlowUsd") is not None]
        days.sort(key=lambda d: d["date"])
        rows = [(d["date"], d["netFlowUsd"] / 1e6, ((d.get("perEtfUsd") or {}).get("IBIT") or 0) / 1e6)
                for d in days]
        out = _etf_recs(rows, src, u, view, rows[-1][0])
        if j.get("updatedThrough"):
            out[0]["note"] += f" / 집계 기준일 {j['updatedThrough']}"
        return out
    except Exception as e:
        return [fail("B.자금흐름", "etf_total", "BTC 현물 ETF 순유입", src, view, e)]


def c_etf(cfg):
    return c_farside(cfg) if cfg.get("etf_source") == "farside" else c_etf_tftc(cfg)


def c_farside(cfg):
    import pandas as pd
    url = "https://farside.co.uk/btc/"
    try:
        r = requests.get(url, headers=UA, timeout=30)
        r.raise_for_status()
        tables = pd.read_html(io.StringIO(r.text))
        tbl = None
        for t in tables:
            cols = [" ".join(map(str, c)) if isinstance(c, tuple) else str(c) for c in t.columns]
            if any("IBIT" in c for c in cols) and any("Total" in c for c in cols):
                t.columns = cols
                tbl = t
                break
        if tbl is None:
            raise ValueError("IBIT/Total 열이 있는 표를 찾지 못함 (사이트 구조 변경 또는 차단 가능성)")
        date_col = tbl.columns[0]
        ibit_col = next(c for c in tbl.columns if "IBIT" in c)
        tot_col = next(c for c in tbl.columns if "Total" in c)
        tbl["_d"] = pd.to_datetime(tbl[date_col], errors="coerce", dayfirst=True)
        tbl["_t"] = tbl[tot_col].map(_farside_num)
        tbl["_i"] = tbl[ibit_col].map(_farside_num)
        rows = tbl.dropna(subset=["_d", "_t"]).sort_values("_d")
        last, prev = rows.iloc[-1], rows.iloc[-2]
        streak, sign = 0, (last["_t"] > 0)
        for v in reversed(rows["_t"].tolist()):
            if v != 0 and (v > 0) == sign:
                streak += 1
            else:
                break
        as_of = last["_d"].strftime("%Y-%m-%d")
        word = "순유입" if sign else "순유출"
        return [rec("B.자금흐름", "etf_total", "BTC 현물 ETF 순유입(전체)", last["_t"], "백만$", "Farside Investors",
                    url, url, as_of, prev=prev["_t"], note=f"{streak}거래일 연속 {word}"),
                rec("B.자금흐름", "etf_ibit", "IBIT(블랙록) 순유입", last["_i"], "백만$", "Farside Investors",
                    url, url, as_of, prev=prev["_i"]),
                rec("B.자금흐름", "etf_5d_sum", "ETF 5거래일 순유입 합계", rnd(float(rows["_t"].tail(5).sum()), 1), "백만$",
                    "Farside Investors", url, url, as_of),
                rec("B.자금흐름", "etf_streak", "ETF 연속일수(+유입/−유출)", streak if sign else -streak, "일",
                    "Farside Investors", url, url, as_of)]
    except Exception as e:
        return [fail("B.자금흐름", "etf_total", "BTC 현물 ETF 순유입", "Farside Investors", url, e)]


# ─────────────────────────── E. 심리 (폴리마켓) ───────────────────────────
def c_polymarket(cfg):
    out = []
    slugs = list(dict.fromkeys(([cfg["polymarket_fomc_slug"]] if cfg.get("polymarket_fomc_slug") else [])
                               + cfg.get("polymarket_slugs", [])))
    for slug in slugs:
        view = f"https://polymarket.com/market/{slug}"
        try:
            j, url = get_json("https://gamma-api.polymarket.com/markets", {"slug": slug})
            m = j[0]
            outcomes, prices = json.loads(m["outcomes"]), json.loads(m["outcomePrices"])
            p = dict(zip(outcomes, prices))
            yes = num(p.get("Yes", prices[0]))
            ev = (m.get("events") or [{}])[0].get("slug")
            if ev:
                view = f"https://polymarket.com/event/{ev}"
            pkey = "pm_fomc" if slug == cfg.get("polymarket_fomc_slug") else f"pm_{slug[:40]}"
            out.append(rec("E.심리", pkey, f"폴리마켓: {m.get('question', slug)}",
                           rnd(yes * 100, 1), "%(Yes)", "Polymarket", url, view,
                           dt.datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")))
        except Exception as e:
            out.append(fail("E.심리", f"pm_{slug[:40]}", f"폴리마켓: {slug}", "Polymarket", view, e))
    return out


# ─────────────────────────── D. 온체인 ───────────────────────────
def _bg_last(path):
    j, url = get_json(f"https://bitcoin-data.com/v1/{path}/last")
    row = j[-1] if isinstance(j, list) else j
    date = row.get("d") or row.get("date") or row.get("day") or ""
    val = next(num(v) for k, v in row.items()
               if k not in ("d", "date", "day", "unixTs", "timestamp", "ts") and num(v) is not None)
    return val, str(date)[:10], url


def c_bgeometrics(cfg):
    out, view = [], "https://charts.bgeometrics.com/"
    vals = {}
    for key, name, path in [("mvrv_z", "MVRV Z-Score", "mvrv-zscore"),
                            ("sth_mvrv", "단기보유자 MVRV", "sth-mvrv"),
                            ("bg_price", "BTC 가격(BGeometrics)", "btc-price")]:
        try:
            v, d, url = _bg_last(path)
            vals[key] = (v, d, url)
            note = "0 이하 역사적 매수구간 / 7 이상 과열" if key == "mvrv_z" else ""
            if key != "bg_price":
                out.append(rec("D.온체인", key, name, rnd(v, 4), "", "BGeometrics", url, view, d, note=note))
        except Exception as e:
            out.append(fail("D.온체인", key, name, "BGeometrics", view, e))
    if "sth_mvrv" in vals and "bg_price" in vals and vals["sth_mvrv"][0]:
        price, sth = vals["bg_price"][0], vals["sth_mvrv"][0]
        out.append(rec("D.온체인", "sth_rp", "단기보유자 실현가(STH-RP)", rnd(price / sth, 0), "$", "BGeometrics",
                       vals["sth_mvrv"][2], view, vals["sth_mvrv"][1],
                       note=f"가격 ÷ STH-MVRV로 계산 (가격 {rnd(price, 0)}$). 가격이 위면 강세 유지"))
    return out


def _cm_metric(metric, page_size=3):
    j, url = get_json("https://community-api.coinmetrics.io/v4/timeseries/asset-metrics",
                      {"assets": "btc", "metrics": metric, "frequency": "1d",
                       "page_size": page_size, "paging_from": "end"})
    rows = [r for r in j["data"] if r.get(metric) is not None]
    return rows, url


def c_coinmetrics(cfg, ctx):
    out, view = [], "https://charts.coinmetrics.io/crypto-data/"
    src = "Coin Metrics 커뮤니티"
    found = {}
    for m in ["PriceUSD", "FlowInExNtv", "FlowOutExNtv", "FlowInExUSD", "FlowOutExUSD", "SplyExNtv"]:
        try:
            rows, url = _cm_metric(m, 130)
            found[m] = (rows, url)
        except Exception as e:
            found[m] = (None, str(e))
    # BTC 단위 유입/유출: 직접 지표가 없으면 USD ÷ 가격 (같은 소스)으로 환산
    for side, ntv, usd, name in [("in", "FlowInExNtv", "FlowInExUSD", "거래소 BTC 유입"),
                                 ("out", "FlowOutExNtv", "FlowOutExUSD", "거래소 BTC 유출")]:
        try:
            if found[ntv][0]:
                rows, url, note = found[ntv][0], found[ntv][1], ""
                cur, prv = num(rows[-1][ntv]), num(rows[-2][ntv])
            else:
                u, p = found[usd][0], found["PriceUSD"][0]
                pmap = {r["time"]: num(r["PriceUSD"]) for r in p}
                rows, url, note = u, found[usd][1], "USD 유입액 ÷ 가격으로 BTC 환산"
                cur = num(u[-1][usd]) / pmap[u[-1]["time"]]
                prv = num(u[-2][usd]) / pmap[u[-2]["time"]]
            as_of = rows[-1]["time"][:10]
            out.append(rec("D.온체인", f"ex_{side}_btc", name, rnd(cur, 1), "BTC", src, url, view, as_of,
                           prev=rnd(prv, 1), note=note))
            ctx[f"ex_{side}_btc"] = (cur, as_of, url)
        except Exception as e:
            out.append(fail("D.온체인", f"ex_{side}_btc", name, src, view, e))
    # 일별 BTC 순유입 이력 → 7일 합과 90일 분포 위치 (소스가 이력을 주므로 바로 계산 가능)
    try:
        def ntv_series(ntv, usd):
            if found[ntv][0]:
                return {r["time"][:10]: num(r[ntv]) for r in found[ntv][0]}
            pmap = {r["time"]: num(r["PriceUSD"]) for r in found["PriceUSD"][0]}
            return {r["time"][:10]: num(r[usd]) / pmap[r["time"]] for r in found[usd][0] if r["time"] in pmap}
        fi, fo = ntv_series("FlowInExNtv", "FlowInExUSD"), ntv_series("FlowOutExNtv", "FlowOutExUSD")
        days = sorted(set(fi) & set(fo))
        net = [fi[d] - fo[d] for d in days]
        roll = [sum(net[i - 6:i + 1]) for i in range(6, len(net))]
        if len(roll) >= 30:
            dist = roll[-90:]
            out.append(rec("D.온체인", "ex_net_7d", "거래소 순유입 7일 합", rnd(roll[-1], 1), "BTC", src,
                           found["FlowInExUSD"][1], view, days[-1]))
            out.append(rec("D.온체인", "ex_net_7d_pct", "거래소 순유입 7일 합 분포 위치", rnd(pct_rank(roll[-1], dist), 1),
                           "백분위", src, found["FlowInExUSD"][1], view, days[-1],
                           note=f"최근 {len(dist)}일 분포 기준. 높을수록 매도 압력"))
    except Exception as e:
        out.append(fail("D.온체인", "ex_net_7d_pct", "거래소 순유입 7일 분포", src, view, e))
    if "ex_in_btc" in ctx and "ex_out_btc" in ctx:
        net = ctx["ex_in_btc"][0] - ctx["ex_out_btc"][0]
        out.append(rec("D.온체인", "ex_net_btc", "거래소 BTC 순유입", rnd(net, 1), "BTC", src, ctx["ex_in_btc"][2],
                       view, ctx["ex_in_btc"][1], note="양수=매도 압력 / 음수=축적"))
    rows, url = found["SplyExNtv"]
    if rows and len(rows) > 31:
        chg30 = (num(rows[-1]["SplyExNtv"]) / num(rows[-31]["SplyExNtv"]) - 1) * 100
        out.append(rec("D.온체인", "ex_supply_30d_pct", "거래소 보유량 30일 변화율", rnd(chg30, 2), "%", src, url, view,
                       rows[-1]["time"][:10]))
    if rows:
        out.append(rec("D.온체인", "ex_supply", "거래소 BTC 보유량", rnd(num(rows[-1]["SplyExNtv"]), 0), "BTC",
                       src, url, view, rows[-1]["time"][:10], prev=rnd(num(rows[-2]["SplyExNtv"]), 0)))
    # 채굴자→거래소: 후보 지표를 순서대로 시도, 모두 안 되면 수동 확인
    ok = False
    for m in cfg.get("coinmetrics_miner_candidates", []):
        try:
            rows, url = _cm_metric(m)
            if rows:
                out.append(rec("D.온체인", "miner_to_ex", f"채굴자→거래소 ({m})", rnd(num(rows[-1][m]), 2), "BTC",
                               src, url, view, rows[-1]["time"][:10], prev=rnd(num(rows[-2][m]), 2)))
                ok = True
                break
        except Exception:
            continue
    if not ok:
        out.append(fail("D.온체인", "miner_to_ex", "채굴자→거래소 유입", "수동 확인",
                        cfg["manual_checks"][0]["url"] if cfg.get("manual_checks") else "",
                        "무료 소스 없음 → 수동 확인 목록 참고", status="manual"))
    return out


def c_arkham(cfg, ctx):
    view = "https://intel.arkm.com/"
    key = cfg["keys"].get("arkham", "")
    if not key:
        return [fail("D.온체인", "whale_ratio_proxy", "고래비율(근사)", "Arkham + Coin Metrics", view, "Arkham 키 없음")]
    if "ex_in_btc" not in ctx:
        return [fail("D.온체인", "whale_ratio_proxy", "고래비율(근사)", "Arkham + Coin Metrics", view,
                     "Coin Metrics 거래소 유입값 없음 (분모 없음)")]
    total, as_of, cm_url = ctx["ex_in_btc"]
    day = dt.datetime.strptime(as_of, "%Y-%m-%d").replace(tzinfo=UTC)  # Coin Metrics와 같은 UTC 날짜로 맞춤
    params = dict(cfg["arkham"]["transfers_params"])
    params.update({"timeGte": int(day.timestamp() * 1000),
                   "timeLte": int((day + dt.timedelta(days=1)).timestamp() * 1000) - 1})
    try:
        j, url = get_json(cfg["arkham"]["base_url"] + "/transfers", params, headers={"API-Key": key}, timeout=40)
        txs = j.get("transfers", []) if isinstance(j, dict) else j
        amts = []
        for t in txs:
            v = num(t.get("unitValue"))
            if v is None:
                continue
            to = t.get("toAddress") or {}
            ent = (to.get("arkhamEntity") or {}).get("name") or (to.get("arkhamLabel") or {}).get("name") or "?"
            amts.append((v, ent, t.get("transactionHash", "")))
        amts.sort(reverse=True)
        top10 = sum(a[0] for a in amts[:10])
        ratio = top10 / total if total else None
        big = "; ".join(f"{rnd(a[0], 1)} BTC→{a[1]}" for a in amts[:5])
        status = "ok" if ratio is not None and ratio <= 1 else "check"
        return [rec("D.온체인", "whale_top10_btc", "거래소 입금 상위 10건 합계", rnd(top10, 1), "BTC", "Arkham",
                    url, view, as_of, note=f"상위 5건: {big}"),
                rec("D.온체인", "whale_ratio_proxy", "고래비율(근사)", rnd(ratio, 4), "", "Arkham ÷ Coin Metrics",
                    f"{url} | {cm_url}", view, as_of, status=status,
                    note="자체 근사치. CryptoQuant 기준선 사용 금지, 자체 90일 평균 대비로만 판단"
                         + ("" if status == "ok" else " / 1 초과: 검증 필요"))]
    except Exception as e:
        return [fail("D.온체인", "whale_ratio_proxy", "고래비율(근사)", "Arkham + Coin Metrics", view, e)]


# ─────────────────────────── 뉴스 / 코멘트 (RSS) ───────────────────────────
def _entry_time(e):
    t = e.get("published_parsed") or e.get("updated_parsed")
    return dt.datetime(*t[:6], tzinfo=UTC) if t else None


def c_news(cfg, now_kst):
    import feedparser
    w = cfg["news_window"]
    start = (now_kst - dt.timedelta(days=1)).replace(hour=w["start_hour_prev_day"], minute=0, second=0, microsecond=0)
    items, status = [], []
    for f in cfg["news_feeds"]:
        try:
            d = feedparser.parse(f["url"], agent=UA["User-Agent"])
            n = 0
            for e in d.entries:
                t = _entry_time(e)
                if t and start <= t.astimezone(KST) <= now_kst:
                    items.append({"source": f["name"], "title": e.get("title", "").strip(),
                                  "link": e.get("link", ""), "time": t.astimezone(KST).strftime("%m-%d %H:%M")})
                    n += 1
            status.append(f"{f['name']}: {n}건" + ("" if d.entries else " (피드 응답 없음)"))
        except Exception as ex:
            status.append(f"{f['name']}: 실패 ({ex})")
    seen, uniq = set(), []
    for it in sorted(items, key=lambda x: x["time"], reverse=True):
        k = re.sub(r"\W", "", it["title"].lower())[:60]
        if k not in seen:
            seen.add(k)
            uniq.append(it)
    return uniq[:60], status, start


def c_commentary(cfg, now_kst):
    import feedparser
    out = []
    for f in cfg.get("commentary_feeds", []):
        if not f.get("url"):
            out.append({"source": f["name"], "title": "(피드 URL 미설정)", "link": "", "time": ""})
            continue
        d = feedparser.parse(f["url"], agent=UA["User-Agent"])
        for e in d.entries[:10]:
            t = _entry_time(e)
            if t and t.astimezone(KST) >= now_kst - dt.timedelta(days=7):
                out.append({"source": f["name"], "title": e.get("title", "").strip(),
                            "link": e.get("link", ""), "time": t.astimezone(KST).strftime("%m-%d")})
    return out


# ─────────────────────────── 저장 / 리포트 ───────────────────────────
def load_history(path):
    if not path.exists():
        return []
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def fill_prev_and_stats(recs, hist):
    last_ok = {}
    for h in hist:
        if h["status"] == "ok" and h["value"] not in ("", None):
            last_ok[h["key"]] = h["value"]
    for r in recs:
        if r["prev"] is None and r["key"] in last_ok:
            r["prev"] = last_ok[r["key"]]


def write_outputs(out_dir, recs, news, news_status, window_start, comments, cfg, now_kst, check=False, score=None,
                  extra=None):
    out_dir.mkdir(parents=True, exist_ok=True)
    run_at = now_kst.strftime("%Y-%m-%d %H:%M KST")
    if not check:
        hp = out_dir / "history.csv"
        new = not hp.exists()
        with open(hp, "a", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=HIST_FIELDS, extrasaction="ignore")
            if new:
                w.writeheader()
            for r in recs:
                w.writerow({**r, "run_at": run_at})
        snap = out_dir / "snapshots"
        snap.mkdir(exist_ok=True)
        (snap / f"{now_kst:%Y-%m-%d}.json").write_text(
            json.dumps({"run_at": run_at, "indicators": recs, "news": news, "commentary": comments},
                       ensure_ascii=False, indent=1), encoding="utf-8")
    ind = [r for r in recs if r["group"] != "Z.점수"]
    ok = sum(r["status"] == "ok" for r in ind)
    bad = [r for r in ind if r["status"] in ("fail", "check")]
    man = [r for r in ind if r["status"] == "manual"]
    L = [f"# 코인 데일리 스냅샷{' (점검 모드)' if check else ''}", "",
         f"- 수집 시각: {run_at}",
         f"- 결과: 성공 {ok} / 실패·검증필요 {len(bad)} / 수동 {len(man)} (전체 {len(ind)})",
         "- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.", ""]
    if extra:
        L += extra
    if score:
        import scoring
        L += scoring.render(score)
    L += ["## 지표", "",
         "| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |",
         "|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(ind, key=lambda x: x["group"]):
        v = "" if r["value"] is None else r["value"]
        p = "" if r["prev"] is None else r["prev"]
        link = f"[{r['source']}]({r['view_url']})" if r["view_url"] else r["source"]
        L.append(f"| {r['group']} | {r['name']} | {v} | {p} | {r['unit']} | {r['data_as_of']} | "
                 f"{r['status']} | {link} | {r['note'].replace('|', '/')} |")
    L += ["", f"## 지난밤 뉴스 ({window_start:%m-%d %H:%M} ~ {now_kst:%m-%d %H:%M} KST)", "",
          "피드 상태: " + " / ".join(news_status), ""]
    L += [f"- [{n['source']}] {n['title']} ({n['time']}) — {n['link']}" for n in news] or ["- (수집된 기사 없음)"]
    L += ["", "## 전문가 코멘트 (최근 7일, RSS)", ""]
    L += [f"- [{c['source']}] {c['title']} ({c['time']}) {c['link']}" for c in comments] or ["- (없음)"]
    L += ["", "## 수동 확인 목록 (자동 수집 불가 항목, 항상 같은 페이지)", "", "| 항목 | 확인 링크 |", "|---|---|"]
    L += [f"| {m['name']} | {m['url']} |" for m in cfg.get("manual_checks", [])]
    if bad:
        L += ["", "## 실패·검증필요 로그", ""]
        L += [f"- {r['name']} ({r['source']}): {r['note']}" for r in bad]
    name = "check_report.md" if check else "latest.md"
    (out_dir / name).write_text("\n".join(L), encoding="utf-8")
    return out_dir / name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="소스 점검만 하고 기록하지 않음")
    args = ap.parse_args()
    cfg = json.loads((BASE_DIR / "config.json").read_text(encoding="utf-8"))
    # API 키는 환경변수(GitHub Secrets)가 있으면 그걸 우선 사용 → 공개 저장소에 키가 올라가지 않음
    for k, env in [("fred", "FRED_API_KEY"), ("coingecko_demo", "COINGECKO_API_KEY"), ("arkham", "ARKHAM_API_KEY")]:
        if os.environ.get(env):
            cfg["keys"][k] = os.environ[env].strip()
    out_dir = Path(cfg["output_dir"])
    if not out_dir.is_absolute():
        out_dir = BASE_DIR / out_dir
    now_kst = dt.datetime.now(KST)
    recs, ctx = [], {}
    steps = [("Yahoo", lambda: c_yahoo(cfg)), ("FRED", lambda: c_fred(cfg)),
             ("현물", lambda: c_spot(cfg)), ("선물", lambda: c_futures(cfg)),
             ("Deribit", lambda: c_deribit(cfg)), ("CoinGecko", lambda: c_coingecko(cfg)),
             ("ETF 자금흐름", lambda: c_etf(cfg)), ("Polymarket", lambda: c_polymarket(cfg)),
             ("BGeometrics", lambda: c_bgeometrics(cfg)), ("Coin Metrics", lambda: c_coinmetrics(cfg, ctx)),
             ("Arkham", lambda: c_arkham(cfg, ctx))]
    for name, fn in steps:
        print(f"[수집] {name} ...", flush=True)
        try:
            recs += fn()
        except Exception:
            print(traceback.format_exc())
    print("[수집] 뉴스·코멘트 RSS ...", flush=True)
    try:
        news, news_status, wstart = c_news(cfg, now_kst)
    except Exception as e:
        news, news_status, wstart = [], [f"뉴스 수집 실패: {e}"], now_kst
    try:
        comments = c_commentary(cfg, now_kst)
    except Exception as e:
        comments = [{"source": "코멘트", "title": f"수집 실패: {e}", "link": "", "time": ""}]
    hist = load_history(out_dir / "history.csv")
    fill_prev_and_stats(recs, hist)
    import scoring
    try:
        score = scoring.compute(recs, hist, cfg, now_kst)
    except Exception:
        print(traceback.format_exc())
        score = None
    if score:
        recs += score["records"]
    extra = probe(cfg) if args.check else None
    path = write_outputs(out_dir, recs, news, news_status, wstart, comments, cfg, now_kst,
                         check=args.check, score=score, extra=extra)
    print("\n상태 요약")
    for r in recs:
        if r["group"] == "Z.점수":
            continue
        print(f"  [{r['status']:>6}] {r['name']}: {r['value']} {r['unit']}  ({r['source']})"
              + (f"  ← {r['note']}" if r['status'] != 'ok' else ""))
    print("  뉴스: " + " / ".join(news_status))
    if score:
        print(f"\n점수: 오늘 {score['total']} / 3일 평균 {score['avg3']} / 판정 {score['judgment']} (목표 비중 {score['target']}%)")
    print(f"\n저장 완료: {path}")


if __name__ == "__main__":
    sys.exit(main())
