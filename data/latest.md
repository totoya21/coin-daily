# 코인 데일리 스냅샷

- 수집 시각: 2026-11-14 15:53 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 -15.1 / 3일 평균 -16.1 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | -62.5 |
| 파생·심리 | 30% | 10.0 |
| 밸류에이션 | 25% | 25.0 |
| 매크로 | 15% | -37.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.71 |
| 밸류에이션 | 가격÷STH-RP | +0 | +0 | 가격÷STH-RP 1.001 |
| 수급 | 현물 ETF 순유입 | -2 | -2 | 5거래일 연속 순유출 |
| 수급 | 거래소 순유입(7일) | -1 | -1 | 7일 순유입 분포 78백분위 |
| 수급 | 거래소 보유량(30일) | -1 | -1 | 30일 +1.80% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | -1 | -1 | 7일 +10.9% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0004% |
| 파생·심리 | RSI(14) | +2 | +2 | RSI 24.7 |
| 파생·심리 | 롱/숏 비율 | -2 | -2 | 롱/숏 분포 90백분위 |
| 파생·심리 | 미결제약정(OI) | +1 | +0 | OI 7일 -10.6%, 가격 -9.9% (레버리지 정리) |
| 파생·심리 | 옵션 스큐 | -1 | -1 | +5.44 (풋 우위 확대, 전일 +4.34) |
| 매크로 | 나스닥 | -1 | -1 | 50일선 아래 |
| 매크로 | DXY | -1 | -1 | 103.41, 20일 +1.5% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 159.88 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -4 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 25136.27 | 25366.09 | pt | 2026-11-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | 2.27 | 4.32 | % | 2026-11-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26350.07 | 26379.03 | pt | 2026-11-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 103.41 | 103.17 | pt | 2026-11-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.54 | 1.28 | % | 2026-11-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 159.875 | 159.734 | 엔 | 2026-11-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | 1.51 | 1.48 | % | 2026-11-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.08 | 4.02 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.87 | 2.79 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.65 | 3.44 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.12 | 3.03 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -4 | -4 |  | 2026-11-14 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 7.61 | 7.471 | % | 2026-11-14 06:53 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.2984 | 2.3529 | 조$ | 2026-11-14 06:53 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | -299.9 | -95.0 | 백만$ | 2026-11-11 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 5거래일 연속 순유출 / 집계 기준일 2026-11-11 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -269.7 | -78.2 | 백만$ | 2026-11-11 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -1438.1 | -1438.1 | 백만$ | 2026-11-11 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | -5 | -5 | 일 | 2026-11-11 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 68236.54 | 71369.9 | USD | 2026-11-13 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 24.73 | 29.78 |  | 2026-11-13 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -9.9 | -6.05 | % | 2026-11-13 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.46 | 3.87 | 십억$ | 2026-11-13 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -10.62 | 7.16 | % | 2026-11-13 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 3.06 | 3.11 | 배 | 2026-11-13 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 90.0 | 100.0 | 백분위 | 2026-11-13 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.0039 | 0.0038 | % | 2026-11-14 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0004 | 0.0089 | % | 2026-11-14 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 42.03 | 39.08 |  | 2026-11-14 06:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 5.44 | 4.34 | vol pt | 2026-11-14 06:54 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-12-04, 콜 BTC-4DEC26-72000-C / 풋 BTC-4DEC26-64000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.7119 | 0.7132 |  | 2026-11-07 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.0008 | 1.0015 |  | 2026-11-07 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 68042.0 | 71174.0 | $ | 2026-11-07 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 68096.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 26738.3 | 26241.0 | BTC | 2026-11-13 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 28867.8 | 27150.7 | BTC | 2026-11-13 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -4017.0 | -6738.7 | BTC | 2026-11-13 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 77.8 | 70.0 | 백분위 | 2026-11-13 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -2129.5 | -909.7 | BTC | 2026-11-13 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | 1.8 | 1.75 | % | 2026-11-13 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2723962.0 | 2723131.0 | BTC | 2026-11-13 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (11-13 18:00 ~ 11-14 15:53 KST)

