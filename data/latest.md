# 코인 데일리 스냅샷

- 수집 시각: 2026-10-23 10:15 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 5.9 / 3일 평균 7.8 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | 37.5 |
| 파생·심리 | 30% | -20.0 |
| 밸류에이션 | 25% | 25.0 |
| 매크로 | 15% | -37.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.92 |
| 밸류에이션 | 가격÷STH-RP | +0 | +0 | 가격÷STH-RP 1.093 |
| 수급 | 현물 ETF 순유입 | +2 | +1 | 3거래일 연속 순유입 |
| 수급 | 거래소 순유입(7일) | +0 | -1 | 7일 순유입 분포 69백분위 |
| 수급 | 거래소 보유량(30일) | +1 | +1 | 30일 -1.63% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | +0 | +0 | 7일 +0.9% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0082% |
| 파생·심리 | RSI(14) | +0 | +0 | RSI 46.0 |
| 파생·심리 | 롱/숏 비율 | -2 | +1 | 롱/숏 분포 100백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +0 | OI 7일 +0.2%, 가격 -1.0% |
| 파생·심리 | 옵션 스큐 | -1 | +0 | +3.84 (풋 우위 확대, 전일 +2.88) |
| 매크로 | 나스닥 | -1 | +1 | 50일선 아래 |
| 매크로 | DXY | -1 | -1 | 101.54, 20일 +0.2% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 156.29 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -2 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 26008.859 | 26702.859 | pt | 2026-10-22 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -2.64 | 0.04 | % | 2026-10-22 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26615.96 | 26627.56 | pt | 2026-10-22 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 101.539 | 101.78 | pt | 2026-10-22 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 0.25 | 0.59 | % | 2026-10-22 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 156.29 | 158.132 | 엔 | 2026-10-23 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | -1.17 | 0.12 | % | 2026-10-23 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.02 | 3.71 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-10-14 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.79 | 2.76 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-10-14 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.42 | 3.36 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.01 | 2.98 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -2 | -2 |  | 2026-10-23 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.642 | 6.447 | % | 2026-10-23 01:13 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.742 | 2.8296 | 조$ | 2026-10-23 01:13 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | 528.4 | 23.2 | 백만$ | 2026-10-21 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 3거래일 연속 순유입 / 집계 기준일 2026-10-21 |
| B.자금흐름 | IBIT(블랙록) 순유입 | 235.0 | 29.9 | 백만$ | 2026-10-21 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | 1000.8 | 211.0 | 백만$ | 2026-10-21 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | 3 | 2 | 일 | 2026-10-21 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 81307.16 | 84024.67 | USD | 2026-10-22 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 46.03 | 56.71 |  | 2026-10-22 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -1.0 | 3.01 | % | 2026-10-22 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.37 | 3.53 | 십억$ | 2026-10-22 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | 0.16 | 6.44 | % | 2026-10-22 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 2.18 | 2.08 | 배 | 2026-10-22 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 100.0 | 16.7 | 백분위 | 2026-10-22 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.0067 | 0.0078 | % | 2026-10-23 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0082 | 0.002 | % | 2026-10-23 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 38.36 | 37.5 |  | 2026-10-23 01:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 3.84 | 2.88 | vol pt | 2026-10-23 01:16 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-11-27, 콜 BTC-27NOV26-88000-C / 풋 BTC-27NOV26-76000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.9227 | 0.9432 |  | 2026-10-16 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.0933 | 1.102 |  | 2026-10-16 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 74415.0 | 76581.0 | $ | 2026-10-16 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 81358.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 21794.4 | 22038.2 | BTC | 2026-10-21 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 28909.5 | 21756.0 | BTC | 2026-10-21 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -5211.1 | 1173.4 | BTC | 2026-10-21 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 68.9 | 84.4 | 백분위 | 2026-10-21 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -7115.1 | 282.2 | BTC | 2026-10-21 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -1.63 | -1.46 | % | 2026-10-21 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2675115.0 | 2681408.0 | BTC | 2026-10-21 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (10-22 18:00 ~ 10-23 10:15 KST)

피드 상태: CoinDesk: 11건 / The Block: 11건 / Cointelegraph: 21건 / 블록미디어: 10건

