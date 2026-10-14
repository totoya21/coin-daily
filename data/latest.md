# 코인 데일리 스냅샷

- 수집 시각: 2026-10-14 10:10 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 0.6 / 3일 평균 -6.7 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | -12.5 |
| 파생·심리 | 30% | 0.0 |
| 밸류에이션 | 25% | 25.0 |
| 매크로 | 15% | -12.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +0 | MVRV Z 0.98 |
| 밸류에이션 | 가격÷STH-RP | +0 | -1 | 가격÷STH-RP 1.121 |
| 수급 | 현물 ETF 순유입 | -1 | -1 | 5일 합 -657백만$ |
| 수급 | 거래소 순유입(7일) | +0 | +0 | 7일 순유입 분포 69백분위 |
| 수급 | 거래소 보유량(30일) | +1 | +1 | 30일 -1.32% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | -1 | -1 | 7일 +3.5% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0019% |
| 파생·심리 | RSI(14) | +0 | +0 | RSI 51.9 |
| 파생·심리 | 롱/숏 비율 | +0 | -1 | 롱/숏 분포 53백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +0 | OI 7일 -2.8%, 가격 -2.9% |
| 파생·심리 | 옵션 스큐 | -1 | +0 | +4.74 (풋 우위 확대, 전일 +2.41) |
| 매크로 | 나스닥 | +1 | +1 | 50일선 위 |
| 매크로 | DXY | -1 | -1 | 102.17, 20일 +2.5% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 158.48 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -1 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 27204.381 | 27245.9 | pt | 2026-10-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -1.43 | -0.84 | % | 2026-10-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26626.23 | 26600.42 | pt | 2026-10-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 102.169 | 102.58 | pt | 2026-10-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 2.53 | 3.12 | % | 2026-10-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 158.479 | 158.52 | 엔 | 2026-10-14 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | 0.12 | 0.48 | % | 2026-10-14 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 3.71 | 3.54 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-09-11 (점수 미반영: 발표 후 30일 경과) |
| A.매크로 | 근원 CPI 전년비 | 2.76 | 2.79 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-09-11 (점수 미반영: 발표 후 30일 경과) |
| A.매크로 | PCE 전년비 | 3.42 | 3.36 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.01 | 2.98 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -1 | -1 |  | 2026-10-14 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.51 | 6.7 | % | 2026-10-14 01:05 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.821 | 2.7373 | 조$ | 2026-10-14 01:05 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | -65.4 | 21.1 | 백만$ | 2026-10-12 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 1거래일 연속 순유출 / 집계 기준일 2026-10-12 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -65.4 | 22.4 | 백만$ | 2026-10-12 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -656.6 | -681.1 | 백만$ | 2026-10-12 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | -1 | 1 | 일 | 2026-10-12 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 83101.99 | 81742.5 | USD | 2026-10-13 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 51.89 | 46.93 |  | 2026-10-13 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -2.85 | -4.67 | % | 2026-10-13 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.23 | 3.29 | 십억$ | 2026-10-13 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -2.78 | 2.72 | % | 2026-10-13 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 1.32 | 1.26 | 배 | 2026-10-13 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 53.3 | 80.0 | 백분위 | 2026-10-13 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | -0.0031 | 0.0048 | % | 2026-10-14 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0019 | 0.003 | % | 2026-10-14 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 38.24 | 37.1 |  | 2026-10-14 01:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 4.74 | 2.41 | vol pt | 2026-10-14 01:11 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-10-30, 콜 BTC-30OCT26-88000-C / 풋 BTC-30OCT26-79000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.9824 | 1.0611 |  | 2026-10-07 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.1213 | 1.152 |  | 2026-10-07 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 74212.0 | 71315.0 | $ | 2026-10-07 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 83214.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 23968.5 | 17953.2 | BTC | 2026-10-12 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 25384.5 | 16818.3 | BTC | 2026-10-12 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -6451.0 | -8017.7 | BTC | 2026-10-12 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 68.9 | 62.2 | 백분위 | 2026-10-12 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -1416.0 | 1134.9 | BTC | 2026-10-12 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -1.32 | -1.25 | % | 2026-10-12 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2674559.0 | 2674829.0 | BTC | 2026-10-12 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (10-13 18:00 ~ 10-14 10:10 KST)

