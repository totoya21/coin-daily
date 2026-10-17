# 코인 데일리 스냅샷

- 수집 시각: 2026-10-17 10:09 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 -9.1 / 3일 평균 -5.9 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | -12.5 |
| 파생·심리 | 30% | -20.0 |
| 밸류에이션 | 25% | 25.0 |
| 매크로 | 15% | -37.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.97 |
| 밸류에이션 | 가격÷STH-RP | +0 | +0 | 가격÷STH-RP 1.115 |
| 수급 | 현물 ETF 순유입 | -1 | -1 | 5일 합 -125백만$ |
| 수급 | 거래소 순유입(7일) | -1 | -1 | 7일 순유입 분포 88백분위 |
| 수급 | 거래소 보유량(30일) | +1 | +1 | 30일 -1.49% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | +0 | +0 | 7일 +1.3% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0084% |
| 파생·심리 | RSI(14) | +0 | +0 | RSI 46.5 |
| 파생·심리 | 롱/숏 비율 | -2 | -1 | 롱/숏 분포 100백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +0 | OI 7일 +0.5%, 가격 -1.3% |
| 파생·심리 | 옵션 스큐 | -1 | -1 | +3.54 (풋 우위 확대, 전일 +3.23) |
| 매크로 | 나스닥 | -1 | +1 | 50일선 아래 |
| 매크로 | DXY | -1 | -1 | 101.78, 20일 +1.6% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 157.99 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -2 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 26140.033 | 26713.029 | pt | 2026-10-16 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -4.48 | -1.77 | % | 2026-10-16 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26631.21 | 26635.38 | pt | 2026-10-16 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 101.779 | 102.0 | pt | 2026-10-16 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.56 | 1.84 | % | 2026-10-16 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 157.987 | 157.957 | 엔 | 2026-10-16 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | -0.05 | 0.06 | % | 2026-10-16 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.02 | 3.71 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-10-14 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.79 | 2.76 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-10-14 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.42 | 3.36 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.01 | 2.98 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -2 | -2 |  | 2026-10-17 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.649 | 6.586 | % | 2026-10-17 01:04 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.7552 | 2.782 | 조$ | 2026-10-17 01:04 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | 5.1 | -261.5 | 백만$ | 2026-10-15 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 1거래일 연속 순유입 / 집계 기준일 2026-10-15 |
| B.자금흐름 | IBIT(블랙록) 순유입 | 16.8 | -110.9 | 백만$ | 2026-10-15 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -125.1 | -374.2 | 백만$ | 2026-10-15 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | 1 | -1 | 일 | 2026-10-15 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 81500.04 | 82131.46 | USD | 2026-10-16 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 46.5 | 48.67 |  | 2026-10-16 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -1.27 | 0.54 | % | 2026-10-16 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.3 | 3.36 | 십억$ | 2026-10-16 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | 0.53 | 1.81 | % | 2026-10-16 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 1.82 | 1.73 | 배 | 2026-10-16 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 100.0 | 83.3 | 백분위 | 2026-10-16 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.01 | 0.0051 | % | 2026-10-17 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0084 | 0.0041 | % | 2026-10-17 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 37.64 | 38.45 |  | 2026-10-17 01:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 3.54 | 3.23 | vol pt | 2026-10-17 01:09 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-11-06, 콜 BTC-6NOV26-86000-C / 풋 BTC-6NOV26-77000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.9714 | 0.9588 |  | 2026-10-10 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.1151 | 1.1102 |  | 2026-10-10 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 73326.0 | 74030.0 | $ | 2026-10-10 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 81765.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 27949.4 | 26132.0 | BTC | 2026-10-15 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 27449.7 | 26862.7 | BTC | 2026-10-15 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | 4083.5 | 3831.1 | BTC | 2026-10-15 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 87.8 | 87.8 | 백분위 | 2026-10-15 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | 499.7 | -730.7 | BTC | 2026-10-15 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -1.49 | -1.17 | % | 2026-10-15 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2676910.0 | 2675717.0 | BTC | 2026-10-15 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (10-16 18:00 ~ 10-17 10:09 KST)

피드 상태: CoinDesk: 9건 / The Block: 8건 / Cointelegraph: 11건 / 블록미디어: 10건

