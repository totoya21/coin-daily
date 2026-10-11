# 코인 데일리 스냅샷

- 수집 시각: 2026-10-11 09:53 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 -14.9 / 3일 평균 -7.2 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | -12.5 |
| 파생·심리 | 30% | -10.0 |
| 밸류에이션 | 25% | -25.0 |
| 매크로 | 15% | -12.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +0 | +0 | MVRV Z 1.09 |
| 밸류에이션 | 가격÷STH-RP | -1 | +0 | 가격÷STH-RP 1.172 |
| 수급 | 현물 ETF 순유입 | -1 | -1 | 5일 합 -681백만$ |
| 수급 | 거래소 순유입(7일) | +0 | +1 | 7일 순유입 분포 38백분위 |
| 수급 | 거래소 보유량(30일) | +1 | +1 | 30일 -1.23% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | -1 | -1 | 7일 +3.3% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0011% |
| 파생·심리 | RSI(14) | +0 | +0 | RSI 51.5 |
| 파생·심리 | 롱/숏 비율 | -1 | -1 | 롱/숏 분포 73백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +0 | OI 7일 +4.5%, 가격 -2.2% |
| 파생·심리 | 옵션 스큐 | -1 | +0 | +2.92 (풋 우위 확대, 전일 +1.39) |
| 매크로 | 나스닥 | +1 | +1 | 50일선 위 |
| 매크로 | DXY | -1 | -1 | 102.21, 20일 +3.1% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 158.25 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -2 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 27366.17 | 27193.34 | pt | 2026-10-09 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | 0.64 | 0.64 | % | 2026-10-09 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26562.98 | 26562.98 | pt | 2026-10-09 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 102.21 | 102.14 | pt | 2026-10-09 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 3.12 | 3.14 | % | 2026-10-09 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 158.246 | 158.06 | 엔 | 2026-10-09 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | 0.2 | 0.2 | % | 2026-10-09 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 3.71 | 3.54 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-09-11 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.76 | 2.79 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-09-11 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.42 | 3.36 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.01 | 2.98 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -2 | -2 |  | 2026-10-11 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.532 | 6.566 | % | 2026-10-11 00:47 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.8118 | 2.7998 | 조$ | 2026-10-11 00:47 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | 21.1 | -244.1 | 백만$ | 2026-10-09 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 1거래일 연속 순유입 / 집계 기준일 2026-10-09 |
| B.자금흐름 | IBIT(블랙록) 순유입 | 22.4 | -5.5 | 백만$ | 2026-10-09 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -681.1 | -512.4 | 백만$ | 2026-10-09 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | 1 | -2 | 일 | 2026-10-09 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 82910.8 | 82544.71 | USD | 2026-10-10 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 51.52 | 50.16 |  | 2026-10-10 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -2.16 | -2.32 | % | 2026-10-10 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.3 | 3.29 | 십억$ | 2026-10-10 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | 4.47 | 1.01 | % | 2026-10-10 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 1.48 | 1.5 | 배 | 2026-10-10 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 73.3 | 73.3 | 백분위 | 2026-10-10 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | -0.0022 | 0.0011 | % | 2026-10-11 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0011 | 0.0017 | % | 2026-10-11 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 36.97 | 36.52 |  | 2026-10-11 00:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 2.92 | 1.39 | vol pt | 2026-10-11 00:54 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-10-30, 콜 BTC-30OCT26-88000-C / 풋 BTC-30OCT26-79000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 1.0926 | 1.0339 |  | 2026-10-04 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.1716 | 1.1469 |  | 2026-10-04 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 70891.0 | 72094.0 | $ | 2026-10-04 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 83055.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 27171.1 | 28184.9 | BTC | 2026-10-09 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 22909.8 | 27937.6 | BTC | 2026-10-09 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -16982.5 | -24551.4 | BTC | 2026-10-09 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 37.8 | 22.2 | 백분위 | 2026-10-09 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | 4261.3 | 247.3 | BTC | 2026-10-09 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -1.23 | -1.44 | % | 2026-10-09 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2672866.0 | 2665392.0 | BTC | 2026-10-09 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (10-10 18:00 ~ 10-11 09:53 KST)

