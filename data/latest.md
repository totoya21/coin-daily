# 코인 데일리 스냅샷

- 수집 시각: 2026-09-29 09:48 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 매수** → BTC 목표 비중 **80%** (전일 판정: 매수)
- 오늘 총점 16.9 / 3일 평균 22.1 / 오늘 구간 '매수'
- 판정 가능 지표 14/17개 (82%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | 83.3 |
| 파생·심리 | 30% | 0.0 |
| 밸류에이션 | 25% | -25.0 |
| 매크로 | 15% | -12.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +0 | +1 | MVRV Z 1.11 |
| 밸류에이션 | 가격÷STH-RP | -1 | -1 | 가격÷STH-RP 1.190 |
| 수급 | 현물 ETF 순유입 | +2 | +2 | 7거래일 연속 순유입 |
| 수급 | 거래소 순유입(7일) | +2 | +2 | 7일 순유입 분포 1백분위 |
| 수급 | 거래소 보유량(30일) | +1 | +1 | 30일 -0.72% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | 제외 | — | 7일 전 값 없음 |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0039% |
| 파생·심리 | RSI(14) | -1 | -1 | RSI 60.8 |
| 파생·심리 | 롱/숏 비율 | +0 | +0 | 롱/숏 분포 67백분위 |
| 파생·심리 | 미결제약정(OI) | +1 | +0 | OI 7일 -7.1%, 가격 -3.6% (레버리지 정리) |
| 파생·심리 | 옵션 스큐 | -1 | +0 | +0.85 (풋 우위 확대, 전일 +0.64) |
| 매크로 | 나스닥 | +1 | +1 | 50일선 위 |
| 매크로 | DXY | -1 | -1 | 101.24, 20일 +1.6% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 157.46 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -1 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 26820.381 | 27068.721 | pt | 2026-09-28 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -1.11 | 2.06 | % | 2026-09-28 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26195.53 | 26169.53 | pt | 2026-09-28 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 101.241 | 100.97 | pt | 2026-09-28 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.55 | 1.83 | % | 2026-09-28 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 157.462 | 157.463 | 엔 | 2026-09-29 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | 0.06 | 0.45 | % | 2026-09-29 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 3.71 | 3.54 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-09-11 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.76 | 2.79 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-09-11 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.7 | 3.72 | % | 2026-07-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-08-26 (점수 미반영: 발표 후 30일 경과) |
| A.매크로 | 근원 PCE 전년비 | 3.34 | 3.34 | % | 2026-07-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-08-26 (점수 미반영: 발표 후 30일 경과) |
| A.매크로 | 인플레이션 방향 합계 | -1 | -1 |  | 2026-09-29 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.38 | 6.383 | % | 2026-09-29 00:44 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.8755 | 2.8736 | 조$ | 2026-09-29 00:44 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | 134.5 | 190.6 | 백만$ | 2026-09-25 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 7거래일 연속 순유입 / 집계 기준일 2026-09-25 |
| B.자금흐름 | IBIT(블랙록) 순유입 | 97.0 | 162.6 | 백만$ | 2026-09-25 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | 2385.8 | 2385.8 | 백만$ | 2026-09-25 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | 7 | 7 | 일 | 2026-09-25 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 83456.74 | 84462.14 | USD | 2026-09-28 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 60.75 | 65.13 |  | 2026-09-28 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -3.62 | 4.07 | % | 2026-09-28 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.15 | 3.11 | 십억$ | 2026-09-28 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -7.14 | -1.93 | % | 2026-09-28 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 1.32 | 1.35 | 배 | 2026-09-28 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 66.7 | 53.3 | 백분위 | 2026-09-28 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.0054 | 0.0071 | % | 2026-09-29 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0039 | 0.0006 | % | 2026-09-29 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 36.03 | 35.2 |  | 2026-09-29 00:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 0.85 | 0.64 | vol pt | 2026-09-29 00:48 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-10-30, 콜 BTC-30OCT26-90000-C / 풋 BTC-30OCT26-78000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 1.11 | 0.9336 |  | 2026-09-22 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.19 | 1.2 |  | 2026-09-22 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 70184.0 | 70258.0 | $ | 2026-09-22 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 83519.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 12578.8 | 11569.7 | BTC | 2026-09-27 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 16041.3 | 17514.6 | BTC | 2026-09-27 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -55059.4 | -51621.6 | BTC | 2026-09-27 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 1.1 | 1.1 | 백분위 | 2026-09-27 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -3462.5 | -5944.9 | BTC | 2026-09-27 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -0.72 | -0.55 | % | 2026-09-27 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2682330.0 | 2682221.0 | BTC | 2026-09-27 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (09-28 18:00 ~ 09-29 09:48 KST)

피드 상태: CoinDesk: 12건 / The Block: 8건 / Cointelegraph: 15건 / 블록미디어: 10건

- [블록미디어] [개장시황] 코스피, 외국인 매도에 장 초반 6800선 약세…삼전·하이닉스 보합권 (09-29 09:14) — https://www.blockmedia.co.kr/archives/1145242?utm_source=general&utm_medium=rss
- [블록미디어] [코인시황] 비트코인, 유가·美 국채금리 동반 상승에 8만3000달러선 약세 (09-29 08:19) — https://www.blockmedia.co.kr/archives/1145228?utm_source=general&utm_medium=rss
- [블록미디어] “달러 넣으면 스테이블코인 자동 전환, 연 3.75% 이자”… 씨티·코인베이스 맞손(종합) (09-29 08:13) — https://www.blockmedia.co.kr/archives/1145224?utm_source=general&utm_medium=rss
- [블록미디어] “애플 기록 깼다”… 엔비디아, 역대 최대 1500억달러 자사주 매입 (09-29 07:29) — https://www.blockmedia.co.kr/archives/1145218?utm_source=general&utm_medium=rss
- [블록미디어] [뉴욕 금·채권·달러] 미 10년물 국채금리 5.23% 상승…2007년 이후 최고치 육박 (09-29 06:50) — https://www.blockmedia.co.kr/archives/1145207?utm_source=general&utm_medium=rss
- [블록미디어] 무디스 잔디의 경고 “고금리 장기화, 미 경제 타격 시작됐다” (09-29 06:43) — https://www.blockmedia.co.kr/archives/1145206?utm_source=general&utm_medium=rss
- [블록미디어] 골드만삭스 “미 고금리 사채 발행 폭주… 투자자 소화불량에 리스크 프리미엄 5개월래 최고” (09-29 06:22) — https://www.blockmedia.co.kr/archives/1145202?utm_source=general&utm_medium=rss
- [블록미디어] 씨티·코인베이스 제휴 확대…“법정화폐 자동 정산으로 스테이블코인 결제 지원” (09-29 05:57) — https://www.blockmedia.co.kr/archives/1145194?utm_source=general&utm_medium=rss
- [블록미디어] [뉴욕 코인시황] 국채금리·유가 상승에…비트코인 8만3000달러대 후퇴 (09-29 05:56) — https://www.blockmedia.co.kr/archives/1145195?utm_source=general&utm_medium=rss
- [Cointelegraph] Canadian ‘crypto king’ set to represent himself at fraud trial (09-29 05:41) — https://cointelegraph.com/news/canada-aiden-pleterski-fraud-trial-crypto?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Blockchain.com eyes $500M IPO as crypto capital markets thaw: Report (09-29 05:28) — https://cointelegraph.com/news/blockchain-com-500m-ipo-bloomberg-reports?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] [뉴욕증시 마감] 미 10년물 금리 5.2% 돌파…증시, 기술주 주도로 하락 (09-29 05:11) — https://www.blockmedia.co.kr/archives/1145180?utm_source=general&utm_medium=rss
- [The Block] Tether’s USDT at center of Iran’s shadow banking network, new Senate Report says (09-29 04:10) — https://www.theblock.co/news/regulation/2026-09-28-tethers-usdt-center-iran-shadow-banking-network-new-senate-report-says-417094
- [Cointelegraph] Here’s what happened in crypto today (09-29 04:02) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] US SEC follows CFTC in staff guidance for crypto (09-29 03:39) — https://cointelegraph.com/news/sec-cftc-staff-guidance-crypto-clarity-fail?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bybit accepts Franklin Templeton tokenized funds as trading collateral (09-29 03:02) — https://cointelegraph.com/news/bybit-accepts-franklin-templeton-tokenized-funds-trading-collateral?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Goldman Sachs brings $100 billion Treasury fund into crypto’s institutional plumbing (09-29 03:00) — https://www.coindesk.com/markets/2026/09/28/goldman-sachs-brings-usd100-billion-treasury-fund-into-crypto-s-institutional-plumbing
- [The Block] Citi expands Coinbase partnership to power stablecoin payments for businesses (09-29 02:22) — https://www.theblock.co/news/business/2026-09-28-citi-coinbase-stablecoin-payments-corporate-clients-417082
- [Cointelegraph] Crypto PAC spends $11M to oppose Sherrod Brown in Ohio (09-29 01:48) — https://cointelegraph.com/news/crypto-industry-spending-ohio-senate-race-sherrod-brown?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] SEC Commissioner Hester Peirce reflects on her time at the agency, what she still wanted to get done: ‘There’s no good time to leave’ (09-29 01:35) — https://www.theblock.co/news/regulation/2026-09-28-sec-commissioner-hester-peirce-reflects-what-she-wanted-get-done-no-good-time-to-leave-417075
- [CoinDesk] The restaking gold rush is over, and top protocols are barely making a profit (09-29 01:24) — https://www.coindesk.com/business/2026/09/28/the-restaking-gold-rush-is-over-and-top-protocols-are-barely-making-a-profit
- [CoinDesk] Tether is a ‘lifeline’ for Iranian regime, Senate Dems say in new report (09-29 01:16) — https://www.coindesk.com/policy/2026/09/28/tether-is-a-lifeline-for-iranian-regime-senate-dems-say-in-new-report
- [The Block] Strive pushes bitcoin holdings above 27,400 BTC with latest $94.5 million purchase (09-29 01:00) — https://www.theblock.co/news/business/2026-09-28-strive-pushes-bitcoin-holdings-above-27400-btc-latest-94-5-million-purchase-417035
- [The Block] Bitget attacker tested risk controls with small transfers before $388 million theft, CEO says (09-29 00:30) — https://www.theblock.co/news/regulation/2026-09-28-bitget-attacker-tested-risk-controls-small-transfers-388-million-theft-ceo-says-417045
- [Cointelegraph] Bitget CEO says $388M hack exploited third-party security vulnerability (09-28 23:46) — https://cointelegraph.com/news/bitget-388m-hack-third-party-security-vulnerability?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] MiCA focus shifts from rulemaking to supervision, ESMA chair says (09-28 23:02) — https://cointelegraph.com/news/mica-shift-rulemaking-to-supervision-esma-chair?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Tom Lee’s Bitmine tops 6 million ETH after buying another 17,362 ether (09-28 22:39) — https://www.theblock.co/news/business/2026-09-28-tom-lees-bitmine-tops-6-million-eth-after-buying-another-17362-ether-416989
- [Cointelegraph] Altseason is coming — and traders are more discerning this time (09-28 22:30) — https://cointelegraph.com/magazine/altseason-is-coming-and-traders-are-more-discerning-this-time?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] AI agents could drain cheap bank deposits, Apollo's Torsten Slok warns (09-28 22:06) — https://www.coindesk.com/markets/2026/09/28/ai-agents-could-drain-cheap-bank-deposits-apollo-s-torsten-slok-warns
- [Cointelegraph] Strategy buys 1,665 Bitcoin for $143M as BTC stack hits 847,666 (09-28 21:38) — https://cointelegraph.com/news/strategy-1665-bitcoin-buy-holdings-847666-btc?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Chainlink launches new version of its crypto bridge tech 'CCIP' to give apps more control over their security (09-28 21:30) — https://www.coindesk.com/business/2026/09/28/chainlink-updates-its-crypto-bridge-tech-months-after-a-usd292-million-hack-shook-the-industry
- [Cointelegraph] BTC price eyes best Q3 in nine years: Three things to know in Bitcoin this week (09-28 21:21) — https://cointelegraph.com/markets/btc-price-eyes-best-q3-in-nine-years-three-things-to-know-in-bitcoin-this-week?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] THORChain rejects Bitget request to block hacker as $6 million moves to bitcoin (09-28 21:13) — https://www.coindesk.com/tech/2026/09/28/thorchain-rejects-bitget-request-to-block-hacker-as-usd6-million-moves-to-bitcoin
- [The Block] ‘Even more orange’: Strategy buys 1,665 bitcoin for $143 million as total holdings reach 847,666 BTC (09-28 21:11) — https://www.theblock.co/news/business/2026-09-28-even-more-orange-michael-saylor-strategy-bitcoin-416976
- [CoinDesk] Traders aren't panicking yet despite cooling crypto sentiment (09-28 20:32) — https://www.coindesk.com/daybook-us/2026/09/28/bitcoin-traders-aren-t-panicking-yet-despite-cooling-sentiment
- [Cointelegraph] Bitget resumes Bitcoin withdrawals as hacker swaps ETH via THORChain (09-28 20:05) — https://cointelegraph.com/news/bitget-btc-withdrawal-hacker-eth-swap-thorchain?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Crypto-friendly institution Franklin Templeton brings its tokenized collateral service to Bybit (09-28 20:00) — https://www.coindesk.com/business/2026/09/28/crypto-friendly-institution-franklin-templeton-brings-its-tokenized-collateral-service-to-bybit
- [CoinDesk] Bitcoin falls to $83,000 while altcoins unwind Friday's rally (09-28 19:15) — https://www.coindesk.com/markets/2026/09/28/bitcoin-falls-to-usd83-000-while-altcoins-unwind-friday-s-rally
- [CoinDesk] Live updates: Bitcoin remains under pressure as Iran denies report of peace progress (09-28 19:02) — https://www.coindesk.com/business/2026/09/28/live-updates-bitcoin-sinks-below-usd83-000-as-iran-talks-stall-and-oil-climbs
- [Cointelegraph] Hong Kong regulators expand financial reporting oversight to licensed crypto firms (09-28 18:58) — https://cointelegraph.com/news/hong-kong-sfc-afrc-crypto-financial-reporting-mou?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Eyes on key U.S. employment data as crypto bulls take a breather: Crypto Week Ahead (09-28 18:45) — https://www.coindesk.com/markets/2026/09/28/bitcoin-rally-takes-a-breather-ahead-of-key-u-s-employment-data-crypto-week-ahead
- [The Block] California Gov. Gavin Newsom bans public officials from launching memecoins, takes aim at Trump (09-28 18:32) — https://www.theblock.co/news/regulation/2026-09-28-california-gov-gavin-newsom-bans-public-officials-from-launching-memecoins-takes-aim-at-trump-416970
- [CoinDesk] Caution builds in the bitcoin market even as prices stay well above summer lows (09-28 18:29) — https://www.coindesk.com/markets/2026/09/28/bitcoin-bears-pay-to-bet-on-further-declines-as-futures-positions-near-yearly-lows
- [Cointelegraph] Scammers steal $2M in ETH as fake GIWA network fools DYORSWAP (09-28 18:19) — https://cointelegraph.com/news/fake-giwa-blockchain-scam-drains-2m-eth?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin drops under $83K as liquidity hunting keeps bulls from targeting yearly open (09-28 18:03) — https://cointelegraph.com/markets/bitcoin-drops-under-83k-as-liquidity-hunting-keeps-bulls-from-targeting-yearly-open?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

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