# 코인 데일리 스냅샷

- 수집 시각: 2026-11-06 16:12 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 -9.9 / 3일 평균 -1.9 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | -25.0 |
| 파생·심리 | 30% | -10.0 |
| 밸류에이션 | 25% | 25.0 |
| 매크로 | 15% | -37.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.76 |
| 밸류에이션 | 가격÷STH-RP | +0 | +0 | 가격÷STH-RP 1.020 |
| 수급 | 현물 ETF 순유입 | -1 | -2 | 5일 합 -1066백만$ |
| 수급 | 거래소 순유입(7일) | +0 | +2 | 7일 순유입 분포 48백분위 |
| 수급 | 거래소 보유량(30일) | -1 | -1 | 30일 +1.87% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | +0 | +0 | 7일 +2.1% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0076% |
| 파생·심리 | RSI(14) | +1 | +0 | RSI 38.6 |
| 파생·심리 | 롱/숏 비율 | -2 | +1 | 롱/숏 분포 100백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +0 | OI 7일 +2.0%, 가격 -2.3% |
| 파생·심리 | 옵션 스큐 | -1 | +0 | +5.99 (풋 우위 확대, 전일 +2.38) |
| 매크로 | 나스닥 | -2 | -1 | 5일 -7.1% 급락 |
| 매크로 | DXY | +0 | +0 | 101.89, 20일 -0.3% |
| 매크로 | USD/JPY | +0 | +0 | 158.03 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -3 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 24315.0 | 25736.51 | pt | 2026-11-05 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -7.14 | -3.06 | % | 2026-11-05 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26497.06 | 26533.36 | pt | 2026-11-05 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 101.888 | 101.55 | pt | 2026-11-06 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | -0.32 | -0.9 | % | 2026-11-06 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 158.03 | 158.357 | 엔 | 2026-11-06 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | 0.14 | 0.07 | % | 2026-11-06 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.02 | 3.71 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-10-14 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.79 | 2.76 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-10-14 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.65 | 3.44 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.12 | 3.03 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -3 | -3 |  | 2026-11-06 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.929 | 6.548 | % | 2026-11-06 07:10 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.5535 | 2.7192 | 조$ | 2026-11-06 07:10 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | 74.6 | -115.6 | 백만$ | 2026-11-04 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 1거래일 연속 순유입 / 집계 기준일 2026-11-04 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -201.2 | -95.0 | 백만$ | 2026-11-04 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -1065.9 | -1003.1 | 백만$ | 2026-11-04 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | 1 | -3 | 일 | 2026-11-04 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 75969.06 | 80428.31 | USD | 2026-11-05 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 38.63 | 50.74 |  | 2026-11-05 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -2.33 | -1.01 | % | 2026-11-05 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.61 | 3.84 | 십억$ | 2026-11-05 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | 1.99 | 10.47 | % | 2026-11-05 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 2.95 | 2.43 | 배 | 2026-11-05 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 100.0 | 23.3 | 백분위 | 2026-11-05 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.0028 | 0.01 | % | 2026-11-06 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0076 | 0.0087 | % | 2026-11-06 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 40.89 | 37.17 |  | 2026-11-06 07:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 5.99 | 2.38 | vol pt | 2026-11-06 07:12 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-11-27, 콜 BTC-27NOV26-81000-C / 풋 BTC-27NOV26-71000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.7563 | 0.7817 |  | 2026-10-30 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.0201 | 1.0286 |  | 2026-10-30 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 74310.0 | 78250.0 | $ | 2026-10-30 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 75803.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 33709.5 | 22712.2 | BTC | 2026-11-05 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 32377.3 | 25114.1 | BTC | 2026-11-05 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -12925.0 | -37838.2 | BTC | 2026-11-05 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 47.8 | 10.0 | 백분위 | 2026-11-05 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | 1332.2 | -2401.9 | BTC | 2026-11-05 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | 1.87 | 1.27 | % | 2026-11-05 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2709957.0 | 2708410.0 | BTC | 2026-11-05 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (11-05 18:00 ~ 11-06 16:12 KST)

피드 상태: CoinDesk: 20건 / The Block: 9건 / Cointelegraph: 19건 / 블록미디어: 10건

