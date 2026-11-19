# 코인 데일리 스냅샷

- 수집 시각: 2026-11-19 16:47 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 5.4 / 3일 평균 4.4 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | -25.0 |
| 파생·심리 | 30% | 20.0 |
| 밸류에이션 | 25% | 50.0 |
| 매크로 | 15% | -37.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.57 |
| 밸류에이션 | 가격÷STH-RP | +1 | +1 | 가격÷STH-RP 0.947 |
| 수급 | 현물 ETF 순유입 | -1 | -1 | 5일 합 -1001백만$ |
| 수급 | 거래소 순유입(7일) | +1 | +0 | 7일 순유입 분포 29백분위 |
| 수급 | 거래소 보유량(30일) | -1 | -1 | 30일 +1.15% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | -1 | -1 | 7일 +11.9% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +2 | 3회 평균 0.0026% |
| 파생·심리 | RSI(14) | +2 | +2 | RSI 21.8 |
| 파생·심리 | 롱/숏 비율 | -1 | +0 | 롱/숏 분포 87백분위 |
| 파생·심리 | 미결제약정(OI) | +1 | +1 | OI 7일 -19.1%, 가격 -14.8% (레버리지 정리) |
| 파생·심리 | 옵션 스큐 | -1 | -1 | +6.73 (풋 우위 확대, 전일 +5.46) |
| 매크로 | 나스닥 | -1 | -1 | 50일선 아래 |
| 매크로 | DXY | -1 | -1 | 103.81, 20일 +2.2% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 159.71 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -4 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 24429.881 | 24328.381 | pt | 2026-11-18 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -4.07 | -2.94 | % | 2026-11-18 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26231.8 | 26268.27 | pt | 2026-11-18 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 103.813 | 103.86 | pt | 2026-11-19 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 2.17 | 1.92 | % | 2026-11-19 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 159.71 | 159.504 | 엔 | 2026-11-19 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | -0.02 | 0.36 | % | 2026-11-19 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.08 | 4.02 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.87 | 2.79 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.65 | 3.44 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.12 | 3.03 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -4 | -4 |  | 2026-11-19 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 7.961 | 7.875 | % | 2026-11-19 07:43 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.1943 | 2.2263 | 조$ | 2026-11-19 07:43 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | -239.9 | 8.0 | 백만$ | 2026-11-17 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 1거래일 연속 순유출 / 집계 기준일 2026-11-17 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -209.5 | 76.5 | 백만$ | 2026-11-17 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -1001.3 | -856.4 | 백만$ | 2026-11-17 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | -1 | 1 | 일 | 2026-11-17 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 62981.71 | 64873.18 | USD | 2026-11-18 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 21.76 | 24.14 |  | 2026-11-18 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -14.81 | -11.97 | % | 2026-11-18 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.11 | 2.95 | 십억$ | 2026-11-18 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -19.1 | -23.55 | % | 2026-11-18 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 3.09 | 3.29 | 배 | 2026-11-18 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 86.7 | 60.0 | 백분위 | 2026-11-18 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | -0.001 | 0.0063 | % | 2026-11-19 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0026 | -0.0001 | % | 2026-11-19 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 46.02 | 43.99 |  | 2026-11-19 07:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 6.73 | 5.46 | vol pt | 2026-11-19 07:47 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-12-25, 콜 BTC-25DEC26-70000-C / 풋 BTC-25DEC26-58000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.5704 | 0.653 |  | 2026-11-12 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 0.9471 | 0.9789 |  | 2026-11-12 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 66410.0 | 66307.0 | $ | 2026-11-12 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 62897.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 27468.9 | 28667.9 | BTC | 2026-11-18 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 32775.8 | 33042.7 | BTC | 2026-11-18 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -25547.9 | -14187.2 | BTC | 2026-11-18 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 28.9 | 47.8 | 백분위 | 2026-11-18 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -5306.9 | -4374.7 | BTC | 2026-11-18 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | 1.15 | 1.04 | % | 2026-11-18 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2711760.0 | 2707552.0 | BTC | 2026-11-18 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (11-18 18:00 ~ 11-19 16:47 KST)

피드 상태: CoinDesk: 18건 / The Block: 17건 / Cointelegraph: 22건 / 블록미디어: 10건

