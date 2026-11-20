# 코인 데일리 스냅샷

- 수집 시각: 2026-11-20 16:39 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 3.5 / 3일 평균 5.5 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | -25.0 |
| 파생·심리 | 30% | 20.0 |
| 밸류에이션 | 25% | 50.0 |
| 매크로 | 15% | -50.0 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.47 |
| 밸류에이션 | 가격÷STH-RP | +1 | +1 | 가격÷STH-RP 0.909 |
| 수급 | 현물 ETF 순유입 | -1 | -1 | 5일 합 -1008백만$ |
| 수급 | 거래소 순유입(7일) | +1 | +1 | 7일 순유입 분포 24백분위 |
| 수급 | 거래소 보유량(30일) | -1 | -1 | 30일 +1.07% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | -1 | -1 | 7일 +9.8% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +2 | +1 | 3회 평균 -0.0013% |
| 파생·심리 | RSI(14) | +2 | +2 | RSI 20.5 |
| 파생·심리 | 롱/숏 비율 | -2 | -1 | 롱/숏 분포 97백분위 |
| 파생·심리 | 미결제약정(OI) | +1 | +1 | OI 7일 -21.1%, 가격 -13.2% (레버리지 정리) |
| 파생·심리 | 옵션 스큐 | -1 | -1 | +9.05 (풋 우위 확대, 전일 +6.73) |
| 매크로 | 나스닥 | -2 | -1 | 5일 -5.9% 급락 |
| 매크로 | DXY | -1 | -1 | 103.72, 20일 +1.9% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 159.04 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -4 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 23879.199 | 24429.881 | pt | 2026-11-19 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -5.86 | -4.07 | % | 2026-11-19 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26187.75 | 26231.8 | pt | 2026-11-19 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 103.715 | 103.9 | pt | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.87 | 2.17 | % | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 159.04 | 159.381 | 엔 | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | -0.52 | -0.02 | % | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.08 | 4.02 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.87 | 2.79 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.65 | 3.44 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.12 | 3.03 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -4 | -4 |  | 2026-11-20 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 8.204 | 7.961 | % | 2026-11-20 07:37 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.1305 | 2.1943 | 조$ | 2026-11-20 07:37 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | -306.4 | -239.9 | 백만$ | 2026-11-18 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 2거래일 연속 순유출 / 집계 기준일 2026-11-18 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -148.7 | -209.5 | 백만$ | 2026-11-18 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -1007.8 | -1001.3 | 백만$ | 2026-11-18 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | -2 | -1 | 일 | 2026-11-18 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 61913.23 | 62981.71 | USD | 2026-11-19 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 20.52 | 21.76 |  | 2026-11-19 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -13.25 | -14.81 | % | 2026-11-19 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.05 | 3.11 | 십억$ | 2026-11-19 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -21.13 | -19.1 | % | 2026-11-19 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 3.2 | 2.92 | 배 | 2026-11-19 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 96.7 | 86.7 | 백분위 | 2026-11-19 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | -0.0016 | -0.0018 | % | 2026-11-20 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | -0.0013 | 0.0026 | % | 2026-11-20 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 48.91 | 45.92 |  | 2026-11-20 07:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 9.05 | 6.73 | vol pt | 2026-11-20 07:39 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-12-25, 콜 BTC-25DEC26-68000-C / 풋 BTC-25DEC26-56000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.4712 | 0.5704 |  | 2026-11-13 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 0.9092 | 0.9471 |  | 2026-11-13 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 68061.0 | 66410.0 | $ | 2026-11-13 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 61881.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 23177.0 | 27468.9 | BTC | 2026-11-19 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 25023.1 | 32775.8 | BTC | 2026-11-19 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -26484.3 | -25547.9 | BTC | 2026-11-19 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 24.4 | 28.9 | 백분위 | 2026-11-19 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -1846.1 | -5306.9 | BTC | 2026-11-19 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | 1.07 | 1.15 | % | 2026-11-19 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2710118.0 | 2711760.0 | BTC | 2026-11-19 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (11-19 18:00 ~ 11-20 16:39 KST)

피드 상태: CoinDesk: 22건 / The Block: 11건 / Cointelegraph: 17건 / 블록미디어: 10건

