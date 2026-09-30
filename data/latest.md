# 코인 데일리 스냅샷

- 수집 시각: 2026-09-30 09:50 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 매수** → BTC 목표 비중 **80%** (전일 판정: 매수)
- 오늘 총점 6.9 / 3일 평균 15.6 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)
- 오늘 구간 '중립'는 첫날 → 내일도 같으면 변경, 오늘은 '매수' 유지

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | 50.0 |
| 파생·심리 | 30% | 0.0 |
| 밸류에이션 | 25% | -25.0 |
| 매크로 | 15% | -12.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +0 | +0 | MVRV Z 1.09 |
| 밸류에이션 | 가격÷STH-RP | -1 | -1 | 가격÷STH-RP 1.160 |
| 수급 | 현물 ETF 순유입 | +2 | +2 | 8거래일 연속 순유입 |
| 수급 | 거래소 순유입(7일) | +2 | +2 | 7일 순유입 분포 2백분위 |
| 수급 | 거래소 보유량(30일) | +1 | +1 | 30일 -0.78% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | -1 | — | 7일 +3.1% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0053% |
| 파생·심리 | RSI(14) | -1 | -1 | RSI 61.3 |
| 파생·심리 | 롱/숏 비율 | -1 | +0 | 롱/숏 분포 77백분위 |
| 파생·심리 | 미결제약정(OI) | +1 | +1 | OI 7일 -9.2%, 가격 -3.0% (레버리지 정리) |
| 파생·심리 | 옵션 스큐 | +0 | -1 | +0.05 |
| 매크로 | 나스닥 | +1 | +1 | 50일선 위 |
| 매크로 | DXY | -1 | -1 | 101.41, 20일 +2.0% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 157.33 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -1 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 26797.541 | 26820.381 | pt | 2026-09-29 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -1.64 | -1.11 | % | 2026-09-29 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26221.32 | 26195.53 | pt | 2026-09-29 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 101.406 | 101.2 | pt | 2026-09-29 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.99 | 1.55 | % | 2026-09-29 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 157.33 | 157.361 | 엔 | 2026-09-30 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | -0.09 | 0.06 | % | 2026-09-30 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 3.71 | 3.54 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-09-11 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.76 | 2.79 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-09-11 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.7 | 3.72 | % | 2026-07-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-08-26 (점수 미반영: 발표 후 30일 경과) |
| A.매크로 | 근원 PCE 전년비 | 3.34 | 3.34 | % | 2026-07-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-08-26 (점수 미반영: 발표 후 30일 경과) |
| A.매크로 | 인플레이션 방향 합계 | -1 | -1 |  | 2026-09-30 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.398 | 6.38 | % | 2026-09-30 00:46 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.8663 | 2.8755 | 조$ | 2026-09-30 00:46 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | 31.1 | 134.5 | 백만$ | 2026-09-28 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 8거래일 연속 순유입 / 집계 기준일 2026-09-28 |
| B.자금흐름 | IBIT(블랙록) 순유입 | 54.8 | 97.0 | 백만$ | 2026-09-28 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | 1417.9 | 2385.8 | 백만$ | 2026-09-28 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | 8 | 7 | 일 | 2026-09-28 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 83638.42 | 83456.74 | USD | 2026-09-29 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 61.26 | 60.75 |  | 2026-09-29 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -2.97 | -3.62 | % | 2026-09-29 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.09 | 3.15 | 십억$ | 2026-09-29 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -9.17 | -7.14 | % | 2026-09-29 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 1.42 | 1.38 | 배 | 2026-09-29 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 76.7 | 66.7 | 백분위 | 2026-09-29 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.01 | 0.0033 | % | 2026-09-30 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0053 | 0.0039 | % | 2026-09-30 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 35.22 | 36.03 |  | 2026-09-30 00:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 0.05 | 0.85 | vol pt | 2026-09-30 00:50 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-10-30, 콜 BTC-30OCT26-90000-C / 풋 BTC-30OCT26-79000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 1.0948 | 1.11 |  | 2026-09-23 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.16 | 1.19 |  | 2026-09-23 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 72239.0 | 70184.0 | $ | 2026-09-23 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 83798.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 28047.1 | 12578.8 | BTC | 2026-09-28 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 30287.7 | 16041.3 | BTC | 2026-09-28 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -53433.0 | -55059.4 | BTC | 2026-09-28 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 2.2 | 1.1 | 백분위 | 2026-09-28 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -2240.5 | -3462.5 | BTC | 2026-09-28 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -0.78 | -0.72 | % | 2026-09-28 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2683692.0 | 2682330.0 | BTC | 2026-09-28 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (09-29 18:00 ~ 09-30 09:50 KST)

피드 상태: CoinDesk: 11건 / The Block: 6건 / Cointelegraph: 15건 / 블록미디어: 10건