피드 상태: CoinDesk: 3건 / The Block: 2건 / Cointelegraph: 2건 / 블록미디어: 10건

- [블록미디어] 비트코인, 연말연초 횡보장과 닮았다…8만500달러 손익 분기점 공방 (10-11 09:51) — https://www.blockmedia.co.kr/archives/1150065?utm_source=general&utm_medium=rss
- [블록미디어] XRP, 핵심 추세선 시험대…1.45달러 돌파가 분수령–기술적 분석 (10-11 09:33) — https://www.blockmedia.co.kr/archives/1150064?utm_source=general&utm_medium=rss
- [블록미디어] 비트와이즈 CIO “비트코인, 금처럼 시총 30조달러 가능” (10-11 09:21) — https://www.blockmedia.co.kr/archives/1150069?utm_source=general&utm_medium=rss
- [블록미디어] 레저 지갑서 무단 삽입 부품 확인…크립토빌리스 유출 사태 확산 (10-11 08:23) — https://www.blockmedia.co.kr/archives/1150062?utm_source=general&utm_medium=rss
- [블록미디어] 월가, 이더리움서 자금 회수…공매도 규모 50억달러 (10-11 07:47) — https://www.blockmedia.co.kr/archives/1150058?utm_source=general&utm_medium=rss
- [블록미디어] 월가 5대 은행 시총 2700억달러 증발… 금리 급등에 실적 시험대 (10-11 06:59) — https://www.blockmedia.co.kr/archives/1150056?utm_source=general&utm_medium=rss
- [블록미디어] AI가 키운 글로벌 사기 산업… 연간 피해액 4420억달러 (10-11 06:48) — https://www.blockmedia.co.kr/archives/1150054?utm_source=general&utm_medium=rss
- [블록미디어] [뉴욕 코인시황] 190억달러 청산 사태 1년…비트코인, 8.3만달러선 기싸움 (10-11 06:29) — https://www.blockmedia.co.kr/archives/1150051?utm_source=general&utm_medium=rss
- [블록미디어] 러시아산 경유 제재 완화 충돌… 트럼프 “젤렌스키 교체돼야” (10-11 05:49) — https://www.blockmedia.co.kr/archives/1150049?utm_source=general&utm_medium=rss
- [블록미디어] 스테이블코인도 과세… 프랑스, 코인 양도세 확대 추진 (10-11 05:26) — https://www.blockmedia.co.kr/archives/1150046?utm_source=general&utm_medium=rss
- [The Block] Kalshi is investigating bets on Trump’s press secretary pick placed before announcement: WSJ (10-11 03:35) — https://www.theblock.co/news/regulation/2026-10-10-kalshi-is-investigating-bets-on-trumps-press-secretary-pick-placed-before-announcement-wsj-418222
- [The Block] Ether ETFs extend outflow streak to nine days as Solana funds snap record 14-week inflow run (10-11 00:10) — https://www.theblock.co/news/markets/2026-10-10-ether-etfs-extend-outflow-streak-to-nine-days-as-solana-funds-snap-record-14-week-inflow-run-418215
- [Cointelegraph] Here’s what happened in crypto today (10-10 21:30) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] One year after 10/10 flash crash, bitcoin and ether liquidity have rebuilt, but altcoins still face risks (10-10 21:00) — https://www.coindesk.com/markets/2026/10/10/one-year-after-10-10-bitcoin-and-ether-liquidity-have-rebuilt-but-other-altcoins-still-face-risks
- [CoinDesk] Tokenized commodities look beyond gold as lending and oil open new markets (10-10 21:00) — https://www.coindesk.com/business/2026/10/05/tokenized-commodities-look-beyond-gold-as-lending-and-oil-open-new-markets
- [Cointelegraph] Justin Sun says Tron’s post-quantum cryptography has gone live on testnet (10-10 20:52) — https://cointelegraph.com/news/justin-sun-says-trons-post-quantum-cryptography-has-gone-live-on-testnet?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin's $19 billion wake-up call: One-year after flash crash, has crypto learned anything? (10-10 20:00) — https://www.coindesk.com/markets/2026/10/10/bitcoin-s-usd19-billion-wake-up-call-one-year-later-has-crypto-learned-anything

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