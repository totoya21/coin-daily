# 코인 데일리 스냅샷

- 수집 시각: 2026-10-02 09:48 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 0.1 / 3일 평균 3.6 / 오늘 구간 '중립'
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
| 밸류에이션 | 가격÷STH-RP | -1 | -1 | 가격÷STH-RP 1.150 |
| 수급 | 현물 ETF 순유입 | +1 | +2 | 5일 합 +274백만$ |
| 수급 | 거래소 순유입(7일) | +1 | +1 | 7일 순유입 분포 17백분위 |
| 수급 | 거래소 보유량(30일) | +1 | +1 | 30일 -0.83% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | +0 | +0 | 7일 -0.1% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0029% |
| 파생·심리 | RSI(14) | -1 | -1 | RSI 64.6 |
| 파생·심리 | 롱/숏 비율 | +0 | -1 | 롱/숏 분포 40백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +1 | OI 7일 -0.6%, 가격 +0.6% |
| 파생·심리 | 옵션 스큐 | -1 | -1 | +2.11 (풋 우위 확대, 전일 +0.97) |
| 매크로 | 나스닥 | +1 | +1 | 50일선 위 |
| 매크로 | DXY | -1 | -1 | 102.08, 20일 +2.5% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 158.03 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -2 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 26871.596 | 26861.061 | pt | 2026-10-01 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -0.25 | -0.28 | % | 2026-10-01 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26265.41 | 26241.79 | pt | 2026-10-01 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 102.079 | 101.45 | pt | 2026-10-01 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 2.53 | 1.83 | % | 2026-10-01 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 158.025 | 157.558 | 엔 | 2026-10-02 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | -0.49 | -0.3 | % | 2026-10-02 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 3.71 | 3.54 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-09-11 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.76 | 2.79 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-09-11 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.42 | 3.36 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.01 | 2.98 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -2 | -2 |  | 2026-10-02 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.328 | 6.385 | % | 2026-10-02 00:42 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.9062 | 2.8712 | 조$ | 2026-10-02 00:42 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | -148.7 | 66.2 | 백만$ | 2026-09-30 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 1거래일 연속 순유출 / 집계 기준일 2026-09-30 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -9.5 | 51.1 | 백만$ | 2026-09-30 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | 273.7 | 769.4 | 백만$ | 2026-09-30 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | -1 | 9 | 일 | 2026-09-30 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 84848.73 | 83556.14 | USD | 2026-10-01 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 64.62 | 60.87 |  | 2026-10-01 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | 0.55 | -0.97 | % | 2026-10-01 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.16 | 3.06 | 십억$ | 2026-10-01 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -0.55 | -8.54 | % | 2026-10-01 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 1.17 | 1.37 | 배 | 2026-10-01 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 40.0 | 76.7 | 백분위 | 2026-10-01 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.0003 | 0.0063 | % | 2026-10-02 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0029 | 0.0041 | % | 2026-10-02 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 36.47 | 35.27 |  | 2026-10-02 00:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 2.11 | 0.97 | vol pt | 2026-10-02 00:49 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-10-30, 콜 BTC-30OCT26-91000-C / 풋 BTC-30OCT26-80000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 1.0332 | 1.0328 |  | 2026-09-25 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.15 | 1.16 |  | 2026-09-25 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 73702.0 | 72180.0 | $ | 2026-09-25 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 84758.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 20094.3 | 28302.4 | BTC | 2026-09-30 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 24558.2 | 26433.3 | BTC | 2026-09-30 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -29064.1 | -34657.1 | BTC | 2026-09-30 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 16.7 | 11.1 | 백분위 | 2026-09-30 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -4463.9 | 1869.0 | BTC | 2026-09-30 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -0.83 | -0.65 | % | 2026-09-30 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2681920.0 | 2686232.0 | BTC | 2026-09-30 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (10-01 18:00 ~ 10-02 09:48 KST)

피드 상태: CoinDesk: 10건 / The Block: 9건 / Cointelegraph: 16건 / 블록미디어: 10건

