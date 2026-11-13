# 코인 데일리 스냅샷

- 수집 시각: 2026-11-13 16:04 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 -18.1 / 3일 평균 -15.2 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | -62.5 |
| 파생·심리 | 30% | 0.0 |
| 밸류에이션 | 25% | 25.0 |
| 매크로 | 15% | -37.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.71 |
| 밸류에이션 | 가격÷STH-RP | +0 | +0 | 가격÷STH-RP 1.002 |
| 수급 | 현물 ETF 순유입 | -2 | -2 | 5거래일 연속 순유출 |
| 수급 | 거래소 순유입(7일) | -1 | -1 | 7일 순유입 분포 70백분위 |
| 수급 | 거래소 보유량(30일) | -1 | -1 | 30일 +1.75% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | -1 | -1 | 7일 +7.8% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0089% |
| 파생·심리 | RSI(14) | +2 | +1 | RSI 29.8 |
| 파생·심리 | 롱/숏 비율 | -2 | -1 | 롱/숏 분포 100백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +0 | OI 7일 +7.2%, 가격 -6.0% |
| 파생·심리 | 옵션 스큐 | -1 | +0 | +4.34 (풋 우위 확대, 전일 +3.52) |
| 매크로 | 나스닥 | -1 | -1 | 50일선 아래 |
| 매크로 | DXY | -1 | -1 | 103.14, 20일 +1.3% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 159.83 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -4 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 25366.09 | 25466.189 | pt | 2026-11-12 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | 4.32 | -1.05 | % | 2026-11-12 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26379.03 | 26396.06 | pt | 2026-11-12 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 103.142 | 103.17 | pt | 2026-11-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.28 | 1.0 | % | 2026-11-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 159.831 | 159.734 | 엔 | 2026-11-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | 1.48 | 0.96 | % | 2026-11-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.08 | 4.02 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.87 | 2.79 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.65 | 3.44 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.12 | 3.03 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -4 | -4 |  | 2026-11-13 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 7.471 | 7.116 | % | 2026-11-13 06:59 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.3529 | 2.4668 | 조$ | 2026-11-13 06:59 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | -299.9 | -95.0 | 백만$ | 2026-11-11 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 5거래일 연속 순유출 / 집계 기준일 2026-11-11 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -269.7 | -78.2 | 백만$ | 2026-11-11 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -1438.1 | -1063.6 | 백만$ | 2026-11-11 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | -5 | -4 | 일 | 2026-11-11 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 71369.9 | 73927.63 | USD | 2026-11-12 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 29.78 | 35.22 |  | 2026-11-12 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -6.05 | -8.08 | % | 2026-11-12 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.87 | 3.85 | 십억$ | 2026-11-12 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | 7.16 | 0.31 | % | 2026-11-12 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 3.24 | 3.2 | 배 | 2026-11-12 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 100.0 | 83.3 | 백분위 | 2026-11-12 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.01 | 0.0074 | % | 2026-11-13 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0089 | 0.0067 | % | 2026-11-13 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 39.09 | 38.87 |  | 2026-11-13 07:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 4.34 | 3.52 | vol pt | 2026-11-13 07:04 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-12-04, 콜 BTC-4DEC26-74000-C / 풋 BTC-4DEC26-65000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.7132 | 0.7153 |  | 2026-11-06 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.0015 | 1.0016 |  | 2026-11-06 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 71174.0 | 73688.0 | $ | 2026-11-06 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 71280.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 26241.0 | 28624.0 | BTC | 2026-11-12 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 27150.7 | 22570.2 | BTC | 2026-11-12 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -6738.7 | -4496.9 | BTC | 2026-11-12 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 70.0 | 74.4 | 백분위 | 2026-11-12 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -909.7 | 6053.8 | BTC | 2026-11-12 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | 1.75 | 1.69 | % | 2026-11-12 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2723131.0 | 2719874.0 | BTC | 2026-11-12 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (11-12 18:00 ~ 11-13 16:04 KST)

피드 상태: CoinDesk: 22건 / The Block: 20건 / Cointelegraph: 22건 / 블록미디어: 10건

