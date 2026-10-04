# 코인 데일리 스냅샷

- 수집 시각: 2026-10-04 12:55 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 0.1 / 3일 평균 1.1 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | 37.5 |
| 파생·심리 | 30% | -10.0 |
| 밸류에이션 | 25% | -25.0 |
| 매크로 | 15% | -12.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +0 | +0 | MVRV Z 1.03 |
| 밸류에이션 | 가격÷STH-RP | -1 | -1 | 가격÷STH-RP 1.160 |
| 수급 | 현물 ETF 순유입 | +1 | +1 | 5일 합 +186백만$ |
| 수급 | 거래소 순유입(7일) | +1 | +1 | 7일 순유입 분포 27백분위 |
| 수급 | 거래소 보유량(30일) | +1 | +1 | 30일 -1.14% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | +0 | +0 | 7일 +0.0% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0031% |
| 파생·심리 | RSI(14) | -1 | -1 | RSI 63.6 |
| 파생·심리 | 롱/숏 비율 | +0 | +0 | 롱/숏 분포 67백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +0 | OI 7일 -100.0%, 가격 +0.4% |
| 파생·심리 | 옵션 스큐 | -1 | +0 | +1.02 (풋 우위 확대, 전일 +0.85) |
| 매크로 | 나스닥 | +1 | +1 | 50일선 위 |
| 매크로 | DXY | -1 | -1 | 101.93, 20일 +3.0% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 157.83 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -2 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 27190.859 | 26871.6 | pt | 2026-10-02 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | 0.45 | 0.45 | % | 2026-10-02 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26306.47 | 26306.47 | pt | 2026-10-02 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 101.93 | 102.1 | pt | 2026-10-02 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 2.96 | 2.95 | % | 2026-10-02 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 157.83 | 157.927 | 엔 | 2026-10-03 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | 0.23 | -0.62 | % | 2026-10-03 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 3.71 | 3.54 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-09-11 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.76 | 2.79 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-09-11 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.42 | 3.36 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.01 | 2.98 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -2 | -2 |  | 2026-10-04 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.324 | 6.356 | % | 2026-10-04 03:47 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.9043 | 2.8897 | 조$ | 2026-10-04 03:47 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | 102.7 | -148.7 | 백만$ | 2026-10-01 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 1거래일 연속 순유입 / 집계 기준일 2026-10-01 |
| B.자금흐름 | IBIT(블랙록) 순유입 | 195.6 | -9.5 | 백만$ | 2026-10-01 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | 185.7 | 185.7 | 백만$ | 2026-10-01 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | 1 | 1 | 일 | 2026-10-01 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 84742.22 | 84504.88 | USD | 2026-10-03 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 63.62 | 62.89 |  | 2026-10-03 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | 0.39 | 0.49 | % | 2026-10-03 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 0.0 | 0.0 | 십억$ | 2026-10-03 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -100.0 | -0.55 | % | 2026-10-03 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 1.33 | 1.26 | 배 | 2026-10-03 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 66.7 | 66.7 | 백분위 | 2026-10-03 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.0028 | 0.0034 | % | 2026-10-04 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0031 | 0.0039 | % | 2026-10-04 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 35.44 | 34.79 |  | 2026-10-04 03:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 1.02 | 0.85 | vol pt | 2026-10-04 03:56 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-10-30, 콜 BTC-30OCT26-91000-C / 풋 BTC-30OCT26-80000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 1.0281 | 1.0198 |  | 2026-09-27 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.16 | 1.15 |  | 2026-09-27 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 73070.0 | 73470.0 | $ | 2026-09-27 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 84762.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 11665.4 | 29853.0 | BTC | 2026-10-03 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 16606.0 | 33160.6 | BTC | 2026-10-03 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -20901.7 | -25758.4 | BTC | 2026-10-03 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 26.7 | 18.9 | 백분위 | 2026-10-03 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -4940.5 | -4355.7 | BTC | 2026-10-03 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -1.14 | -1.02 | % | 2026-10-03 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2673624.0 | 2678292.0 | BTC | 2026-10-03 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (10-03 18:00 ~ 10-04 12:55 KST)

