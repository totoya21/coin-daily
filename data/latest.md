# 코인 데일리 스냅샷

- 수집 시각: 2026-10-24 13:55 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 -5.4 / 3일 평균 5.5 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | 0.0 |
| 파생·심리 | 30% | -20.0 |
| 밸류에이션 | 25% | 25.0 |
| 매크로 | 15% | -37.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.92 |
| 밸류에이션 | 가격÷STH-RP | +0 | +0 | 가격÷STH-RP 1.092 |
| 수급 | 현물 ETF 순유입 | +1 | +2 | 5일 합 +360백만$ |
| 수급 | 거래소 순유입(7일) | -1 | +0 | 7일 순유입 분포 81백분위 |
| 수급 | 거래소 보유량(30일) | +0 | +1 | 30일 -0.35% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | +0 | +0 | 7일 +0.4% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0081% |
| 파생·심리 | RSI(14) | +0 | +0 | RSI 45.2 |
| 파생·심리 | 롱/숏 비율 | -2 | -2 | 롱/숏 분포 100백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +0 | OI 7일 +3.5%, 가격 -0.5% |
| 파생·심리 | 옵션 스큐 | -1 | -1 | +5.09 (풋 우위 확대, 전일 +3.84) |
| 매크로 | 나스닥 | -1 | -1 | 50일선 아래 |
| 매크로 | DXY | -1 | -1 | 101.81, 20일 +0.8% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 156.81 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -2 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 25955.34 | 26008.859 | pt | 2026-10-23 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -0.71 | -2.64 | % | 2026-10-23 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26599.01 | 26615.96 | pt | 2026-10-23 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 101.81 | 101.61 | pt | 2026-10-23 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 0.83 | 0.25 | % | 2026-10-23 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 156.814 | 158.132 | 엔 | 2026-10-23 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | -0.84 | -1.17 | % | 2026-10-23 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.02 | 3.71 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-10-14 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.79 | 2.76 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-10-14 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.42 | 3.36 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.01 | 2.98 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -2 | -2 |  | 2026-10-24 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.678 | 6.642 | % | 2026-10-24 04:47 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.7266 | 2.742 | 조$ | 2026-10-24 04:47 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | -635.5 | 528.4 | 백만$ | 2026-10-22 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 1거래일 연속 순유출 / 집계 기준일 2026-10-22 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -254.1 | 235.0 | 백만$ | 2026-10-22 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | 360.3 | 1000.8 | 백만$ | 2026-10-22 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | -1 | 3 | 일 | 2026-10-22 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 81078.04 | 81307.16 | USD | 2026-10-23 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 45.25 | 46.03 |  | 2026-10-23 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -0.52 | -1.0 | % | 2026-10-23 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.42 | 3.37 | 십억$ | 2026-10-23 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | 3.52 | 0.16 | % | 2026-10-23 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 2.13 | 2.13 | 배 | 2026-10-23 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 100.0 | 100.0 | 백분위 | 2026-10-23 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.01 | 0.0069 | % | 2026-10-24 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0081 | 0.0082 | % | 2026-10-24 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 37.5 | 37.85 |  | 2026-10-24 04:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 5.09 | 3.84 | vol pt | 2026-10-24 04:55 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-11-27, 콜 BTC-27NOV26-88000-C / 풋 BTC-27NOV26-75000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.9178 | 0.9227 |  | 2026-10-17 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.0921 | 1.0933 |  | 2026-10-17 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 74102.0 | 74415.0 | $ | 2026-10-17 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 80927.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 25783.9 | 25125.8 | BTC | 2026-10-23 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 19528.0 | 27725.5 | BTC | 2026-10-23 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -329.9 | -5211.1 | BTC | 2026-10-23 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 81.1 | 68.9 | 백분위 | 2026-10-23 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | 6256.0 | -7115.1 | BTC | 2026-10-23 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -0.35 | -1.63 | % | 2026-10-23 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2685905.0 | 2676873.0 | BTC | 2026-10-23 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (10-23 18:00 ~ 10-24 13:55 KST)

피드 상태: CoinDesk: 8건 / The Block: 8건 / Cointelegraph: 13건 / 블록미디어: 10건

