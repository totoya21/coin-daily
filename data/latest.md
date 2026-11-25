# 코인 데일리 스냅샷

- 수집 시각: 2026-11-25 17:59 KST
- 결과: 성공 38 / 실패·검증필요 2 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 6.9 / 3일 평균 8.8 / 오늘 구간 '중립'
- 판정 가능 지표 14/17개 (82%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | -50.0 |
| 파생·심리 | 30% | 50.0 |
| 밸류에이션 | 25% | 50.0 |
| 매크로 | 15% | -37.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.31 |
| 밸류에이션 | 가격÷STH-RP | +1 | +1 | 가격÷STH-RP 0.853 |
| 수급 | 현물 ETF 순유입 | -2 | -2 | 5거래일 연속 순유출 |
| 수급 | 거래소 순유입(7일) | +0 | +0 | 7일 순유입 분포 60백분위 |
| 수급 | 거래소 보유량(30일) | -1 | -1 | 30일 +0.83% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | -1 | -1 | 7일 +7.4% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0048% |
| 파생·심리 | RSI(14) | +2 | +2 | RSI 24.8 |
| 파생·심리 | 롱/숏 비율 | +0 | +0 | 롱/숏 분포 47백분위 |
| 파생·심리 | 미결제약정(OI) | +1 | +1 | OI 7일 -8.8%, 가격 -7.9% (레버리지 정리) |
| 파생·심리 | 옵션 스큐 | 제외 | -1 | 값 없음 |
| 매크로 | 나스닥 | -1 | -1 | 50일선 아래 |
| 매크로 | DXY | -1 | -1 | 104.01, 20일 +1.8% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 159.40 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -4 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 23733.539 | 24089.561 | pt | 2026-11-24 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -2.45 | -1.71 | % | 2026-11-24 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26026.54 | 26071.5 | pt | 2026-11-24 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 104.006 | 103.81 | pt | 2026-11-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.78 | 1.8 | % | 2026-11-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 159.399 | 159.009 | 엔 | 2026-11-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | -0.07 | 0.0 | % | 2026-11-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.08 | 4.02 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.87 | 2.79 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.65 | 3.44 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.12 | 3.03 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -4 | -4 |  | 2026-11-25 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 8.46 | 8.479 | % | 2026-11-25 08:55 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.0595 | 2.0562 | 조$ | 2026-11-25 08:55 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | -569.7 | -669.2 | 백만$ | 2026-11-23 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 5거래일 연속 순유출 / 집계 기준일 2026-11-23 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -509.3 | -544.7 | 백만$ | 2026-11-23 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -2367.5 | -2367.5 | 백만$ | 2026-11-23 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | -5 | -5 | 일 | 2026-11-23 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 59740.87 | 61189.97 | USD | 2026-11-24 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 24.77 | 26.85 |  | 2026-11-24 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -7.91 | -5.6 | % | 2026-11-24 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 2.69 | 2.8 | 십억$ | 2026-11-24 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -8.85 | -6.25 | % | 2026-11-24 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 2.62 | 2.57 | 배 | 2026-11-24 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 46.7 | 43.3 | 백분위 | 2026-11-24 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.0063 | 0.0056 | % | 2026-11-25 08:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0048 | 0.0036 | % | 2026-11-25 08:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 54.26 | 52.99 |  | 2026-11-25 08:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐 |  | 9.05 |  |  | fail | [Deribit](https://www.deribit.com/options/BTC) | 429 Client Error: Too Many Requests for url: https://www.deribit.com/api/v2/public/ticker?instrument_name=BTC-25DEC26-54000-C |
| D.온체인 | MVRV Z-Score | 0.3085 | 0.3721 |  | 2026-11-18 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 0.8532 | 0.8778 |  | 2026-11-18 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 70078.0 | 69780.0 | $ | 2026-11-18 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 59791.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 25236.8 | 40662.7 | BTC | 2026-11-24 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 25269.8 | 31283.6 | BTC | 2026-11-24 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -9423.4 | -13765.1 | BTC | 2026-11-24 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 60.0 | 48.9 | 백분위 | 2026-11-24 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -33.0 | 9379.1 | BTC | 2026-11-24 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | 0.83 | 0.84 | % | 2026-11-24 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2709516.0 | 2708749.0 | BTC | 2026-11-24 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (11-24 18:00 ~ 11-25 17:59 KST)

피드 상태: CoinDesk: 20건 / The Block: 20건 / Cointelegraph: 22건 / 블록미디어: 10건

- [Cointelegraph] EU seeks up to $55B for AI and quantum computing fund: Report (11-25 17:40) — https://cointelegraph.com/news/eu-55-billion-ai-quantum-computing-investment-fund?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Live updates: Bitcoin slips back under $60,000 as HYPE leads altcoins lower (11-25 17:35) — https://www.coindesk.com/business/2026/11/25/live-updates-bitcoin-slips-back-under-usd60-000-as-hype-leads-altcoins-lower
- [블록미디어] “AI 거품 터지면 비트코인 100만달러 길 열린다”…아서 헤이즈의 ‘역발상’ (11-25 17:30) — https://www.blockmedia.co.kr/archives/1170320?utm_source=general&utm_medium=rss
- [블록미디어] 비트코인 약세장, 얼마나 더 갈까⋯온체인 지표가 가리킨 5만3300달러 (11-25 17:15) — https://www.blockmedia.co.kr/archives/1170458?utm_source=general&utm_medium=rss
- [블록미디어] 월러 연준 이사 “토큰화 자산, ‘좀비체인’에 갇힐 수도”…법적 안전장치 촉구 (11-25 17:03) — https://www.blockmedia.co.kr/archives/1170275?utm_source=general&utm_medium=rss
- [The Block] Ark sells $6.8 million in its own bitcoin ETF as BTC dips below $59,000 (11-25 16:26) — https://www.theblock.co/news/business/2026-11-25-ark-sells-own-bitcoin-btc-dips-446109
- [블록미디어] 비트코인·이더리움 ETF서 하루 3억달러 이탈⋯블랙록에 집중된 매도세 (11-25 16:15) — https://www.blockmedia.co.kr/archives/1170399?utm_source=general&utm_medium=rss
- [블록미디어] “닷컴버블 때 아마존도 94% 폭락했다”…AI에 보내는 경고 (11-25 16:01) — https://www.blockmedia.co.kr/archives/1170337?utm_source=general&utm_medium=rss
- [블록미디어] 스트라이브 부사장, 은행 자본규제 개편 주목…”비트코인 역대급 호재 온다” (11-25 16:00) — https://www.blockmedia.co.kr/archives/1170370?utm_source=general&utm_medium=rss
- [블록미디어] ‘비트코인 10만달러’ 꿈 더 멀어지나⋯풋옵션 비중, 2022년 하락장 수준 복귀 (11-25 16:00) — https://www.blockmedia.co.kr/archives/1170393?utm_source=general&utm_medium=rss
- [Cointelegraph] South Korea’s crypto bill could move stablecoin race beyond token issuance (11-25 15:54) — https://cointelegraph.com/news/south-korea-crypto-bill-stablecoin-race-beyond-issuance?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] [마감시황] 코스피, 반등 하루 만에 6%대 폭락…4700선 붕괴 (11-25 15:49) — https://www.blockmedia.co.kr/archives/1170429?utm_source=general&utm_medium=rss
- [CoinDesk] Solana developers move to stop validators finishing work on blocks that already lost (11-25 15:33) — https://www.coindesk.com/tech/2026/11/25/solana-developers-move-to-stop-validators-finishing-work-on-blocks-that-already-lost
- [블록미디어] 디지털자산기본법: 4대 플레이어가 반드시 알아야 할 생존 법칙 (11-25 15:30) — https://www.blockmedia.co.kr/archives/1170379?utm_source=general&utm_medium=rss
- [CoinDesk] Just 10 accounts drove all of the XRP Ledger's trading growth last quarter (11-25 15:15) — https://www.coindesk.com/markets/2026/11/25/ten-accounts-drove-all-of-the-xrp-ledger-s-trading-growth-last-quarter
- [블록미디어] 트럼프, 젠슨 황 ‘사면 가능성’ 열어뒀다…엔비디아 지분 확보까지 거론 (11-25 15:00) — https://www.blockmedia.co.kr/archives/1170371?utm_source=general&utm_medium=rss
- [Cointelegraph] Here’s what happened in crypto today (11-25 14:50) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Solana DEX Velocity halts trading over bug just months after relaunch (11-25 14:32) — https://cointelegraph.com/news/solana-dex-velocity-halts-transactions-over-bug-coming-2-months-after-relaunch?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Bitcoin, ether get CFTC staff nod for expense requirements, Ethereum Foundation doubles security team, and more (11-25 14:15) — https://www.theblock.co/newsletters/the-daily/2026-11-25-bitcoin-ether-cftc-staff-nod-ethereum-foundation-doubles-security-team-more-crypto-news-446074
- [CoinDesk] Crypto traders can now hedge Nvidia, Anthropic and oil bets on Derive (11-25 13:57) — https://www.coindesk.com/markets/2026/11/25/crypto-traders-can-now-hedge-nvidia-and-oil-bets-on-derive
- [CoinDesk] A year after buying bitcoin, Czech central bank won't say what it's worth (11-25 13:50) — https://www.coindesk.com/markets/2026/11/23/a-year-after-buying-bitcoin-czech-central-bank-won-t-say-what-it-s-worth
- [Cointelegraph] Trump willing to pardon Jensen Huang, says it won’t be necessary (11-25 13:14) — https://cointelegraph.com/news/trump-willing-to-pardon-jensen-huang-but-says-it-wont-be-necessary?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Utah moves to drop criminal charges against Kalshi after platform halts operations (11-25 12:59) — https://www.theblock.co/news/regulation/2026-11-24-utah-moves-to-drop-criminal-charges-kalshi-446090
- [CoinDesk] Trump says he's willing to give Nvidia's Huang a pardon, doesn't think he needs one (11-25 12:35) — https://www.coindesk.com/policy/2026/11/24/trump-says-he-s-willing-to-give-nvidia-s-huang-a-pardon-doesn-t-think-he-needs-one
- [The Block] New York senator proposes 10% tax on prediction market fees to fund universal pre-K (11-25 11:46) — https://www.theblock.co/news/regulation/2026-11-24-new-york-proposal-prediction-market-tax-446082
- [Cointelegraph] CleanSpark weighs selling more Bitcoin than it mines to de-risk books (11-25 10:40) — https://cointelegraph.com/news/cleanspark-weighs-selling-more-bitcoin-than-it-mines-to-de-risk-books?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Hackers breach CIA intelligence network in latest US cyberattack (11-25 08:48) — https://cointelegraph.com/news/hackers-breach-cia-intelligence-network-in-latest-us-cyberattack?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Bitcoin miner CleanSpark swings to $987 million annual loss as BTC production declines (11-25 07:10) — https://www.theblock.co/news/business/2026-11-24-bitcoin-miner-cleanspark-swings-987-million-annual-loss-btc-production-declines-446061
- [Cointelegraph] Europol follows $28.5M crypto trail in streaming piracy crackdown (11-25 06:50) — https://cointelegraph.com/news/europol-crypto-trail-streaming-piracy-crackdown?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] SEC staff gives Molecule no-action relief for scientific research tokens (11-25 05:53) — https://www.theblock.co/news/regulation/2026-11-24-sec-staff-gives-molecule-no-action-relief-scientific-research-tokens-446067
- [Cointelegraph] Utah moves to dismiss criminal charges against Kalshi after trading halt (11-25 05:48) — https://cointelegraph.com/news/utah-moves-to-dismiss-criminal-charges-against-kalshi-after-trading-halt?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin sell-off driven by weak demand, forced liquidations: 21Shares (11-25 04:44) — https://cointelegraph.com/news/bitcoin-selloff-weak-demand-forced-liquidations-21shares?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Coldcard reveals how Bitcoin wallet flaw went undetected for over 5 years (11-25 04:04) — https://cointelegraph.com/news/coldcard-how-security-reviews-missed-bitcoin-wallet-flaw-years?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Payward’s Krak plans early 2027 launch of US credit cards with bitcoin cashback, including one secured by USDC (11-25 03:35) — https://www.theblock.co/news/business/2026-11-24-kraken-krak-early-2027-launch-us-credit-cards-bitcoin-cashback-usdc-collateral-445498
- [Cointelegraph] CFTC sets new prediction market rules as more firms seek US entry (11-25 03:31) — https://cointelegraph.com/news/cftc-new-prediction-market-rules-firms-seek-us-entry?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] BlackRock launches tokenized money market fund accepting stablecoins in Hong Kong (11-25 03:07) — https://cointelegraph.com/news/blackrock-launches-tokenized-money-market-fund-stablecoins-hong-kong?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Rep. Raskin probes Trump Jr.’s firm’s investments into Polymarket and Juul over ‘suspiciously well-timed government favors’ (11-25 03:05) — https://www.theblock.co/news/regulation/2026-11-24-rep-raskin-probes-trump-jr-s-firms-investments-polymarket-juul-suspiciously-well-timed-government-favors-446052
- [CoinDesk] Utah moves to drop criminal pursuit of Kalshi after the firm halted services there (11-25 02:50) — https://www.coindesk.com/policy/2026/11/24/utah-moves-to-drop-criminal-pursuit-of-kalshi-after-the-firm-halted-services-there
- [The Block] We’ve Entered Peak FEAR; SKY Falls (11-25 02:42) — https://www.theblock.co/newsletters/data-and-insights/2026-11-24-weve-entered-peak-fear-sky-falls-445476
- [Cointelegraph] Bitcoin slides amid US tariff nerves as Anthropic falls below IPO price (11-25 02:09) — https://cointelegraph.com/markets/bitcoin-slides-us-tariff-nerves-anthropic-falls-ipo-price?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Robinhood co-leads $5 million seed round for onchain trading platform Rialto (11-25 02:00) — https://www.theblock.co/news/deals/2026-11-24-robinhood-onchain-trading-platform-rialto-funding-446030
- [The Block] Ansem denies involvement in $2.57 million wallet drain; Black Bull creator coin plummets 55% (11-25 01:51) — https://www.theblock.co/news/defi/2026-11-24-ansem-denies-involvement-2-57-million-wallet-drain-black-bull-creator-coin-plummets-55-445705
- [The Block] Europol operation involving Binance, Coinbase and Chainalysis traces more than $28.5 million in crypto behind illegal streaming services (11-25 01:45) — https://www.theblock.co/news/regulation/2026-11-24-europol-operation-binance-coinbase-chainalysis-traces-28-5-million-crypto-illegal-streaming-services-446019
- [Cointelegraph] How South Korea’s proposed 20% cap could change who runs Upbit (11-25 01:33) — https://cointelegraph.com/news/how-south-koreas-proposed-20-cap-could-change-who-runs-upbit?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] 'AI trade never died': Traders see room for market recovery, but bitcoin's participation is another story (11-25 01:00) — https://www.coindesk.com/markets/2026/11/24/ai-trade-never-died-traders-see-room-for-market-recovery-despite-bitcoin-s-weakness
- [The Block] Ethereum treasury firm BTCS sells $43.8 million in ETH to cut Aave debt, CEO says ‘we do not take this lightly’ (11-25 00:27) — https://www.theblock.co/news/business/2026-11-24-ethereum-treasury-firm-btcs-sells-43-8-million-eth-cut-aave-debt-ceo-says-we-do-not-take-this-lightly-445562
- [CoinDesk] Anchorage Digital to unveil new asset-management subsidiary (11-25 00:06) — https://www.coindesk.com/business/2026/11/24/anchorage-digital-to-unveil-new-asset-management-subsidiary
- [CoinDesk] South Korea proposes ending 2017 ICO ban to boost jobs and onshore crypto investment (11-24 23:40) — https://www.coindesk.com/policy/2026/11/24/south-korea-proposes-ending-2017-ico-ban-to-boost-jobs-and-onshore-crypto-investment
- [The Block] Crypto Market Structure Basics (11-24 23:40) — https://www.theblock.co/learn/campus/crypto-market-structure-basics-442986
- [The Block] Bitcoin ETFs see another $570 million in net outflows as November total nears $5 billion and BTC dips below $60K (11-24 23:32) — https://www.theblock.co/news/markets/2026-11-24-bitcoin-etfs-another-570-million-net-outflows-november-total-nears-5-billion-btc-dips-below-60k-445548
- [Cointelegraph] USDT buyers face 22% VAT when Moscow Exchange opens crypto trading (11-24 23:10) — https://cointelegraph.com/news/russia-usdt-buyer-face-22-tax-december-launch?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] XRP Ledger DEX volume hits 4.51 million XRP a day in Q3 as big traders take over: Evernorth (11-24 23:00) — https://www.theblock.co/news/markets/2026-11-24-xrpl-dex-volume-q3-2026-evernorth-report-445395
- [The Block] Ledn brings US business onshore with account to hold, swap and borrow against bitcoin (11-24 23:00) — https://www.theblock.co/news/business/2026-11-24-ledn-launches-us-custody-account-bitcoin-gold-stablecoins-lending-445411
- [The Block] Neuberger Berman’s HINC fund brings high-yield credit to Aave’s institutional lending platform (11-24 23:00) — https://www.theblock.co/news/markets/2026-11-24-neuberger-berman-tokenized-hinc-fund-aave-horizon-collateral-445391
- [Cointelegraph] Swiss central bank, UBS and SIX study ledger for tokenized settlement (11-24 22:57) — https://cointelegraph.com/news/swiss-central-bank-ubs-six-explore-ledger-tokenized-settlement?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Sky lender proposes buyback of up to $50M to fund stUSDS withdrawals (11-24 22:43) — https://cointelegraph.com/news/sky-community-proposes-50m-buybacks-stusds-liquidity-crisis?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] BlackRock opens tokenized money market fund with $100 million in assets to Hong Kong investors (11-24 22:17) — https://www.theblock.co/news/business/2026-11-24-blackrock-opens-tokenized-money-market-fund-with-100-million-in-assets-to-hong-kong-investors-445524
- [Cointelegraph] Grayscale calls Bitcoin ‘oversold’ at $62K but warns of AI risks (11-24 22:11) — https://cointelegraph.com/markets/bitcoin-oversold-ai-risks-grayscale?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Crypto trader Ansem says his wallet was hacked as $2 million in memecoins were sold (11-24 21:47) — https://www.coindesk.com/markets/2026/11/24/a-wallet-linked-to-popular-crypto-trader-ansem-sold-usd2-million-in-memecoins-as-his-namesake-token-cratered
- [CoinDesk] Live updates: Bitcoin pulls back below $60,000, stock rally fades, as tariffs re-enter the picture (11-24 21:47) — https://www.coindesk.com/tech/2026/11/24/live-updates-bitcoin-pulls-back-to-usd60-000-as-stock-rally-fails-to-budge-crypto

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
- 고래비율(근사) (Arkham + Coin Metrics): Arkham 키 없음