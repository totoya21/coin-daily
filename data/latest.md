# 코인 데일리 스냅샷

- 수집 시각: 2026-09-26 09:46 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 26.4 / 3일 평균 24.1 / 오늘 구간 '매수'
- 판정 가능 지표 14/17개 (82%)
- 오늘 구간 '매수'는 첫날 → 내일도 같으면 변경, 오늘은 '중립' 유지

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | 83.3 |
| 파생·심리 | 30% | -10.0 |
| 밸류에이션 | 25% | 25.0 |
| 매크로 | 15% | -12.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.93 |
| 밸류에이션 | 가격÷STH-RP | +0 | +0 | 가격÷STH-RP 1.130 |
| 수급 | 현물 ETF 순유입 | +2 | +2 | 6거래일 연속 순유입 |
| 수급 | 거래소 순유입(7일) | +2 | +2 | 7일 순유입 분포 2백분위 |
| 수급 | 거래소 보유량(30일) | +1 | +0 | 30일 -0.60% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | 제외 | — | 7일 전 값 없음 |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0041% |
| 파생·심리 | RSI(14) | -1 | -1 | RSI 64.3 |
| 파생·심리 | 롱/숏 비율 | -1 | +0 | 롱/숏 분포 73백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +0 | OI 7일 +0.2%, 가격 +4.0% |
| 파생·심리 | 옵션 스큐 | +0 | +0 | +0.62 |
| 매크로 | 나스닥 | +1 | +1 | 50일선 위 |
| 매크로 | DXY | -1 | -1 | 101.03, 20일 +1.9% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 157.19 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -1 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 27068.717 | 26939.369 | pt | 2026-09-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | 2.06 | 3.7 | % | 2026-09-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26169.53 | 26126.29 | pt | 2026-09-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 101.035 | 101.29 | pt | 2026-09-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.89 | 2.4 | % | 2026-09-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 157.185 | 158.265 | 엔 | 2026-09-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | 0.68 | 1.67 | % | 2026-09-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 3.71 | 3.54 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-09-11 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.76 | 2.79 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-09-11 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.7 | 3.72 | % | 2026-07-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-08-26 (점수 미반영: 발표 후 30일 경과) |
| A.매크로 | 근원 PCE 전년비 | 3.34 | 3.34 | % | 2026-07-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-08-26 (점수 미반영: 발표 후 30일 경과) |
| A.매크로 | 인플레이션 방향 합계 | -1 | -1 |  | 2026-09-26 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.355 | 6.334 | % | 2026-09-26 00:37 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.8869 | 2.8957 | 조$ | 2026-09-26 00:37 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | 190.6 | 347.0 | 백만$ | 2026-09-24 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 6거래일 연속 순유입 / 집계 기준일 2026-09-24 |
| B.자금흐름 | IBIT(블랙록) 순유입 | 162.6 | 166.3 | 백만$ | 2026-09-24 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | 2684.4 | 2653.2 | 백만$ | 2026-09-24 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | 6 | 5 | 일 | 2026-09-24 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 84093.13 | 84385.46 | USD | 2026-09-25 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 64.31 | 65.43 |  | 2026-09-25 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | 3.98 | 10.53 | % | 2026-09-25 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.16 | 3.17 | 십억$ | 2026-09-25 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | 0.18 | 8.86 | % | 2026-09-25 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 1.29 | 1.33 | 배 | 2026-09-25 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 73.3 | 56.7 | 백분위 | 2026-09-25 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.0017 | 0.0034 | % | 2026-09-26 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0041 | 0.0007 | % | 2026-09-26 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 34.77 | 36.0 |  | 2026-09-26 00:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 0.62 | 1.12 | vol pt | 2026-09-26 00:46 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-10-30, 콜 BTC-30OCT26-91000-C / 풋 BTC-30OCT26-79000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.9259 | 0.78 |  | 2026-09-19 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.13 | 1.13 |  | 2026-09-19 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 74401.0 | 74640.0 | $ | 2026-09-19 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 84074.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 19032.1 | 22387.6 | BTC | 2026-09-24 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 26693.5 | 32444.5 | BTC | 2026-09-24 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -41054.2 | -34394.8 | BTC | 2026-09-24 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 2.2 | 6.7 | 백분위 | 2026-09-24 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -7661.3 | -10056.9 | BTC | 2026-09-24 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -0.6 | -0.45 | % | 2026-09-24 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2690689.0 | 2695209.0 | BTC | 2026-09-24 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (09-25 18:00 ~ 09-26 09:46 KST)

피드 상태: CoinDesk: 11건 / The Block: 8건 / Cointelegraph: 13건 / 블록미디어: 10건

