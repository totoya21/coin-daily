# 코인 데일리 스냅샷

- 수집 시각: 2026-10-01 09:50 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 매수)
- 오늘 총점 3.9 / 3일 평균 9.2 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)
- '중립' 구간 2일 연속 → 판정 변경 (매수 → 중립)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | 50.0 |
| 파생·심리 | 30% | -10.0 |
| 밸류에이션 | 25% | -25.0 |
| 매크로 | 15% | -12.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +0 | +0 | MVRV Z 1.03 |
| 밸류에이션 | 가격÷STH-RP | -1 | -1 | 가격÷STH-RP 1.160 |
| 수급 | 현물 ETF 순유입 | +2 | +2 | 9거래일 연속 순유입 |
| 수급 | 거래소 순유입(7일) | +1 | +2 | 7일 순유입 분포 11백분위 |
| 수급 | 거래소 보유량(30일) | +1 | +1 | 30일 -0.65% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | +0 | -1 | 7일 +0.3% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0041% |
| 파생·심리 | RSI(14) | -1 | -1 | RSI 60.9 |
| 파생·심리 | 롱/숏 비율 | -1 | -1 | 롱/숏 분포 77백분위 |
| 파생·심리 | 미결제약정(OI) | +1 | +1 | OI 7일 -8.5%, 가격 -1.0% (레버리지 정리) |
| 파생·심리 | 옵션 스큐 | -1 | +0 | +0.97 (풋 우위 확대, 전일 +0.05) |
| 매크로 | 나스닥 | +1 | +1 | 50일선 위 |
| 매크로 | DXY | -1 | -1 | 101.49, 20일 +1.8% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 157.80 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -2 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 26861.064 | 26797.539 | pt | 2026-09-30 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -0.28 | -1.64 | % | 2026-09-30 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26241.79 | 26221.32 | pt | 2026-09-30 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 101.493 | 101.37 | pt | 2026-09-30 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.83 | 1.99 | % | 2026-09-30 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 157.796 | 157.404 | 엔 | 2026-10-01 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | -0.3 | -0.09 | % | 2026-10-01 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 3.71 | 3.54 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-09-11 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.76 | 2.79 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-09-11 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.42 | 3.36 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.01 | 2.98 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -2 | -1 |  | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.385 | 6.398 | % | 2026-10-01 00:49 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.8712 | 2.8663 | 조$ | 2026-10-01 00:49 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | 66.2 | 31.1 | 백만$ | 2026-09-29 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 9거래일 연속 순유입 / 집계 기준일 2026-09-29 |
| B.자금흐름 | IBIT(블랙록) 순유입 | 51.1 | 54.8 | 백만$ | 2026-09-29 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | 769.4 | 1417.9 | 백만$ | 2026-09-29 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | 9 | 8 | 일 | 2026-09-29 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 83556.14 | 83638.42 | USD | 2026-09-30 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 60.87 | 61.26 |  | 2026-09-30 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -0.97 | -2.97 | % | 2026-09-30 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.06 | 3.09 | 십억$ | 2026-09-30 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -8.54 | -9.17 | % | 2026-09-30 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 1.38 | 1.32 | 배 | 2026-09-30 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 76.7 | 76.7 | 백분위 | 2026-09-30 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.0053 | 0.0037 | % | 2026-10-01 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0041 | 0.0053 | % | 2026-10-01 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 35.25 | 35.1 |  | 2026-10-01 00:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 0.97 | 0.05 | vol pt | 2026-10-01 00:51 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-10-30, 콜 BTC-30OCT26-90000-C / 풋 BTC-30OCT26-79000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 1.0328 | 1.0948 |  | 2026-09-24 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.16 | 1.16 |  | 2026-09-24 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 72180.0 | 72239.0 | $ | 2026-09-24 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 83728.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 28302.4 | 28047.1 | BTC | 2026-09-29 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 26433.3 | 30287.7 | BTC | 2026-09-29 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -34657.1 | -53433.0 | BTC | 2026-09-29 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 11.1 | 2.2 | 백분위 | 2026-09-29 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | 1869.0 | -2240.5 | BTC | 2026-09-29 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -0.65 | -0.78 | % | 2026-09-29 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2686232.0 | 2683692.0 | BTC | 2026-09-29 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (09-30 18:00 ~ 10-01 09:50 KST)