피드 상태: CoinDesk: 14건 / The Block: 7건 / Cointelegraph: 16건 / 블록미디어: 10건

- [CoinDesk] Largest Philippines crypto exchange, Coins.ph, said to face central bank regulatory action (10-14 10:00) — https://www.coindesk.com/policy/2026/10/13/largest-philippines-crypto-exchange-coins-ph-said-to-face-central-bank-regulatory-action
- [블록미디어] 플록, 2B 의사결정 모델 ‘THIS/THAT’ 공개…GPT-5.6·클로드 오퍼스 5 앞서 (10-14 09:55) — https://www.blockmedia.co.kr/archives/1151234?utm_source=general&utm_medium=rss
- [블록미디어] [개장시황] 코스피, 저가 매수에 2%대 반등…삼전·하이닉스 동반 강세 (10-14 09:15) — https://www.blockmedia.co.kr/archives/1151220?utm_source=general&utm_medium=rss
- [Cointelegraph] Ledger asks resellers to halt sales in Southeast Asia and Hong Kong (10-14 08:28) — https://cointelegraph.com/news/ledger-asks-resellers-to-halt-sales-in-southeast-asia-and-hong-kong?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Strive raising $500 million to buy additional bitcoin with new preferred share class (10-14 08:23) — https://www.coindesk.com/markets/2026/10/13/strive-to-ipo-second-preferred-share-class-as-it-looks-to-further-build-bitcoin-treasury
- [블록미디어] [코인시황] 비트코인, 美 CPI 발표 앞두고 반등…8만3000달러선 회복 (10-14 08:22) — https://www.blockmedia.co.kr/archives/1151205?utm_source=general&utm_medium=rss
- [블록미디어] 트론, 3분기 스테이블코인 결제액 2조2100억달러…활성 이용자 10% 증가 (10-14 08:16) — https://www.blockmedia.co.kr/archives/1151201?utm_source=general&utm_medium=rss
- [블록미디어] “장 닫혀도 24시간 거래”…토큰화 주식 33억달러 돌파 (10-14 06:53) — https://www.blockmedia.co.kr/archives/1151192?utm_source=general&utm_medium=rss
- [CoinDesk] BNY, Citadel Securities test tokenized U.S. Treasuries to speed up Wall Street financing (10-14 06:52) — https://www.coindesk.com/business/2026/10/13/bny-citadel-securities-test-tokenized-u-s-treasuries-to-speed-up-wall-street-financing
- [블록미디어] XRP 투자 기업 에버노스, 주주 명단 공개…리플 창업자·SBI 대거 참여 (10-14 06:39) — https://www.blockmedia.co.kr/archives/1151181?utm_source=general&utm_medium=rss
- [블록미디어] [뉴욕 금·채권·달러] 달러인덱스 101선 후퇴…CPI 발표 앞두고 국채금리 5.2% 유지 (10-14 06:37) — https://www.blockmedia.co.kr/archives/1151186?utm_source=general&utm_medium=rss
- [블록미디어] “비트코인 다시 10만달러 간다”…세일러, 강세장 진입 선언 (10-14 06:08) — https://www.blockmedia.co.kr/archives/1151179?utm_source=general&utm_medium=rss
- [블록미디어] [뉴욕 코인시황/마감] 8.3만달러 되찾은 비트코인…물가 지표 앞두고 눈치보기 (10-14 05:52) — https://www.blockmedia.co.kr/archives/1151176?utm_source=general&utm_medium=rss
- [블록미디어] [뉴욕증시 마감] 은행 실적 기대 못 미치고 반도체주 하락…다우 180포인트↓ (10-14 05:16) — https://www.blockmedia.co.kr/archives/1151163?utm_source=general&utm_medium=rss
- [Cointelegraph] Most tokenized stock trading on Solana, BNB Chain occurs outside US market hours (10-14 04:48) — https://cointelegraph.com/news/tokenized-stocks-after-hours-trading-solana-bnb-chain?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Here’s what happened in crypto today (10-14 04:33) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Trezor reduces resellers as a ‘preventative step’ amid Ledger tampering reports (10-14 04:07) — https://cointelegraph.com/news/trezor-preventative-steps-wallet-tampering-reports?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] How the SEC’s lack of leadership could facilitate crypto rulemaking (10-14 01:51) — https://cointelegraph.com/news/sec-leadership-facilitate-crypto-rulemaking?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Ripple, Stripe-owned Privy partner to bring embedded wallets to XRP Ledger (10-14 01:00) — https://www.theblock.co/news/business/2026-10-13-stripe-privy-ripple-xrp-ledger-wallets-418463
- [Cointelegraph] Strive reports $208M in warrant exercises as Bitcoin holdings jump 11% (10-14 00:57) — https://cointelegraph.com/news/strive-bitcoin-holdings-32773-btc-warrant-exercises?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Crypto exchange MNX takes on OKX, Bitget offering pre-IPO futures for AI giants (10-14 00:52) — https://www.coindesk.com/business/2026/10/13/new-crypto-exchange-takes-on-okx-bitget-with-unique-way-to-trade-ai-giants
- [Cointelegraph] Bitcoin keeps up pressure on $84K as US stocks skirt Korea tech sell-off (10-14 00:27) — https://cointelegraph.com/markets/bitcoin-keeps-up-pressure-on-84k-as-us-stocks-sidestep-korea-tech-sell-off?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] UK crypto trader says almost $800,000 lost in knife assault as wrench attacks proliferate (10-14 00:24) — https://www.coindesk.com/policy/2026/10/13/why-self-custody-and-hardware-wallets-cannot-prevent-physical-crypto-extortion
- [The Block] Interactive Brokers expands crypto services with Ethereum staking via Zerohash (10-14 00:24) — https://www.theblock.co/news/ecosystems/2026-10-13-interactive-brokers-ethereum-staking-zerohash-418457
- [The Block] DRW and Marex complete OTC swap referencing tokenized S&P iBoxx Index (10-14 00:00) — https://www.theblock.co/news/markets/2026-10-13-drw-marex-first-otc-swap-tokenized-sp-iboxx-index-canton-network-418440
- [The Block] Ledger confirms hardware implant in CryptoBilis reseller units as MediaMarkt suspends sales in Europe (10-13 23:45) — https://www.theblock.co/news/business/2026-10-13-ledger-confirms-hardware-implant-cryptobilis-reseller-units-mediamarkt-suspends-sales-europe-418442
- [Cointelegraph] Anthropic warns ‘AI worms’ may autonomously spread across devices like a virus (10-13 22:55) — https://cointelegraph.com/news/anthropic-ai-worms-autonomously-spread-devices-virus?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Strive buys 3,311 bitcoin for $280 million in largest acquisition since January (10-13 22:42) — https://www.theblock.co/news/business/2026-10-13-strive-buys-3311-bitcoin-280-million-largest-acquisition-since-january-418430
- [Cointelegraph] Is Bitcoin kidding itself about the Lightning Network? (10-13 22:30) — https://cointelegraph.com/magazine/is-bitcoin-kidding-itself-about-the-lightning-network?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Digital cash offers ‘cash-like privacy,’ but bank data breaches threaten users: BIS (10-13 22:17) — https://cointelegraph.com/news/bis-digital-cash-privacy-bank-data-breaches?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Russia clears Sberbank for crypto trading ahead of December launch (10-13 21:22) — https://cointelegraph.com/news/sberbank-russia-crypto-trading-approval?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] South Korea blocks 27 crypto exchanges, including Bitmart and Kucoin (10-13 20:58) — https://www.coindesk.com/policy/2026/10/13/south-korea-blocks-27-crypto-exchanges-including-bitmart-and-kucoin
- [CoinDesk] Federated Hermes joins Wall Street's tokenization push with plans for first onchain fund shares (10-13 20:56) — https://www.coindesk.com/business/2026/10/13/federated-hermes-joins-wall-street-s-tokenization-push-with-plans-for-first-onchain-fund-shares
- [The Block] Binance to shut down mining pool, cloud mining and related services (10-13 20:40) — https://www.theblock.co/news/business/2026-10-13-binance-to-shut-down-mining-pool-cloud-mining-and-related-services-418410
- [The Block] UK High Court rules Chinese law governs claims over $5 billion in seized bitcoin (10-13 20:38) — https://www.theblock.co/news/regulation/2026-10-13-uk-high-court-rules-chinese-law-governs-claims-over-5-billion-in-seized-bitcoin-418409
- [CoinDesk] Stacks' STX, a Bitcoin layer-2 token, has surged by 50% in four weeks (10-13 20:26) — https://www.coindesk.com/daybook-us/2026/10/13/stacks-stx-a-bitcoin-layer-2-token-has-surged-by-50-in-four-weeks
- [Cointelegraph] ENS seeks DAO approval to activate upgraded Ethereum naming system (10-13 20:11) — https://cointelegraph.com/news/ens-dao-ensv2-upgrade-eth-domain-registrations?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin, ether slip and rebound as South Korean stocks slide on AI-related concerns (10-13 20:06) — https://www.coindesk.com/markets/2026/10/13/bitcoin-ether-slip-and-rebound-as-south-korean-stocks-slide-on-ai-related-concerns
- [CoinDesk] Russia’s largest bank Sberbank secures approval to trade crypto (10-13 20:02) — https://www.coindesk.com/business/2026/10/13/russia-s-largest-bank-sberbank-secures-approval-to-trade-crypto
- [CoinDesk] Live updates: Bitcoin trading in tight range near $83,000 ahead of key U.S. inflation data (10-13 19:46) — https://www.coindesk.com/markets/2026/10/13/live-updates-bitcoin-whipsaws-between-usd81-000-and-usd84-000-as-altcoins-slide
- [CoinDesk] Bitcoin diverges from South Korean stocks as AI concerns deepen the Kospi selloff (10-13 19:38) — https://www.coindesk.com/markets/2026/10/13/bitcoin-diverges-from-south-korean-stocks-as-ai-concerns-deepen-the-kospi-selloff
- [Cointelegraph] Metaplanet to issue $329M convertible bonds to pay debt, fund share buybacks (10-13 19:23) — https://cointelegraph.com/news/metaplanet-329m-convertible-bonds-pay-debt-share-buybacks?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] MediaMarktSaturn pulls Ledger products amid tampering reports (10-13 19:09) — https://cointelegraph.com/news/mediamarkt-pulls-ledger-wallet-security-incident?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin hits $84K resistance as Korean tech rout deepens KOSPI losses (10-13 18:42) — https://cointelegraph.com/markets/bitcoin-hits-84k-resistance-as-korea-tech-sell-off-sends-kospi-down-74?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Ledger says 'spy' chip inside CryptoBilis Ledger devices transmitted wallet keys over mobile network (10-13 18:27) — https://www.coindesk.com/tech/2026/10/13/ledger-says-spy-chip-inside-cryptobilis-ledger-devices-transmitted-wallet-keys-over-mobile-network
- [CoinDesk] UK court ruling boosts government’s chances of keeping $5 billion in seized bitcoin (10-13 18:25) — https://www.coindesk.com/policy/2026/10/13/u-k-court-ruling-boosts-government-s-chances-of-keeping-gbp3-8-billion-seized-bitcoin
- [Cointelegraph] Chinese fraud victims lose key court battle over 61,000 Bitcoin (10-13 18:03) — https://cointelegraph.com/news/uk-court-chinese-law-61k-bitcoin-fraud-victims?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

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