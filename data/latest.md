# 코인 데일리 스냅샷

- 수집 시각: 2026-11-11 15:57 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 -12.5 / 3일 평균 -9.8 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | -50.0 |
| 파생·심리 | 30% | 0.0 |
| 밸류에이션 | 25% | 25.0 |
| 매크로 | 15% | -25.0 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.86 |
| 밸류에이션 | 가격÷STH-RP | +0 | +0 | 가격÷STH-RP 1.060 |
| 수급 | 현물 ETF 순유입 | -2 | -1 | 3거래일 연속 순유출 |
| 수급 | 거래소 순유입(7일) | +0 | +0 | 7일 순유입 분포 50백분위 |
| 수급 | 거래소 보유량(30일) | -1 | -1 | 30일 +1.25% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | -1 | +0 | 7일 +5.3% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0083% |
| 파생·심리 | RSI(14) | +1 | +1 | RSI 34.2 |
| 파생·심리 | 롱/숏 비율 | -1 | -2 | 롱/숏 분포 87백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +0 | OI 7일 +5.2%, 가격 -4.7% |
| 파생·심리 | 옵션 스큐 | -1 | +0 | +3.98 (풋 우위 확대, 전일 +3.32) |
| 매크로 | 나스닥 | -1 | -1 | 50일선 아래 |
| 매크로 | DXY | +0 | +0 | 102.35, 20일 -0.2% |
| 매크로 | USD/JPY | +0 | +0 | 158.84 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -4 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 25065.869 | 25253.141 | pt | 2026-11-10 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -1.21 | 0.35 | % | 2026-11-10 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26408.73 | 26434.83 | pt | 2026-11-10 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 102.349 | 102.23 | pt | 2026-11-11 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | -0.2 | -0.6 | % | 2026-11-11 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 158.84 | 157.983 | 엔 | 2026-11-11 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | 0.23 | 0.04 | % | 2026-11-11 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.08 | 4.02 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.87 | 2.79 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.65 | 3.44 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.12 | 3.03 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -4 | -3 |  | 2026-11-11 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 7.108 | 7.009 | % | 2026-11-11 06:51 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.4683 | 2.5166 | 조$ | 2026-11-11 06:51 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | -201.1 | -411.9 | 백만$ | 2026-11-09 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 3거래일 연속 순유출 / 집계 기준일 2026-11-09 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -213.2 | -403.0 | 백만$ | 2026-11-09 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -1084.2 | -1281.7 | 백만$ | 2026-11-09 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | -3 | -2 | 일 | 2026-11-09 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 73697.87 | 75259.28 | USD | 2026-11-10 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 34.21 | 37.92 |  | 2026-11-10 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -4.71 | -1.85 | % | 2026-11-10 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.86 | 3.85 | 십억$ | 2026-11-10 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | 5.21 | 6.2 | % | 2026-11-10 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 2.92 | 3.19 | 배 | 2026-11-10 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 86.7 | 90.0 | 백분위 | 2026-11-10 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.01 | 0.0048 | % | 2026-11-11 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0083 | 0.0066 | % | 2026-11-11 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 39.8 | 39.44 |  | 2026-11-11 06:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 3.98 | 3.32 | vol pt | 2026-11-11 06:57 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-11-27, 콜 BTC-27NOV26-78000-C / 풋 BTC-27NOV26-70000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.8591 | 0.7698 |  | 2026-11-04 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.0603 | 1.0255 |  | 2026-11-04 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 69472.0 | 73292.0 | $ | 2026-11-04 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 73661.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 38720.9 | 19946.6 | BTC | 2026-11-10 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 31999.2 | 24537.9 | BTC | 2026-11-10 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -12952.6 | -13674.9 | BTC | 2026-11-10 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 50.0 | 48.9 | 백분위 | 2026-11-10 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | 6721.7 | -4591.3 | BTC | 2026-11-10 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | 1.25 | 1.04 | % | 2026-11-10 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2708334.0 | 2701577.0 | BTC | 2026-11-10 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (11-10 18:00 ~ 11-11 15:57 KST)

피드 상태: CoinDesk: 14건 / The Block: 18건 / Cointelegraph: 23건 / 블록미디어: 10건