피드 상태: CoinDesk: 5건 / The Block: 0건 / Cointelegraph: 3건 / 블록미디어: 10건

- [블록미디어] 미 백악관 ‘슈퍼 인텔리전스 포스’ 구성…AI 위험 120일간 점검 (10-04 12:32) — https://www.blockmedia.co.kr/archives/1147553?utm_source=general&utm_medium=rss
- [블록미디어] 리플 지원 ‘XRP 아시아’ 출범…아시아 XRPL 생태계 확장(종합) (10-04 12:10) — https://www.blockmedia.co.kr/archives/1147551?utm_source=general&utm_medium=rss
- [블록미디어] 미 연준 9월 회의록, 금리 인상 놓고 내부 이견 드러낼 듯 (10-04 11:33) — https://www.blockmedia.co.kr/archives/1147529?utm_source=general&utm_medium=rss
- [블록미디어] AI 연산능력도 선물로 거래한다…비트코인 채굴업체 새 수익원 부상 (10-04 11:13) — https://www.blockmedia.co.kr/archives/1147536?utm_source=general&utm_medium=rss
- [블록미디어] 이더리움 언스테이킹 봇물, 매물화 우려…출금 대기 77만 ETH 육박 (10-04 09:51) — https://www.blockmedia.co.kr/archives/1147510?utm_source=general&utm_medium=rss
- [블록미디어] 캐시 우드 “AI가 고성장·저물가 시대 연다…비트코인도 반등” (10-04 09:35) — https://www.blockmedia.co.kr/archives/1147517?utm_source=general&utm_medium=rss
- [블록미디어] 비트코인, 9만6000달러 재도전하나…기술적 지표 점검 (10-04 09:33) — https://www.blockmedia.co.kr/archives/1147512?utm_source=general&utm_medium=rss
- [블록미디어] 엑스알피, 2달러 돌파 가능한가?…기술적 지표 점검 (10-04 09:19) — https://www.blockmedia.co.kr/archives/1147511?utm_source=general&utm_medium=rss
- [블록미디어] 美 고용지표보다 빨랐던 비트코인, 정작 발표 뒤에는 하락 (10-04 09:01) — https://www.blockmedia.co.kr/archives/1147518?utm_source=general&utm_medium=rss
- [블록미디어] 베선트 “미 국채금리 상승 우려할 수준 아니다”…AI 버블론도 일축(종합) (10-04 08:45) — https://www.blockmedia.co.kr/archives/1147514?utm_source=general&utm_medium=rss
- [CoinDesk] Payments firm OpenPayd targets year-end Nasdaq listing to fund U.S. expansion and acquisitions (10-04 01:00) — https://www.coindesk.com/business/2026/10/03/openpayd-targets-year-end-nasdaq-listing-to-fund-u-s-expansion-and-acquisitions
- [CoinDesk] Crypto job postings triple to over 1,200 in September, but applications fall (10-04 01:00) — https://www.coindesk.com/business/2026/10/03/crypto-job-postings-triple-to-over-1-200-in-september-but-applications-fall
- [CoinDesk] Cathie Wood says smart investors need to start watching where AI agents spend money (10-04 00:00) — https://www.coindesk.com/markets/2026/10/01/cathie-wood-says-smart-investors-need-to-start-watching-where-ai-agents-spend-money
- [CoinDesk] Crypto's Sisyphean struggle (10-03 22:00) — https://www.coindesk.com/opinion/2026/10/03/crypto-s-sisyphean-struggle
- [CoinDesk] BlackRock offers a glimpse of how tokenization may change your investment portfolio (10-03 22:00) — https://www.coindesk.com/business/2026/10/03/blackrock-offers-a-glimpse-of-how-tokenization-may-change-your-investment-portfolio
- [Cointelegraph] Here’s what happened in crypto today (10-03 21:20) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] NEAR Intents recovers entire stolen $3.8M after ultimatum to exploiter (10-03 20:59) — https://cointelegraph.com/news/near-intents-recovers-entire-stolen-38m-after-ultimatum-to-exploiter?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Community banks sue OCC over trust bank charters of crypto firms (10-03 18:25) — https://cointelegraph.com/news/community-banks-sue-occ-over-trust-bank-charters-of-crypto-firms?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

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