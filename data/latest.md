# 코인 데일리 스냅샷

- 수집 시각: 2026-11-21 16:36 KST
- 결과: 성공 38 / 실패·검증필요 2 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 12.5 / 3일 평균 7.1 / 오늘 구간 '중립'
- 판정 가능 지표 14/17개 (82%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | -37.5 |
| 파생·심리 | 30% | 62.5 |
| 밸류에이션 | 25% | 50.0 |
| 매크로 | 15% | -50.0 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.34 |
| 밸류에이션 | 가격÷STH-RP | +1 | +1 | 가격÷STH-RP 0.856 |
| 수급 | 현물 ETF 순유입 | -2 | -1 | 3거래일 연속 순유출 |
| 수급 | 거래소 순유입(7일) | +1 | +1 | 7일 순유입 분포 29백분위 |
| 수급 | 거래소 보유량(30일) | -1 | -1 | 30일 +1.30% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | -1 | -1 | 7일 +13.1% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +2 | +2 | 3회 평균 -0.0019% |
| 파생·심리 | RSI(14) | +2 | +2 | RSI 17.4 |
| 파생·심리 | 롱/숏 비율 | +0 | -2 | 롱/숏 분포 50백분위 |
| 파생·심리 | 미결제약정(OI) | +1 | +1 | OI 7일 -15.5%, 가격 -13.8% (레버리지 정리) |
| 파생·심리 | 옵션 스큐 | 제외 | -1 | 값 없음 |
| 매크로 | 나스닥 | -2 | -2 | 5일 -10.0% 급락 |
| 매크로 | DXY | -1 | -1 | 103.81, 20일 +2.0% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 159.71 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -4 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 22617.73 | 23879.199 | pt | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -10.02 | -5.86 | % | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26113.44 | 26187.75 | pt | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 103.81 | 103.9 | pt | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.96 | 1.87 | % | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 159.707 | 159.381 | 엔 | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | -0.11 | -0.52 | % | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.08 | 4.02 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.87 | 2.79 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.65 | 3.44 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.12 | 3.03 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -4 | -4 |  | 2026-11-21 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 8.608 | 8.204 | % | 2026-11-21 07:31 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.0165 | 2.1305 | 조$ | 2026-11-21 07:31 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | -582.2 | -306.4 | 백만$ | 2026-11-19 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 3거래일 연속 순유출 / 집계 기준일 2026-11-19 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -541.1 | -148.7 | 백만$ | 2026-11-19 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -1306.0 | -1007.8 | 백만$ | 2026-11-19 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | -3 | -2 | 일 | 2026-11-19 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 58814.99 | 61913.23 | USD | 2026-11-20 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 17.44 | 20.52 |  | 2026-11-20 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -13.81 | -13.25 | % | 2026-11-20 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 2.92 | 3.05 | 십억$ | 2026-11-20 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -15.48 | -21.13 | % | 2026-11-20 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 2.69 | 2.97 | 배 | 2026-11-20 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 50.0 | 96.7 | 백분위 | 2026-11-20 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | -0.0059 | 0.0038 | % | 2026-11-21 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | -0.0019 | -0.0013 | % | 2026-11-21 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 55.21 | 46.69 |  | 2026-11-21 07:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐 |  | 9.05 |  |  | fail | [Deribit](https://www.deribit.com/options/BTC) | 429 Client Error: Too Many Requests for url: https://www.deribit.com/api/v2/public/ticker?instrument_name=BTC-25DEC26-54000-C |
| D.온체인 | MVRV Z-Score | 0.338 | 0.4712 |  | 2026-11-14 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 0.856 | 0.9092 |  | 2026-11-14 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 68751.0 | 68061.0 | $ | 2026-11-14 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 58851.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 41305.5 | 23177.0 | BTC | 2026-11-20 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 41820.9 | 25023.1 | BTC | 2026-11-20 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -24870.2 | -26484.3 | BTC | 2026-11-20 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 28.9 | 24.4 | 백분위 | 2026-11-20 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -515.4 | -1846.1 | BTC | 2026-11-20 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | 1.3 | 1.07 | % | 2026-11-20 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2709906.0 | 2710118.0 | BTC | 2026-11-20 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (11-20 18:00 ~ 11-21 16:36 KST)

피드 상태: CoinDesk: 17건 / The Block: 12건 / Cointelegraph: 12건 / 블록미디어: 10건

- [CoinDesk] Bitcoin nodes could be stalled by repeating one ID 50,000 times. AI found the bug (11-21 15:16) — https://www.coindesk.com/markets/2026/11/21/bitcoin-nodes-could-be-stalled-by-repeating-one-id-50-000-times-ai-found-the-bug
- [CoinDesk] XRP falls 10% as long bets unwind and ETF assets slip below $1 billion (11-21 14:59) — https://www.coindesk.com/markets/2026/11/21/xrp-falls-10-as-long-bets-unwind-and-etf-assets-slip-below-usd1-billion
- [Cointelegraph] Hong Kong pushes to bring crypto custodians, advisers under licensing rules (11-21 14:40) — https://cointelegraph.com/news/hong-kong-crypto-custody-advisory-licensing-bill?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 앤트로픽 급락, 비트코인에 불똥…월가IB · 투자자 ‘네 탓’ 공방 (11-21 14:36) — https://www.blockmedia.co.kr/archives/1168933?utm_source=general&utm_medium=rss
- [블록미디어] 엑스알피 0.90달러 이탈…추가 하락 경고속 다음 지지선은? (11-21 14:05) — https://www.blockmedia.co.kr/archives/1168930?utm_source=general&utm_medium=rss
- [블록미디어] 비트코인 55K로 밀려, 공포감 확산 “5만달러까지 하락” 경고 나와(상보) (11-21 13:54) — https://www.blockmedia.co.kr/archives/1168927?utm_source=general&utm_medium=rss
- [블록미디어] [속보] 비트코인 5만5000달러대로 하락 (11-21 13:45) — https://www.blockmedia.co.kr/archives/1168925?utm_source=general&utm_medium=rss
- [The Block] JPMorgan says bitcoin’s price drop pressures miners, Senate passes ‘Death Bets Act’, and more (11-21 13:30) — https://www.theblock.co/newsletters/the-daily/2026-11-20-jpmorgan-bitcoin-price-drop-miners-senate-passes-death-bets-act-more-crypto-news-444786
- [CoinDesk] Bitcoin tanks below $57,000 for the first time in two years, and its not alone (11-21 13:10) — https://www.coindesk.com/markets/2026/11/21/bitcoin-tanks-below-usd57-000-for-the-first-time-in-two-years-and-its-not-alone
- [블록미디어] 비트코인 5만7000달러선 붕괴…15.3억달러 강제 청산 (11-21 13:05) — https://www.blockmedia.co.kr/archives/1168913?utm_source=general&utm_medium=rss
- [블록미디어] HYPE 최대 롱 고래, 청산 피하려 500만달러 추가 투입 (11-21 12:59) — https://www.blockmedia.co.kr/archives/1168900?utm_source=general&utm_medium=rss
- [블록미디어] 트럼프 “中엔 구형 칩만”…반도체주·비트코인 동반 급락 (11-21 12:31) — https://www.blockmedia.co.kr/archives/1168893?utm_source=general&utm_medium=rss
- [블록미디어] 데리비트 19분 거래 중단…파생상품 거래소 안정성 ‘도마 위’ (11-21 11:31) — https://www.blockmedia.co.kr/archives/1168886?utm_source=general&utm_medium=rss
- [블록미디어] 스트래티지, 비트코인 매입 전 ‘세 가지’ 본다 (11-21 10:32) — https://www.blockmedia.co.kr/archives/1168884?utm_source=general&utm_medium=rss
- [블록미디어] ‘예측시장’ 칼시, 뉴욕주 법원行…본사 영업 전면중단 위기 (11-21 09:54) — https://www.blockmedia.co.kr/archives/1168875?utm_source=general&utm_medium=rss
- [CoinDesk] Kalshi races to get ahead of New York order that could shut down exchange (11-21 07:51) — https://www.coindesk.com/policy/2026/11/20/kalshi-races-to-get-ahead-of-new-york-order-that-could-shut-down-exchange
- [CoinDesk] Fairmint plans tokenized stock venue on Canton, Ethereum under SEC experiment (11-21 07:05) — https://www.coindesk.com/business/2026/11/20/fairmint-plans-tokenized-stock-venue-on-canton-ethereum-under-sec-experiment
- [The Block] DCG’s Zcash miner Fortitude clears vote for Nasdaq listing as ZEC retreats from all-time high (11-21 06:40) — https://www.theblock.co/news/business/2026-11-20-dcgs-zcash-miner-fortitude-clears-vote-nasdaq-listing-zec-retreats-all-time-high-444784
- [The Block] Rep. Casten seeks to curb prediction market insider trading with DOJ whistleblower program (11-21 04:41) — https://www.theblock.co/news/regulation/2026-11-20-rep-casten-seeks-curb-prediction-market-insider-trading-doj-whistleblower-program-444779
- [Cointelegraph] Wrapped Monero token crashes 99.8% amid suspected $13.5M exploit (11-21 04:37) — https://cointelegraph.com/news/wrapped-monero-token-crashes-998-amid-suspected-135m-exploit?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Sky Protocol sees $2 billion in stablecoin withdrawals, disputes illicit fund claims (11-21 03:37) — https://cointelegraph.com/news/sky-protocol-sees-2b-in-stablecoin-withdrawals-disputes-illicit-fund-claims?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Binance hack laundering ramps up as $149 million in bitcoin mixed through coinjoins: Elliptic (11-21 03:22) — https://www.theblock.co/news/markets/2026-11-20-binance-hack-laundering-ramps-up-149-million-bitcoin-mixed-coinjoins-elliptic-444758
- [The Block] JPMorgan says bitcoin price correction widens gap to estimated $86,000 production cost (11-21 03:17) — https://www.theblock.co/news/markets/2026-11-20-jpmorgan-bitcoin-price-correction-gap-86000-production-cost-444763
- [CoinDesk] Bitcoin plunges below $59,000 as rush to cash puts new bear market lows back in play (11-21 03:13) — https://www.coindesk.com/markets/2026/11/20/bitcoin-plunges-below-usd59-000-as-rush-to-cash-puts-new-bear-market-lows-back-in-play
- [Cointelegraph] Bitcoin falls below $60K for first time since July amid broader market selloff (11-21 01:55) — https://cointelegraph.com/markets/bitcoin-falls-below-60k-for-first-time-since-july-amid-broader-market-selloff?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Wagyu’s XMR1 wrapped Monero plunges 99% after $13 million hack as founder promises refunds (11-21 01:11) — https://www.theblock.co/news/defi/2026-11-20-wagyus-xmr1-wrapped-monero-plunges-99-after-13-million-hack-founder-promises-refunds-444747
- [Cointelegraph] US Senate advances prediction market restrictions with DEATH BETS Act (11-21 00:55) — https://cointelegraph.com/news/us-senate-advances-prediction-market-restrictions-with-death-bets-act?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin price drops to $60K as Anthropic drops to $87 in tech sell-off (11-21 00:52) — https://cointelegraph.com/markets/bitcoin-hits-new-20-week-low-anthropic-drops-87-tech-sell-off?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] DBS bets it can lose the deposit and keep the client (11-21 00:32) — https://cointelegraph.com/news/dbs-bets-it-can-lose-the-deposit-and-keep-the-client?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Former Point72 head of proprietary research says AI could turn data into a new asset class for Wall Street (11-20 23:54) — https://www.coindesk.com/markets/2026/11/20/former-point72-head-of-proprietary-research-says-ai-could-turn-data-into-a-new-asset-class-for-wall-street
- [The Block] Rep. Horsford sees opening for House vote on crypto tax bill before Congress ends (11-20 23:51) — https://www.theblock.co/news/regulation/2026-11-20-rep-horsford-sees-opening-house-vote-crypto-tax-bill-before-congress-ends-444720
- [CoinDesk] Hong Kong moves to extend crypto licensing rules to brokers, advisers and custodians (11-20 23:38) — https://www.coindesk.com/policy/2026/11/20/hong-kong-moves-to-extend-crypto-licensing-rules-to-brokers-advisers-and-custodians
- [The Block] Wintermute policy chief calls for crypto lobby to ‘clean house’ in D.C. (11-20 23:36) — https://www.theblock.co/news/regulation/2026-11-20-wintermute-policy-chief-calls-for-crypto-lobby-clean-house-d-c-444721
- [CoinDesk] U.S. Senate passes bill to ban prediction market bets on war and death (11-20 23:25) — https://www.coindesk.com/policy/2026/11/20/u-s-senated-passes-bill-to-ban-prediction-market-best-on-war-and-death
- [CoinDesk] Live news: Bitcoin slips to fresh lows below $59,000 as Anthropic slides after Nasdaq debut (11-20 22:35) — https://www.coindesk.com/tech/2026/11/20/live-news-bitcoin-hovers-just-above-usd61-000-as-anthropic-slides-13-after-nasdaq-debut
- [CoinDesk] Bitcoin bots pounced within seconds when researchers exposed their wallet keys (11-20 22:30) — https://www.coindesk.com/tech/2026/11/20/bitcoin-bots-pounced-within-seconds-when-researchers-exposed-their-keys
- [Cointelegraph] Here’s what happened in crypto today (11-20 22:29) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Lagarde warns Europe could miss chance to unify tokenized markets (11-20 22:21) — https://cointelegraph.com/news/lagarde-europe-limited-window-tokenization-rules?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] ECB’s Lagarde warns Europe could lose control of growing tokenized asset market (11-20 22:11) — https://www.coindesk.com/policy/2026/11/20/ecb-s-largarde-warns-europe-could-lose-control-of-growing-tokenized-asset-market
- [The Block] US spot bitcoin ETFs see $582 million in daily net outflows as November total nears $3.5 billion (11-20 21:29) — https://www.theblock.co/news/markets/2026-11-20-us-spot-bitcoin-etfs-see-582-million-in-daily-net-outflows-as-november-total-nears-3-5-billion-444217
- [CoinDesk] Bitcoin, stocks and gold traders getting nervous, and volatility gauges are surging (11-20 21:15) — https://www.coindesk.com/daybook-us/2026/11/20/bitcoin-stocks-and-gold-traders-getting-nervous-and-volatility-gauges-are-surging
- [The Block] Ark buys $90 million worth of Anthropic shares on debut, trims Ethereum and Solana staking ETF holdings (11-20 21:12) — https://www.theblock.co/news/markets/2026-11-20-ark-buys-90-million-worth-of-anthropic-shares-on-debut-trims-ethereum-and-solana-staking-etf-holdings-444226
- [CoinDesk] Bitcoin drops for third straight day as Asian tech shares slide (11-20 20:42) — https://www.coindesk.com/markets/2026/11/20/bitcoin-drops-for-third-straight-day-as-asian-tech-shares-slide
- [Cointelegraph] Binance hacker moves nearly $600M in ETH, routes funds through THORChain, Chainflip (11-20 20:31) — https://cointelegraph.com/news/binance-hacker-600m-eth-routes-thorchain-chainflip?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] VanEck to end Gemini ETF custody deals, keeps Coinbase (11-20 19:54) — https://cointelegraph.com/news/vaneck-gemini-etf-custody-end-keep-coinbase?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Coinbase targets first-half 2027 for its own prediction market contracts (11-20 19:48) — https://www.coindesk.com/business/2026/11/20/coinbase-targets-first-half-2027-for-its-own-prediction-market-contracts
- [The Block] MoonPay applies for national trust bank charter to expand stablecoin services (11-20 19:39) — https://www.theblock.co/news/business/2026-11-20-moonpay-applies-occ-national-bank-charter-444198
- [Cointelegraph] Bitcoin nears repeat of chart pattern that preceded 2023’s $25K retest (11-20 19:29) — https://cointelegraph.com/markets/bitcoin-first-death-cross-repeat-2023-bottom-25k?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Senate passes ‘Death Bets Act’ to ban prediction market contracts tied to death and war (11-20 19:09) — https://www.theblock.co/news/regulation/2026-11-20-senate-death-bets-act-444200
- [CoinDesk] No special rules for Hyperliquid or other onchain trading platforms, CFTC says (11-20 19:02) — https://www.coindesk.com/markets/2026/11/20/cftc-tells-hyperliquid-and-crypto-rivals-no-special-rules-for-onchain-trading
- [CoinDesk] Cathie Wood's Ark Invest piled into Anthropic IPO, buying $90 million worth of shares (11-20 18:48) — https://www.coindesk.com/markets/2026/11/20/cathie-wood-s-ark-invest-piled-into-anthropic-ipo-buying-usd90-million-worth-of-shares

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

- 옵션 25델타 스큐 (Deribit): 429 Client Error: Too Many Requests for url: https://www.deribit.com/api/v2/public/ticker?instrument_name=BTC-25DEC26-54000-C
- 고래비율(근사) (Arkham + Coin Metrics): Arkham 키 없음