- [블록미디어] 비트코인으로 미국 국채보다 더 번다?…시그넘 “2027년 캐리 트레이드 부활” (11-19 16:32) — https://www.blockmedia.co.kr/archives/1168045?utm_source=general&utm_medium=rss
- [블록미디어] 유에스디에이아이, “GPU 거래 평가액 250억달러 달해” AI 인프라 금융시장 공략 (11-19 16:20) — https://www.blockmedia.co.kr/archives/1167877?utm_source=general&utm_medium=rss
- [블록미디어] 비트코인·이더리움 ETF서 하루 3.4억달러 이탈…블랙록이 유출 주도 (11-19 16:02) — https://www.blockmedia.co.kr/archives/1168018?utm_source=general&utm_medium=rss
- [블록미디어] 이더리움 급락 중 ‘재단 연계 지갑’ 매도 지속…커뮤니티 “성과 없이 ETH만 팔아” (11-19 15:30) — https://www.blockmedia.co.kr/archives/1168012?utm_source=general&utm_medium=rss
- [CoinDesk] Fed's rate hike push may be a mistake. Here's why (11-19 15:23) — https://www.coindesk.com/markets/2026/11/19/fed-s-push-for-more-rate-hikes-leans-on-backward-looking-data-as-gas-prices-slide-analysts-argue
- [The Block] Sygnum sees bitcoin carry trades beating Treasury bills in 2027 as funding recovers (11-19 15:00) — https://www.theblock.co/news/markets/2026-11-19-sygnum-bitcoin-carry-trades-beating-treasury-bills-2027-443547
- [The Block] Binance gets $6.5 billion freezing order, CryptoQuant says bitcoin is in a ‘value zone’, and more (11-19 15:00) — https://www.theblock.co/newsletters/the-daily/2026-11-19-binance-gets-6-5-billion-freezing-order-cryptoquant-says-bitcoin-is-in-a-value-zone-and-more-443511
- [Cointelegraph] Bitcoin carry trades could beat Treasury bills in 2027, Sygnum predicts (11-19 15:00) — https://cointelegraph.com/markets/sygnum-bitcoin-carry-trades-2027?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Here’s what happened in crypto today (11-19 15:00) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 루미스·질리브랜드, 재무부에 스테이블코인 사업자 보호 초당적 요구 (11-19 15:00) — https://www.blockmedia.co.kr/archives/1167977?utm_source=general&utm_medium=rss
- [CoinDesk] Ethereum block builders received the most in a $3.4 million vault hack, data shows (11-19 14:39) — https://www.coindesk.com/tech/2026/11/19/ethereum-block-builders-received-the-most-in-a-usd3-4-million-vault-hack-data-shows
- [Cointelegraph] Senators warn GENIUS Act rules could push stablecoin firms toward federal oversight (11-19 14:27) — https://cointelegraph.com/news/us-senators-genius-act-rules-favor-federal-stablecoin-issuers?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 13년 만에 돌아온 GTA6, 전 세계 공식 출시…게임업계 흥행 신기록 세울까 (11-19 14:19) — https://www.blockmedia.co.kr/archives/1167998?utm_source=general&utm_medium=rss
- [블록미디어] 금값 3700달러대 추락…1년 넘게 지킨 3800달러 붕괴, 연준 ‘긴축 공포’ 확산 (11-19 14:15) — https://www.blockmedia.co.kr/archives/1167988?utm_source=general&utm_medium=rss
- [블록미디어] 톰 리 “이더리움, 가치저장 수단으로 전환”…비탈릭 주장에 힘 실었다 (11-19 14:15) — https://www.blockmedia.co.kr/archives/1167975?utm_source=general&utm_medium=rss
- [블록미디어] 바이낸스, 블랙록 비트코인 ETF 선물 출시…24시간 거래·최대 20배 레버리지 (11-19 14:13) — https://www.blockmedia.co.kr/archives/1167979?utm_source=general&utm_medium=rss
- [Cointelegraph] Binance hackers stole 192 tokens across 11 networks, court docs show (11-19 14:09) — https://cointelegraph.com/news/binance-hackers-stole-192-tokens-across-11-networks?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin miner that sold its last BTC warns it may run short of cash for $1.2 billion AI deal (11-19 13:46) — https://www.coindesk.com/markets/2026/11/19/bitcoin-miner-that-sold-its-last-btc-warns-it-may-run-short-of-cash-for-usd1-2-billion-ai-deal
- [블록미디어] 글램스터담 ‘EIP-8037 포함’ 놓고 갈라진 이더리움…비탈릭 “지지” VS 유니스왑 등 “앱 중단 위험” (11-19 13:40) — https://www.blockmedia.co.kr/archives/1167949?utm_source=general&utm_medium=rss
- [The Block] Ledger expands hardware hack investigation to Germany, UAE as new cases emerge (11-19 13:13) — https://www.theblock.co/news/web3/2026-11-18-ledger-new-hardware-incidents-germany-uae-443530
- [CoinDesk] CZ says tokenized Anthropic is coming to BNB Chain on IPO day (11-19 12:40) — https://www.coindesk.com/markets/2026/11/19/cz-says-tokenized-anthropic-is-coming-to-bnb-chain-on-ipo-day
- [The Block] Kraken parent Payward to acquire Tribe Capital to expand private-market offerings (11-19 12:18) — https://www.theblock.co/news/business/2026-11-18-kraken-parent-payward-tribe-capital-443522
- [The Block] Standard Chartered, StraitsX, OCBC complete trial of tokenized deposit interoperability (11-19 11:30) — https://www.theblock.co/news/web3/2026-11-18-standard-chartered-straitsx-ocbc-tokenized-deposit-poc-442964
- [Cointelegraph] Trump administration unveils new center to choke off scam payments (11-19 10:45) — https://cointelegraph.com/news/trump-administration-unveils-new-center-choke-off-scam-payments?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Fed officials saw October rate hold as a ‘close call,’ minutes show (11-19 09:35) — https://cointelegraph.com/markets/fed-officials-saw-october-rate-hold-as-close-call-minutes-show?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Another U.S. appellate court goes against Kalshi, building the industry's legal headwinds (11-19 09:33) — https://www.coindesk.com/policy/2026/11/18/another-u-s-appellate-court-goes-against-kalshi-building-the-industry-s-legal-headwinds
- [CoinDesk] Payward, the owner of crypto exchange Kraken, is buying its CEO’s venture capital business, Tribe (11-19 07:30) — https://www.coindesk.com/business/2026/11/18/payward-the-owner-of-crypto-exchange-kraken-is-buying-its-ceo-s-venture-capital-business-tribe
- [The Block] Senators: Treasury must ensure ‘equal footing’ for stablecoin issuers in GENIUS Act implementation (11-19 07:09) — https://www.theblock.co/news/regulation/2026-11-18-senators-treasury-must-ensure-equal-footing-for-stablecoin-issuers-in-genius-act-implementation-443501
- [Cointelegraph] Tether invokes The Big Short in swipe at S&P over USDT reserve risks (11-19 06:57) — https://cointelegraph.com/news/tether-usdt-sp-stability-assessment-reserve-risks?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Ledger warns Berlin customers as hardware wallet tampering investigation expands (11-19 06:13) — https://cointelegraph.com/news/ledger-warns-berlin-customers-hardware-wallet-investigation?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bain Capital Crypto leads $110M Variational round at $1.5B valuation (11-19 05:32) — https://cointelegraph.com/news/variational-series-b-bain-capital-crypto?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Binance says it obtained $6.5B worldwide freezing order after hack (11-19 05:20) — https://cointelegraph.com/news/binance-says-won-65b-worldwide-freezing-order-after-hack?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Binance obtains $6.5 billion freezing order from Abu Dhabi court in bid to recover stolen crypto (11-19 04:40) — https://www.theblock.co/news/business/2026-11-18-binance-freezing-court-order-adgm-crypto-october-hack-443491
- [The Block] Ondo to launch tokenized Anthropic stock on IPO day (11-19 03:51) — https://www.theblock.co/news/markets/2026-11-18-ondo-to-launch-tokenized-anthropic-stock-on-ipo-day-443482
- [Cointelegraph] MARA prices $185M debt offering after $1.1B Bitcoin sale (11-19 03:27) — https://cointelegraph.com/markets/mara-long-ridge-debt-offering-bitcoin-sales?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] A $1.5 billion crypto startup is taking on Hyperliquid with a Wall Street playbook (11-19 02:22) — https://www.coindesk.com/business/2026/11/18/a-usd1-5-billion-crypto-startup-is-taking-on-hyperliquid-with-a-wall-street-playbook
- [The Block] CryptoQuant says bitcoin is back in a bearish phase but has reached a ‘value zone’ (11-19 02:13) — https://www.theblock.co/news/markets/2026-11-18-cryptoquant-bitcoin-bearish-value-zone-443471
- [Cointelegraph] $25M Ethereum MEV acquittal tests criminal enforcement limits (11-19 02:05) — https://cointelegraph.com/news/25m-ethereum-mev-acquittal-tests-criminal-enforcement-limits?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Bullish’s Q3 adjusted profit rises 35%, digital asset sales fall 23% (11-19 02:02) — https://www.theblock.co/news/business/2026-11-18-bullishs-q3-adjusted-profit-rises-35-digital-asset-sales-fall-23-443456
- [Cointelegraph] Polymarket US takes rapid-fire crypto trading format to oil, natural gas (11-19 02:00) — https://cointelegraph.com/news/polymarket-us-takes-rapid-fire-crypto-trading-format-oil-natural-gas?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin, stocks wobble as Fed’s Waller talks of ‘shock’ 50-point rate hike (11-19 01:34) — https://cointelegraph.com/markets/bitcoin-stocks-wobble-waller-talks-shock-50-point-rate-hike?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Visa Direct to extend stablecoin prefunding for cross-border payouts to Asia-Pacific (11-19 01:30) — https://www.theblock.co/news/business/2026-11-18-visa-direct-extend-stablecoin-prefunding-cross-border-payouts-asia-pacific-443457
- [CoinDesk] Crypto Long & Short: Crypto exchanges shouldn’t double as the vault (11-19 01:02) — https://www.coindesk.com/coindesk-indices/2026/11/18/crypto-long-and-short-crypto-exchanges-shouldn-t-double-as-the-vault
- [The Block] Variational raises $110 million at $1.5 billion valuation to expand onchain derivatives trading (11-19 00:51) — https://www.theblock.co/news/deals/2026-11-18-variational-raises-110-million-at-1-5-billion-valuation-to-expand-onchain-derivatives-trading-443445
- [CoinDesk] German judge proposes dropping Movie2k case if operator hands over $2.56 billion in bitcoin (11-19 00:38) — https://www.coindesk.com/business/2026/11/18/german-judge-proposes-dropping-movie2k-case-if-operator-hands-over-usd2-56-billion-in-bitcoin
- [CoinDesk] Hong Kong wants banks to use AI to catch crypto crime before money disappears (11-19 00:23) — https://www.coindesk.com/business/2026/11/18/hong-kong-wants-banks-to-use-ai-to-catch-crypto-crime-before-money-disappears
- [The Block] StoneX cuts Bitdeer price target to $15 amid new US chip export controls (11-19 00:16) — https://www.theblock.co/news/markets/2026-11-18-stonex-cuts-bitdeer-price-target-to-15-amid-new-us-chip-export-controls-443440
- [The Block] Backpack secures NFA approval, completing licensing stack for US derivatives launch (11-18 23:49) — https://www.theblock.co/news/business/2026-11-18-backpack-completes-regulatory-framework-us-entry-442980
- [Cointelegraph] Bitcoin Covenants Part 6: FE Covenants — Enforcing covenants through cryptographically restricted signing keys (11-18 23:04) — https://cointelegraph.com/research/bitcoin-covenants-part-6-fe-covenants-enforcing-covenants-through-cryptographically-restricted-signing-keys?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] ‘Gift from the market’: Bitcoin shows signs of a local bottom after six weeks of losses, analyst says (11-18 23:01) — https://www.theblock.co/news/markets/2026-11-18-gift-from-the-market-bitcoin-shows-signs-of-a-local-bottom-after-six-weeks-of-losses-analyst-says-443017
- [Cointelegraph] CoinShares sells all treasury ETH, halves SOL holdings for buybacks (11-18 22:42) — https://cointelegraph.com/news/coinshares-sells-eth-treasury-holdings-halves-sol-share-buybacks?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Sanctions fears loom over Russia’s regulated crypto trading launch (11-18 22:32) — https://cointelegraph.com/news/sanctions-fears-russia-crypto-launch?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] How to preserve wealth and access funds during a national emergency (11-18 22:30) — https://cointelegraph.com/magazine/how-to-preserve-wealth-and-access-it-during-a-national-emergency?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin miner MARA raises $185 million in debt after selling $1 billion BTC to repay loans (11-18 21:53) — https://www.coindesk.com/markets/2026/11/18/bitcoin-miner-mara-raises-usd185-million-in-debt-after-selling-usd1-billion-btc-to-repay-loans
- [Cointelegraph] Tokenized Nvidia market cap surges 159% amid Jensen Huang’s exit (11-18 21:53) — https://cointelegraph.com/news/tokenized-nvidia-cap-rises-158-stock-loses-750b?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bullish beats revenue estimates as institutional services offset sluggish spot crypto volumes (11-18 21:41) — https://www.coindesk.com/markets/2026/11/18/bullish-beats-revenue-estimates-as-institutional-services-offset-sluggish-spot-crypto-volumes
- [CoinDesk] Circle turns to DBS as banks build rival digital payment systems across Asia (11-18 21:25) — https://www.coindesk.com/business/2026/11/18/circle-turns-to-dbs-as-banks-build-rival-digital-payment-systems-across-asia
- [CoinDesk] Blaming Anthropic’s IPO for bitcoin’s slide is 'easy to believe,' but flawed, analysts say (11-18 21:15) — https://www.coindesk.com/daybook-us/2026/11/18/blaming-anthropic-s-ipo-for-bitcoin-s-slide-is-easy-to-believe-but-flawed-analysts-say
- [CoinDesk] Bitcoin drops as Nvidia earnings report drives stock index futures higher (11-18 20:42) — https://www.coindesk.com/markets/2026/11/18/bitcoin-drops-as-nvidia-earnings-report-drives-stock-index-futures-higher
- [The Block] TD Cowen tempers ether outlook, maintains Buy rating on Sharplink (11-18 20:08) — https://www.theblock.co/news/ecosystems/2026-11-18-td-cowen-maintains-buy-rating-sharplink-442987

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