- [블록미디어] [마감 시황] 젠슨황 여파, 삼전닉스 동반 하락 (11-13 16:04) — https://www.blockmedia.co.kr/archives/1165520?utm_source=general&utm_medium=rss
- [블록미디어] 미국 재무부, 국채 5억5600만달러 바이백…비트코인 반등에는 영향 제한적 (11-13 16:00) — https://www.blockmedia.co.kr/archives/1165470?utm_source=general&utm_medium=rss
- [블록미디어] 디지털자산 과세가 유예되면 무엇을 사야 할까? (11-13 15:45) — https://www.blockmedia.co.kr/archives/1165463?utm_source=general&utm_medium=rss
- [The Block] Bitcoin tumbles below $69,000 as Nvidia turmoil adds to Fed-driven market jitters (11-13 15:23) — https://www.theblock.co/news/markets/2026-11-13-bitcoin-tumbles-below-69000-439643
- [Cointelegraph] Here’s what happened in crypto today (11-13 15:16) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin firm Nakamoto owes Kraken $165 million, more than its entire market value (11-13 15:03) — https://www.coindesk.com/markets/2026/11/13/bitcoin-firm-nakamoto-owes-kraken-usd165-million-more-than-its-entire-market-value
- [Cointelegraph] Bitcoin slides below $70K amid thin liquidity, ETF outflows (11-13 15:00) — https://cointelegraph.com/markets/bitcoin-falls-below-70k-crypto-extreme-fear?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 비트코인 7만달러 깨지자 피터 시프 “5년 전 가격으로 회귀…장기 약세장 진입” (11-13 15:00) — https://www.blockmedia.co.kr/archives/1165457?utm_source=general&utm_medium=rss
- [CoinDesk] Bitcoin ETFs are now down over $1.5 billion in net outflows for the year (11-13 14:45) — https://www.coindesk.com/markets/2026/11/13/bitcoin-etfs-are-now-down-over-usd1-5-billion-in-net-outflows-for-the-year
- [블록미디어] 비트코인 7만달러 붕괴에 엇갈린 전망…”6만5000달러 추락” vs “마지막 투매” (11-13 14:30) — https://www.blockmedia.co.kr/archives/1165449?utm_source=general&utm_medium=rss
- [블록미디어] 젠슨 황의 마지막 “난 완전히 X됐다”… 트럼프 “끝까지 싸우라” (11-13 14:22) — https://www.blockmedia.co.kr/archives/1165452?utm_source=general&utm_medium=rss
- [CoinDesk] SpaceX-Tesla merger talks put 30,000 bitcoin back in focus (11-13 14:08) — https://www.coindesk.com/markets/2026/11/13/spacex-tesla-merger-talks-put-30-000-bitcoin-back-in-focus
- [The Block] TRM Labs launches new service to help police seize stolen crypto in minutes (11-13 14:08) — https://www.theblock.co/news/defi/2026-11-13-trm-labs-beacon-concierge-439609
- [The Block] White House sends crypto-relevant picks to fill SEC and CFTC seats (11-13 13:56) — https://www.theblock.co/news/regulation/2026-11-12-white-house-crypto-picks-sec-cftc-439175
- [블록미디어] 비트코인, ‘심리적 지지선’ 7만달러 3개월 만 붕괴…롱 6.8억달러 ‘폭풍 청산’ (11-13 13:32) — https://www.blockmedia.co.kr/archives/1165420?utm_source=general&utm_medium=rss
- [The Block] Bitcoin falls to 12-week low, Strategy and Metaplanet to lose MSCI index membership, and more (11-13 13:20) — https://www.theblock.co/newsletters/the-daily/2026-11-12-bitcoin-12-week-low-strategy-metaplanet-msci-more-crypto-news-439049
- [블록미디어] 미 법무부, 바이낸스 해킹 자금 12억달러 압수·동결 승인…북한 자금줄 차단 (11-13 13:15) — https://www.blockmedia.co.kr/archives/1165405?utm_source=general&utm_medium=rss
- [블록미디어] 스텔라에 자산 50억달러 쌓였는데 XLM은 14센트…XRP 못 따라가는 이유 (11-13 13:00) — https://www.blockmedia.co.kr/archives/1165290?utm_source=general&utm_medium=rss
- [CoinDesk] Bitcoin dips below $70,000 as Dollar Index hits 19-month high (11-13 12:37) — https://www.coindesk.com/markets/2026/11/13/bitcoin-dips-below-usd70-000-as-selloff-gathers-pace
- [블록미디어] 미국 법무부·월가, 일리노아주 디지털자산 과세 반대 공동전선 (11-13 12:35) — https://www.blockmedia.co.kr/archives/1165395?utm_source=general&utm_medium=rss
- [Cointelegraph] Trump nominates Hester Peirce successor among SEC, CFTC picks (11-13 11:29) — https://cointelegraph.com/news/trump-nominates-hester-peirce-successor-among-sec-cftc-picks?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Former Nvidia CEO Huang had third alleged affair: Reuters (11-13 10:26) — https://cointelegraph.com/news/former-nvidia-ceo-huang-had-third-alleged-affair-reuters?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Gemini’s quarterly retail trading volume sinks to 3-year low (11-13 09:52) — https://cointelegraph.com/markets/geminis-quarterly-retail-trading-volume-sinks-to-3-year-low?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Maple Finance’s strategy rift sends co-founder, COO to the exits (11-13 08:12) — https://cointelegraph.com/news/maple-finance-strategy-rift-co-founder-coo-exit?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] North Korea's Binance hack faces U.S. crackdown as DOJ targets $1.2 billion in stolen crypto (11-13 07:55) — https://www.coindesk.com/policy/2026/11/12/north-korea-s-binance-hack-faces-u-s-crackdown-as-doj-targets-usd1-2-billion-in-stolen-crypto
- [CoinDesk] U.S. President Trump names CFTC, SEC nominees for first time in a year (11-13 07:47) — https://www.coindesk.com/policy/2026/11/12/u-s-president-names-cftc-sec-nominees-for-first-time-in-a-year
- [The Block] DOJ moves to seize $1.2 billion from Binance hack, disrupts North Korean deepfake scheme (11-13 07:40) — https://www.theblock.co/news/business/2026-11-12-doj-seize-1-2-billion-binance-hack-north-korea-facestealer-439065
- [Cointelegraph] NK hackers join memecoin trenches, xStocks adds Hong Kong equities: Asia Express (11-13 07:29) — https://cointelegraph.com/magazine/nk-hackers-join-memecoin-trenches-xstocks-adds-hong-kong-equities-asia-express?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Gemini trading volume drops 73% as Q3 revenue falls to $41 million (11-13 07:18) — https://www.theblock.co/news/markets/2026-11-12-gemini-trading-volume-drops-q3-revenue-falls-to-41-million-439050
- [Cointelegraph] Kalshi ends Donald Trump Jr. advisory role over Polymarket investment: Reuters (11-13 07:05) — https://cointelegraph.com/news/kalshi-ends-donald-trump-jr-advisory-role-polymarket-investment?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Strategy stock sheds 5% amid MSCI index removal, Bitcoin sell-off (11-13 06:52) — https://cointelegraph.com/markets/strategy-shares-fall-5-msci-index-removal-bitcoin?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Louisiana sues Kalshi, Robinhood and other prediction markets in escalating regulatory fight (11-13 06:44) — https://www.theblock.co/news/regulation/2026-11-12-louisiana-sues-kalshi-robinhood-other-prediction-markets-escalating-regulatory-fight-439052
- [CoinDesk] Kalshi ends Donald Trump Jr.’s advisory contract over 1789 Capital’s Polymarket investment (11-13 06:07) — https://www.coindesk.com/policy/2026/11/12/kalshi-ends-donald-trump-jr-s-advisory-contract-over-1789-capital-s-polymarket-investment
- [Cointelegraph] US Justice Department, business groups and DeFi firms challenge Illinois crypto tax (11-13 05:58) — https://cointelegraph.com/news/us-justice-department-business-groups-defi-illinois-crypto-tax?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] DTCC Plans Solana Expansion as Wallet Rules Limit Access (11-13 05:07) — https://cointelegraph.com/news/dtcc-plans-solana-expansion-wallet-rules-limit-access?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Avalanche Owns Five Percent of Tokenized Stocks (11-13 05:02) — https://www.theblock.co/newsletters/tokenization-briefing/2026-11-12-avalanche-owns-five-percent-tokenized-stocks-437310
- [The Block] NYDFS sets fresh advertising standards for crypto firms (11-13 03:03) — https://www.theblock.co/news/regulation/2026-11-12-nydfs-sets-fresh-advertising-standards-crypto-firms-439014
- [The Block] Bitcoin falls to 12-week low as Jensen Huang’s exit from Nvidia rattles markets (11-13 02:40) — https://www.theblock.co/news/markets/2026-11-12-bitcoin-12-week-low-jensen-huang-exit-nvidia-438992
- [The Block] Exodus’ ‘cost reset is real’ as payments offset crypto wallet slowdown, StoneX says (11-13 01:55) — https://www.theblock.co/news/markets/2026-11-12-exodus-cost-reset-real-payments-offset-crypto-wallet-slowdown-stonex-438988
- [CoinDesk] Illinois crypto tax is impossible to enforce as written, crypto industry tells court (11-13 01:45) — https://www.coindesk.com/policy/2026/11/12/illinois-crypto-tax-is-impossible-to-enforce-as-written-crypto-industry-tells-court
- [The Block] Visa adds Western Union’s USDPT stablecoin to its settlement network in Anchorage tie-up (11-13 01:00) — https://www.theblock.co/news/business/2026-11-12-visa-adds-western-unions-usdpt-stablecoin-to-its-settlement-network-in-anchorage-tie-up-438520
- [Cointelegraph] Bitcoin slides toward $71K as Nvidia stock tumbles after Huang steps down (11-13 00:46) — https://cointelegraph.com/markets/bitcoin-price-drops-71k-stocks-nvidia-huang-resignation?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] DTCC adds Solana to Wall Street tokenization plans, targeting 2027 rollout (11-13 00:45) — https://www.coindesk.com/business/2026/11/12/dtcc-adds-solana-to-wall-street-tokenization-plans-targeting-2027-rollout
- [The Block] Unocoin ‘login suspension’ continues as exchange flags outgoing BitGo ETH transactions (11-13 00:36) — https://www.theblock.co/news/ecosystems/2026-11-12-unocoin-login-suspension-continues-as-exchange-flags-outgoing-bitgo-eth-transactions-438654
- [CoinDesk] Crypto for Advisors: The blockchain built to run financial markets (11-13 00:34) — https://www.coindesk.com/coindesk-indices/2026/11/12/crypto-for-advisors-the-blockchain-built-to-run-financial-markets
- [The Block] Tether Gold issuer follows USDT to complete Big Four audit (11-13 00:23) — https://www.theblock.co/news/business/2026-11-12-tether-gold-issuer-follows-usdt-to-complete-big-four-audit-438849
- [The Block] Andreessen Horowitz, DeFi Education Fund push back against Illinois crypto tax (11-13 00:01) — https://www.theblock.co/news/regulation/2026-11-12-andreessen-horowitz-defi-education-fund-push-back-against-illinois-crypto-tax-438573
- [CoinDesk] Jupiter adds Anchorage-backed USDGO to its $1 billion Solana lending platform (11-12 23:45) — https://www.coindesk.com/business/2026/11/12/jupiter-adds-anchorage-backed-usdgo-to-its-usd1-billion-solana-lending-platform
- [CoinDesk] The next Congress will write rules for AI and emerging tech. They should use the stuff first. (11-12 23:24) — https://www.coindesk.com/opinion/2026/11/12/the-next-congress-will-write-rules-for-ai-and-emerging-tech-they-should-use-the-stuff-first
- [The Block] DTCC plans to bring tokenized securities to Solana in second half of 2027 (11-12 23:23) — https://www.theblock.co/news/business/2026-11-12-dtcc-plans-bring-tokenized-securities-solana-second-half-of-2027-438559
- [The Block] Securitize and Ethena’s $100 million BlackRock BUIDL liquidity facility goes live (11-12 23:00) — https://www.theblock.co/news/ecosystems/2026-11-12-securitize-ethena-buidl-liquidity-facility-live-usdc-438442
- [The Block] SoFiUSD goes live on Polygon as bank-issued stablecoin expands reach (11-12 23:00) — https://www.theblock.co/news/ecosystems/2026-11-12-sofiusd-goes-live-on-polygon-as-bank-issued-stablecoin-expands-reach-438542
- [Cointelegraph] Jensen Huang resigns as Nvidia CEO, exits board; shares plunge (11-12 22:59) — https://cointelegraph.com/news/jensen-huang-resigns-nvidia-ceo-board-member?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Nvidia CEO Huang quits company he co-founded, led for 3 decades. Shares slump (11-12 22:57) — https://www.coindesk.com/markets/2026/11/12/nvidia-shares-plunge-10-as-jensen-huang-resigns
- [Cointelegraph] Bit Digital stock falls 5% in pre-market after Q3 revenue miss (11-12 22:52) — https://cointelegraph.com/news/bit-digital-stock-falls-q3-revenue-miss?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Thailand proposes $148K daily cap on stablecoin deposits and withdrawals (11-12 22:44) — https://cointelegraph.com/news/thailand-tighter-stablecoin-rules-crypto-exchange?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Crypto hack losses equal 57 cents per $1 earned onchain: Ark’s Valente (11-12 22:31) — https://cointelegraph.com/news/crypto-hackers-stole-57-cents-every-1-earned-ark?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Are Alt-L1s over? Security, costs drive smaller chains to Ethereum (11-12 22:30) — https://cointelegraph.com/magazine/are-alt-l1s-over-security-costs-drive-smaller-chains-to-ethereum?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Uber’s UK banking partner Griffin raises $20M for stablecoin services (11-12 22:21) — https://cointelegraph.com/news/digital-bank-griffin-100m-valuation-card-stablecoin?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] BNY taps Figment to support staking on its digital asset custody platform (11-12 22:05) — https://www.theblock.co/news/business/2026-11-12-bny-taps-figment-to-support-staking-on-its-digital-asset-custody-platform-438538

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