- [블록미디어] 비트코인·이더리움 ETF서 7.1억달러 순유출…블랙록에서만 6억달러 ‘썰물’ (11-20 15:59) — https://www.blockmedia.co.kr/archives/1168547?utm_source=general&utm_medium=rss
- [블록미디어] [마감시황] ‘블랙 프라이데이’…코스피·코스닥 5%대 폭락 (11-20 15:42) — https://www.blockmedia.co.kr/archives/1168550?utm_source=general&utm_medium=rss
- [블록미디어] 코인베이스, 미 CFTC 예측시장 규제안 지지…”이벤트 계약, 도박 아닌 파생상품” (11-20 15:30) — https://www.blockmedia.co.kr/archives/1168525?utm_source=general&utm_medium=rss
- [Cointelegraph] Anthropic’s $81B IPO draws half the net retail buying of SpaceX’s (11-20 15:24) — https://cointelegraph.com/markets/anthropic-ipo-spacex-retail-buying-first-day-gains?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 특금법 재신고 오늘 마감…중소 거래소 ‘내년 8월이 고비’ (11-20 15:20) — https://www.blockmedia.co.kr/archives/1168507?utm_source=general&utm_medium=rss
- [CoinDesk] Here's what's crashing gold and likely weighing on bitcoin too (11-20 15:12) — https://www.coindesk.com/markets/2026/11/20/here-s-what-s-crashing-gold-and-likely-weighing-on-bitcoin-too
- [CoinDesk] Anthropic shares may fall 5% at Friday’s open, crypto futures suggest (11-20 15:08) — https://www.coindesk.com/markets/2026/11/20/crypto-traders-have-anthropic-trading-below-its-first-nasdaq-close-on-hyperliquid
- [Cointelegraph] Here’s what happened in crypto today (11-20 15:00) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 킬라 “비트코인 4만~5만달러대 가도 2배 롱 유지” (11-20 14:45) — https://www.blockmedia.co.kr/archives/1168520?utm_source=general&utm_medium=rss
- [The Block] CFTC Chair on Hyperliquid and onchain venues, Ripple CLO doubts Elizabeth Warren will set crypto policy, and more (11-20 14:40) — https://www.theblock.co/newsletters/the-daily/2026-11-20-cftc-chair-hyperliquid-ripple-clo-elizabeth-warren-crypto-policy-more-news-444143
- [CoinDesk] This Bitcoin miner sold 267 BTC to clear $22 million debt. It still may not survive (11-20 14:32) — https://www.coindesk.com/markets/2026/11/20/this-bitcoin-miner-sold-267-btc-to-clear-usd22-million-debt-it-still-may-not-survive
- [블록미디어] 42매크로 “2027년 비트코인에 최고의 해 될 것”…12월 단기 긴축이 호재 (11-20 14:30) — https://www.blockmedia.co.kr/archives/1168499?utm_source=general&utm_medium=rss
- [CoinDesk] Big money bought a net $4 billion of bitcoin funds in Q3, ending 9 months of selling (11-20 14:20) — https://www.coindesk.com/markets/2026/11/20/big-money-bought-a-net-usd4-billion-of-bitcoin-funds-in-q3-ending-9-months-of-selling
- [블록미디어] 문페이, 미 신탁은행 인가 신청…前 CFTC 수장 영입·트럼프 사업 협력 ‘눈길’ (11-20 14:00) — https://www.blockmedia.co.kr/archives/1168487?utm_source=general&utm_medium=rss
- [CoinDesk] Ethereum’s next big upgrade is pushed into 2027 by apps it would break (11-20 13:58) — https://www.coindesk.com/tech/2026/11/20/ethereum-s-next-big-upgrade-is-pushed-into-2027-by-apps-it-would-break
- [CoinDesk] VanEck drops Gemini as custodian of its bitcoin, ether and SOL ETFs (11-20 13:28) — https://www.coindesk.com/markets/2026/11/20/vaneck-drops-gemini-as-custodian-of-its-bitcoin-ether-and-sol-etfs
- [The Block] Coinbase backs CFTC proposal to distinguish prediction market contracts from gambling (11-20 13:24) — https://www.theblock.co/news/business/2026-11-19-coinbase-backs-cftc-prediction-markets-444152
- [블록미디어] ‘친 크립토’ 민주당 의원 쓴소리 “업계, 트럼프·중간선거에 베팅 잘못했다” (11-20 13:10) — https://www.blockmedia.co.kr/archives/1168471?utm_source=general&utm_medium=rss
- [블록미디어] 바이낸스US, 美 파생상품 인가 본심사…비트코인·이더리움 무기한 선물 추진 (11-20 12:58) — https://www.blockmedia.co.kr/archives/1168438?utm_source=general&utm_medium=rss
- [Cointelegraph] Institutions pile back into US Bitcoin ETFs in Q3 after selling streak (11-20 12:33) — https://cointelegraph.com/markets/institutional-bitcoin-etf-holdings-clock-record-quarter-after-selling-streak?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin hits four-month low after Anthropic's IPO as tech stocks wilt (11-20 12:32) — https://www.coindesk.com/markets/2026/11/20/bitcoin-hits-four-month-low-after-anthropic-s-ipo-as-tech-stocks-wilt
- [블록미디어] 세일러 “STRC, 하루 거래대금 6억달러 돌파… 100달러 아래서 계속 매입” (11-20 12:30) — https://www.blockmedia.co.kr/archives/1168453?utm_source=general&utm_medium=rss
- [Cointelegraph] Ledger CTO Charles Guillemet to leave after nine years at company (11-20 08:44) — https://cointelegraph.com/news/ledger-cto-charles-guillemet-to-leave-after-nine-years-at-company?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Binance’s $6.5B freeze order, Hong Kong ‘suspicious’ of HYPE: Asia Express (11-20 07:25) — https://cointelegraph.com/magazine/binances-65b-freeze-order-hong-kong-suspicious-of-hype-asia-express?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] MoonPay seeks US bank charter for stablecoin, custody services (11-20 06:01) — https://cointelegraph.com/news/moonpay-seeks-us-bank-charter-for-stablecoin-custody-services?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Hyperliquid Anthropic futures priced within 1% of Nasdaq opening price (11-20 05:33) — https://cointelegraph.com/markets/hyperliquid-anthropic-futures-nasdaq-opening-price?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Kalshi’s Quintenz says insider trading is ‘just easier to see’ in prediction markets than stocks (11-20 05:20) — https://www.theblock.co/news/markets/2026-11-19-kalshi-quintenz-insider-trading-prediction-markets-stocks-444133
- [Cointelegraph] Trump’s SEC nominee Johnson backs formal rulemaking for tokenized stock trading (11-20 05:06) — https://cointelegraph.com/news/sec-nominees-johnson-levine-tokenized-stocks?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Sky's USDS stablecoin shrinks 35% as $1.5 billion exits reserves after illicit-finance report (11-20 04:53) — https://www.coindesk.com/business/2026/11/19/sky-s-usds-stablecoin-shrinks-35-as-usd1-5-billion-exits-reserves-after-illicit-finance-report
- [The Block] Ripple’s Alderoty doubts Elizabeth Warren will ‘set crypto policy in this country,’ backs durable agency rules (11-20 03:47) — https://www.theblock.co/news/regulation/2026-11-19-ripple-alderoty-elizabeth-warren-wont-set-crypto-policy-backs-durable-agency-rules-444105
- [Cointelegraph] Ethereum’s Glamsterdam upgrade could slip to May 2027 over compatibility concerns (11-20 03:20) — https://cointelegraph.com/news/ethereum-glamsterdam-could-slip-to-may-2027?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Trump's Democratic SEC pick suggests tokenization policy deserves full rule process (11-20 03:15) — https://www.coindesk.com/policy/2026/11/19/trump-s-democratic-sec-pick-suggests-tokenization-policy-deserves-full-rule-process
- [Cointelegraph] Why higher rates could slow Bitcoin buying at treasury firms (11-20 03:09) — https://cointelegraph.com/news/why-higher-rates-could-slow-bitcoin-buying-at-treasury-firms?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin price ignores Anthropic debut as ANT share price dips below $100 (11-20 03:06) — https://cointelegraph.com/markets/bitcoin-price-ignores-anthropic-debut-ant-share-price-dips-below-100?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] CFTC Chair Selig outlines how Hyperliquid and other onchain venues could enter the US (11-20 03:04) — https://www.theblock.co/news/regulation/2026-11-19-cftc-chair-selig-hyperliquid-onchain-venues-the-us-444106
- [The Block] Tokenized Stocks Shrug Off the Crypto Selloff (11-20 02:12) — https://www.theblock.co/newsletters/tokenization-briefing/2026-11-19-tokenized-stocks-shrug-off-crypto-selloff-442829
- [CoinDesk] Anthropic gains after IPO, but pulls off highest levels (11-20 02:01) — https://www.coindesk.com/markets/2026/11/19/anthropic-opens-for-trade-at-usd11-50-up-34-from-ipo-price
- [CoinDesk] Crypto for Advisors: Falling prices drove October’s 10% drop in institutional crypto exposure (11-20 01:09) — https://www.coindesk.com/coindesk-indices/2026/11/19/crypto-for-advisors-falling-prices-drove-october-s-10-drop-in-institutional-crypto-exposure
- [Cointelegraph] Anthropic shares open at $111.50, 34.3% above $83 IPO price (11-20 01:07) — https://cointelegraph.com/markets/anthropic-shares-expected-to-open-above-83-ipo-price?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Hill, Moreno blame delays for missed Clarity Act window but differ on reach of agency rulemaking (11-20 01:01) — https://www.theblock.co/news/regulation/2026-11-19-hill-moreno-blame-delays-missed-clarity-act-window-split-regulators-fill-gap-443615
- [CoinDesk] Binance wins $6.5 billion feezing order against hackers behind crypto's largest theft (11-20 00:20) — https://www.coindesk.com/business/2026/11/19/binance-wins-usd6-5-billion-feezing-order-against-hackers-behind-crypto-s-largest-theft
- [The Block] Bitcoin finance protocol Hashi goes live on Sui mainnet (11-19 23:00) — https://www.theblock.co/news/defi/2026-11-19-bitcoin-finance-protocol-hashi-goes-live-on-sui-mainnet-443608
- [Cointelegraph] Ethereum’s new DeFi security tool raises questions over censorship (11-19 22:30) — https://cointelegraph.com/magazine/ethereums-new-defi-security-tool-raises-questions-over-censorship?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Crypto traders vs. Wall Street: OKX’s Anthropic markets put IPO pricing to the test (11-19 22:11) — https://www.coindesk.com/markets/2026/11/19/crypto-traders-vs-wall-street-okx-s-anthropic-markets-put-ipo-pricing-to-the-test
- [Cointelegraph] Hong Kong adds Hyperliquid to list of ‘suspicious’ crypto platforms (11-19 21:44) — https://cointelegraph.com/news/hyperliquid-hong-kong-regulators-alert-list?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Trump Media wants to clear $884 million of debt without selling its bitcoin (11-19 21:40) — https://www.coindesk.com/markets/2026/11/19/trump-media-wants-to-clear-usd884-million-of-debt-without-selling-its-bitcoin
- [Cointelegraph] GTA VI publisher racks up nearly 3x Nvidia’s tokenized stock volume (11-19 21:33) — https://cointelegraph.com/news/gta-vi-launch-tokenized-ttwo-trade-triple-nvidia?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin ETF outflows show waning crypto appetite ahead of Anthropic's Nasdaq debut (11-19 21:20) — https://www.coindesk.com/daybook-us/2026/11/19/bitcoin-etf-outflows-show-waning-crypto-appetite-ahead-of-anthropic-s-nasdaq-debut
- [CoinDesk] Bitcoin holds above $63,750 but Fed rate-hike threats loom large (11-19 21:08) — https://www.coindesk.com/markets/2026/11/19/bitcoin-holds-above-usd63-750-but-fed-rate-hike-threats-loom-large
- [The Block] US launches cybercrime center with TRM Labs to help trace crypto tied to scams (11-19 20:55) — https://www.theblock.co/news/regulation/2026-11-19-us-launches-cybercrime-center-with-trm-labs-to-help-trace-crypto-tied-to-scams-443599
- [CoinDesk] North Korean hackers used Sky's stablecoin system, putting billions at freeze risk (11-19 20:30) — https://www.coindesk.com/business/2026/11/19/north-korean-hackers-used-sky-s-stablecoin-system-putting-billions-at-freeze-risk
- [Cointelegraph] Sweden’s H100 could tap Bitcoin trading pool to fund share buybacks (11-19 20:19) — https://cointelegraph.com/news/swedens-h100-13m-q3-loss-share-buyback-approval?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Anthropic’s $107 billion sale set to top SpaceX’s IPO as tokenized stocks gain traction (11-19 20:06) — https://www.coindesk.com/markets/2026/11/19/anthropic-s-usd107-billion-raise-set-to-surpass-spacex-s-ipo-haul
- [The Block] 1inch integrates Hyperliquid’s perpetual futures contracts into its dApp and wallet platform (11-19 20:00) — https://www.theblock.co/news/web3/2026-11-19-1inch-integrates-hyperliquid-perpetual-futures-443574
- [CoinDesk] Financial firms must act now as quantum computers grow ‘highly advanced,’ IOSCO warns (11-19 19:55) — https://www.coindesk.com/tech/2026/11/19/banks-and-blockchains-lag-on-quantum-defense-as-encryption-risks-loom-watchdog-warns
- [CoinDesk] Live updates: Bitcoin plunges to lowest since July as Anthropic gains, but broader markets tumble (11-19 19:48) — https://www.coindesk.com/markets/2026/11/19/live-updates-bitcoin-nears-usd64-000-as-anthropic-s-record-ipo-lifts-tech
- [CoinDesk] Singapore settles $77.5 million tokenized bill sale in local CBDC (11-19 19:39) — https://www.coindesk.com/business/2026/11/19/singapore-settles-usd77-5-million-tokenized-bill-sale-in-local-cbdc
- [The Block] Ant International launches protocol for real-time settlement between tokenized deposits and money market funds (11-19 19:39) — https://www.theblock.co/news/business/2026-11-19-ant-international-protocol-tokenized-assets-443586
- [Cointelegraph] IOSCO warns quantum upgrades could slow blockchains, leave security gaps (11-19 19:32) — https://cointelegraph.com/news/iosco-quantum-blockchain-upgrades-security-risks?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Roundhill scraps Solana and XRP income ETFs as rival funds indicate low demand (11-19 19:22) — https://www.coindesk.com/markets/2026/11/19/roundhill-scraps-solana-and-xrp-income-etfs-as-rival-funds-attract-just-usd12-million

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