# 코인 데일리 스냅샷

- 수집 시각: 2026-10-20 10:12 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 -9.1 / 3일 평균 -7.1 / 오늘 구간 '중립'
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
| 수급 | 현물 ETF 순유입 | -1 | -1 | 5일 합 -229백만$ |
| 수급 | 거래소 순유입(7일) | -1 | -1 | 7일 순유입 분포 81백분위 |
| 수급 | 거래소 보유량(30일) | +1 | +1 | 30일 -1.44% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | +0 | +0 | 7일 -0.5% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0080% |
| 파생·심리 | RSI(14) | +0 | +0 | RSI 48.0 |
| 파생·심리 | 롱/숏 비율 | -2 | -2 | 롱/숏 분포 93백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +0 | OI 7일 +0.1%, 가격 +0.1% |
| 파생·심리 | 옵션 스큐 | -1 | +0 | +2.99 (풋 우위 확대, 전일 +2.63) |
| 매크로 | 나스닥 | -1 | -1 | 50일선 아래 |
| 매크로 | DXY | -1 | -1 | 101.95, 20일 +1.5% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 158.51 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -2 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 26430.887 | 26140.029 | pt | 2026-10-19 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -2.99 | -4.48 | % | 2026-10-19 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26626.02 | 26631.21 | pt | 2026-10-19 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 101.954 | 101.84 | pt | 2026-10-19 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.52 | 1.4 | % | 2026-10-19 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 158.514 | 157.806 | 엔 | 2026-10-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | -0.0 | -0.21 | % | 2026-10-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.02 | 3.71 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-10-14 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.79 | 2.76 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-10-14 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.42 | 3.36 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.01 | 2.98 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -2 | -2 |  | 2026-10-20 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.668 | 6.669 | % | 2026-10-20 01:12 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.7361 | 2.746 | 조$ | 2026-10-20 01:12 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | -82.4 | 5.1 | 백만$ | 2026-10-16 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 1거래일 연속 순유출 / 집계 기준일 2026-10-16 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -71.8 | 16.8 | 백만$ | 2026-10-16 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -228.6 | -228.6 | 백만$ | 2026-10-16 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | -1 | -1 | 일 | 2026-10-16 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 81837.69 | 82006.85 | USD | 2026-10-19 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 48.02 | 48.69 |  | 2026-10-19 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | 0.12 | -2.0 | % | 2026-10-19 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.3 | 3.33 | 십억$ | 2026-10-19 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | 0.14 | 2.45 | % | 2026-10-19 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 1.74 | 1.6 | 배 | 2026-10-19 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 93.3 | 93.3 | 백분위 | 2026-10-19 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.0082 | 0.01 | % | 2026-10-20 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.008 | 0.0053 | % | 2026-10-20 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 38.21 | 38.72 |  | 2026-10-20 01:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 2.99 | 2.63 | vol pt | 2026-10-20 01:13 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-11-27, 콜 BTC-27NOV26-89000-C / 풋 BTC-27NOV26-76000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.9731 | 0.9331 |  | 2026-10-13 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.1145 | 1.0996 |  | 2026-10-13 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 73565.0 | 74403.0 | $ | 2026-10-13 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 81988.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 11526.6 | 14233.6 | BTC | 2026-10-18 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 11689.6 | 12183.2 | BTC | 2026-10-18 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -1876.2 | -578.4 | BTC | 2026-10-18 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 81.1 | 83.3 | 백분위 | 2026-10-18 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -162.9 | 2050.5 | BTC | 2026-10-18 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -1.44 | -1.38 | % | 2026-10-18 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2679759.0 | 2679804.0 | BTC | 2026-10-18 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (10-19 18:00 ~ 10-20 10:12 KST)

피드 상태: CoinDesk: 11건 / The Block: 10건 / Cointelegraph: 17건 / 블록미디어: 10건