- [블록미디어] XRP 4% 하락…고래 투자자 거래소 입금 7개월 만에 최대 (10-23 10:07) — https://www.blockmedia.co.kr/archives/1155256?utm_source=general&utm_medium=rss
- [Cointelegraph] Switzerland approves first spot Bitcoin ETF for retail investors (10-23 09:59) — https://cointelegraph.com/news/switzerland-approves-first-spot-bitcoin-etf-for-retail-investors?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 테더, 볼리비아 핀테크 ‘페소’에 투자…남미 USDT 결제 시장 공략 본격화 (10-23 09:43) — https://www.blockmedia.co.kr/archives/1155270?utm_source=general&utm_medium=rss
- [블록미디어] [개장시황] 코스피, 美 AI주 급락 여파에 3%대 하락…5300선 위협 (10-23 09:16) — https://www.blockmedia.co.kr/archives/1155257?utm_source=general&utm_medium=rss
- [블록미디어] 일본, 외국인 관광객 세금 환급에 스테이블코인 도입 검토 (10-23 08:51) — https://www.blockmedia.co.kr/archives/1155222?utm_source=general&utm_medium=rss
- [Cointelegraph] Pentagon bans US forces from using military info to bet in prediction markets (10-23 08:50) — https://cointelegraph.com/news/pentagon-bans-us-forces-from-using-military-info-to-bet-in-prediction-markets?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] [메타에 발목 잡힌 업토버 ④] 기술주 충격, 비트코인에도 매도 압력 (10-23 08:24) — https://www.blockmedia.co.kr/archives/1155243?utm_source=general&utm_medium=rss
- [블록미디어] [코인시황] 비트코인 8만1000달러대로 하락…美 기술주 매도·중동 긴장 겹쳐 (10-23 08:22) — https://www.blockmedia.co.kr/archives/1155234?utm_source=general&utm_medium=rss
- [블록미디어] [메타에 발목 잡힌 업토버 ③] 부유세 납부와 경영권…저커버그를 위한 신주 발행 논란 (10-23 08:20) — https://www.blockmedia.co.kr/archives/1155233?utm_source=general&utm_medium=rss
- [블록미디어] [메타에 발목 잡힌 업토버 ②] 메타 CDS 사상 최고…채권시장으로 번진 위험신호 (10-23 08:12) — https://www.blockmedia.co.kr/archives/1155230?utm_source=general&utm_medium=rss
- [블록미디어] [메타에 발목 잡힌 업토버 ①] 과도한 AI 투자 우려 재부상… 저커버그 부유세 논란도 가세 (10-23 08:07) — https://www.blockmedia.co.kr/archives/1155227?utm_source=general&utm_medium=rss
- [블록미디어] “코인의 실적은 현금흐름”…그레이스케일, 디지털자산 가치평가 기준 제시 (10-23 08:05) — https://www.blockmedia.co.kr/archives/1155182?utm_source=general&utm_medium=rss
- [Cointelegraph] New DeepSeek ban in US, Swiss-Asia crypto ties deepen: Asia Express (10-23 07:50) — https://cointelegraph.com/magazine/new-deepseek-ban-in-us-swiss-asia-crypto-ties-deepen-asia-express?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Senate's top Democratic investigator looking into Tether payments to Bo Hines' firm (10-23 07:43) — https://www.coindesk.com/policy/2026/10/22/senate-s-top-democratic-investigator-looking-into-tether-payments-to-bo-hines-firm
- [Cointelegraph] Circle shareholder sues Trump, World Liberty and Steve Witkoff over crypto deals (10-23 06:39) — https://cointelegraph.com/news/circle-shareholder-lawsuit-donald-trump-world-liberty-financial-steve-witkoff-crypto-corruption?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Dune launches real-time data feeds covering 200 onchain trading venues (10-23 05:36) — https://cointelegraph.com/news/dune-launches-real-time-data-feeds-covering-200-onchain-trading-venues?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Here’s what happened in crypto today (10-23 05:09) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Winklevoss PAC moves into Texas Senate race with $81K ad buy (10-23 04:29) — https://cointelegraph.com/news/winklevoss-pac-texas-senate-race-media-paxton-talarico?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] JPMorgan says crypto regulatory moves partly offset Clarity Act failure, but risks remain (10-23 04:14) — https://www.theblock.co/news/regulation/2026-10-22-jpmorgan-crypto-regulatory-moves-clarity-act-failure-risks-423473
- [The Block] Blockchain Association pushes for crypto tax clarity as broader bill stalls (10-23 03:59) — https://www.theblock.co/news/regulation/2026-10-22-blockchain-association-pushes-crypto-tax-clarity-broader-bill-stalls-423475
- [CoinDesk] A16z is the latest VC giant to widen bets beyond crypto and into AI and emerging tech (10-23 03:30) — https://www.coindesk.com/business/2026/10/22/a16z-is-the-latest-vc-giant-to-widen-bets-beyond-crypto-and-into-ai-and-emerging-tech
- [Cointelegraph] Underdog taps zerohash to bring crypto deposits to prediction markets (10-23 02:24) — https://cointelegraph.com/news/underdog-taps-zerohash-to-bring-crypto-deposits-to-prediction-markets?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin hashrate hits seven-month high as AI shift fails to ease mining competition (10-23 01:50) — https://cointelegraph.com/news/bitcoin-mining-difficulty-hashrate-recovery-ai-shift?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Irish cenbank fines Coinbase arm $3.6M for oversight, safeguard failures (10-23 01:48) — https://cointelegraph.com/news/ireland-central-bank-coinbase-oversight-safeguard-failure?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin circles $81.5K ETF cost basis as Trump Iran comments send stocks lower (10-23 01:20) — https://cointelegraph.com/markets/bitcoin-circles-815k-etf-cost-basis-as-trump-iran-comments-send-stocks-lower?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Irish central bank fines Coinbase Ireland $3.6 million over fund safeguarding failures (10-23 00:40) — https://www.coindesk.com/policy/2026/10/22/irish-central-bank-fines-coinbase-ireland-usd3-6-million-over-fund-safeguarding-failures
- [CoinDesk] Crypto for Advisors: Stablecoins are ready for prime time (10-22 23:58) — https://www.coindesk.com/coindesk-indices/2026/10/22/crypto-for-advisors-stablecoins-are-ready-for-prime-time
- [Cointelegraph] Fireblocks disputes report of $2.5B Visa acquisition talks (10-22 23:41) — https://cointelegraph.com/news/fireblocks-disputes-report-of-25b-visa-acquisition-talks?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Crypto custody specialist Fireblocks denies it's in talks to be acquired by Visa (10-22 23:37) — https://www.coindesk.com/business/2026/10/22/crypto-custody-specialist-fireblocks-denies-its-in-talks-to-be-acquired-by-visa
- [The Block] Coinbase Ireland fined $3.6 million over customer fund segregation, oversight failures (10-22 23:03) — https://www.theblock.co/news/regulation/2026-10-22-coinbase-ireland-fined-3-6-million-over-customer-fund-segregation-oversight-failures-421943
- [The Block] Uniswap’s aggregator hooks go live on Ethereum, Base and Robinhood Chain (10-22 22:55) — https://www.theblock.co/news/defi/2026-10-22-uniswaps-aggregator-hooks-go-live-ethereum-base-robinhood-chain-421932
- [Cointelegraph] CryptoQuant CEO calls rising Bitcoin hashrate ‘indirect bullish signal’ from institutions (10-22 22:42) — https://cointelegraph.com/markets/cryptoquant-rising-bitcoin-hashrate-indirect-bullish-signal?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Fireblocks denies report of $2.5 billion acquisition talks with Visa (10-22 22:27) — https://www.theblock.co/news/deals/2026-10-22-visa-in-talks-acquire-crypto-custody-firm-fireblocks-around-2-5-billion-axios-421926
- [Cointelegraph] Thailand SEC says several companies eye crypto ETFs, none has applied (10-22 22:20) — https://cointelegraph.com/news/thailand-sec-crypto-etf-applications?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] SoFi unveils bank-issued tokenized deposit for yield-bearing crypto funds (10-22 22:13) — https://cointelegraph.com/news/sofi-bank-issued-tokenized-deposit-yield-bearing-crypto-funds?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Crypto is making a splash in U.S. elections — but chiefly in jabs about industry influence (10-22 22:00) — https://www.coindesk.com/news-analysis/2026/10/21/crypto-is-making-a-splash-in-u-s-elections-but-chiefly-in-jabs-about-industry-influence
- [Cointelegraph] Bitcoin ETF buyers are trend followers, not setters, DWF Labs says (10-22 22:00) — https://cointelegraph.com/news/bitcoin-etf-flows-follow-price-trends-dwf-labs?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Ethereum’s four-minute settlement plan could lower the cost of moving crypto (10-22 21:14) — https://www.coindesk.com/tech/2026/10/22/ethereum-s-four-minute-settlement-plan-could-lower-the-cost-of-moving-crypto
- [The Block] Dune launches onchain trading data feeds as tokenized markets expand (10-22 21:00) — https://www.theblock.co/news/business/2026-10-22-dune-onchain-trading-data-feeds-421889
- [The Block] SoFi launches interest-bearing, FDIC-insured tokenized deposit for crypto users (10-22 21:00) — https://www.theblock.co/news/business/2026-10-22-sofi-fdic-insured-tokenized-deposit-421916
- [Cointelegraph] The UK needs a workable route to regulated DeFi access (10-22 21:00) — https://cointelegraph.com/opinion/uk-crypto-rules-regulated-defi-access?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Crypto traders seek shelter in bitcoin as altcoins slide and ETF flows wobble (10-22 20:20) — https://www.coindesk.com/daybook-us/2026/10/22/crypto-traders-seek-shelter-in-bitcoin-as-altcoins-slide-and-etf-flows-wobble
- [Cointelegraph] CoinDCX admits ‘operational losses’ after $16M wallet transfers draw scrutiny (10-22 19:53) — https://cointelegraph.com/news/coindcx-suspicious-outflows-wallet-compromised-2025-exploit?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin slides below $82,000 as AI doubts return, with DeFi tokens leading declines (10-22 19:50) — https://www.coindesk.com/markets/2026/10/22/bitcoin-slides-below-usd82-000-as-ai-doubts-return-with-defi-tokens-leading-declines
- [Cointelegraph] Bitcoin corrects below $82K after Tesla Q3 results, KOSPI falls (10-22 19:38) — https://cointelegraph.com/markets/bitcoin-corrects-below-82k-after-tesla-q3-results-kospi-falls?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Crypto traders price India telecoms company Reliance Jio's IPO at about $110 billion (10-22 19:18) — https://www.coindesk.com/markets/2026/10/22/crypto-traders-price-india-telecoms-company-reliance-jio-s-ipo-at-about-usd110-billion
- [The Block] Bitcoin ETFs draw $528 million as ether funds snap five-day outflow streak (10-22 18:56) — https://www.theblock.co/news/markets/2026-10-22-bitcoin-etfs-draw-528-million-as-ether-funds-snap-five-day-outflow-streak-421904
- [CoinDesk] Live updates: Bitcoin falls back to $81,000, with interest rates tumbling as stocks crack (10-22 18:54) — https://www.coindesk.com/business/2026/10/22/live-updates-bitcoin-s-round-trip-to-usd85-000-burns-traders-on-both-sides
- [Cointelegraph] Starknet voters back research into life beyond Ethereum (10-22 18:37) — https://cointelegraph.com/news/starknet-vote-post-quantum-l1-research-ethereum?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Starknet community overwhelmingly backs research into becoming an independent post-quantum Layer 1 (10-22 18:32) — https://www.theblock.co/news/ecosystems/2026-10-22-starknet-community-backs-independent-post-quantum-layer-1-421885
- [The Block] Layer 2 Scaling Solutions (10-22 18:15) — https://www.theblock.co/learn/campus/layer-2-scaling-solutions-419685
- [The Block] South Korea’s crypto bill nears completion while tax debate intensifies: reports (10-22 18:11) — https://www.theblock.co/news/regulation/2026-10-22-south-koreas-crypto-bill-nears-completion-421880
- [Cointelegraph] PHP flaw draws millions of exploit attempts, Cloudflare CEO warns (10-22 18:06) — https://cointelegraph.com/news/cloudflare-millions-exploit-attempts-php-vulnerability-disclosure?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

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