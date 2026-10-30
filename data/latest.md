# 코인 데일리 스냅샷

- 수집 시각: 2026-10-30 15:16 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 17.5 / 3일 평균 -0.1 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | 50.0 |
| 파생·심리 | 30% | 0.0 |
| 밸류에이션 | 25% | 25.0 |
| 매크로 | 15% | -25.0 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.89 |
| 밸류에이션 | 가격÷STH-RP | +0 | +0 | 가격÷STH-RP 1.067 |
| 수급 | 현물 ETF 순유입 | +2 | +1 | 3거래일 연속 순유입 |
| 수급 | 거래소 순유입(7일) | +1 | +0 | 7일 순유입 분포 21백분위 |
| 수급 | 거래소 보유량(30일) | +1 | +0 | 30일 -0.96% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | +0 | -1 | 7일 +2.2% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0077% |
| 파생·심리 | RSI(14) | +1 | +0 | RSI 35.9 |
| 파생·심리 | 롱/숏 비율 | -2 | -2 | 롱/숏 분포 100백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +0 | OI 7일 +5.1%, 가격 -4.3% |
| 파생·심리 | 옵션 스큐 | +0 | -1 | +2.13 |
| 매크로 | 나스닥 | -1 | -1 | 50일선 아래 |
| 매크로 | DXY | +0 | -1 | 101.81, 20일 -0.1% |
| 매크로 | USD/JPY | +0 | +0 | 157.60 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -3 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 26184.721 | 26549.85 | pt | 2026-10-29 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | 0.68 | -0.57 | % | 2026-10-29 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26586.75 | 26589.67 | pt | 2026-10-29 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 101.808 | 102.04 | pt | 2026-10-30 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | -0.12 | 0.16 | % | 2026-10-30 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 157.602 | 157.833 | 엔 | 2026-10-30 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | 0.71 | -0.17 | % | 2026-10-30 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.02 | 3.71 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-10-14 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.79 | 2.76 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-10-14 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.65 | 3.44 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.12 | 3.03 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -3 | -2 |  | 2026-10-30 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.786 | 6.679 | % | 2026-10-30 06:11 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.651 | 2.6986 | 조$ | 2026-10-30 06:11 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | 137.3 | 176.0 | 백만$ | 2026-10-28 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 3거래일 연속 순유입 / 집계 기준일 2026-10-28 |
| B.자금흐름 | IBIT(블랙록) 순유입 | 136.0 | 151.5 | 백만$ | 2026-10-28 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -349.8 | 41.3 | 백만$ | 2026-10-28 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | 3 | 2 | 일 | 2026-10-28 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 77780.33 | 81249.31 | USD | 2026-10-29 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 35.87 | 47.59 |  | 2026-10-29 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -4.34 | -3.3 | % | 2026-10-29 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.54 | 3.47 | 십억$ | 2026-10-29 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | 5.11 | -1.76 | % | 2026-10-29 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 2.47 | 1.75 | 배 | 2026-10-29 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 100.0 | 96.7 | 백분위 | 2026-10-29 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.01 | 0.0096 | % | 2026-10-30 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0077 | 0.0089 | % | 2026-10-30 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 38.07 | 36.52 |  | 2026-10-30 06:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 2.13 | 3.27 | vol pt | 2026-10-30 06:17 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-11-27, 콜 BTC-27NOV26-85000-C / 풋 BTC-27NOV26-74000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.8918 | 0.9074 |  | 2026-10-23 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.0671 | 1.0739 |  | 2026-10-23 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 73277.0 | 75647.0 | $ | 2026-10-23 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 78193.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 22395.0 | 19977.3 | BTC | 2026-10-29 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 45976.0 | 16140.2 | BTC | 2026-10-29 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -26008.7 | -5027.5 | BTC | 2026-10-29 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 21.1 | 64.4 | 백분위 | 2026-10-29 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -23581.0 | 3837.1 | BTC | 2026-10-29 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -0.96 | -0.02 | % | 2026-10-29 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2660348.0 | 2683288.0 | BTC | 2026-10-29 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (10-29 18:00 ~ 10-30 15:16 KST)

피드 상태: CoinDesk: 25건 / The Block: 8건 / Cointelegraph: 29건 / 블록미디어: 10건