피드 상태: CoinDesk: 13건 / The Block: 10건 / Cointelegraph: 16건 / 블록미디어: 10건

- [블록미디어] 블록페스타 2026 개막…기관 ‘온체인 금융’ 전환 머리 맞댄다 (10-01 09:45) — https://www.blockmedia.co.kr/archives/1146351?utm_source=general&utm_medium=rss
- [블록미디어] [개장시황] 코스피, 9월 수출 사상 최대에도 금리 부담…0.29% 하락 출발 (10-01 09:23) — https://www.blockmedia.co.kr/archives/1146338?utm_source=general&utm_medium=rss
- [Cointelegraph] MetaMask exits Ethereum validators as it investigates security incident (10-01 09:15) — https://cointelegraph.com/news/metamask-exits-lido-validators-as-it-investigates-security-incident?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 비트코인 3분기 43% 급등…10월 업토버 가능할까 (10-01 08:50) — https://www.blockmedia.co.kr/archives/1146334?utm_source=general&utm_medium=rss
- [블록미디어] 마이크론, 4분기 ‘어닝 깜짝실적’에도 시간외 0.7% 약세 (10-01 07:08) — https://www.blockmedia.co.kr/archives/1146317?utm_source=general&utm_medium=rss
- [The Block] Clarity Act’s failure gave crypto ‘faster’ regulatory wins, Bitwise CIO says (10-01 06:53) — https://www.theblock.co/news/markets/2026-09-30-clarity-acts-failure-gave-crypto-faster-regulatory-wins-bitwise-says-417362
- [블록미디어] [뉴욕 금·채권·달러] “물가 내렸지만 경기는 강하다”…미 10년물 금리 5.29% 육박 (10-01 06:49) — https://www.blockmedia.co.kr/archives/1146309?utm_source=general&utm_medium=rss
- [Cointelegraph] Standard Chartered sees Ethena’s USDe reaching $40B, ENA hitting $2 (10-01 05:57) — https://cointelegraph.com/markets/standard-chartered-ethena-usde-growth-40b?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] [뉴욕 코인시황] “물가 둔화에도 꺾였다”… 비트코인, 8만3000달러대 후퇴 (10-01 05:48) — https://www.blockmedia.co.kr/archives/1146293?utm_source=general&utm_medium=rss
- [The Block] CFTC secures over $30 million judgment against defendants in Fundsz fraud case (10-01 05:37) — https://www.theblock.co/news/regulation/2026-09-30-cftc-secures-over-30-million-judgment-against-defendants-in-fundsz-fraud-case-417365
- [블록미디어] [뉴욕증시 마감] 물가 둔화에도 장기금리 고공행진…주요지수 혼조세·다우 444p↓ (10-01 05:13) — https://www.blockmedia.co.kr/archives/1146278?utm_source=general&utm_medium=rss
- [Cointelegraph] Here’s what happened in crypto today (10-01 04:37) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Crypto advocacy group announces picks for US Congress as midterms loom (10-01 04:11) — https://cointelegraph.com/news/stand-with-crypto-coinbase-senate-picks-us-midterms?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Base launches Cobalt upgrade with conditional transactions and new B20 asset functions (10-01 04:00) — https://www.theblock.co/news/ecosystems/2026-09-30-base-launches-cobalt-upgrade-with-conditional-transactions-and-new-b20-asset-functions-417308
- [Cointelegraph] Base completes Cobalt upgrade, adds new tools for tokenized assets (10-01 04:00) — https://cointelegraph.com/news/base-cobalt-upgrade-tokenized-finance-b20-kyc?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bloomberg brings onchain stablecoin data to its Terminal (10-01 03:49) — https://cointelegraph.com/news/bloomberg-brings-onchain-stablecoin-data-to-its-terminal-news-brief?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] [속보] 비트코인 8만3000달러대 재하락 (10-01 03:41) — https://www.blockmedia.co.kr/archives/1146264?utm_source=general&utm_medium=rss
- [블록미디어] 연준 감찰관실 “24억달러 본부 리노베이션, 범죄 행위 증거 없어” (10-01 03:38) — https://www.blockmedia.co.kr/archives/1146260?utm_source=general&utm_medium=rss
- [블록미디어] 애플, ‘6인치 AI 허브’로 스마트홈 시장 본격 진격…13일 공개 (10-01 03:26) — https://www.blockmedia.co.kr/archives/1146258?utm_source=general&utm_medium=rss
- [The Block] DogeOS launches testnet to bring EVM smart contracts to Dogecoin (10-01 03:23) — https://www.theblock.co/news/ecosystems/2026-09-30-dogeos-launches-public-testnet-dogecoin-zk-rollup-evm-417307
- [The Block] White House weighs new CFTC event contract rules in growing prediction market power struggle (10-01 02:54) — https://www.theblock.co/news/regulation/2026-09-30-white-house-weighs-new-cftc-event-contract-rules-in-growing-prediction-market-power-struggle-417345
- [Cointelegraph] Brazil’s Petrobras uses Cardano to track sustainable aviation fuel, renewable diesel (10-01 02:17) — https://cointelegraph.com/news/brazils-petrobras-uses-cardano-to-track-sustainable-aviation-fuel-renewable-diesel?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Crypto industry gave $8 million to Clarity Act lobbyists who didn't close the deal (10-01 02:16) — https://www.coindesk.com/news-analysis/2026/09/30/crypto-industry-gave-usd8-million-to-clarity-act-lobbyists-who-didn-t-close-the-deal
- [Cointelegraph] Bitget ‘gradually back to usual’ as protection fund reaches $309M (10-01 01:28) — https://cointelegraph.com/news/bitget-operations-protection-fund-security-breach?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Bitcoin steadies as soft PCE cools October Fed rate hike bets (10-01 01:10) — https://www.theblock.co/news/markets/2026-09-30-bitcoin-pce-inflation-october-rate-hike-417335
- [CoinDesk] Open USD takes on Tether, Circle with a different stablecoin model that's 'building money' (10-01 00:34) — https://www.coindesk.com/business/2026/09/24/open-usd-takes-on-tether-circle-with-a-different-stablecoin-model-that-s-building-money
- [CoinDesk] U.S. CFTC  seeks event contract definitions that may defy states' gambling claims (10-01 00:19) — https://www.coindesk.com/policy/2026/09/30/u-s-cftc-seeks-event-contract-definitions-that-may-defy-states-gambling-claims
- [CoinDesk] Crypto Long & Short: What will the AI agents run on? (09-30 23:56) — https://www.coindesk.com/coindesk-indices/2026/09/30/crypto-long-and-short-what-will-the-ai-agents-run-on
- [CoinDesk] Clock's ticking: UK's crypto regulatory application window opens with February deadline (09-30 23:04) — https://www.coindesk.com/policy/2026/09/30/the-clock-s-ticking-uk-s-crypto-regulatory-application-window-opens-with-february-deadline
- [The Block] Hyperliquid Co-founder Jeff Yan says 24-hour clock is not onchain finance’s true differentiator (09-30 22:33) — https://www.theblock.co/news/defi/2026-09-30-hyperliquid-co-founder-jeff-yan-24-hour-clock-not-onchain-finances-true-differentiator-417286
- [Cointelegraph] Could THORChain face prosecution over stolen Bitget funds? Legal opinion (09-30 22:30) — https://cointelegraph.com/magazine/does-thorchain-face-a-criminal-reckoning-near-intents-bitget?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] FCA starts accepting crypto authorization applications ahead of 2027 regime (09-30 22:21) — https://www.theblock.co/news/regulation/2026-09-30-fca-starts-accepting-crypto-authorization-applications-ahead-of-2027-regime-417284
- [CoinDesk] Cardano tapped by Brazil’s state oil giant to track cleaner jet fuel and diesel (09-30 22:00) — https://www.coindesk.com/tech/2026/09/30/embargo-1-pm-utc-cardano-tapped-by-brazil-s-state-oil-giant-to-track-cleaner-jet-fuel-and-diesel
- [Cointelegraph] Singapore crypto activity grows 55% as broader region contracts (09-30 22:00) — https://cointelegraph.com/news/singapore-crypto-economy-284b-institutional-activity-chainalysis?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] FCA opens crypto authorization window ahead of 2027 UK regime (09-30 21:06) — https://cointelegraph.com/news/fca-crypto-authorization-2027-uk-regime?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Standard Chartered sees over 600% upside for ENA, expects USDe to hit $40 billion by 2028 (09-30 21:00) — https://www.theblock.co/news/markets/2026-09-30-standard-chartered-sees-over-600-upside-for-ena-expects-usde-to-hit-40-billion-by-2028-417274
- [The Block] Crypto advocacy group Stand With Crypto rolls out its first round of Senate endorsements after failed Clarity vote (09-30 21:00) — https://www.theblock.co/news/regulation/2026-09-30-crypto-advocacy-group-stand-with-crypto-first-senate-endorsements-after-failed-clarity-417223
- [Cointelegraph] Altcoin exchange deposit count jumps 160% in 2 weeks (09-30 20:23) — https://cointelegraph.com/markets/altcoin-exchange-deposits-spike-160-in-two-weeks?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] A stronger dollar is a weaker threat to bitcoin than traders think (09-30 20:20) — https://www.coindesk.com/daybook-us/2026/09/30/a-stronger-dollar-is-a-weaker-threat-to-bitcoin-than-traders-think
- [CoinDesk] Bitget hackers move $4 million into Zcash’s private pool, making funds harder to trace (09-30 20:04) — https://www.coindesk.com/markets/2026/09/30/bitget-hackers-move-usd4-million-into-zcash-s-private-pool-making-funds-harder-to-trace
- [CoinDesk] The SEC Is finally modernizing transfer-agent rules. Wall Street must not repeat the ‘paperwork crisis’ (09-30 20:00) — https://www.coindesk.com/opinion/2026/09/30/the-sec-is-finally-modernizing-transfer-agent-rules-wall-street-must-not-repeat-the-paperwork-crisis
- [Cointelegraph] A single market worth protecting: Getting the MiCA review right (09-30 20:00) — https://cointelegraph.com/opinion/a-single-market-worth-protecting-getting-the-mica-review-right?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] OpenAI, Google and Meta pledge independent AI safety audits under voluntary White House deal (09-30 19:43) — https://www.coindesk.com/tech/2026/09/30/openai-google-and-meta-pledge-outside-ai-audits-under-voluntary-white-house-deal
- [CoinDesk] Metaplanet directors push back against shareholder fury over a controversial executive payout plan (09-30 19:28) — https://www.coindesk.com/markets/2026/09/30/metaplanet-directors-push-back-against-shareholder-fury-over-a-controversial-executive-payout-plan
- [CoinDesk] Live updates: Bitcoin closing out best quarter since 2024, ether its best since 2021 (09-30 19:18) — https://www.coindesk.com/markets/2026/09/30/live-updates-bitcoin-below-usd84-000-ahead-of-pce-inflation-data-micron-earnings
- [Cointelegraph] Bitcoin ETFs stretch $3.1B inflow streak as Ether funds turn red (09-30 19:12) — https://cointelegraph.com/markets/bitcoin-etf-streak-9-day-ether-zcash-flip-red?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin stalls near $83,000 while lighter drops 17% on Robinhood perps plan (09-30 19:11) — https://www.coindesk.com/markets/2026/09/30/bitcoin-stalls-near-usd83-000-while-lighter-drops-17-on-robinhood-perps-plan
- [Cointelegraph] Crypto hardware wallets compared for 2026 (09-30 19:11) — https://cointelegraph.com/magazine/crypto-hardware-wallets-compared-for-2026?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] SlowMist traces Bitget hack activity to Aug. 31 zero-day exploit (09-30 19:05) — https://cointelegraph.com/news/bitget-hack-zero-day-slowmist-investigation?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

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