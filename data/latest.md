# 코인 데일리 스냅샷

- 수집 시각: 2026-11-22 16:18 KST
- 결과: 성공 32 / 실패·검증필요 4 / 수동 1 (전체 37)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 5.0 / 3일 평균 7.0 / 오늘 구간 '중립'
- 판정 가능 지표 12/17개 (71%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | -75.0 |
| 파생·심리 | 30% | 75.0 |
| 밸류에이션 | 25% | 50.0 |
| 매크로 | 15% | -50.0 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.38 |
| 밸류에이션 | 가격÷STH-RP | +1 | +1 | 가격÷STH-RP 0.875 |
| 수급 | 현물 ETF 순유입 | -2 | -2 | 3거래일 연속 순유출 |
| 수급 | 거래소 순유입(7일) | 제외 | +1 | 값 없음 |
| 수급 | 거래소 보유량(30일) | 제외 | -1 | 값 없음 |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | -1 | -1 | 7일 +6.9% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +2 | +2 | 3회 평균 -0.0028% |
| 파생·심리 | RSI(14) | +2 | +2 | RSI 22.6 |
| 파생·심리 | 롱/숏 비율 | +1 | +0 | 롱/숏 분포 20백분위 |
| 파생·심리 | 미결제약정(OI) | +1 | +1 | OI 7일 -12.9%, 가격 -6.3% (레버리지 정리) |
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
| A.매크로 | 나스닥 5거래일 변화율 | -10.02 | -10.02 | % | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26113.44 | 26113.44 | pt | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 103.81 | 103.9 | pt | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.96 | 1.96 | % | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 159.707 | 159.381 | 엔 | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | -0.11 | -0.11 | % | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.08 | 4.02 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.87 | 2.79 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.65 | 3.44 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.12 | 3.03 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -4 | -4 |  | 2026-11-22 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 8.478 | 8.608 | % | 2026-11-22 07:14 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.052 | 2.0165 | 조$ | 2026-11-22 07:14 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | -582.2 | -306.4 | 백만$ | 2026-11-19 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 3거래일 연속 순유출 / 집계 기준일 2026-11-19 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -541.1 | -148.7 | 백만$ | 2026-11-19 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -1306.0 | -1306.0 | 백만$ | 2026-11-19 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | -3 | -3 | 일 | 2026-11-19 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 60086.0 | 58814.99 | USD | 2026-11-21 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 22.58 | 17.44 |  | 2026-11-21 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -6.29 | -13.81 | % | 2026-11-21 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 2.82 | 2.92 | 십억$ | 2026-11-21 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -12.92 | -15.48 | % | 2026-11-21 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 2.12 | 2.15 | 배 | 2026-11-21 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 20.0 | 50.0 | 백분위 | 2026-11-21 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | -0.0038 | 0.0001 | % | 2026-11-22 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | -0.0028 | -0.0019 | % | 2026-11-22 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 58.36 | 54.52 |  | 2026-11-22 07:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐 |  | 9.05 |  |  | fail | [Deribit](https://www.deribit.com/options/BTC) | 429 Client Error: Too Many Requests for url: https://www.deribit.com/api/v2/public/ticker?instrument_name=BTC-25DEC26-54000-C |
| D.온체인 | MVRV Z-Score | 0.3784 | 0.338 |  | 2026-11-15 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 0.8747 | 0.856 |  | 2026-11-15 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 68735.0 | 68751.0 | $ | 2026-11-15 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 60123.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 |  | 41305.5 |  |  | fail | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 'NoneType' object is not iterable |
| D.온체인 | 거래소 BTC 유출 | 49689.5 | 41820.9 | BTC | 2026-11-21 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 분포 |  | 28.9 |  |  | fail | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 'NoneType' object is not iterable |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (11-21 18:00 ~ 11-22 16:18 KST)

피드 상태: CoinDesk: 3건 / The Block: 3건 / Cointelegraph: 3건 / 블록미디어: 10건

- [Cointelegraph] Chainflip confirms $12M hack, offers attacker 10% bounty (11-22 14:28) — https://cointelegraph.com/news/chainflip-12m-crypto-hack-10-percent-bounty?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 비트코인 6만달러 붕괴…하루 11억달러 강제 청산 (11-22 12:54) — https://www.blockmedia.co.kr/archives/1169095?utm_source=general&utm_medium=rss
- [블록미디어] 중앙은행들 “금고에 둬야 내 자산”…비트코인은 아직 ‘관망’ (11-22 12:11) — https://www.blockmedia.co.kr/archives/1169093?utm_source=general&utm_medium=rss
- [블록미디어] 월가 강세론자 야데니 “S&P500 약세장 아닌 조정”…변수는 연준 (11-22 11:20) — https://www.blockmedia.co.kr/archives/1169091?utm_source=general&utm_medium=rss
- [블록미디어] 크라켄, 캐나다달러 시장서 비트코인 ‘헐값’ 체결…”거래 유지”(종합) (11-22 10:35) — https://www.blockmedia.co.kr/archives/1169088?utm_source=general&utm_medium=rss
- [블록미디어] 아크 “디지털자산 ETF 2종 철회…SEC에 의사 전달” (11-22 09:49) — https://www.blockmedia.co.kr/archives/1169082?utm_source=general&utm_medium=rss
- [블록미디어] 고점 대비 95% 빠진 아발란체…NYSE 호재에도 회복 ‘불투명’ (11-22 09:02) — https://www.blockmedia.co.kr/archives/1169072?utm_source=general&utm_medium=rss
- [블록미디어] IOSCO “양자내성 전환, 블록체인 속도 최대 90% 저하” (11-22 08:39) — https://www.blockmedia.co.kr/archives/1169071?utm_source=general&utm_medium=rss
- [블록미디어] 싱가포르, AI 에이전트에 기업 자금관리 맡긴다(종합) (11-22 08:15) — https://www.blockmedia.co.kr/archives/1169069?utm_source=general&utm_medium=rss
- [블록미디어] 비트코인 2년 만에 최저인데…AI 알트코인 3종 올랐다 (11-22 07:36) — https://www.blockmedia.co.kr/archives/1169067?utm_source=general&utm_medium=rss
- [블록미디어] 캘리포니아주, 엔비디아 중국 반도체 밀반출 조사 ‘형사처벌’로 확대-블룸버그 (11-22 06:50) — https://www.blockmedia.co.kr/archives/1169063?utm_source=general&utm_medium=rss
- [The Block] Kalshi faces Monday hearing on New York order it says would shut down its exchange nationwide (11-22 06:17) — https://www.theblock.co/news/regulation/2026-11-21-kalshi-faces-monday-hearing-on-new-york-order-it-says-would-shut-down-its-exchange-nationwide-444813
- [The Block] Cyber investigating suspected $1 million bridge exploit as Upbit, Bithumb freeze transfers (11-22 03:51) — https://www.theblock.co/news/defi/2026-11-21-cyber-investigating-suspected-1-million-bridge-exploit-as-upbit-bithumb-freeze-transfers-444810
- [CoinDesk] Bitcoin rebounds above $60,000 after $1.8 billion crypto liquidation wave (11-22 02:50) — https://www.coindesk.com/markets/2026/11/21/bitcoin-bounces-9-from-two-year-low-to-retake-usd60-000-as-traders-eye-monday-s-stock-open
- [CoinDesk] Cross-chain protocol Chainflip's FLIP tanks 30% after suspected $4.86 million vault drain (11-22 01:41) — https://www.coindesk.com/business/2026/11/21/cross-chain-protocol-chainflip-s-flip-tanks-30-after-suspected-usd4-86-million-vault-drain
- [The Block] Chainflip’s FLIP drops 34% after attacker drains $4.86 million from vault with suspected key compromise (11-22 00:24) — https://www.theblock.co/news/defi/2026-11-21-chainflips-flip-drops-34-after-attacker-drains-4-86-million-from-vault-with-suspected-key-compromise-444804
- [CoinDesk] Ether treasury firm BTCS warns SEC its $54 million Aave loan could be liquidated (11-21 21:30) — https://www.coindesk.com/markets/2026/11/21/ether-treasury-firm-btcs-warns-sec-its-usd54-million-aave-loan-could-be-liquidated
- [Cointelegraph] Here’s what happened in crypto today (11-21 20:18) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] ECB seeks industry partners for tokenized deposits, securities experiments (11-21 18:48) — https://cointelegraph.com/news/ecb-tokenized-deposits-securities-experiments-appia?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

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
- 거래소 BTC 유입 (Coin Metrics 커뮤니티): 'NoneType' object is not iterable
- 거래소 순유입 7일 분포 (Coin Metrics 커뮤니티): 'NoneType' object is not iterable
- 고래비율(근사) (Arkham + Coin Metrics): Arkham 키 없음