- [The Block] Bitmine reports $6.3 billion net loss in latest fiscal year, driven by 44% ether decline (11-11 15:22) — https://www.theblock.co/news/business/2026-11-11-bitmine-6-3-billion-net-loss-437812
- [Cointelegraph] Here’s what happened in crypto today (11-11 15:00) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] “바닥 찍었나” 비트코인 저점 낮추는데…단기 보유자 손실 물량 거래소 유입은 ‘급감’ (11-11 15:00) — https://www.blockmedia.co.kr/archives/1164380?utm_source=general&utm_medium=rss
- [블록미디어] 이더리움 ETF 나흘 연속 순유출…블랙록 스테이킹 상품엔 자금 유입 (11-11 14:58) — https://www.blockmedia.co.kr/archives/1164395?utm_source=general&utm_medium=rss
- [Cointelegraph] Initia confirms second exploit in 3 weeks, $3.27M stolen in latest attack (11-11 14:52) — https://cointelegraph.com/news/initia-second-crypto-exploit-three-weeks?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 비트코인 ETF 4거래일 연속 자금 유출…블랙록서 7800만달러 빠져 (11-11 14:49) — https://www.blockmedia.co.kr/archives/1164396?utm_source=general&utm_medium=rss
- [블록미디어] 美 금리 인상 내년까지 간다…골드만삭스 “3월에도 추가 인상” (11-11 14:31) — https://www.blockmedia.co.kr/archives/1164357?utm_source=general&utm_medium=rss
- [블록미디어] STRC 어떻게 볼 것인가? 신규 발행 없이 100달러선에 도달–비트플래닛 (11-11 14:23) — https://www.blockmedia.co.kr/archives/1164249?utm_source=general&utm_medium=rss
- [블록미디어] 루미스, ‘디지털자산 효용 없다’는 워런 정면 비판…”급여·해외송금 혁신 외면” (11-11 14:00) — https://www.blockmedia.co.kr/archives/1164329?utm_source=general&utm_medium=rss
- [Cointelegraph] Across Protocol restores website after hackers hijack domain (11-11 13:42) — https://cointelegraph.com/news/across-protocol-restores-website-after-hackers-hijack-domain?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 7만4000달러 하회한 비트코인 다시 출렁이나…PPI·AI 실적·MSCI 편출 ‘3대 변수’ (11-11 13:25) — https://www.blockmedia.co.kr/archives/1164313?utm_source=general&utm_medium=rss
- [블록미디어] 이더리움 고점에 팔고 26% 하락하자 재매수…고래 719개 더 확보 (11-11 13:08) — https://www.blockmedia.co.kr/archives/1164286?utm_source=general&utm_medium=rss
- [The Block] Tron Inc reports 22% rise in Q3 net income as unrealized staking revenue grows (11-11 13:02) — https://www.theblock.co/news/business/2026-11-10-tron-inc-q3-net-income-437786
- [블록미디어] 엔비디아 이틀간 10% 급락…월가 “저가 매수 기회” vs “CEO 교체 위험”(종합) (11-11 12:35) — https://www.blockmedia.co.kr/archives/1164284?utm_source=general&utm_medium=rss
- [블록미디어] 48시간 만에 ‘안도’가 ‘패닉’으로…월가 공황지수, 13년 전 기록 갈아치웠다 (11-11 12:30) — https://www.blockmedia.co.kr/archives/1164342?utm_source=general&utm_medium=rss
- [Cointelegraph] Crypto ally Tom Emmer elected House GOP minority whip (11-11 12:07) — https://cointelegraph.com/news/crypto-ally-tom-emmer-elected-house-gop-minority-whip?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] LNbits rushes emergency patch after reported Bitcoin wallet thefts (11-11 10:16) — https://cointelegraph.com/news/lnbits-rushes-emergency-patch-after-reported-bitcoin-wallet-thefts?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] CFTC warns Kalshi of imminent charges over notification of contracts: Politico (11-11 08:49) — https://cointelegraph.com/news/cftc-warns-kalshi-imminent-charges-over-contracts?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Global banks commit $270M to stablecoin venture targeting 2027 launch (11-11 08:08) — https://cointelegraph.com/news/banks-270m-project-faro-stablecoin-2027?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Forward Industries grows SOL treasury to 8.7 million as token hits nearly three-month low (11-11 06:51) — https://www.theblock.co/news/markets/2026-11-10-forward-industries-grows-sol-treasury-8-7-million-token-hits-three-month-low-437330
- [Cointelegraph] Can crypto trust firms compete with banks in US derivatives settlements? (11-11 06:34) — https://cointelegraph.com/news/crypto-trust-firms-compete-banks-us-derivatives-settlements?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Across Protocol warns users to avoid app amid reports of drained wallets (11-11 06:24) — https://cointelegraph.com/news/across-protocol-warns-avoid-app-drained-wallets?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Ava Labs exec says NYSE deal marks end of blockchain’s ‘general purpose era’ (11-11 06:07) — https://cointelegraph.com/interview/ava-labs-nyse-general-purpose-chains?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Warren: What is White House doing to prevent a repeat of teleprompter's Trump bets? (11-11 05:36) — https://www.coindesk.com/policy/2026/11/10/warren-what-is-white-house-doing-to-prevent-a-repeat-of-teleprompter-s-trump-bets
- [Cointelegraph] Kimber Digital Securities gains broker-dealer status for tokenized assets (11-11 05:26) — https://cointelegraph.com/news/kimber-digital-securities-broker-dealer-tokenization?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Former NYSE president says stock issuers hold the key to tokenization as Bullish builds its platform (11-11 05:15) — https://www.coindesk.com/business/2026/11/10/former-nyse-president-says-stock-issuers-hold-the-key-to-tokenization-as-bullish-builds-its-platform
- [The Block] Bitcoin slides below $74,000 after hotter-than-expected CPI as analysts warn of drop to $70k (11-11 04:38) — https://www.theblock.co/news/markets/2026-11-10-bitcoin-price-cpi-inflation-73000-support-437301
- [Cointelegraph] Mercado Bitcoin to resume cash withdrawals after $49M hack (11-11 03:12) — https://cointelegraph.com/news/pix-withdrawals-resume-mercado-bitcoin-hack?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Grayscale pledges $1 million alongside Zcash ad blitz as token and ETF fall 12% (11-11 02:52) — https://www.theblock.co/news/markets/2026-11-10-grayscale-pledges-1-million-alongside-zcash-ad-blitz-as-token-and-etf-fall-12-437277
- [CoinDesk] Goldman Sachs, Citi among banks said to commit $270 million to stablecoin venture (11-11 02:32) — https://www.coindesk.com/business/2026/11/10/goldman-sachs-citi-among-banks-said-to-commit-usd270-million-to-stablecoin-venture
- [Cointelegraph] Hot US inflation raises odds of half-point Fed hike in December (11-11 02:31) — https://cointelegraph.com/news/hot-us-inflation-raises-rate-hike-crypto?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] TON Strategy earns $13.1 million from GRAM staking in Q3 as Telegram rolls out native wallet (11-11 02:24) — https://www.theblock.co/news/markets/2026-11-10-ton-strategy-tonx-q3-2026-earnings-gram-staking-437278
- [CoinDesk] Crypto is now teamed up with U.S. government in two legal battles over perps (11-11 02:07) — https://www.coindesk.com/news-analysis/2026/11/10/crypto-teams-up-with-u-s-government-to-defend-stock-perps-in-legal-fight
- [Cointelegraph] Polymarket US trading volume jumps 266% despite regulatory battles (11-11 02:07) — https://cointelegraph.com/news/polymarket-us-trading-volume-jumps-regulatory-battles?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin nears 11-week low after ‘discouraging’ US CPI inflation beat (11-11 01:25) — https://cointelegraph.com/markets/bitcoin-11-week-low-discouraging-us-cpi-inflation?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Alta raises $47.5 million Series A to build a blockchain for financial institutions (11-11 01:19) — https://www.theblock.co/news/business/2026-11-10-alta-raises-80-million-build-blockchain-banks-payment-firms-437244
- [The Block] Canaan’s Q3 revenue plunges 90% to $14.5 million as bitcoin mining hardware sales slump (11-11 01:02) — https://www.theblock.co/news/business/2026-11-10-canaans-q3-revenue-plunges-90-to-14-5-million-as-bitcoin-mining-hardware-sales-slump-437252
- [The Block] MEGA commits $30 million to new products, starting with AI inference (11-11 00:56) — https://www.theblock.co/news/ecosystems/2026-11-10-megaeth-rebrand-30-million-new-products-ai-inference-437249
- [CoinDesk] Plume affiliate lands broker-dealer license to bring real U.S. assets onchain (11-11 00:51) — https://www.coindesk.com/markets/2026/11/10/emb-10-am-et-plume-affiliate-gets-the-legal-green-light-to-trade-regulated-security-entitlements-onchain
- [The Block] Moody’s and Chainlink test cross-chain credit ratings distribution (11-11 00:49) — https://www.theblock.co/news/ecosystems/2026-11-10-moodys-chainlink-ccip-cross-chain-credit-ratings-pilot-437245
- [The Block] Bitdeer reports record Q3 revenue as net loss widens to $125.5 million (11-10 23:26) — https://www.theblock.co/news/business/2026-11-10-bitdeer-reports-record-q3-revenue-as-net-loss-widens-to-125-5-million-437217
- [CoinDesk] Will stablecoins survive once the banks catch up? (11-10 23:00) — https://www.coindesk.com/opinion/2026/11/10/will-stablecoins-survive-once-the-banks-catch-up
- [The Block] Visa adds Monad to stablecoin settlement network options (11-10 23:00) — https://www.theblock.co/news/ecosystems/2026-11-10-visa-monad-stablecoin-settlement-network-437201
- [The Block] eToro’s Q3 profit plunges 74% as weaker crypto trading weighs on earnings (11-10 22:44) — https://www.theblock.co/news/business/2026-11-10-etoros-q3-profit-plunges-74-as-weaker-crypto-trading-weighs-on-earnings-437192
- [Cointelegraph] Poland’s lower house backs sanctions bill covering crypto freezes (11-10 22:40) — https://cointelegraph.com/news/poland-bill-freeze-sanctions-crypto-assets?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] U.S. CPI rose stronger than expected 0.4% in October; core rate rose 0.3% (11-10 22:32) — https://www.coindesk.com/markets/2026/11/10/u-s-cpi-rose-stronger-than-expected-0-4-in-october-core-rate-rose-0-3
- [Cointelegraph] Bitcoin’s ‘best buying opportunity ever’ has arrived: Mark Moss (11-10 22:30) — https://cointelegraph.com/magazine/bitcoins-best-buying-opportunity-ever-has-arrived-mark-moss?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin may benefit as global tightening slows, Binance Research says (11-10 22:15) — https://cointelegraph.com/markets/bitcoin-price-global-tightening-binance-research?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Ripple Prime head Marc Asch to step down, Noel Kimmel named successor (11-10 21:38) — https://www.coindesk.com/business/2026/11/09/ripple-prime-head-marc-asch-to-step-down-noel-kimmel-named-successor
- [CoinDesk] Bitcoin breaks with stocks, declines as ETF outflows mount, MARA reduces holdings (11-10 21:15) — https://www.coindesk.com/daybook-us/2026/11/10/bitcoin-breaks-with-stocks-declines-as-etf-outflows-mount-mara-sells-holdings
- [The Block] HIVE reports $79 million quarterly net loss as bitcoin mining revenue falls and AI business grows (11-10 20:52) — https://www.theblock.co/news/business/2026-11-10-hive-reports-79-million-quarterly-net-loss-as-bitcoin-mining-revenue-falls-and-ai-business-grows-437177
- [Cointelegraph] Coinbase, Kalshi join lawsuit backing CFTC over US stock perp futures (11-10 20:44) — https://cointelegraph.com/news/coinbase-kalshi-cftc-stock-perpetual-futures-lawsuit?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Binance warns iOS flaw could expose crypto wallet keys (11-10 20:25) — https://cointelegraph.com/news/binance-warns-ios-flaw-could-expose-crypto-wallet-keys?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin lags stock rebound in advance of U.S. inflation report (11-10 20:24) — https://www.coindesk.com/markets/2026/11/10/bitcoin-lags-stock-rebound-in-advance-of-u-s-inflation-report
- [Cointelegraph] Ex-employee sues Ethereum Foundation and Vitalik Buterin over firing (11-10 19:56) — https://cointelegraph.com/news/ex-employee-sues-ethereum-foundation-vitalik-buterin-over-firing?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Exodus shares rise 10% ahead of Q3 earnings showing 7% revenue growth, $8.3 million loss (11-10 19:53) — https://www.theblock.co/news/business/2026-11-10-exodus-shares-rise-10-ahead-of-q3-earnings-showing-7-revenue-growth-8-3-million-loss-437012
- [CoinDesk] Bitcoin slips before U.S. inflation report as traders price in Fed rate increase (11-10 19:48) — https://www.coindesk.com/markets/2026/11/10/bitcoin-slips-before-u-s-inflation-report-as-traders-price-in-fed-rate-increase
- [CoinDesk] Live news: Bitcoin falls to nearly three-month low after disappointing inflation data (11-10 19:41) — https://www.coindesk.com/markets/2026/11/10/live-news-traders-price-in-fed-rate-hike-for-december-as-bitcoin-and-gold-retreat
- [The Block] Ark Invest trims Block, Bullish and its own bitcoin ETF holdings while buying Nvidia, SoFi (11-10 19:36) — https://www.theblock.co/news/business/2026-11-10-ark-invest-trims-block-bullish-holdings-437003
- [The Block] NEAR AI says SGLang vulnerability exposed user account details in security breach (11-10 19:17) — https://www.theblock.co/news/defi/2026-11-10-near-ai-security-breach-437002

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