- [블록미디어] [개장시황] 코스피, 수출 호조에도 0.47% 하락 출발…외국인·기관 ‘팔자’ (10-02 09:28) — https://www.blockmedia.co.kr/archives/1146929?utm_source=general&utm_medium=rss
- [The Block] Ethereum Foundation launches zkAPI to let users pay for AI models without revealing identity (10-02 09:22) — https://www.theblock.co/news/defi/2026-10-01-ethereum-foundation-launches-zkapi-417504
- [블록미디어] [블록페스타 2026] 스파르탄 켈빈 코 “월가 온체인 진입 이끈 건 기술 아닌 규제 변화” (10-02 09:10) — https://www.blockmedia.co.kr/archives/1146605?utm_source=general&utm_medium=rss
- [블록미디어] [코인시황] 비트코인, 1%대 반등에도 8만5000달러선 고전…ETF 순유출·유가 급등 부담 (10-02 08:26) — https://www.blockmedia.co.kr/archives/1146898?utm_source=general&utm_medium=rss
- [Cointelegraph] China warns foreign spies about crypto, Singapore dominates Asia: Asia Express (10-02 08:17) — https://cointelegraph.com/magazine/china-claims-crypto-used-by-spies-singapore-dominates-asian-crypto-asia-express?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] Cboe, ‘공포지수’ VIX 무기한 선물 상장 추진… 코인 넘어 전통 자산으로 영토 확장 (10-02 07:33) — https://www.blockmedia.co.kr/archives/1146881?utm_source=general&utm_medium=rss
- [블록미디어] 글로벌 국채 투매 ‘이상징후’…美 금리 내렸지만 프랑스·이탈리아는 급등-WSJ (10-02 07:05) — https://www.blockmedia.co.kr/archives/1146869?utm_source=general&utm_medium=rss
- [블록미디어] [뉴욕 금·채권·달러] 미 10년물, 5.34% 찍고 반락… ‘고금리 발작’ (10-02 06:49) — https://www.blockmedia.co.kr/archives/1146872?utm_source=general&utm_medium=rss
- [블록미디어] SK하이닉스 265억달러 상장에 美 IPO 시장 ‘훈풍’…중소형주는 부진 (10-02 06:15) — https://www.blockmedia.co.kr/archives/1146859?utm_source=general&utm_medium=rss
- [Cointelegraph] Evernorth clears shareholder vote ahead of Nasdaq debut with 473M XRP treasury (10-02 06:07) — https://cointelegraph.com/news/evernorth-clears-shareholder-vote-ahead-nasdaq-debut-473m-xrp-treasury?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] SEC proposes framework allowing investment advisers, funds to self-custody crypto (10-02 06:00) — https://www.theblock.co/news/regulation/2026-10-01-sec-proposes-crypto-custody-rule-investment-advisers-funds-417498
- [Cointelegraph] Trump to host 3rd ‘exclusive’ memecoin event amid corruption claims (10-02 06:00) — https://cointelegraph.com/news/donald-trump-memecoin-dinner-corruption-claims?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] [뉴욕 코인시황] PCE 둔화에 ‘업토버’ 기대감… 비트코인 8만5000달러 재탈환 시도 (10-02 05:57) — https://www.blockmedia.co.kr/archives/1146860?utm_source=general&utm_medium=rss
- [블록미디어] 美 30년 모기지 금리 7.28%…4년 만에 최대폭 급등 (10-02 05:34) — https://www.blockmedia.co.kr/archives/1146854?utm_source=general&utm_medium=rss
- [CoinDesk] SEC proposes new crypto custody rules for investment advisers and funds (10-02 05:20) — https://www.coindesk.com/policy/2026/10/01/u-s-sec-maps-out-crypto-custody-in-new-proposal-that-furthers-its-digital-assets-agenda
- [블록미디어] [뉴욕증시 마감] 20년래 최고 금리 꺾이자 반등…기술·중소형주 저가 매수 (10-02 05:11) — https://www.blockmedia.co.kr/archives/1146844?utm_source=general&utm_medium=rss
- [Cointelegraph] Here’s what happened in crypto today (10-02 05:07) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Hyperliquid Policy Center, Circle press EU on perps and stablecoin reserves in MiCA review (10-02 04:10) — https://www.theblock.co/news/regulation/2026-10-01-hyperliquid-circle-mica-review-417452
- [CoinDesk] Another Trump memecoin dinner advertised for token's top investors (10-02 03:45) — https://www.coindesk.com/policy/2026/10/01/another-trump-memecoin-dinner-advertised-for-token-s-top-investors
- [Cointelegraph] 50,000 Europeans call on EU to ease stablecoin rewards restrictions in MiCA review (10-02 03:45) — https://cointelegraph.com/news/50000-europeans-call-on-eu-to-ease-stablecoin-rewards-restrictions-in-mica-review?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Illinois will postpone implementation of crypto tax following lawsuit (10-02 03:01) — https://cointelegraph.com/news/illinois-postpones-crypto-tax-industry-lawsuit?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Ethereum staking reward burn proposal EIP-8363 pulled from Hegota upgrade (10-02 01:17) — https://www.theblock.co/news/ecosystems/2026-10-01-ethereum-staking-reward-burn-proposal-eip-8363-pulled-hegota-upgrade-417419
- [Cointelegraph] New York, Wyoming regulators sign pact to coordinate crypto oversight (10-02 01:12) — https://cointelegraph.com/news/new-york-wyoming-regulators-sign-pact-coordinate-crypto-oversight?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin fights for local uptrend as US bond yields drop from new 24-year highs (10-02 00:55) — https://cointelegraph.com/markets/bitcoin-fights-local-uptrend-us-bond-yields-drop-from-new-24-year-highs?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] NEAR Intents suffers $3.8M exploit after assistance with Bitget breach (10-02 00:43) — https://cointelegraph.com/news/near-intents-exploit-assistance-bitget-hack?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Evernorth shareholders approve $1 billion XRP treasury deal, clearing path to Nasdaq debut (10-02 00:17) — https://www.theblock.co/news/deals/2026-10-01-evernorth-xrpn-nasdaq-armada-shareholders-approve-417413
- [CoinDesk] Crypto for Advisors: The CLARITY Act failed, but the rules came anyway (10-02 00:00) — https://www.coindesk.com/coindesk-indices/2026/10/01/crypto-for-advisors-the-clarity-act-failed-but-the-rules-came-anyway
- [CoinDesk] NEAR Intents hit by $3.8 million exploit as crypto's rough year of hacks continues (10-01 23:18) — https://www.coindesk.com/tech/2026/10/01/near-intents-hit-by-usd3-8-million-exploit-as-crypto-s-rough-year-of-hacks-continues
- [The Block] NEAR Intents halts services after $3.8 million exploit, promises full compensation (10-01 23:18) — https://www.theblock.co/news/ecosystems/2026-10-01-near-intents-halts-services-after-3-8-million-exploit-promises-full-compensation-417404
- [Cointelegraph] Bitget’s $388M hack pushes Q3 crypto security losses past $1B (10-01 22:35) — https://cointelegraph.com/news/bitget-hack-q3-industry-losses-1-26-billion?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] LATAM stablecoin liquidity may depend on few providers, investor says (10-01 22:30) — https://cointelegraph.com/news/latam-stablecoin-liquidity-may-depend-on-few-providers-investor-says?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Stablecoins can drain from banks and nations at lightning speed (10-01 22:30) — https://cointelegraph.com/magazine/stablecoins-can-drain-from-banks-and-nations-at-lightning-speed?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Robinhood Wallet integrates Arcus RFQ system for stock token swaps (10-01 22:00) — https://www.theblock.co/news/business/2026-10-01-robinhood-wallet-integrates-arcus-rfq-system-for-stock-token-swaps-417394
- [The Block] Bitcoin ETFs’ 9-day, $3 billion inflow streak comes to an end as $149 million exits the funds (10-01 21:17) — https://www.theblock.co/news/markets/2026-10-01-bitcoin-etfs-9-day-3-billion-inflow-streak-comes-to-an-end-as-149-million-exits-the-funds-417384
- [CoinDesk] Live updates: Bitcoin posts tentative gains as rates drop ahead of Friday's jobs report (10-01 20:59) — https://www.coindesk.com/tech/2026/10/01/live-updates-bitcoin-flat-near-usd84-000-after-best-quarter-since-2024
- [CoinDesk] Illinois agrees to six-month delay of crypto tax as industry continues court battle (10-01 20:58) — https://www.coindesk.com/policy/2026/09/30/illinois-agrees-to-six-month-delay-of-crypto-tax-as-industry-continues-court-battle
- [CoinDesk] Crypto lost $1.26 billion in hacks while bitcoin bulls enjoyed a monster quarter (10-01 20:30) — https://www.coindesk.com/daybook-us/2026/10/01/crypto-lost-usd1-26-billion-in-hacks-while-bitcoin-bulls-enjoyed-a-monster-quarter
- [The Block] Lloyds, Visa settle $750,000 using USDC in live cross-border pilot (10-01 20:13) — https://www.theblock.co/news/business/2026-10-01-lloyds-visa-settle-750000-using-usdc-in-live-cross-border-pilot-417378
- [CoinDesk] Synthetic tokenized stocks are bad for American investors (10-01 20:00) — https://www.coindesk.com/opinion/2026/10/01/synthetic-tokenized-stocks-are-bad-for-american-investors
- [Cointelegraph] Tokenized assets don’t always mirror traditional markets, Dune finds (10-01 19:50) — https://cointelegraph.com/news/tokenized-assets-traditional-markets-dune-rwa-report?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin kicks off new quarter in the old $82,000-$85,000 price range (10-01 19:38) — https://www.coindesk.com/markets/2026/10/01/bitcoin-kicks-off-new-quarter-in-the-old-usd82-000-usd85-000-price-range
- [Cointelegraph] Bitcoin trapped below $86K as PCE changes cloud inflation reading (10-01 19:30) — https://cointelegraph.com/markets/bitcoin-rally-lower-us-inflation-data?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Binance’s EU services face scrutiny over licensing exemption: Report (10-01 19:07) — https://cointelegraph.com/news/europe-binance-questions-esma-tighter-mica-oversight?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Citigroup raises 12-month bitcoin target to $113,000 as ETF inflows resume (10-01 18:59) — https://www.coindesk.com/markets/2026/10/01/citigroup-raises-12-month-bitcoin-target-to-usd113-000-as-etf-inflows-resume
- [Cointelegraph] Chainalysis beats most Celsius claims, but ‘audit’ lawsuit survives (10-01 18:09) — https://cointelegraph.com/news/celsius-chainalysis-lawsuit-audit-claim-survives?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

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