- [블록미디어] 바이낸스 해커, 첫 자산 탈취 시도는 실패…”XRP 지갑 미개설로 4275만달러 송금 무산” (10-30 15:10) — https://www.blockmedia.co.kr/archives/1158993?utm_source=general&utm_medium=rss
- [블록미디어] 1인치, 바이낸스 보안 사고 연루 지갑 차단…“탈취된 1INCH 토큰 동결 불가” (10-30 15:08) — https://www.blockmedia.co.kr/archives/1159006?utm_source=general&utm_medium=rss
- [블록미디어] 바이낸스 · 비트겟 탈취 자금 한곳에…잭XBT “해킹 배후 같을 가능성” (10-30 15:06) — https://www.blockmedia.co.kr/archives/1159024?utm_source=general&utm_medium=rss
- [Cointelegraph] Here’s what happened in crypto today (10-30 15:00) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 강형구 교수 “디지털자산 기본법 제정이 우선, 코인 과세 시점 다시 정해야” (10-30 14:57) — https://www.blockmedia.co.kr/archives/1158978?utm_source=general&utm_medium=rss
- [Cointelegraph] Strategy eyes more Bitcoin buys as Saylor touts $30B credit capacity (10-30 14:53) — https://cointelegraph.com/news/strategy-30-billion-digital-credit-capacity-bitcoin-buys?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] North Korea’s TraderTraitor linked to $6.3B Binance hack (10-30 14:51) — https://cointelegraph.com/news/north-korea-linked-to-63b-binance-hack-by-crypto-investigators?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 미래에셋증권 뉴욕법인, DTCC 토큰화 서비스 참여 (10-30 14:50) — https://www.blockmedia.co.kr/archives/1159002?utm_source=general&utm_medium=rss
- [CoinDesk] XRP Ledger developers tighten the rules for who can hold 'restricted' tokens (10-30 14:45) — https://www.coindesk.com/tech/2026/10/30/xrp-ledger-developers-tighten-the-rules-for-who-can-hold-restricted-tokens
- [CoinDesk] Binance hack bites India's largest crypto exchange as it curbs futures trading (10-30 14:43) — https://www.coindesk.com/markets/2026/10/30/coindcx-halts-new-crypto-futures-bets-as-binance-incident-disrupts-liquidity
- [블록미디어] 바이낸스 해킹 여파에 에테나 긴급 준비금 증명…”USDe 담보비율 101% 이상” (10-30 14:30) — https://www.blockmedia.co.kr/archives/1158983?utm_source=general&utm_medium=rss
- [CoinDesk] Binance hacker splits $1.4 billion of bitcoin into 19 wallets that no one can freeze (10-30 13:50) — https://www.coindesk.com/markets/2026/10/30/binance-hacker-splits-usd1-4-billion-of-bitcoin-into-19-wallets-that-no-one-can-freeze
- [블록미디어] 바이낸스 “48시간 내 출금 재개”…입금은 정상 운영 (10-30 13:50) — https://www.blockmedia.co.kr/archives/1158970?utm_source=general&utm_medium=rss
- [블록미디어] 바이낸스 63억달러 해킹, 이더리움 ‘EIP-7702’ 악용…토큰 63종 · ETH 16만7464개 인출 (10-30 13:35) — https://www.blockmedia.co.kr/archives/1158931?utm_source=general&utm_medium=rss
- [블록미디어] 바이낸스 해커 매도 의혹 속 STRK 10% 급락… 숏 투자자 446만달러 평가익 (10-30 13:10) — https://www.blockmedia.co.kr/archives/1158844?utm_source=general&utm_medium=rss
- [CoinDesk] $6 billion Binance hack sends bitcoin, ether tumbling; Standard Chartered expects more pain (10-30 13:00) — https://www.coindesk.com/markets/2026/10/30/usd6-billion-binance-hack-sends-bitcoin-ether-tumbling-standard-chartered-sees-more-losses-ahead
- [CoinDesk] Institutional crypto investors rush to pull funds from exchanges after Binance hack (10-30 12:56) — https://www.coindesk.com/markets/2026/10/30/institutional-crypto-investors-rush-to-pull-funds-from-exchanges-after-binance-hack
- [Cointelegraph] Binance hack could accelerate shift to DEXs: Standard Chartered (10-30 12:47) — https://cointelegraph.com/news/binance-hack-could-accelerate-shift-to-dexs-standard-chartered?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 바이낸스 해킹 배후에 ‘북한 라자루스’ 의혹 부상…4월 켈프다오 해킹과 연관설도 (10-30 12:40) — https://www.blockmedia.co.kr/archives/1158918?utm_source=general&utm_medium=rss
- [CoinDesk] Crypto's longtime foe, North Korea's Lazarus Group, likely behind Binance hack: blockchain sleuths (10-30 12:36) — https://www.coindesk.com/policy/2026/10/29/crypto-s-longtime-foe-north-korea-s-lazarus-group-likely-behind-binance-hack-blockchain-sleuths
- [The Block] Bitcoin slides below $77,000, BNB drops amid Binance hack (10-30 11:22) — https://www.theblock.co/news/markets/2026-10-29-bitcoin-slides-below-77000-binance-hack-432183
- [CoinDesk] Binance hack drained wallets backing customer assets, reserve data shows (10-30 09:17) — https://www.coindesk.com/business/2026/10/30/binance-hack-drained-wallets-backing-customer-assets-reserve-data-shows
- [Cointelegraph] Binance points to engineer’s hacked laptop in $6.3B breach (10-30 09:11) — https://cointelegraph.com/news/binance-hack-may-involve-private-key-misuse-not-theft-blockaid-ceo?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Binance hack rattles markets as BNB falls 8%, Bitcoin nears $77K (10-30 08:24) — https://cointelegraph.com/markets/binance-hack-rattles-crypto-markets-bnb-bitcoin-slide?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Tampered Ledger reported in Singapore a month before news broke: Asia Express (10-30 07:31) — https://cointelegraph.com/magazine/tampered-ledger-reported-in-singapore-a-month-before-news-broke-asia-express?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Binance investigating hack as suspicious outflows reach up to $5.8 billion (10-30 06:49) — https://www.theblock.co/news/markets/2026-10-29-binance-investigating-hack-suspicious-outflows-5-billion-432171
- [Cointelegraph] Live updates: Binance $6.3B hack linked to North Korea’s TraderTraitor (10-30 06:24) — https://cointelegraph.com/news/binance-linked-wallet-faces-possible-exploit-blockchain-researcher-warns?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Binance loses over $6 billion in 'biggest crypto hack in history' (10-30 06:12) — https://www.coindesk.com/business/2026/10/29/potential-multi-billion-binance-hack-hitting-crypto-markets
- [The Block] Strategy reports $19.5 billion in Q3 net income as preferred shareholders approve daily dividends (10-30 05:58) — https://www.theblock.co/news/business/2026-10-29-strategy-q3-net-income-preferred-daily-dividends-432141
- [Cointelegraph] Public companies double share of blockchain revenue since 2022: Report (10-30 04:53) — https://cointelegraph.com/news/public-companies-double-share-of-blockchain-revenue-since-2022-report?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Polymarket suspended trading amid reports of user funds being drained (10-30 04:23) — https://cointelegraph.com/news/polymarket-suspends-trading-user-funds-compromised?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Polymarket resumes trading after $2.65 million exploit, says third-party provider was compromised (10-30 04:00) — https://www.theblock.co/news/defi/2026-10-29-polymarket-exploit-2-5-million-cancel-only-mode-432158
- [CoinDesk] Polymarket suspends trading after third-party breach leads to user losses (10-30 03:55) — https://www.coindesk.com/markets/2026/10/29/polymarket-suspends-trading-after-third-party-breach-leads-to-user-losses
- [Cointelegraph] HYPE teases all-time high as NYSE owner ICE eyes US Hyperliquid perps (10-30 02:12) — https://cointelegraph.com/markets/hype-price-all-time-high-ice-us-hyperliquid-perps?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] KuCoin suspends services in Russia and Belarus (10-30 02:08) — https://cointelegraph.com/news/kucoin-services-russia-belarus-suspended?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Stanley Druckenmiller's first X post backs Hyperliquid venture after $23 million indirect investment (10-30 02:04) — https://www.coindesk.com/business/2026/10/29/stanley-druckenmiller-s-first-x-post-backs-hyperliquid-venture-after-usd23-million-indirect-investment
- [CoinDesk] KuCoin exits Russia and Belarus as crypto exchanges withdraw from Western-sanctioned markets (10-30 01:51) — https://www.coindesk.com/policy/2026/10/29/kucoin-exits-russia-and-belarus-as-crypto-exchanges-withdraw-from-western-sanctioned-markets
- [CoinDesk] From rivals to partners: Polygon and Solana team to bring stablecoin payments to banks (10-30 01:35) — https://www.coindesk.com/business/2026/10/29/from-rivals-to-partners-polygon-and-solana-team-to-bring-stablecoin-payments-to-banks
- [Cointelegraph] Nasdaq-listed Canton Strategic Holdings plans tokenized stock trading from Nov. 2 (10-30 01:27) — https://cointelegraph.com/news/canton-strategic-holdings-tokenized-stock-trading-november-2026?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Crypto exchange HTX exits the UK after settling with the FCA (10-30 01:11) — https://www.coindesk.com/policy/2026/10/29/crypto-exchange-htx-exits-the-uk-after-settling-with-the-fca
- [Cointelegraph] Kalshi raises $1B at $40B valuation as non-sports revenue run rate tops $1B (10-30 00:52) — https://cointelegraph.com/news/kalshi-closes-1b-funding-round-at-40b-valuation-as-non-sports-revenue-run-rate-tops-1b?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin price jumps to $81.5K as US GDP data beats expectations (10-30 00:39) — https://cointelegraph.com/markets/bitcoin-reaction-to-pce-data?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] French Senate adopts bill for automatic sharing of crypto tax data (10-30 00:00) — https://cointelegraph.com/news/french-senate-adopts-bill-automatic-crypto-tax-data?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Polymarket brings ultra-short crypto prediction markets to U.S. platform (10-29 23:55) — https://www.coindesk.com/markets/2026/10/29/polymarket-brings-ultra-short-crypto-prediction-markets-to-u-s-platform
- [The Block] HYPE surges 15% as NYSE parent ICE moves to bring Hyperliquid perps to US (10-29 23:44) — https://www.theblock.co/news/business/2026-10-29-ice-tradexyz-hyperliquid-perpetual-futures-us-432132
- [CoinDesk] Crypto for Advisors: Only 1 in 5 Americans say the financial system is secure (10-29 23:39) — https://www.coindesk.com/coindesk-indices/2026/10/29/crypto-for-advisors-only-1-in-5-americans-say-the-financial-system-is-secure
- [The Block] Uniswap Labs opens fee conversion tool TJAR to apps, starting with Robinhood (10-29 23:34) — https://www.theblock.co/news/defi/2026-10-29-uniswap-token-jar-tjar-robinhood-432131
- [Cointelegraph] Bank of England opens consultation on tokenized collateral for clearing (10-29 23:27) — https://cointelegraph.com/news/bank-of-england-opens-consultation-on-tokenized-collateral-for-clearing?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Why Switzerland’s first genuine spot bitcoin ETF could soon attract overseas banks and brokers (10-29 23:15) — https://www.coindesk.com/business/2026/10/29/switzerland-s-first-bitcoin-etf-gets-rare-exemption-will-open-to-overseas-brokers
- [CoinDesk] Chainlink adds weekend pricing for tokenized assets, with Aave as launch partner (10-29 23:15) — https://www.coindesk.com/tech/2026/10/28/chainlink-adds-weekend-pricing-for-tokenized-assets-with-aave-as-launch-partner
- [Cointelegraph] Canton Foundation grants RedStone 15.8M Canton Coin for pricing standard (10-29 23:00) — https://cointelegraph.com/news/canton-foundation-redstone-coin-pricing-standard?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] New quantum model slashes hardware needed to break bitcoin keys by 17 times (10-29 22:55) — https://www.coindesk.com/tech/2026/10/29/new-quantum-model-slashes-hardware-needed-to-break-bitcoin-keys-by-17-times
- [CoinDesk] Walmart, Eli Lilly join growing pushback against OKX–ICE tokenized stock plans (10-29 22:39) — https://www.coindesk.com/business/2026/10/29/walmart-eli-lilly-join-growing-pushback-against-okx-ice-tokenized-stock-plans
- [Cointelegraph] Brazil’s Halloween eve crypto deadline brings more tricks than treats (10-29 22:30) — https://cointelegraph.com/news/brazil-crypto-license-filing-deadline-hurdles-uncertainty?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Private, fast USDT is coming to Bitcoin. Can it compete with Ethereum and Tron? (10-29 22:30) — https://cointelegraph.com/magazine/private-fast-usdt-is-coming-to-bitcoin-can-it-compete-with-ethereum-and-tron?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Polygon adds Solana to payment stack linking bank accounts, crypto and payouts (10-29 22:00) — https://www.theblock.co/news/defi/2026-10-29-polygon-adds-solana-payment-stack-432115
- [Cointelegraph] Polygon expands Open Money Stack to Solana, after Tron rollout (10-29 22:00) — https://cointelegraph.com/news/polygon-brings-open-money-stack-payments-services-to-solana?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] A new framework for tokenized asset tracking (10-29 21:57) — https://www.coindesk.com/opinion/2026/10/28/a-new-framework-for-tokenized-asset-tracking
- [CoinDesk] Tokenized stock venue on Canton could beat OKX–ICE to first trade under SEC framework (10-29 21:51) — https://www.coindesk.com/business/2026/10/29/tokenized-stock-venue-on-canton-could-beat-okx-ice-to-first-trade-under-sec-framework
- [Cointelegraph] Chainalysis traces North Korean crypto cash-outs through Garantex (10-29 21:38) — https://cointelegraph.com/news/chainalysis-dprk-crypto-cash-out-network-ofac-sanctions?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

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