피드 상태: CoinDesk: 9건 / The Block: 14건 / Cointelegraph: 15건 / 블록미디어: 10건

- [블록미디어] 비트코인 현물 ETF 1억8500만달러 순유출…이더리움은 236만달러 유입 (11-14 15:43) — https://www.blockmedia.co.kr/archives/1165896?utm_source=general&utm_medium=rss
- [Cointelegraph] Bitcoin ETFs shed $2.35B in two weeks as BlackRock’s losing streak hits 11 sessions (11-14 15:33) — https://cointelegraph.com/markets/bitcoin-etf-outflows-2-35-billion-blackrock-11-session-streak?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] [코생지] 엔비디아발 충격에 7만달러 내준 비트코인⋯하락장서 10위권 오른 이더파이 (11-14 15:03) — https://www.blockmedia.co.kr/archives/1165357?utm_source=general&utm_medium=rss
- [The Block] Meta tests prediction-market app, DOJ moves to seize $1.2 billion from Binance hack, and more (11-14 14:40) — https://www.theblock.co/newsletters/the-daily/2026-11-14-meta-prediction-market-app-doj-binance-hack-more-crypto-news-440304
- [CoinDesk] Satoshi-era wallet served in a $260 billion lawsuit moves 75 BTC it held since 2011 (11-14 13:30) — https://www.coindesk.com/markets/2026/11/13/satoshi-era-wallet-served-in-a-usd260-billion-lawsuit-moves-75-btc-it-held-since-2011
- [블록미디어] 머스크, 앤트로픽 이탈설 일축…스페이스X 740억달러 AI 증설 (11-14 13:00) — https://www.blockmedia.co.kr/archives/1165872?utm_source=general&utm_medium=rss
- [블록미디어] AI 에이전트 결제 1500만건…XRP 레저 생태계 확대 (11-14 12:22) — https://www.blockmedia.co.kr/archives/1165866?utm_source=general&utm_medium=rss
- [블록미디어] 오픈AI “35초면 멈춘다”…AI 에이전트 ‘킬스위치’ 경쟁 (11-14 11:40) — https://www.blockmedia.co.kr/archives/1165853?utm_source=general&utm_medium=rss
- [블록미디어] 비트코인 68K 밑으로, XRP 1달러 아래로…추가 하락 경고음(상보) (11-14 11:39) — https://www.blockmedia.co.kr/archives/1165854?utm_source=general&utm_medium=rss
- [블록미디어] [속보] 비트코인 68K 밑으로, 엑스알피 1달러 밑으로 하락 (11-14 11:24) — https://www.blockmedia.co.kr/archives/1165851?utm_source=general&utm_medium=rss
- [블록미디어] 일론 머스크, 젠슨 황 엔비디아 CEO 복귀 청원 지지 (11-14 11:13) — https://www.blockmedia.co.kr/archives/1165844?utm_source=general&utm_medium=rss
- [블록미디어] 비트코인 35% 공개키 노출…양자컴퓨터 위험권 ‘경고’ (11-14 10:23) — https://www.blockmedia.co.kr/archives/1165835?utm_source=general&utm_medium=rss
- [블록미디어] 파라과이, 비트코인 채굴 계약 ‘연장 불가’…AI에 전력 넘긴다 (11-14 09:36) — https://www.blockmedia.co.kr/archives/1165822?utm_source=general&utm_medium=rss
- [CoinDesk] Bitcoin miners pay Paraguay $350 million a year, but AI is pushing them out (11-14 08:30) — https://www.coindesk.com/tech/2026/11/13/bitcoin-miners-pay-paraguay-usd350-million-a-year-but-ai-is-pushing-them-out
- [Cointelegraph] Here’s what happened in crypto today (11-14 07:08) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] OpenAI launches AI payments in ChatGPT with Visa, Mastercard and Amex (11-14 07:01) — https://cointelegraph.com/news/openai-ai-payments-chatgpt-wallet-visa-mastercard-amex?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Adam Back makes case for simpler security as Blockstream launches Bitcoin custody system (11-14 06:49) — https://cointelegraph.com/news/adam-back-simpler-security-blockstream-bitcoin-custody-system?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Kraken parent Payward gains market share as slower trading weighs on earnings (11-14 06:01) — https://cointelegraph.com/news/kraken-parent-payward-gains-market-share-slower-trading-earnings?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Meta tests prediction market app using ‘cred’ points instead of cash: WSJ (11-14 05:55) — https://www.theblock.co/news/markets/2026-11-13-meta-tests-prediction-market-app-using-cred-points-instead-cash-wsj-440215
- [Cointelegraph] US regulators move ahead on crypto trust charters as Senate scrutiny grows (11-14 05:53) — https://cointelegraph.com/news/us-regulators-crypto-trust-charters-senate-scrutiny-grows?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] MEGA cuts 20% of workforce as former MegaETH Foundation restructures (11-14 04:26) — https://www.theblock.co/news/business/2026-11-13-megaeth-mega-layoffs-20-percent-restructuring-440206
- [The Block] House Oversight Chair calls for possible ban on government officials’ prediction market bets over insider trading concerns (11-14 04:09) — https://www.theblock.co/news/regulation/2026-11-13-house-oversight-chair-possible-ban-government-officials-prediction-market-bets-insider-trading-concerns-440207
- [The Block] CFTC’s Selig accuses states of trying to ‘lock up’ prediction market founders (11-14 03:51) — https://www.theblock.co/news/regulation/2026-11-13-cftcs-selig-accuses-states-trying-lock-up-prediction-market-founders-440199
- [CoinDesk] Bitcoin plunges to $68,000 as Anthropic IPO frenzy adds to market jitters (11-14 03:39) — https://www.coindesk.com/markets/2026/11/13/bitcoin-slides-to-usd68k-as-nvidia-turmoil-anthropic-ipo-fuel-broader-market-sell-off
- [Cointelegraph] Metaplanet swings to $170M loss as Bitcoin sale hits earnings (11-14 03:28) — https://cointelegraph.com/news/metaplanet-swings-170m-loss-bitcoin-sale-earnings?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] U.S. Senate Banking Committee races toward hearing on new SEC nominations (11-14 02:05) — https://www.coindesk.com/policy/2026/11/13/u-s-senate-banking-committee-races-toward-hearing-on-new-sec-nominations
- [Cointelegraph] Bitcoin holds below $70K as stocks slip despite a cooler US PPI print (11-14 01:39) — https://cointelegraph.com/markets/bitcoin-below-70k-stocks-slip-cooler-us-ppi-print?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Hyperliquid leapfrogs Bybit, Kraken and OKX in open interest as Q3 positions grow 80% (11-14 01:37) — https://www.theblock.co/news/markets/2026-11-13-hyperliquid-leapfrogs-bybit-kraken-okx-open-interest-q3-positions-grow-440053
- [CoinDesk] Bitcoin heads for sixth weekly loss as Anthropic’s blockbuster IPO looms (11-14 01:01) — https://www.coindesk.com/markets/2026/11/13/bitcoin-heads-for-sixth-weekly-loss-as-anthropic-s-blockbuster-ipo-looms
- [The Block] Kraken parent Payward posts 66% drop in Q3 adjusted EBITDA, plans US prediction markets and personal finance AI agent (11-14 00:31) — https://www.theblock.co/news/business/2026-11-13-kraken-parent-payward-posts-66-drop-in-q3-adjusted-ebitda-plans-us-prediction-markets-and-personal-finance-ai-agent-439721
- [The Block] Tether-backed Twenty One Capital reports $1.09 billion Q3 net income on bitcoin gains (11-13 23:50) — https://www.theblock.co/news/business/2026-11-13-tether-backed-twenty-one-capital-reports-1-09-billion-q3-net-income-on-bitcoin-gains-439711
- [The Block] Ethereum and Layer 1s Explained (11-13 23:12) — https://www.theblock.co/learn/campus/ethereum-and-layer-1s-explained-435883
- [CoinDesk] Kraken parent Payward says expansion outside crypto trading helps cushion revenue decline (11-13 23:02) — https://www.coindesk.com/business/2026/11/13/kraken-parent-payward-says-expansion-outside-crypto-trading-helps-cushion-revenue-decline
- [Cointelegraph] Arthur Hayes ‘flattered’ as Coinbase backs US stock perps (11-13 22:41) — https://cointelegraph.com/news/arthur-hayes-coinbase-us-stock-perps-cftc?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] From $6 to $6.9 million: Two dormant Bitcoin addresses wake up to move 100 BTC after more than 16 years (11-13 22:34) — https://www.theblock.co/news/markets/2026-11-13-from-6-to-6-9-million-two-dormant-bitcoin-addresses-wake-up-to-move-100-btc-after-more-than-16-years-439698
- [Cointelegraph] Nakamoto shares fall 6% premarket after Q3 revenue turns negative (11-13 22:04) — https://cointelegraph.com/markets/nakamoto-shares-fall-after-negative-q3-revenue?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] UK, Singapore, and Thailand central banks complete foreign exchange settlement trial linking traditional and tokenized systems (11-13 21:27) — https://www.theblock.co/news/regulation/2026-11-13-uk-singapore-and-thailand-central-banks-complete-foreign-exchange-settlement-trial-linking-traditional-and-tokenized-systems-439692
- [Cointelegraph] Israeli police arrest five in $5M WhatsApp crypto trading probe (11-13 21:19) — https://cointelegraph.com/news/israel-police-arrest-five-5m-whatsapp-crypto-scheme?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin's momentum gauge is turning red, could send prices back below $60,000 (11-13 21:14) — https://www.coindesk.com/daybook-us/2026/11/13/bitcoin-s-momentum-gauge-is-turning-red-could-send-prices-back-below-usd60-000
- [CoinDesk] Bitcoin hits 12-week low as dollar rallies on interest-rate outlook, liquidations top $1.6 billion (11-13 20:52) — https://www.coindesk.com/markets/2026/11/13/bitcoin-hits-12-week-low-as-dollar-rallies-on-interest-rate-outlook-liquidations-top-usd1-6-billion
- [The Block] Thailand seeks $148,000 daily cap on certain stablecoin transfers to curb money laundering (11-13 19:16) — https://www.theblock.co/news/regulation/2026-11-13-thailand-seeks-daily-stablecoin-cap-439676
- [The Block] JPMorgan reports 36% rise in Strategy share holdings and $540 million in BlackRock’s bitcoin ETF (11-13 18:59) — https://www.theblock.co/news/business/2026-11-13-jpmorgan-reports-36-rise-in-strategy-share-holdings-and-540-million-in-blackrocks-bitcoin-etf-439671
- [Cointelegraph] Unocoin keeps deposits and withdrawals halted over suspect transfers (11-13 18:58) — https://cointelegraph.com/news/unocoin-withdrawals-halted-bitgo-wallet-transfer-probe?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin returns to 200-week trend line as analyst sees risk of $57.7K next (11-13 18:39) — https://cointelegraph.com/markets/bitcoin-returns-200-week-trend-line-analyst-sees-risk-57k-next?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] DOJ, CFTC sue Arkansas to block state enforcement action against Kalshi (11-13 18:32) — https://www.theblock.co/news/regulation/2026-11-13-doj-cftc-sue-arkansas-to-block-state-enforcement-action-against-kalshi-439669
- [Cointelegraph] DOJ moves to seize $1.2B from Binance hack, disrupts FaceStealer scam (11-13 18:27) — https://cointelegraph.com/news/doj-12b-north-korean-crypto-seizure-400m-facestealer-scheme?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Live updates: Bitcoin eyes bear market lows as late summer rally mostly wiped out (11-13 18:16) — https://www.coindesk.com/tech/2026/11/13/live-news-bitcoin-drops-below-200-week-moving-average-as-dollar-strength-pressures-risk-assets
- [Cointelegraph] Jane Street boosts Fidelity Bitcoin ETF holdings nearly 8x, trims IBIT (11-13 18:05) — https://cointelegraph.com/news/jane-street-add-fidelity-bitcoin-etf-ibit-cut-q3-2026?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

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