- [CoinDesk] Franklin Templeton adds $150 million in fund shares to XRP Ledger, all in one wallet (10-24 13:45) — https://www.coindesk.com/markets/2026/10/24/franklin-templeton-adds-usd150-million-in-fund-shares-to-xrp-ledger-all-in-one-wallet
- [블록미디어] 미국·이란 군사 긴장 재고조…중동 외교관 철수 (10-24 13:31) — https://www.blockmedia.co.kr/archives/1155720?utm_source=general&utm_medium=rss
- [블록미디어] AI 보안 ‘검은 10월’ … “누구나 공격하는 대해킹 시대 왔다” (10-24 13:13) — https://www.blockmedia.co.kr/archives/1155680?utm_source=general&utm_medium=rss
- [블록미디어] 크라켄, 모네로 출금 고객 ‘사용처 질문’ 철회…상장은 유지 (10-24 12:58) — https://www.blockmedia.co.kr/archives/1155716?utm_source=general&utm_medium=rss
- [블록미디어] 이니시아, 해킹에 체인 멈춰…270만달러 유출 (10-24 12:44) — https://www.blockmedia.co.kr/archives/1155714?utm_source=general&utm_medium=rss
- [블록미디어] 이더리움 OG, 1000개 추가 매도…누적 수익 880만달러 (10-24 12:01) — https://www.blockmedia.co.kr/archives/1155705?utm_source=general&utm_medium=rss
- [블록미디어] 비트코인, 미국 중간선거 공식 깨졌다…일찍 온 저점, 7월 대비 40% 반등 (10-24 11:35) — https://www.blockmedia.co.kr/archives/1155692?utm_source=general&utm_medium=rss
- [블록미디어] 비트코인 8만달러 사수 충력전…美 증시 후퇴, 국채로 자금 이동(종합) (10-24 11:20) — https://www.blockmedia.co.kr/archives/1155694?utm_source=general&utm_medium=rss
- [블록미디어] 공황장에 비트코인도 흔들…2027년 금융위기 경고등 (10-24 10:26) — https://www.blockmedia.co.kr/archives/1155679?utm_source=general&utm_medium=rss
- [블록미디어] 트론, 월간 수수료 2340만달러…테더 의존은 변수 (10-24 09:36) — https://www.blockmedia.co.kr/archives/1155675?utm_source=general&utm_medium=rss
- [블록미디어] [속보] 비트코인 8만달러선으로 후퇴 (10-24 09:19) — https://www.blockmedia.co.kr/archives/1155671?utm_source=general&utm_medium=rss
- [Cointelegraph] Wells Fargo and five others object to OKX-ICE tokenized stock listings: Report (10-24 06:32) — https://cointelegraph.com/news/nasdaq-companies-object-tokenized-stock-listings-okx-ice?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] IRS plans lower tax disclosure penalties, including for crypto: Forbes (10-24 05:54) — https://cointelegraph.com/news/irs-plans-lower-penalties-for-crypto-tax-disclosures-forbes-reports?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Initia halts blockchain after exploit reportedly drains over $2.6M (10-24 03:39) — https://cointelegraph.com/news/initia-halts-blockchain-exploit-drained?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Netanyahu seeking blockchain plan to prepare for possible sanctions (10-24 03:15) — https://www.theblock.co/news/markets/2026-10-23-netanyahu-israel-blockchain-plan-possible-sanctions-427792
- [The Block] Sen. Blumenthal seeks answers from Tether over payments to firm founded by ex-White House crypto adviser (10-24 02:46) — https://www.theblock.co/news/regulation/2026-10-23-sen-blumenthal-seeks-answers-tether-payments-firm-founded-ex-white-house-crypto-adviser-427785
- [Cointelegraph] US senator probes Tether after reported deal with ex-Trump crypto adviser (10-24 02:42) — https://cointelegraph.com/news/us-senator-probe-bo-hines-trump-crypto-adviser-tether-deal?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Initia halts network after security incident as attacker reportedly mints tokens (10-24 02:03) — https://www.theblock.co/news/defi/2026-10-23-initia-halts-network-after-security-incident-attacker-reportedly-mints-tokens-427755
- [Cointelegraph] SEC flags tokenization as high-risk area in 2027 market examinations (10-24 01:08) — https://cointelegraph.com/news/sec-adds-tokenized-securities-to-2027-examination-priorities?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin seeks support above $81K as Brent crude oil hits highest level since March (10-24 00:39) — https://cointelegraph.com/markets/bitcoin-seeks-support-above-81k-as-brent-crude-oil-hits-highest-level-since-march?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Robinhood sees surge in bitcoin, gold prediction markets as traders move beyond sports (10-23 22:58) — https://www.coindesk.com/markets/2026/10/23/robinhood-sees-surge-in-bitcoin-gold-prediction-markets-as-traders-move-beyond-sports
- [Cointelegraph] Here’s what happened in crypto today (10-23 22:38) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] China targets 2030 for its national blockchain network buildout (10-23 22:21) — https://cointelegraph.com/news/china-2030-national-blockchain-network-buildout?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Phantom rolls out Kalshi prediction markets to US users, says it’s ‘confident and comfortable’ amid state lawsuits (10-23 22:00) — https://www.theblock.co/news/markets/2026-10-23-phantom-rolls-out-kalshi-prediction-markets-us-421652
- [The Block] Singapore, Malaysia and Thailand central banks expand cross-border stablecoin initiative involving Ripple, Visa and Mastercard (10-23 21:55) — https://www.theblock.co/news/regulation/2026-10-23-singapore-malaysia-and-thailand-central-banks-expand-cross-border-stablecoin-initiative-involving-ripple-visa-and-mastercard-426492
- [Cointelegraph] New York AG seeks $1.37B from NovaTech founders over Ponzi scheme (10-23 21:33) — https://cointelegraph.com/news/new-york-ag-novatech-founders-companies-crypto-ponzi?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin consolidates after 3% loss as AI fears stoke fresh stock-market weakness (10-23 21:23) — https://cointelegraph.com/markets/bitcoin-consolidates-after-3-loss-as-ai-fears-stoke-fresh-stock-market-weakness?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin Core changes security rules as AI makes finding code bugs dangerously easy (10-23 21:03) — https://www.coindesk.com/tech/2026/10/23/bitcoin-will-now-stop-hiding-bugs-an-ai-can-find-in-one-prompt
- [Cointelegraph] Was crypto self-custody ever designed for beginners? (10-23 20:47) — https://cointelegraph.com/news/self-custody-crypto-beginners-mainstream-adoption?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Bitcoin ETFs swing back to net outflows as $636 million in withdrawals erase previous day’s inflows (10-23 20:39) — https://www.theblock.co/news/markets/2026-10-23-bitcoin-etfs-swing-back-to-net-outflows-erase-previous-day-inflows-426483
- [CoinDesk] Bitcoin's price is as jumpy as Nvidia's and eight times more turbulent than the euro (10-23 20:22) — https://www.coindesk.com/daybook-us/2026/10/23/bitcoin-s-volatility-is-well-above-euro-dollar-gyrations-though-it-has-calmed-to-rival-nvidia-s
- [CoinDesk] Live updates: Bitcoin holds above $81,000 as oil prices hit six-month high (10-23 20:13) — https://www.coindesk.com/markets/2026/10/23/live-updates-bitcoin-holds-above-usd81-000-as-the-ai-rout-fades-and-oil-climbs
- [CoinDesk] Bitcoin steadies near $81,700 as altcoins rebound, pepe climbs 13% (10-23 19:54) — https://www.coindesk.com/markets/2026/10/23/bitcoin-steadies-near-usd81-700-as-altcoins-rebound-pepe-climbs-13
- [CoinDesk] Bitcoin appears to have decoupled from midterm cycle bottom history (10-23 19:53) — https://www.coindesk.com/markets/2026/10/23/bitcoin-approaches-midterms-as-july-low-challenges-historical-cycle-pattern
- [CoinDesk] HSBC rolls out its first stablecoin to over 3 million everyday app users (10-23 19:22) — https://www.coindesk.com/business/2026/10/23/hsbc-rolls-out-its-first-stablecoin-to-over-3-million-everyday-app-users
- [Cointelegraph] Cysic dangles a 10% bounty, hacker pours loot into Tornado Cash (10-23 19:13) — https://cointelegraph.com/news/cysic-exploiter-eth-tornado-cash-white-hat-offer?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] New York seeks over $1.3 billion from NovaTech founders after couple fled the US (10-23 19:12) — https://www.theblock.co/news/regulation/2026-10-23-new-york-seeks-over-1-3-billion-from-novatech-founders-after-couple-fled-the-us-424453
- [The Block] South Korea to amend forex law to regulate stablecoins as payment instruments: report (10-23 18:52) — https://www.theblock.co/news/regulation/2026-10-23-south-korea-stablecoins-payment-instruments-424028
- [Cointelegraph] Bybit secures first full Dubai license for spot trading services (10-23 18:50) — https://cointelegraph.com/news/bybit-first-full-dubai-spot-trading-license?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

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