- [블록미디어] 코인 세금 이렇게 바뀐다…과세 유예에서 손실 공제까지 Q&A (11-06 16:00) — https://www.blockmedia.co.kr/archives/1162278?utm_source=general&utm_medium=rss
- [Cointelegraph] Chainalysis says breach exposed password hashes and live tokens (11-06 15:54) — https://cointelegraph.com/news/chainalysis-cyberattack-password-hashes-live-tokens-exposed?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] [마감시황] 코스피, 6% 급락 끝 5000선 간신히 회복…코스닥도 5% 하락 (11-06 15:45) — https://www.blockmedia.co.kr/archives/1162369?utm_source=general&utm_medium=rss
- [Cointelegraph] Here’s what happened in crypto today (11-06 15:04) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 러시아, 디지털자산 금지에서 제도권 편입으로…12월 비트코인 거래 허용(종합) (11-06 14:51) — https://www.blockmedia.co.kr/archives/1162319?utm_source=general&utm_medium=rss
- [블록미디어] 유럽 최대 운용사 아문디, 이더리움에서 주가지수펀드 토큰화 (11-06 14:45) — https://www.blockmedia.co.kr/archives/1162310?utm_source=general&utm_medium=rss
- [CoinDesk] Zcash’s landmark NU7 upgrade goes live, speeding up private payments (11-06 14:14) — https://www.coindesk.com/tech/2026/11/06/zcash-s-landmark-nu7-upgrade-goes-live-speeding-up-private-payments
- [Cointelegraph] Crypto exchanges tout cold storage ratios after Binance attack (11-06 14:07) — https://cointelegraph.com/news/binance-hack-puts-crypto-exchanges-cold-wallet-ratio-under-spotlight?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 미국 민주당, 트럼프의 CZ 사면 과정 조사 예고…바이낸스·WLFI 거래 정조준 (11-06 14:00) — https://www.blockmedia.co.kr/archives/1162272?utm_source=general&utm_medium=rss
- [The Block] IREN’s bitcoin mining revenue drops 58% as firm plans full exit by year-end (11-06 13:29) — https://www.theblock.co/news/business/2026-11-05-irens-mining-revenue-drops-435783
- [블록미디어] 트럼프, 척 슈머에 이례적 호평…중간선거 이후 민주당에 우호적 태도 (11-06 13:00) — https://www.blockmedia.co.kr/archives/1162246?utm_source=general&utm_medium=rss
- [The Block] Ark Invest buys more Coinbase as shares plunge 10% in wider market rout (11-06 12:56) — https://www.theblock.co/news/markets/2026-11-05-ark-invest-buys-coinbase-trims-bullish-bitmine-435769
- [블록미디어] 미 AI 쇼크에 10억달러 청산·DePIN ‘직격탄’…비트코인 7만6000달러 붕괴 (11-06 12:45) — https://www.blockmedia.co.kr/archives/1162229?utm_source=general&utm_medium=rss
- [블록미디어] 세계 최대 비트코인 채굴업체 코어사이언티픽, 연내 채굴사업 완전 철수 (11-06 12:20) — https://www.blockmedia.co.kr/archives/1162237?utm_source=general&utm_medium=rss
- [블록미디어] 코스피 5000선 붕괴·비트코인 75K 후퇴…반도체 투매, 디지털자산에 독일까 기회일까 (11-06 12:00) — https://www.blockmedia.co.kr/archives/1162230?utm_source=general&utm_medium=rss
- [블록미디어] HYPE DAT 기업, 선물 중개업 등록 신청…다수당 교체에도 선물시장 진출 추진 (11-06 11:30) — https://www.blockmedia.co.kr/archives/1162219?utm_source=general&utm_medium=rss
- [CoinDesk] Hyperliquid treasury firm seeking U.S. regulatory nod as a domestic futures platform (11-06 11:24) — https://www.coindesk.com/policy/2026/11/05/hyperliquid-treasury-firm-seeking-u-s-regulatory-nod-as-a-domestic-futures-platform
- [CoinDesk] Bitcoin developer proposes ‘landmines’ to make quantum thieves lose their own BTC (11-06 10:30) — https://www.coindesk.com/tech/2026/11/05/bitcoin-developer-proposes-landmines-to-make-quantum-thieves-lose-their-own-btc
- [Cointelegraph] Core Scientific to quit Bitcoin mining by year-end as AI business surges (11-06 09:19) — https://cointelegraph.com/news/core-scientific-to-quit-bitcoin-mining-by-year-end-as-ai-business-surges?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] American Bitcoin’s $126M profit masks mining pressure as rivals turn to AI (11-06 07:43) — https://cointelegraph.com/news/american-bitcoins-126m-profit-masks-mining-pressure-ai?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Asian crypto exchanges batten down the hatches as hacks surge: Asia Express (11-06 07:18) — https://cointelegraph.com/magazine/asian-crypto-exchanges-bunker-down-as-hacks-surge-asia-express?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Hyperliquid Strategies files to become CFTC-registered FCM, posts $13.3 million in quaterly revenue (11-06 07:09) — https://www.theblock.co/news/markets/2026-11-05-hyperliquid-strategies-files-become-cftc-registered-fcm-posts-13-3-million-quaterly-revenue-435455
- [Cointelegraph] Crypto ally French Hill wins reelection but set to lose House chair (11-06 06:39) — https://cointelegraph.com/news/crypto-ally-french-hill-wins-reelection-arkansas?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Bitcoin erases post-election gains as Wall Street selloff triggers over $1 billion in crypto liquidations (11-06 05:11) — https://www.theblock.co/news/markets/2026-11-05-bitcoin-erases-post-election-gains-wall-street-selloff-liquidations-435434
- [Cointelegraph] Binance, Deribit revoke SignalPlus API keys after fake Teams invite attack (11-06 04:02) — https://cointelegraph.com/news/binance-deribit-revoke-signalplus-api-fake-teams-attack?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Base deploys Denim upgrade on mainnet, replacing Flashblocks with 200ms block times (11-06 04:00) — https://www.theblock.co/news/ecosystems/2026-11-05-base-deploys-denim-upgrade-on-mainnet-replacing-flashblocks-with-200ms-block-times-434433
- [CoinDesk] U.S. Justice Department assembles force to shield against foreign AI threats (11-06 03:59) — https://www.coindesk.com/policy/2026/11/05/u-s-justice-department-assembles-force-to-shield-against-foreign-ai-threats
- [CoinDesk] Bitcoin tumbles to $76,000 as collapsing AI trade drags stocks sharply lower (11-06 03:48) — https://www.coindesk.com/markets/2026/11/05/bitcoin-crypto-stocks-caught-in-ai-trade-meltdown-but-wintermute-trader-sees-glass-half-full
- [Cointelegraph] Fed, OCC check US banks after Binance hack as experts flag security risks (11-06 03:32) — https://cointelegraph.com/news/fed-occ-check-us-banks-binance-hack-security-risks?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Europe’s largest asset manager Amundi tokenizes equity index fund on Ethereum (11-06 03:09) — https://cointelegraph.com/news/amundi-tokenizes-european-equity-index-fund-ethereum?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Paraguay president resigns after collapse of Ueno digital bank (11-06 02:40) — https://cointelegraph.com/news/paraguay-president-resigns-after-collapse-ueno-digital-bank?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] What is TraderTraitor, the hacking squad behind the $6.3 billion Binance heist? (11-06 01:58) — https://www.coindesk.com/business/2026/11/05/what-is-tradertraitor-the-hacking-squad-behind-the-usd6-3-billion-binance-heist
- [The Block] Canary’s Injective ETF debuts on Nasdaq with exposure to staking rewards (11-06 01:53) — https://www.theblock.co/news/markets/2026-11-05-canary-staked-inj-etf-launches-nasdaq-injc-435115
- [CoinDesk] Standard Chartered and SBI back crypto insurer Soter as funding reaches $23.5 million (11-06 01:49) — https://www.coindesk.com/business/2026/11/05/soter-raises-usd23-5m-plus-btc-and-eth-as-banks-demand-theft-protection
- [Cointelegraph] Bitcoin crashes 6% to 7-week low as US stocks erase election gains (11-06 01:48) — https://cointelegraph.com/markets/bitcoin-price-crashes-7-week-low-stocks-election-gains?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Crypto for Advisors: Where investors stake crypto shapes how much of the reward they keep (11-06 01:13) — https://www.coindesk.com/coindesk-indices/2026/11/05/crypto-for-advisors-where-investors-stake-crypto-shapes-how-much-of-the-reward-they-keep
- [The Block] Anchorage Digital seeks CFTC swap dealer registration for crypto options business (11-06 01:00) — https://www.theblock.co/news/business/2026-11-05-anchorage-digital-seeks-cftc-swap-dealer-registration-for-crypto-options-business-434437
- [The Block] Payward-affiliated fund and clients buy AAVE token stake on secondary market (11-06 00:36) — https://www.theblock.co/news/business/2026-11-05-payward-affiliated-fund-clients-buy-aave-token-stake-secondary-market-aave-says-434798
- [CoinDesk] Gate CEO says crypto exchanges must prove they can survive a hack like Binance’s (11-05 23:21) — https://www.coindesk.com/business/2026/11/05/gate-ceo-says-crypto-exchanges-must-prove-they-can-survive-a-hack-like-binance-s
- [The Block] Samsung Wallet launches USDC accounts on Solana for US Galaxy users (11-05 23:19) — https://www.theblock.co/news/business/2026-11-05-samsung-wallet-launches-usdc-accounts-solana-us-galaxy-users-434523
- [CoinDesk] Kraken parent Payward and its clients buy AAVE tokens in DeFi investment push (11-05 23:00) — https://www.coindesk.com/business/2026/11/05/kraken-parent-payward-and-its-clients-buy-aave-tokens-in-defi-investment-push
- [Cointelegraph] Blockchain is ‘perfect solution’ for AI agent trust, VeChain CEO says (11-05 22:34) — https://cointelegraph.com/news/blockchain-is-perfect-solution-for-ai-agent-trust-vechain-ceo-says?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Can decentralized phone networks power the AI revolution? (11-05 22:30) — https://cointelegraph.com/magazine/can-decentralized-phone-networks-power-the-ai-revolution?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Google could take stake in bitcoin miner TeraWulf’s $19 billion AI project if Anthropic defaults (11-05 22:29) — https://www.coindesk.com/tech/2026/11/05/google-could-take-ownership-stake-in-bitcoin-miner-terawulf-s-ai-project-if-anthropic-defaults
- [CoinDesk] Binance cuts SignalPlus access after security warning, urges users to check accounts (11-05 21:55) — https://www.coindesk.com/tech/2026/11/05/binance-cuts-signalplus-access-after-security-warning-urges-users-to-check-accounts
- [CoinDesk] Ukraine’s central bank opposes crypto bill, citing monetary sovereignty concerns (11-05 21:50) — https://www.coindesk.com/business/2026/11/05/ukraine-s-central-bank-opposes-crypto-bill-citing-monetary-sovereignty-concerns
- [Cointelegraph] Trump’s memecoin ventures derailed CLARITY Act, Scaramucci says (11-05 21:39) — https://cointelegraph.com/news/scaramucci-trump-memecoins-clarity-act-failure?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin is resilient, but leverage is missing and demand still tepid (11-05 21:27) — https://www.coindesk.com/daybook-us/2026/11/05/bitcoin-is-resilient-but-leverage-is-missing-and-demand-still-tepid
- [CoinDesk] Bitcoin miners are oversold following 35% October rout, VanEck says (11-05 20:49) — https://www.coindesk.com/markets/2026/11/05/bitcoin-miners-are-oversold-following-35-october-rout-says-vaneck
- [CoinDesk] Trump-linked American Bitcoin swings to $126 million profit but misses revenue estimates (11-05 20:45) — https://www.coindesk.com/business/2026/11/05/trump-linked-american-bitcoin-swings-to-usd126-million-profit-in-q3-2026
- [Cointelegraph] Thailand to block Bitget in December over unlicensed crypto trading (11-05 20:33) — https://cointelegraph.com/news/thailand-block-bitget-december-unlicensed-crypto-trading?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin holds above $80,000 after Wednesday’s jump as injective rallies on staked ETF listing (11-05 20:30) — https://www.coindesk.com/markets/2026/11/05/bitcoin-holds-above-usd80-000-after-wednesday-s-jump-as-injective-rallies-on-staked-etf-listing
- [CoinDesk] Live updates: Bitcoin drops more than 5% as stocks close out worst day since April 2025 (11-05 19:57) — https://www.coindesk.com/business/2026/11/05/live-updates-bitcoin-steady-around-usd80-000-as-markets-rally-after-democratic-sweep
- [CoinDesk] Mercado Bitcoin hack continued hours after exchange said attack was contained, report finds (11-05 19:44) — https://www.coindesk.com/business/2026/11/05/mercado-bitcoin-hack-continued-hours-after-exchange-said-attack-was-contained-report-finds
- [Cointelegraph] Bitcoin win rate vs. S&P 500 recovers as post-midterm history favors stocks (11-05 19:28) — https://cointelegraph.com/markets/bitcoin-win-rate-sp-500-us-midterms-stocks-gains?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin miner Riot could pay Anthropic 12% interest under $28 billion AI deal (11-05 18:36) — https://www.coindesk.com/tech/2026/11/05/bitcoin-miner-riot-could-pay-anthropic-12-interest-under-usd28-billion-ai-deal
- [Cointelegraph] South Korea seeks 4th crypto tax delay, targets 2029 start (11-05 18:35) — https://cointelegraph.com/news/south-korea-crypto-tax-fourth-delay-2029?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] France budget rejection sidelines stablecoin tax, wallet reporting (11-05 18:04) — https://cointelegraph.com/news/france-rejects-budget-revenue-sidelines-crypto-amendments?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

## 전문가 코멘트 (최근 7일, RSS)

- [Sean Farrell (구글 알리미)] (피드 URL 미설정) () 

## 수동 확인 목록 (자동 수집 불가 항목, 항상 같은 페이지)

| 항목 | 확인 링크 |
|---|---|
| 채굴자→거래소 유입 (CryptoQuant) | https://cryptoquant.com/asset/btc/chart/miner-flows |
| 원조 고래비율 (CryptoQuant, 근사치 대조용) | https://cryptoquant.com/asset/btc/chart/flow-indicator/exchange-whale-ratio |
| 고래 대량 이동 (Whale Alert) | https://whale-alert.io/ |
| Glassnode / Sean Farrell X 목록 | (본인 X 목록 URL 입력) |

## 실패·검증필요 로그

- 고래비율(근사) (Arkham + Coin Metrics): Arkham 키 없음