- [블록미디어] 4년 잠자던 비트코인 4500개 이동…매도 여부는 미확인 (09-26 09:19) — https://www.blockmedia.co.kr/archives/1144408?utm_source=general&utm_medium=rss
- [블록미디어] 美 항소법원 “칼시의 스포츠 예측 계약 파생상품 아냐”…대법원 판단 주목 (09-26 08:53) — https://www.blockmedia.co.kr/archives/1144401?utm_source=general&utm_medium=rss
- [블록미디어] 프랑스 시퀀스, 마지막 비트코인 314개 매각…기업 부채 완전 청산 (09-26 08:16) — https://www.blockmedia.co.kr/archives/1144395?utm_source=general&utm_medium=rss
- [블록미디어] SEC “스테이킹 증표 토큰, 경우에 따라 증권 아닐 수도” (09-26 07:32) — https://www.blockmedia.co.kr/archives/1144393?utm_source=general&utm_medium=rss
- [CoinDesk] U.S. SEC's steadiest crypto advocate, Hester Peirce, to depart next week (09-26 07:17) — https://www.coindesk.com/policy/2026/09/25/u-s-sec-s-steadiest-crypto-advocate-hester-peirce-to-depart-next-week
- [블록미디어] [뉴욕 금·채권·달러] 금리·달러 오름세 주춤…유가 하락에 원화·금값 반등 (09-26 06:48) — https://www.blockmedia.co.kr/archives/1144385?utm_source=general&utm_medium=rss
- [CoinDesk] Another appeals court rules against prediction market provider Kalshi, says sports contracts are subject to state regulations (09-26 06:17) — https://www.coindesk.com/policy/2026/09/25/another-appeals-court-rules-against-prediction-market-provider-kalshi-says-sports-contracts-are-subject-to-state-regulations
- [블록미디어] [뉴욕 코인시황] 미 금리·고유가에 주춤한 비트코인…ETF 자금이 하방 지지 (09-26 05:49) — https://www.blockmedia.co.kr/archives/1144382?utm_source=general&utm_medium=rss
- [Cointelegraph] OG.com seeks CFTC approval for single-stock perpetual futures (09-26 05:37) — https://cointelegraph.com/news/og-com-seeks-cftc-approval-single-stock-perpetual-futures?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] SEC crypto FAQ addresses token buybacks, network upgrades and promises of profit (09-26 05:32) — https://www.theblock.co/news/regulation/2026-09-25-sec-crypto-faq-addresses-token-buybacks-network-upgrades-promises-profit-416914
- [Cointelegraph] Ex-CFTC leader to leave Blockchain Association after CLARITY vote fails (09-26 05:26) — https://cointelegraph.com/news/cftc-commissioner-leaving-blockchain-association-ceo?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] [뉴욕증시 마감] 미 10년물 금리 5.2% 육박에도 S&P500·나스닥 반등 (09-26 05:13) — https://www.blockmedia.co.kr/archives/1144378?utm_source=general&utm_medium=rss
- [CoinDesk] Blockchain Association sees leadership shift shortly after crypto Clarity Act fizzles (09-26 05:01) — https://www.coindesk.com/policy/2026/09/25/blockchain-association-sees-leadership-shift-shortly-after-crypto-clarity-act-fizzles
- [The Block] Blockchain Association CEO Summer Mersinger to step down, Kristin Smith to return as interim CEO (09-26 04:48) — https://www.theblock.co/news/regulation/2026-09-25-blockchain-association-ceo-summer-mersinger-tstep-down-kristin-smith-interim-ceo-416913
- [블록미디어] AI 데이터센터 IPO 옥석가리기 (09-26 04:27) — https://www.blockmedia.co.kr/archives/1144374?utm_source=general&utm_medium=rss
- [블록미디어] 이란, 미 협상 재개 보도 일축…”유가 조작 목적의 거짓” (09-26 04:14) — https://www.blockmedia.co.kr/archives/1144372?utm_source=general&utm_medium=rss
- [블록미디어] 나델라 MS CEO “AI 자율 업무 시대, 최대 과제는 ‘신뢰'” (09-26 04:01) — https://www.blockmedia.co.kr/archives/1144370?utm_source=general&utm_medium=rss
- [Cointelegraph] Tether says it had ‘limited’ exposure to bank linked to $84M US seizure (09-26 03:56) — https://cointelegraph.com/news/us-authorities-seize-accounts-tether-bitfinex?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Here’s what happened in crypto today (09-26 03:42) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Former Hack VC partner Hsin-Ju Chuang’s death ruled a suicide (09-26 03:33) — https://cointelegraph.com/news/former-hack-vc-partner-hsin-ju-chuang-found-dead?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Man charged in $16 million crypto ‘massive pig butchering’ scam (09-26 02:48) — https://www.theblock.co/news/regulation/2026-09-25-man-charged-in-16-million-crypto-massive-pig-butchering-scam-416895
- [Cointelegraph] Bitget clarifies $388M in assets affected by security breach (09-26 02:17) — https://cointelegraph.com/news/bitget-clarifies-assets-affected-security-breach?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Strategy seeks shareholder approval for daily preferred stock dividends (09-26 01:34) — https://cointelegraph.com/news/strategy-seeks-shareholder-approval-daily-preferred-stock-dividends?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Crypto Biz: Wall Street and crypto fight for the same turf (09-26 00:49) — https://cointelegraph.com/news/crypto-biz-crypto-tradfi-stablecoins-tokenized-assets?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Circle and Tether step in to freeze hacker wallet after massive Bitget crypto heist (09-25 23:41) — https://www.coindesk.com/markets/2026/09/25/circle-and-tether-step-in-to-freeze-hacker-wallet-after-massive-bitget-crypto-heist
- [CoinDesk] Tokenization is moving faster than Washington (09-25 23:37) — https://www.coindesk.com/opinion/2026/09/25/tokenization-is-moving-faster-than-washington
- [CoinDesk] Tether confirms minimal EQIBank exposure following $89M US asset seizure (09-25 23:32) — https://www.coindesk.com/policy/2026/09/25/tether-confirms-minimal-eqibank-exposure-following-usd89m-us-asset-seizure
- [CoinDesk] Strategy proposes daily dividends to bring STRC back toward $100 (09-25 23:22) — https://www.coindesk.com/markets/2026/09/25/strategy-proposes-daily-dividends-to-bring-strc-back-toward-usd100
- [The Block] Magic Eden legacy approvals leave $5.7 million in NFTs exposed to exploit before rescue (09-25 23:09) — https://www.theblock.co/news/web3/2026-09-25-magic-eden-legacy-approvals-leave-5-7-million-in-nfts-exposed-to-exploit-before-rescue-416874
- [The Block] Aave V4 on Base adds Coinbase tokenized stocks as collateral for USDC loans (09-25 23:00) — https://www.theblock.co/news/defi/2026-09-25-aave-v4-on-base-adds-coinbase-tokenized-stocks-as-collateral-for-usdc-loans-416372
- [The Block] Strategy proposes daily dividends for STRC, STRD, STRF and STRK preferred stocks (09-25 22:48) — https://www.theblock.co/news/business/2026-09-25-strategy-proposes-daily-dividends-for-strc-strd-strf-and-strk-preferred-stocks-416869
- [Cointelegraph] Exchanges reporting crypto gains to IRS becomes tax nightmare (09-25 22:30) — https://cointelegraph.com/magazine/exchanges-reporting-crypto-gains-to-irs-becomes-tax-nightmare?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] CoinMarketCap buys CoinGlass to expand crypto derivatives data (09-25 21:44) — https://cointelegraph.com/news/coinmarketcap-coinglass-expand-crypto-derivatives-data?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] SlowMist has yet to confirm crypto theft from iPhone Safari attack (09-25 21:19) — https://cointelegraph.com/news/no-confirmed-crypto-theft-iphone-safari-attack-slowmist?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bond volatility surges while bitcoin and Wall Street stay calm (09-25 20:54) — https://www.coindesk.com/markets/2026/09/25/bond-volatility-surges-while-bitcoin-and-wall-street-stay-calm
- [CoinDesk] Bitcoin holders are cashing out, just not the way they did at prior market tops (09-25 20:29) — https://www.coindesk.com/daybook-us/2026/09/25/bitcoin-holders-are-cashing-out-just-not-the-way-they-did-at-prior-market-tops
- [Cointelegraph] IBIT options price trading more calmly after Bitcoin rebound (09-25 20:11) — https://cointelegraph.com/markets/ibit-options-trading-bitcoins-rebound?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Ethena expands USDe backing strategy into bStocks and equity perpetuals on Binance (09-25 20:00) — https://www.theblock.co/news/deals/2026-09-25-ethena-expands-usde-backing-strategy-into-bstocks-and-equity-perpetuals-on-binance-416367
- [CoinDesk] Altcoins rally across the board as bitcoin consolidates near $84,000 (09-25 18:59) — https://www.coindesk.com/markets/2026/09/25/altcoins-rally-across-the-board-as-bitcoin-consolidates-near-usd84-000
- [Cointelegraph] Magic Eden scare puts 3,832 NFTs in whitehat protective custody (09-25 18:48) — https://cointelegraph.com/news/magic-eden-nft-whitehat-vulnerability?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin ETF flows turn positive for 2026 after erasing $5.8 billion deficit (09-25 18:13) — https://www.coindesk.com/markets/2026/09/25/bitcoin-etfs-have-erased-a-usd5-8-billion-hole
- [The Block] KelpDAO sues LayerZero, claims it endorsed setup used in $292 million rsETH exploit (09-25 18:13) — https://www.theblock.co/news/regulation/2026-09-25-kelpdao-sues-layerzero-claims-it-endorsed-setup-used-in-292-million-rseth-exploit-416361

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