- [블록미디어] [개장시황] 美 반도체주 강세에 코스피 1%대 반등⋯외국인·기관 동반 매수 (09-30 09:33) — https://www.blockmedia.co.kr/archives/1145793?utm_source=general&utm_medium=rss
- [Cointelegraph] Trump accord calls for tech firms to ‘self police’ their own frontier AI (09-30 09:28) — https://cointelegraph.com/news/trump-accord-calls-for-tech-firms-to-self-police-their-own-frontier-ai?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 두나무 찾은 백악관 디지털자산 책임자 “전통금융과 통합될 것…韓, 지금이 제도 마련 적기” (09-30 09:06) — https://www.blockmedia.co.kr/archives/1145785?utm_source=general&utm_medium=rss
- [블록미디어] [코인시황] 비트코인, 금 급락 속 상대적 강세…10만달러 전망도 (09-30 08:24) — https://www.blockmedia.co.kr/archives/1145772?utm_source=general&utm_medium=rss
- [블록미디어] 연준 비둘기파 발언도 안 먹혔다…美 30년물 금리 24년 만에 최고 (09-30 08:10) — https://www.blockmedia.co.kr/archives/1145768?utm_source=general&utm_medium=rss
- [CoinDesk] Robinhood adds AI agents, perps and weekend trading in push to win active traders (09-30 08:00) — https://www.coindesk.com/markets/2026/09/29/robinhood-adds-ai-agents-perps-and-weekend-trading-in-push-to-win-active-traders
- [블록미디어] ‘사토시 후보’ 아담 백의 비트코인 제국 흔들…3.2억달러 해킹에 소송까지 (09-30 07:49) — https://www.blockmedia.co.kr/archives/1145762?utm_source=general&utm_medium=rss
- [블록미디어] 메타 AI ‘뮤즈’, 애플 앱스토어 30% 수수료 흔드나… “서비스 사업에 경고등” (09-30 07:11) — https://www.blockmedia.co.kr/archives/1145744?utm_source=general&utm_medium=rss
- [블록미디어] 美 신용카드 연체율 급등… 비트코인에도 ‘위험회피’ 경고등 (09-30 06:53) — https://www.blockmedia.co.kr/archives/1145741?utm_source=general&utm_medium=rss
- [블록미디어] [뉴욕 금·채권·달러] 달러·국채금리 고공행진에도 금 1.7% 반등 (09-30 06:46) — https://www.blockmedia.co.kr/archives/1145745?utm_source=general&utm_medium=rss
- [블록미디어] 칼시, 기업가치 400억달러로 10억달러 조달 추진… 4개월 만에 몸값 82% 뛰었다 (09-30 06:21) — https://www.blockmedia.co.kr/archives/1145732?utm_source=general&utm_medium=rss
- [블록미디어] [뉴욕 코인시황] 비트코인 8만3500달러 공방…고금리·고유가 속 ETF 순유입 (09-30 06:00) — https://www.blockmedia.co.kr/archives/1145736?utm_source=general&utm_medium=rss
- [Cointelegraph] Crypto regulation at SEC, CFTC to come down to 3 commissioners following key resignation (09-30 04:59) — https://cointelegraph.com/news/us-sec-cftc-crypto-regulation-few-commissioners?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] OpenAI valuation could hit $1.4T in new funding round: Report (09-30 04:55) — https://cointelegraph.com/news/openai-30-billion-funding-round-1-4-trillion-valuation?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Kakaopay partners with Dinari, Ondo to explore tokenized Korean stocks (09-30 04:49) — https://cointelegraph.com/news/kakaopay-securities-dinari-ondo-tokenized-korean-stocks-push?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Here’s what happened in crypto today (09-30 04:42) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] CryptoQuant says bitcoin correction could be near as traders’ unrealized profit hits 21-month high (09-30 04:14) — https://www.theblock.co/news/markets/2026-09-29-cryptoquant-says-bitcoin-correction-could-near-traders-unrealized-profit-21-month-high-417206
- [CoinDesk] Cboe, S&P Dow Jones may explore tokenized options contracts under extended licensing deal (09-30 03:21) — https://www.coindesk.com/business/2026/09/29/cboe-s-and-p-dow-jones-may-explore-tokenized-options-contracts-under-extended-licensing-deal
- [The Block] Comer presses Crypto.com, Hyperliquid and PredictIt on identity checks and suspicious trades (09-30 02:40) — https://www.theblock.co/news/regulation/2026-09-29-comer-presses-crypto-com-hyperliquid-predictit-identity-checks-suspicious-trades-417192
- [Cointelegraph] Bitwise launches first US spot NEAR ETF after token’s recent surge (09-30 02:14) — https://cointelegraph.com/news/bitwise-launches-first-us-spot-near-etf-after-tokens-recent-surge?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin gives back gains as long-term holder supply keeps $85K out of reach (09-30 01:26) — https://cointelegraph.com/markets/bitcoin-gives-back-gains-long-term-holder-supply-keeps-85k-out-of-reach?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitget CEO ‘not very optimistic’ on recovering funds from $388M breach (09-30 01:18) — https://cointelegraph.com/news/bitget-ceo-gracy-chen-chances-recovering-funds-security-breach?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Ethereum users get another way to pay privately as zk.money returns after three years (09-30 01:00) — https://www.coindesk.com/tech/2026/09/29/embargo-12-et-ethereum-users-get-another-way-to-pay-privately-as-zk-money-returns-after-three-years
- [The Block] Aztec relaunches zk.money privacy wallet on its Ethereum Layer 2 (09-30 01:00) — https://www.theblock.co/news/defi/2026-09-29-aztec-zk-money-privacy-wallet-ethereum-layer-2-417174
- [The Block] Bitcoin tests long-term holder supply cluster as leverage clears, analysts say (09-30 00:09) — https://www.theblock.co/news/markets/2026-09-29-bitcoin-tests-long-term-holder-supply-cluster-leverage-clears-analysts-say-417162
- [The Block] Bitwise launches first US spot NEAR ETF with staking rewards (09-29 23:27) — https://www.theblock.co/news/markets/2026-09-29-bitwise-near-etf-nrr-launch-staking-417150
- [CoinDesk] Democrats killed the Clarity Act (09-29 23:08) — https://www.coindesk.com/opinion/2026/09/29/democrats-killed-the-clarity-act
- [Cointelegraph] Peter Brandt says Bitcoin may hit $600K by 2029, calls XRP a ‘fool coin’ (09-29 22:30) — https://cointelegraph.com/magazine/peter-brandt-says-bitcoin-may-hit-600k-by-2029-calls-xrp-a-fool-coin?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin ETF inflows leave institutional demand unclear: CoinShares (09-29 21:40) — https://cointelegraph.com/markets/bitcoin-etf-mixed-read-institutional-demand-coinshares?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] ECB puts AI agent payments on the digital euro drawing board (09-29 21:00) — https://cointelegraph.com/news/ecb-private-firms-ai-agents-digital-euro?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin surging to $100,000 may be in play, after outperforming gold (09-29 20:34) — https://www.coindesk.com/daybook-us/2026/09/29/bitcoin-outperforms-gold-usd100-000-surge-in-play
- [CoinDesk] Zcash developers begin moving Tachyon code into faster private-payment software (09-29 20:15) — https://www.coindesk.com/tech/2026/09/29/zcash-s-faster-private-payment-code-is-being-rebuilt-for-its-bigger-scaling-plan
- [The Block] Ondo Perps CEO sees ‘huge opportunity’ for perps in US market, under different model (09-29 19:58) — https://www.theblock.co/news/regulation/2026-09-29-ondo-perps-ceo-interview-david-wells-417125
- [Cointelegraph] Ethereum schedules Glamsterdam upgrade on Sepolia for Oct. 6 (09-29 19:46) — https://cointelegraph.com/news/ethereum-glamsterdam-upgrade-sepolia?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Aave leads DeFi higher as crypto shrugs off surging bond market (09-29 19:28) — https://www.coindesk.com/markets/2026/09/29/aave-leads-defi-higher-as-crypto-shrugs-off-surging-treasury-yields
- [Cointelegraph] US crypto ETF inflows cool after $3.3B week but streaks hold (09-29 19:15) — https://cointelegraph.com/markets/us-crypto-etf-inflows-cool-bitcoin-ether-solana-xrp?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Live updates: Bitcoin turns lower as rates rise, consumer confidence plunges (09-29 19:14) — https://www.coindesk.com/markets/2026/09/29/live-updates-bitcoin-rebounds-above-usd84-000-as-treasury-yields-steady
- [CoinDesk] Blockchain.com targets $500 million IPO this year at up to $6 billion valuation (09-29 19:13) — https://www.coindesk.com/business/2026/09/29/blockchain-com-targets-usd500-million-ipo-at-up-to-usd6-billion-valuation
- [Cointelegraph] Bitcoin bounces to $84K after US 30-year bond yield sets 24-year high (09-29 19:04) — https://cointelegraph.com/markets/bitcoin-bounces-to-84k-after-us-30-year-bond-yield-sets-24-year-high?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Greece gets first MiCA entrants as watchdog denies Binance-Lagarde claim (09-29 18:50) — https://cointelegraph.com/news/greece-first-mica-entrants-hcmc-binance-lagarde?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin is on track to shatter a major decade-long streak as September gains surge (09-29 18:45) — https://www.coindesk.com/markets/2026/09/29/bitcoin-is-on-track-to-shatter-a-major-decade-long-streak-as-september-gains-surge
- [CoinDesk] Analysts see 10-year Treasury yield hitting 6%. Bitcoin bulls shouldn't panic (09-29 18:06) — https://www.coindesk.com/markets/2026/09/29/analysts-see-10-year-treasury-yield-hitting-6-bitcoin-bulls-shouldn-t-panic

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