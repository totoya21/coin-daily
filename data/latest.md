# 코인 데일리 스냅샷

- 수집 시각: 2026-11-18 16:50 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 7.6 / 3일 평균 4.9 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | -37.5 |
| 파생·심리 | 30% | 40.0 |
| 밸류에이션 | 25% | 50.0 |
| 매크로 | 15% | -37.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.65 |
| 밸류에이션 | 가격÷STH-RP | +1 | +1 | 가격÷STH-RP 0.979 |
| 수급 | 현물 ETF 순유입 | -1 | -2 | 5일 합 -856백만$ |
| 수급 | 거래소 순유입(7일) | +0 | -1 | 7일 순유입 분포 48백분위 |
| 수급 | 거래소 보유량(30일) | -1 | -1 | 30일 +1.04% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | -1 | -1 | 7일 +10.8% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +2 | +1 | 3회 평균 -0.0001% |
| 파생·심리 | RSI(14) | +2 | +2 | RSI 24.1 |
| 파생·심리 | 롱/숏 비율 | +0 | +0 | 롱/숏 분포 60백분위 |
| 파생·심리 | 미결제약정(OI) | +1 | +1 | OI 7일 -23.6%, 가격 -12.0% (레버리지 정리) |
| 파생·심리 | 옵션 스큐 | -1 | +0 | +5.46 (풋 우위 확대, 전일 +4.43) |
| 매크로 | 나스닥 | -1 | -1 | 50일선 아래 |
| 매크로 | DXY | -1 | -1 | 103.73, 20일 +1.9% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 159.28 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -4 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 24328.381 | 24509.76 | pt | 2026-11-17 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -2.94 | -2.94 | % | 2026-11-17 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26268.27 | 26310.13 | pt | 2026-11-17 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 103.734 | 103.49 | pt | 2026-11-18 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.92 | 1.81 | % | 2026-11-18 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 159.281 | 159.523 | 엔 | 2026-11-18 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | 0.36 | 0.78 | % | 2026-11-18 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.08 | 4.02 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.87 | 2.79 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.65 | 3.44 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.12 | 3.03 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -4 | -4 |  | 2026-11-18 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 7.875 | 7.885 | % | 2026-11-18 07:49 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.2263 | 2.217 | 조$ | 2026-11-18 07:49 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | 8.0 | -185.5 | 백만$ | 2026-11-16 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 1거래일 연속 순유입 / 집계 기준일 2026-11-16 |
| B.자금흐름 | IBIT(블랙록) 순유입 | 76.5 | -143.5 | 백만$ | 2026-11-16 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -856.4 | -1065.4 | 백만$ | 2026-11-16 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | 1 | -7 | 일 | 2026-11-16 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 64873.18 | 64816.79 | USD | 2026-11-17 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 24.14 | 23.91 |  | 2026-11-17 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -11.97 | -13.88 | % | 2026-11-17 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 2.95 | 2.99 | 십억$ | 2026-11-17 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -23.55 | -22.52 | % | 2026-11-17 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 2.7 | 2.93 | 배 | 2026-11-17 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 60.0 | 66.7 | 백분위 | 2026-11-17 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | -0.0011 | -0.0007 | % | 2026-11-18 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | -0.0001 | 0.004 | % | 2026-11-18 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 43.88 | 43.64 |  | 2026-11-18 07:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 5.46 | 4.43 | vol pt | 2026-11-18 07:50 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-12-25, 콜 BTC-25DEC26-72000-C / 풋 BTC-25DEC26-60000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.653 | 0.6457 |  | 2026-11-11 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 0.9789 | 0.9751 |  | 2026-11-11 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 66307.0 | 66601.0 | $ | 2026-11-11 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 64908.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 28667.9 | 28742.8 | BTC | 2026-11-17 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 33042.7 | 26181.8 | BTC | 2026-11-17 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -14187.2 | -3090.7 | BTC | 2026-11-17 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 47.8 | 83.3 | 백분위 | 2026-11-17 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -4374.7 | 2561.0 | BTC | 2026-11-17 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | 1.04 | 1.19 | % | 2026-11-17 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2707552.0 | 2711617.0 | BTC | 2026-11-17 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (11-17 18:00 ~ 11-18 16:50 KST)

피드 상태: CoinDesk: 24건 / The Block: 20건 / Cointelegraph: 19건 / 블록미디어: 10건