- [블록미디어] [개장시황] 코스피, 삼전·하이닉스 약세에 5600선까지 밀려 (10-20 09:15) — https://www.blockmedia.co.kr/archives/1153631?utm_source=general&utm_medium=rss
- [블록미디어] 저스틴 선 “하이퍼리퀴드, 이번 시장 주기 최대 발견 중 하나”…美 규제가 판도 가른다 (10-20 08:51) — https://www.blockmedia.co.kr/archives/1153589?utm_source=general&utm_medium=rss
- [블록미디어] [코인시황] 비트코인, 美 기술주 반등에도 8만2000달러대 횡보…금리·유가 부담 (10-20 08:21) — https://www.blockmedia.co.kr/archives/1153616?utm_source=general&utm_medium=rss
- [블록미디어] CME, 비트코인캐시·유니스왑 선물 출시 추진…기관투자자 선택지 확대 (10-20 08:08) — https://www.blockmedia.co.kr/archives/1153591?utm_source=general&utm_medium=rss
- [블록미디어] 캔튼 네트워크, 3분기 수수료 1억5500만달러 돌파…CC 가격 5.83% 상승 (10-20 07:38) — https://www.blockmedia.co.kr/archives/1153595?utm_source=general&utm_medium=rss
- [블록미디어] 비트코인 공매도 함정 경고…킬라 “한 번의 급등이 수익 지운다” (10-20 07:23) — https://www.blockmedia.co.kr/archives/1153599?utm_source=general&utm_medium=rss
- [블록미디어] 트론, 한 달 수익 2341만달러로 이더리움·솔라나 제쳐…가격은 0.48% 하락 (10-20 07:11) — https://www.blockmedia.co.kr/archives/1153585?utm_source=general&utm_medium=rss
- [The Block] BlackRock files for bitcoin ETF offering downside protection and upside exposure to IBIT (10-20 07:00) — https://www.theblock.co/news/regulation/2026-10-19-blackrock-files-bitcoin-managed-protect-etf-downside-protection-ibit-421087
- [블록미디어] 카드·환전 없이 지갑 그대로…비자·메시, 1.75억 가맹점 코인 결제 추진 (10-20 06:50) — https://www.blockmedia.co.kr/archives/1153580?utm_source=general&utm_medium=rss
- [블록미디어] 도지코인, 0.08달러서 매수 신호 포착…고래는 6억개 사들였다 (10-20 06:43) — https://www.blockmedia.co.kr/archives/1153579?utm_source=general&utm_medium=rss
- [블록미디어] 지캐시 선물 미결제약정 30% 급감…고래는 100억원대 추가 매수 ‘엇갈린 베팅’ (10-20 06:27) — https://www.blockmedia.co.kr/archives/1153576?utm_source=general&utm_medium=rss
- [Cointelegraph] Solana treasury firm SkyAI sells all SOL holdings, launches $201M buyback (10-20 06:04) — https://cointelegraph.com/news/solana-treasury-skyai-sells-all-sol-holdings-launches-201m-buyback?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Crypto PAC pours $362K into California race voters essentially decided in August (10-20 05:22) — https://cointelegraph.com/news/crypto-pac-california-race-voters-special-election?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Tether: Senator's investigation misses positive work that's led to lower Iran volumes (10-20 05:21) — https://www.coindesk.com/policy/2026/10/19/tether-senator-s-investigation-misses-positive-work-that-s-led-to-lower-iran-volumes
- [Cointelegraph] Here’s what happened in crypto today (10-20 05:02) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Market participants weigh in on SEC’s proposed crypto regulations (10-20 04:54) — https://cointelegraph.com/news/public-comments-us-sec-proposed-crypto-rules?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Visa, Mesh partner to enable crypto spending at 175M merchant locations (10-20 04:16) — https://cointelegraph.com/news/visa-mesh-partner-crypto-spending-175m-merchant-locations?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Mastercard launches stablecoin risk screening for banks and payment providers (10-20 04:03) — https://cointelegraph.com/news/mastercard-stablecoin-risk-screening-banks-payments?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Revolut secures Gibraltar crypto license to support global expansion (10-20 02:24) — https://cointelegraph.com/news/revolut-secures-gibraltar-crypto-license-to-support-global-expansion?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] U.S. CFTC rebuffs CME legal stance in consequential fight over perpetual futures (10-20 01:47) — https://www.coindesk.com/policy/2026/10/19/u-s-cftc-rebuffs-cme-legal-stance-in-consequential-fight-over-perpetual-futures
- [Cointelegraph] Metaplanet to take 93.7% stake in Super League through 2,100 BTC deal (10-20 01:41) — https://cointelegraph.com/news/metaplanet-super-league-2100-btc-us-bitcoin-treasury-deal?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Strive buys $335M in Bitcoin, boosting holdings to 36,818 BTC (10-20 01:30) — https://cointelegraph.com/news/strive-buys-335m-in-bitcoin-boosting-holdings-to-36818-btc?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Mesh taps Visa to let users spend crypto without a separate card (10-20 01:10) — https://www.theblock.co/news/business/2026-10-19-mesh-visa-partner-spend-crypto-stablecoins-421058
- [Cointelegraph] Bitcoin is rejected at $83K as US bond yields reverse higher with equities (10-20 01:05) — https://cointelegraph.com/markets/bitcoin-is-rejected-at-83k-as-us-bond-yields-reverse-higher-with-equities?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Mastercard unveils Stablecoin Security tool to screen payments for fraud and sanctions risks (10-20 01:00) — https://www.theblock.co/news/business/2026-10-19-mastercard-unveils-stablecoin-security-tool-to-screen-payments-for-fraud-and-sanctions-risks-420658
- [The Block] Galaxy’s AI data center business is undervalued amid CoreWeave debt concerns, StoneX says (10-20 00:53) — https://www.theblock.co/news/markets/2026-10-19-galaxy-digital-glxy-stonex-buy-coreweave-helios-ai-data-center-421045
- [The Block] SkyAI sells off entire Solana treasury as it launches $201 million buyback (10-20 00:28) — https://www.theblock.co/news/business/2026-10-19-skyai-sells-off-entire-solana-treasury-launches-201-million-buyback-421037
- [The Block] AnchorWatch Trust Company launches bitcoin custody service with up to $370 million in insurance per client (10-20 00:00) — https://www.theblock.co/news/business/2026-10-19-anchorwatch-bitcoin-custody-insurance-421011
- [CoinDesk] Zerohash rolls out a new tool to move crypto without copying wallet addresses (10-19 23:58) — https://www.coindesk.com/business/2026/10/19/zerohash-rolls-out-a-new-tool-to-move-crypto-without-copying-wallet-addresses
- [The Block] Strive scoops up another 1,223 bitcoin for $100 million as total holdings reach 36,818 BTC (10-19 22:45) — https://www.theblock.co/news/business/2026-10-19-strive-scoops-1223-bitcoin-100-million-total-holdings-reach-36818-btc-421020
- [The Block] Bitmine adds 12,535 ETH as treasury reaches 6.04 million tokens (10-19 22:36) — https://www.theblock.co/news/business/2026-10-19-bitmine-adds-12535-eth-as-treasury-reaches-6-04-million-tokens-421018
- [Cointelegraph] Made an ‘honest’ mistake with crypto taxes? New bill offers way out (10-19 22:30) — https://cointelegraph.com/magazine/made-an-honest-mistake-with-crypto-taxes-new-bill-offers-way-out?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Public companies object to OKX-ICE’s tokenized stock plan (10-19 22:13) — https://cointelegraph.com/news/public-companies-object-okx-ice-tokenized-stock?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Strategy buys $22M in Bitcoin, repurchases $193M in STRC (10-19 21:30) — https://cointelegraph.com/news/strategy-btc-22-million-buy-strc-buyback-193-million?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Cardano founder Charles Hoskinson is building a new programming language for the network (10-19 21:16) — https://www.coindesk.com/tech/2026/10/19/cardano-founder-charles-hoskinson-is-building-a-new-programming-language-for-the-network
- [The Block] ‘We found room for more orange’: Michael Saylor’s Strategy buys another 267 bitcoin for $22 million (10-19 21:10) — https://www.theblock.co/news/business/2026-10-19-we-found-room-for-more-orange-michael-saylors-strategy-buys-more-bitcoin-418895
- [Cointelegraph] World Liberty’s USD1 stablecoin sheds $400M in market cap in two weeks (10-19 20:57) — https://cointelegraph.com/news/world-liberty-usd1-stablecoin-market-cap-drops-400-million?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] BingX, YouHodler added to ESMA MiCA register in latest update (10-19 20:32) — https://cointelegraph.com/news/bingx-youhodler-esma-mica-register-friday-update?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Strategy's price chart is about to flash a major bullish signal weeks after bitcoin did (10-19 20:15) — https://www.coindesk.com/daybook-us/2026/10/19/strategy-on-verge-of-golden-cross-just-weeks-after-bitcoin-flashed-same-bullish-signal
- [CoinDesk] Live updates: Bitcoin holds near $82,000 as Nasdaq rebounds more than 1% (10-19 20:05) — https://www.coindesk.com/markets/2026/10/19/live-updates-bitcoin-tags-usd83-000-and-slips-back-as-chip-stocks-lead-a-rebound
- [The Block] Revolut secures Gibraltar crypto licence to support international expansion plans (10-19 19:42) — https://www.theblock.co/news/regulation/2026-10-19-revolut-secures-gibraltar-crypto-licence-to-support-international-expansion-plans-418889
- [CoinDesk] Bitcoin extends bounce above $82,000 as stocks rebound, DeFi tokens lead altcoin gains (10-19 19:26) — https://www.coindesk.com/markets/2026/10/19/bitcoin-extends-bounce-above-usd82-000-as-stocks-rebound-defi-tokens-lead-altcoin-gains
- [Cointelegraph] France advances stablecoin tax, eyes self-custodial wallets and exit tax proposals (10-19 19:22) — https://cointelegraph.com/news/france-stablecoin-tax-eyes-self-custodial-wallets-exit-tax?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Stocks rebound into key tech earnings: Three things to know in Bitcoin this week (10-19 19:20) — https://cointelegraph.com/markets/stocks-rebound-into-key-tech-earnings-three-things-to-know-in-bitcoin-this-week?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] JPMorgan brings JPM Coin, representing dollar deposits, to Ethereum (10-19 19:03) — https://www.coindesk.com/markets/2026/10/19/jpmorgan-s-jpm-coin-representing-dollar-deposits-is-coming-to-ethereum-bloomberg
- [CoinDesk] Crypto vault deposits top $10 billion as lending risks draw regulatory scrutiny (10-19 18:32) — https://www.coindesk.com/markets/2026/10/19/crypto-vault-deposits-top-usd10-billion-as-lending-risks-draw-regulatory-scrutiny
- [CoinDesk] Bitcoin mining offshoot Nscale loses Microsoft AI deal as power delay stretches into 2030s (10-19 18:15) — https://www.coindesk.com/tech/2026/10/19/bitcoin-mining-offshoot-nscale-loses-microsoft-ai-deal-as-power-delay-stretches-into-2030s
- [CoinDesk] CME’s bitcoin cash, uniswap futures, global PMIs: Crypto Week Ahead (10-19 18:12) — https://www.coindesk.com/markets/2026/10/19/cme-s-bitcoin-cash-uniswap-futures-global-pmis-crypto-week-ahead

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