- [블록미디어] 비트코인 신규 고래 비중 33% 돌파…7만7000달러 주목 (10-17 09:57) — https://www.blockmedia.co.kr/archives/1152819?utm_source=general&utm_medium=rss
- [블록미디어] 미 상원선거에 디지털자산 정치자금 확대…PAC 5260만달러 투입 (10-17 09:15) — https://www.blockmedia.co.kr/archives/1152816?utm_source=general&utm_medium=rss
- [블록미디어] AI 투자에 기댄 세계 경제…호황 뒤에 커지는 붕괴 위험 (10-17 08:49) — https://www.blockmedia.co.kr/archives/1152799?utm_source=general&utm_medium=rss
- [블록미디어] 젠슨 황 “이 또한 지나가리라” ⋯AI 혼란과 주가 급락에도 낙관론 유지 (10-17 08:36) — https://www.blockmedia.co.kr/archives/1152800?utm_source=general&utm_medium=rss
- [블록미디어] JP모건, 외부 AI 차단…보안·책임 문제 부상(종합) (10-17 08:12) — https://www.blockmedia.co.kr/archives/1152791?utm_source=general&utm_medium=rss
- [블록미디어] 라울 팔 “이더리움 크게 저평가”…비트코인·솔라나도 보유 (10-17 07:28) — https://www.blockmedia.co.kr/archives/1152788?utm_source=general&utm_medium=rss
- [블록미디어] 210% 급등했던 스타크넷, 네트워크 활동 급감에 조정 위기 (10-17 06:50) — https://www.blockmedia.co.kr/archives/1152782?utm_source=general&utm_medium=rss
- [블록미디어] TD코웬, 스트라이브 목표가 56달러 상향…BTC 매수 조명 (10-17 06:38) — https://www.blockmedia.co.kr/archives/1152785?utm_source=general&utm_medium=rss
- [블록미디어] 비트코인 채굴 난도 5.92% 급등…140.58조로 7개월 만에 최고 (10-17 06:01) — https://www.blockmedia.co.kr/archives/1152778?utm_source=general&utm_medium=rss
- [블록미디어] [뉴욕 금·채권·달러] “AI 악재 vs 고물가”…미 국채금리·달러 혼조 (10-17 05:47) — https://www.blockmedia.co.kr/archives/1152772?utm_source=general&utm_medium=rss
- [The Block] Strive’s bitcoin buying spree earns 27% price target hike from TD Cowen (10-17 05:22) — https://www.theblock.co/news/markets/2026-10-16-strives-bitcoin-buying-spree-earns-27-price-target-hike-td-cowen-418839
- [Cointelegraph] Here’s what happened in crypto today (10-17 04:17) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Crypto PACs escalate spending against Sherrod Brown in Ohio Senate race (10-17 02:30) — https://cointelegraph.com/news/crypto-pac-fairshake-spending-ohio-senate-race-sherrod-brown?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Coinbase to power stablecoin-backed cards for Marqeta customers (10-17 02:21) — https://www.theblock.co/news/business/2026-10-16-coinbase-to-power-stablecoin-backed-cards-for-marqeta-customers-418833
- [Cointelegraph] Stablecoin remittances cost 84% less than traditional transfers, report finds (10-17 02:21) — https://cointelegraph.com/news/stablecoin-remittances-cost-savings-traditional-transfers?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Crypto Biz: Wall Street closes at 4. Tokenized stocks keep trading (10-17 00:52) — https://cointelegraph.com/news/tokenized-stocks-after-hours-trading-crypto-biz?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin price steadies around $82K after Fed’s Warsh avoids rate-hike hints (10-17 00:45) — https://cointelegraph.com/markets/bitcoin-price-steadies-82k-fed-warsh-avoids-rate-hike-hints?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Big Tech's AI auditors will only see what they're shown (10-16 23:58) — https://www.coindesk.com/opinion/2026/10/16/big-tech-s-ai-auditors-will-only-see-what-they-re-shown
- [The Block] Circle details USDC revenue split, says $819 million went to partners and costs in H1 2026 (10-16 23:58) — https://www.theblock.co/news/business/2026-10-16-circle-usdc-revenue-split-partners-418826
- [Cointelegraph] Strategy conditionally declares daily dividends as STRC hovers below $100 (10-16 23:11) — https://cointelegraph.com/news/strategy-daily-dividends-strc-hovers-below-100?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Ledger’s early implant warnings deserved more action, Karpelès says (10-16 22:51) — https://cointelegraph.com/news/ledger-early-implant-warnings-mark-karpeles?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Deutsche Bank prepares German crypto custody launch, eyes Asia: Report (10-16 22:33) — https://cointelegraph.com/news/deutsche-bank-crypto-custody-expansion-asia-2027?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] How Ethereum Works (10-16 22:31) — https://www.theblock.co/learn/ethereum/how-ethereum-works-418525
- [The Block] OpenAI says research model spent another wallet’s testnet ETH without authorization on coding task (10-16 20:34) — https://www.theblock.co/news/business/2026-10-16-openai-says-research-model-spent-another-wallets-testnet-eth-without-authorization-on-coding-task-418798
- [The Block] Visa Direct moves USDC prefunding into commercial production with Inyo Global (10-16 20:25) — https://www.theblock.co/news/business/2026-10-16-visa-direct-moves-usdc-prefunding-into-commercial-production-with-inyo-global-418802
- [Cointelegraph] Solana’s Liu says Shanghai event postponed over registration surge (10-16 20:22) — https://cointelegraph.com/news/solana-shanghai-postponed-exceeding-event-cap?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Traders will soon be able to bet on whether Coinbase, Robinhood and Marathon will hit their targets (10-16 20:15) — https://www.coindesk.com/daybook-us/2026/10/16/traders-will-soon-be-able-to-bet-on-whether-coinbase-robinhood-and-marathon-will-hit-their-targets
- [CoinDesk] Circle targets 40 new markets as stablecoin demand grows globally (10-16 19:54) — https://www.coindesk.com/business/2026/10/16/circle-targets-40-new-markets-as-stablecoin-demand-grows-globally
- [CoinDesk] Quantum Alliance forms amid warnings 6.4 million bitcoin face future quantum threat (10-16 19:52) — https://www.coindesk.com/tech/2026/10/16/experts-agree-quantum-computers-could-put-satoshi-s-bitcoin-at-risk-but-not-on-what-s-next
- [CoinDesk] Tokenized Tesla surges as Elon Musk unveils SpaceX-powered flying Roadster prototype (10-16 19:48) — https://www.coindesk.com/business/2026/10/16/elon-musk-s-flying-roadster-reveal-sent-tesla-crypto-trading-into-overdrive-while-stock-markets-were-closed
- [CoinDesk] Altcoins outpace bitcoin as celestia jumps 16%, Warsh silent on interest-rate plans (10-16 19:41) — https://www.coindesk.com/markets/2026/10/16/altcoins-outpace-bitcoin-as-celestia-jumps-16-warsh-silent-on-interest-rate-plans
- [Cointelegraph] CONNECT recap: Liquidity is tokenization’s next challenge, everyday stablecoins (10-16 19:27) — https://cointelegraph.com/news/connect-recap-tokenizations-next-challenge-is-building-liquidity-gsr-executive-says?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Scammer gets scammed in Ledger spy-chip exploit, loses almost $5 million in bitcoin (10-16 19:24) — https://www.coindesk.com/business/2026/10/16/scammer-gets-scammed-in-ledger-spy-chip-exploit-loses-almost-usd5-million-in-bitcoin
- [The Block] Google demonstrates quantum computing breakthrough as observers weigh Q-day implications (10-16 19:13) — https://www.theblock.co/news/web3/2026-10-16-google-quantum-computing-breakthrough-418787
- [CoinDesk] Live updates: Bitcoin dips to $81,000 as stocks slide, VIX soars ahead of Black Monday anniversary (10-16 18:48) — https://www.coindesk.com/markets/2026/10/16/live-updates-bitcoin-back-above-usd82-000-zec-jumps-11-as-etf-outflows-continue
- [CoinDesk] U.S. judge rejects Gemini’s appeal to void $5 million settlement despite CFTC backing (10-16 18:36) — https://www.coindesk.com/policy/2026/10/16/u-s-judge-rejects-gemini-s-appeal-to-void-usd5-million-settlement-despite-cftc-backing
- [The Block] Capital B posts wider H1 net loss of $78 million on bitcoin impairment charge (10-16 18:30) — https://www.theblock.co/news/business/2026-10-16-capital-b-wider-h1-net-loss-418781
- [Cointelegraph] Bitcoin may seek 20-month trend line reclaim before new record highs: CryptoQuant (10-16 18:22) — https://cointelegraph.com/markets/bitcoin-seeks-20-month-trend-line-reclaim-before-new-record-highs-cryptoquant?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

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