- [CoinDesk] Google finds self-running AI hacking tool with Russian comments in its files (11-18 16:37) — https://www.coindesk.com/tech/2026/11/18/google-finds-self-running-ai-hacking-tool-with-russian-comments-in-its-files
- [CoinDesk] Live updates: Bitcoin stuck near $65,000 as popular 'basis trade' returns dry up (11-18 16:27) — https://www.coindesk.com/business/2026/11/18/live-updates-bitcoin-stuck-near-usd65-000-as-popular-basis-trade-returns-dry-up
- [블록미디어] 유에스디에이아이, 코벡스AI에 3800만달러 추가 지원…GPU 금융 확대 (11-18 16:05) — https://www.blockmedia.co.kr/archives/1167421?utm_source=general&utm_medium=rss
- [블록미디어] ‘상장 눈앞’ 앤트로픽 최종 몸값은 얼마?… 무기한 선물 시장은 이 금액 찍었다 (11-18 15:58) — https://www.blockmedia.co.kr/archives/1167485?utm_source=general&utm_medium=rss
- [블록미디어] [마감시황] 코스피, 엔비디아 훈풍에 5000선 회복…반도체주 강세 (11-18 15:53) — https://www.blockmedia.co.kr/archives/1167483?utm_source=general&utm_medium=rss
- [블록미디어] 코인 시장 침체에 손발 묶인 韓 거래소, 수익 악화 대안이 없다 (11-18 15:23) — https://www.blockmedia.co.kr/archives/1167455?utm_source=general&utm_medium=rss
- [블록미디어] 비트코인·이더리움 ETF 하루 2억6900만달러 유출…블랙록서 매도 집중 (11-18 15:12) — https://www.blockmedia.co.kr/archives/1167452?utm_source=general&utm_medium=rss
- [Cointelegraph] Here’s what happened in crypto today (11-18 15:00) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] AI로 만든 사기, AI가 막았다…코인베이스, 470만달러 피해 차단 (11-18 14:50) — https://www.blockmedia.co.kr/archives/1167446?utm_source=general&utm_medium=rss
- [블록미디어] 민주당, 트럼프 13%p 앞섰던 알래스카까지 가져왔다…상원 56석 확보 (11-18 14:48) — https://www.blockmedia.co.kr/archives/1167445?utm_source=general&utm_medium=rss
- [블록미디어] 1039만달러 유출 후폭풍…아브락사스, 하이퍼리퀴드 2억달러 포지션 전량 정리 (11-18 14:45) — https://www.blockmedia.co.kr/archives/1167376?utm_source=general&utm_medium=rss
- [CoinDesk] U.S. judge says Ethereum has ‘no terms of use,’ clears MIT brothers of $25 million fraud (11-18 14:30) — https://www.coindesk.com/policy/2026/11/18/u-s-judge-says-ethereum-has-no-terms-of-use-clears-mit-brothers-of-usd25-million-fraud
- [블록미디어] 비트코인보다 더 빠진 BTC DAT주…스트래티지 보통주 MSTR, 우선주보다 싸졌다 (11-18 14:30) — https://www.blockmedia.co.kr/archives/1167398?utm_source=general&utm_medium=rss
- [블록미디어] 세계은행, 개발자금 지급에 스테이블코인 도입 추진…시티·써클과 협력 (11-18 14:18) — https://www.blockmedia.co.kr/archives/1167403?utm_source=general&utm_medium=rss
- [The Block] Ark Invest buys crypto stocks as it sells $85 million in Nvidia, Coinbase brings onchain loans to New York, and more (11-18 14:01) — https://www.theblock.co/newsletters/the-daily/2026-11-18-ark-invest-crypto-stocks-nvidia-coinbase-loans-new-york-crypto-news-442902
- [CoinDesk] Bitcoin's 12% slide through key support looks scary, but history says give it 3 months. (11-18 13:34) — https://www.coindesk.com/markets/2026/11/18/bitcoin-s-rare-12-crash-through-its-200-week-average-has-a-bullish-track-record
- [CoinDesk] XRP whales moved $270 million during the selloff. The coins didn’t go to exchanges (11-18 13:28) — https://www.coindesk.com/markets/2026/11/18/xrp-whales-moved-usd270-million-during-the-selloff-the-coins-didn-t-go-to-exchanges
- [The Block] World Bank Group taps Circle and Citi to test stablecoin-based fund disbursements (11-18 13:21) — https://www.theblock.co/news/business/2026-11-17-world-bank-group-citi-circle-fund-disbursements-442924
- [The Block] Coinbase AI defense blocks $4.7 million from being sent to deepfake Elon Musk scam (11-18 11:47) — https://www.theblock.co/news/defi/2026-11-17-coinbase-ai-defense-deepfake-elon-musk-442918
- [The Block] What’s happening to crypto startup valuations? (11-18 11:40) — https://www.theblock.co/newsletters/the-funding/2026-11-17-crypto-startup-valuations-442903
- [Cointelegraph] Ledger hardware implant saga reaches Dubai’s Virgin Megastore (11-18 11:39) — https://cointelegraph.com/news/ledger-hardware-implant-saga-reaches-dubais-virgin-megastore?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] CFTC nominee questions public benefit of prediction markets as legal fight grows (11-18 09:46) — https://www.coindesk.com/policy/2026/11/17/nominee-says-u-s-cftc-must-think-hard-about-public-benefit-of-prediction-markets
- [Cointelegraph] Nvidia board rejects Huang comeback despite record $116B quarter (11-18 09:16) — https://cointelegraph.com/markets/nvidia-board-rejects-huang-comeback-amid-record-116b-quarter?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Trump’s CFTC picks face Senate scrutiny as prediction market turf war heats up (11-18 08:32) — https://www.theblock.co/news/regulation/2026-11-17-trumps-cftc-picks-face-senate-scrutiny-as-prediction-market-turf-war-heats-up-442909
- [The Block] Robinhood shrugs off Kalshi equities threat as Mizuho sees 86% HOOD upside (11-18 07:23) — https://www.theblock.co/news/business/2026-11-17-robinhoods-non-sports-prediction-market-share-doubles-mizuho-442904
- [Cointelegraph] CFTC halts some Kalshi Trump mention markets over manipulation concerns (11-18 07:20) — https://cointelegraph.com/news/cftc-kalshi-trump-mention-markets-review?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Maple Finance CEO targets up to $15B in assets by the end of 2027 (11-18 06:56) — https://cointelegraph.com/news/maple-finance-15b-assets-target-2027?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Nvidia shares rise on earnings beat, raised outlook despite leadership uncertainty (11-18 06:25) — https://www.coindesk.com/markets/2026/11/17/nvidia-tops-estimates-issues-strong-guidance-adds-usd150-billion-to-buyback-authorization
- [Cointelegraph] Eastern Europe crypto flows fall 7.9% as Ukraine draws $12B in stablecoins (11-18 05:05) — https://cointelegraph.com/news/eastern-europe-crypto-activity-decline-chainalysis?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Coinbase CEO says AI agents will account for '99.9%' of transactions within a decade (11-18 04:45) — https://www.coindesk.com/markets/2026/11/17/coinbase-ceo-says-ai-agents-will-account-for-99-9-of-transactions-within-a-decade
- [The Block] Jito’s Lucas Bruder says crypto builders need to ‘slow down’ and fix security weaknesses (11-18 04:29) — https://www.theblock.co/news/ecosystems/2026-11-17-jito-lucas-bruder-crypto-builders-need-slow-down-fix-security-weaknesses-442850
- [CoinDesk] Predictions platform Kalshi complies with order to halt Trump mention contracts (11-18 04:16) — https://www.coindesk.com/policy/2026/11/17/predictions-platform-kalshi-complies-with-order-to-halt-trump-mention-contracts
- [The Block] Coinbase expands onchain crypto loans to New York via Morpho (11-18 03:00) — https://www.theblock.co/news/business/2026-11-17-coinbase-borrow-new-york-morpho-442842
- [Cointelegraph] Lighter incident exposes risks beyond withdrawal controls (11-18 02:51) — https://cointelegraph.com/news/lighter-incident-exposes-risks-beyond-withdrawal-controls?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Druckenmiller says he is short copper, warns of economic weakness in 2027 (11-18 02:42) — https://www.coindesk.com/business/2026/11/17/druckenmiller-says-he-is-short-copper-warns-of-economic-weakness-in-2027
- [The Block] Fomo pays creators $30 million, sharing ‘lion’s share’ of revenue, Se Yong Park says (11-18 02:41) — https://www.theblock.co/news/business/2026-11-17-fomo-pays-creators-30-million-sharing-lions-share-revenue-park-says-442332
- [Cointelegraph] Fed’s Waller cites Binance hack in warning over tokenized finance (11-18 02:39) — https://cointelegraph.com/news/feds-waller-cites-binance-hack-in-warning-over-tokenized-finance?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Everyone is Trading Tokenized Nvidia Derivatives (11-18 02:15) — https://www.theblock.co/newsletters/data-and-insights/2026-11-17-everyone-is-trading-tokenized-nvidia-derivatives-442818
- [CoinDesk] U.S. Fed Governor Waller pitches keeping central bank at the center of tokenization (11-18 02:00) — https://www.coindesk.com/policy/2026/11/17/u-s-fed-governor-waller-pitches-keeping-central-bank-at-the-center-of-tokenization
- [Cointelegraph] Bitcoin drops 2.5% as Nvidia stock risks new 5-month lows into Q3 earnings (11-18 01:39) — https://cointelegraph.com/markets/bitcoin-drops-25-nvidia-stock-risks-new-5-month-low-q3-earnings?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Alpaca says tokenization network tops $10 billion in minting and redemption volume (11-18 01:35) — https://www.theblock.co/news/business/2026-11-17-alpaca-says-tokenization-network-tops-10-billion-minting-redemption-volume-442667
- [The Block] Anchorage, Kalshi Prime let institutions use custodied bitcoin as margin (11-18 00:53) — https://www.theblock.co/news/business/2026-11-17-anchorage-digital-kalshi-prime-hodl-margining-bitcoin-collateral-442568
- [CoinDesk] Hong Kong, Swift test tokenized deposits as banks chase stablecoin-style speed (11-18 00:11) — https://www.coindesk.com/business/2026/11/17/hong-kong-swift-test-tokenized-deposits-as-banks-chase-stablecoin-style-speed
- [Cointelegraph] Solana Foundation takes majority interest in crypto data firm CoinGecko (11-17 23:45) — https://cointelegraph.com/news/coingecko-solana-foundation-majority-stake?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Solana’s Trump memecoin launch tested infrastructure ahead of institutional push, Lily Liu says (11-17 23:27) — https://www.theblock.co/news/ecosystems/2026-11-17-solana-trump-memecoin-launch-tested-infrastructure-institutional-push-lily-liu-says-442132
- [The Block] Bitwise launches ZDAY, its first non-crypto ETF, to bet on AI cyber defense (11-17 23:00) — https://www.theblock.co/news/markets/2026-11-17-bitwise-zday-ai-cyber-defense-etf-442062
- [The Block] Bernstein sees upside for bitcoin miners Riot and TeraWulf, citing discounts to implied AI data center values (11-17 22:56) — https://www.theblock.co/news/markets/2026-11-17-bernstein-sees-upside-for-bitcoin-miners-riot-and-terawulf-citing-discounts-to-implied-ai-data-center-values-442125
- [Cointelegraph] Bitcoin to $1M by 2030? ‘Almost certainly not,’ says Dragonfly’s Qureshi (11-17 22:30) — https://cointelegraph.com/magazine/bitcoin-to-1m-by-2030-almost-certainly-not-says-dragonflys-qureshi?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] ARK sells $85M in Nvidia shares ahead of chipmaker’s Q3 earnings results (11-17 22:12) — https://cointelegraph.com/news/ark-crypto-stock-purchases-nvidia-staking-etf-sales?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Stablecoin infrastructure firm Avenia raises $25 million in Series A extension (11-17 22:08) — https://www.theblock.co/news/deals/2026-11-17-avenia-funding-stablecoin-crypto-infrastructure-442119
- [CoinDesk] Ethereum's Glamsterdam upgrade risks breaking up to 15,000 automated apps (11-17 22:02) — https://www.coindesk.com/tech/2026/11/17/ethereum-s-glamsterdam-upgrade-risks-breaking-up-to-15-000-contracts
- [CoinDesk] Decentralized exchange Grvt looks to makes commodity trading more predictable with stable funding perps (11-17 22:00) — https://www.coindesk.com/markets/2026/11/17/decentralized-exchange-grvt-makes-commodity-trading-more-predictable-with-stable-funding-perps
- [The Block] Grvt launches RWA perpetuals with funding tied to traditional markets (11-17 22:00) — https://www.theblock.co/news/ecosystems/2026-11-17-grvt-launches-rwa-perpetuals-with-funding-tied-to-traditional-markets-442089
- [Cointelegraph] Revolut plans four blockchain-based funds for private markets, chair says (11-17 21:24) — https://cointelegraph.com/news/revolut-four-blockchain-funds-private-markets?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Crypto's 'casino-chips' are disappearing, adding to pain from spot ETF outflows (11-17 21:16) — https://www.coindesk.com/daybook-us/2026/11/17/crypto-s-casino-chips-are-disappearing-adding-to-pain-from-spot-etf-outflows
- [CoinDesk] Ex-OpenAI researcher fund dumps bitcoin miners, cuts IREN 94% after portfolio slump (11-17 21:00) — https://www.coindesk.com/business/2026/11/17/ex-openai-researcher-fund-dumps-bitcoin-miners-cuts-iren-94-after-portfolio-slump
- [The Block] Lighter reopens withdrawals after trader’s API key leak, returns about $5 million in USDC (11-17 21:00) — https://www.theblock.co/news/defi/2026-11-17-lighter-reopens-withdrawals-after-traders-api-key-leak-returns-about-5-million-in-usdc-442113
- [CoinDesk] Bitcoin remains penned in near $64,000 even as ETF outflow streak ends (11-17 20:36) — https://www.coindesk.com/markets/2026/11/17/bitcoin-remains-penned-in-near-usd64-000-even-as-etf-outflow-streak-ends
- [Cointelegraph] US senators seek SEC answers on tokenized stock money laundering risks (11-17 20:36) — https://cointelegraph.com/news/us-senators-sec-tokenized-stock-safeguards?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Solana Foundation takes majority stake in crypto data provider CoinGecko (11-17 20:29) — https://www.coindesk.com/business/2026/11/17/solana-foundation-takes-majority-stake-in-crypto-data-provider-coingecko

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