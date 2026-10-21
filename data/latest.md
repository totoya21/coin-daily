# 코인 데일리 스냅샷

- 수집 시각: 2026-10-21 10:13 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 1.4 / 3일 평균 -4.6 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | 12.5 |
| 파생·심리 | 30% | -10.0 |
| 밸류에이션 | 25% | 25.0 |
| 매크로 | 15% | -37.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.92 |
| 밸류에이션 | 가격÷STH-RP | +0 | +0 | 가격÷STH-RP 1.093 |
| 수급 | 현물 ETF 순유입 | +1 | -1 | 5일 합 +363백만$ |
| 수급 | 거래소 순유입(7일) | -1 | -1 | 7일 순유입 분포 84백분위 |
| 수급 | 거래소 보유량(30일) | +1 | +1 | 30일 -1.36% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | +0 | +0 | 7일 +0.3% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0053% |
| 파생·심리 | RSI(14) | +0 | +0 | RSI 52.6 |
| 파생·심리 | 롱/숏 비율 | -1 | -2 | 롱/숏 분포 70백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +0 | OI 7일 -1.4%, 가격 -0.2% |
| 파생·심리 | 옵션 스큐 | -1 | -1 | +3.43 (풋 우위 확대, 전일 +2.99) |
| 매크로 | 나스닥 | -1 | -1 | 50일선 아래 |
| 매크로 | DXY | -1 | -1 | 101.79, 20일 +1.2% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 158.25 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -2 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 26424.816 | 26430.891 | pt | 2026-10-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -2.87 | -2.99 | % | 2026-10-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26622.41 | 26626.02 | pt | 2026-10-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 101.791 | 101.98 | pt | 2026-10-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.18 | 1.52 | % | 2026-10-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 158.253 | 158.523 | 엔 | 2026-10-21 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | -0.04 | -0.0 | % | 2026-10-21 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.02 | 3.71 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-10-14 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.79 | 2.76 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-10-14 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.42 | 3.36 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.01 | 2.98 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -2 | -2 |  | 2026-10-21 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.532 | 6.668 | % | 2026-10-21 01:05 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.7898 | 2.7361 | 조$ | 2026-10-21 01:05 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | 526.6 | -82.4 | 백만$ | 2026-10-19 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 1거래일 연속 순유입 / 집계 기준일 2026-10-19 |
| B.자금흐름 | IBIT(블랙록) 순유입 | 665.2 | -71.8 | 백만$ | 2026-10-19 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | 363.4 | -228.6 | 백만$ | 2026-10-19 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | 1 | -1 | 일 | 2026-10-19 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 82938.26 | 81837.69 | USD | 2026-10-20 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 52.63 | 48.02 |  | 2026-10-20 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -0.2 | 0.12 | % | 2026-10-20 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.19 | 3.3 | 십억$ | 2026-10-20 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -1.35 | 0.14 | % | 2026-10-20 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 1.55 | 1.63 | 배 | 2026-10-20 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 70.0 | 93.3 | 백분위 | 2026-10-20 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.0055 | 0.0052 | % | 2026-10-21 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0053 | 0.008 | % | 2026-10-21 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 37.14 | 38.07 |  | 2026-10-21 01:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 3.43 | 2.99 | vol pt | 2026-10-21 01:13 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-11-27, 콜 BTC-27NOV26-90000-C / 풋 BTC-27NOV26-77000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.9213 | 0.9731 |  | 2026-10-14 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.0932 | 1.1145 |  | 2026-10-14 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 75900.0 | 73565.0 | $ | 2026-10-14 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 82974.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 16537.6 | 11526.6 | BTC | 2026-10-19 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 15578.3 | 11689.6 | BTC | 2026-10-19 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | 499.1 | -1876.2 | BTC | 2026-10-19 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 84.4 | 81.1 | 백분위 | 2026-10-19 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | 959.3 | -162.9 | BTC | 2026-10-19 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -1.36 | -1.44 | % | 2026-10-19 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2680975.0 | 2679759.0 | BTC | 2026-10-19 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (10-20 18:00 ~ 10-21 10:13 KST)

피드 상태: CoinDesk: 12건 / The Block: 11건 / Cointelegraph: 20건 / 블록미디어: 10건

- [블록미디어] 신한은행, 외국인 의료비 스테이블코인 결제·원화 정산 실증 (10-21 10:00) — https://www.blockmedia.co.kr/archives/1154162?utm_source=general&utm_medium=rss
- [블록미디어] 코인베이스 비트코인 보유량 1년 최저 수준…다음 방향은? (10-21 09:41) — https://www.blockmedia.co.kr/archives/1154125?utm_source=general&utm_medium=rss
- [블록미디어] [개장시황] 코스피, 슈퍼마이크로 깜짝 실적에 2%대 반등…반도체주 강세 (10-21 09:15) — https://www.blockmedia.co.kr/archives/1154147?utm_source=general&utm_medium=rss
- [Cointelegraph] Qubic restarts blockchain, opens recovery claims after $1.4M hack (10-21 08:26) — https://cointelegraph.com/news/qubic-restarts-blockchain-opens-recovery-claims-after-14m-hack?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] [코인시황] 비트코인, 美 기업 실적 호조에 8만3000달러 터치…유가·금리 하락도 뒷받침 (10-21 08:19) — https://www.blockmedia.co.kr/archives/1154132?utm_source=general&utm_medium=rss
- [블록미디어] 앤트로픽, 상반기 807억달러 순손실…막대한 인프라 비용에 ‘깜놀’ (10-21 07:30) — https://www.blockmedia.co.kr/archives/1154121?utm_source=general&utm_medium=rss
- [블록미디어] 2억8500만달러 훔친 드리프트 해킹범…이번엔 이더리움 3200만달러 옮겼다 (10-21 07:23) — https://www.blockmedia.co.kr/archives/1154105?utm_source=general&utm_medium=rss
- [블록미디어] 일론 머스크 “스페이스X·테슬라 합병 논의 착수”…양사 특별위원회 구성 (10-21 06:57) — https://www.blockmedia.co.kr/archives/1154116?utm_source=general&utm_medium=rss
- [블록미디어] “자율 AI가 직접 매매”… 미 CFTC, AI 에이전트 규제 착수 (10-21 06:48) — https://www.blockmedia.co.kr/archives/1154112?utm_source=general&utm_medium=rss
- [블록미디어] [뉴욕 금·채권·달러] “AI 거품·고금리 여파”…달러·국채금리 하락 속 자산 엇갈림 (10-21 06:39) — https://www.blockmedia.co.kr/archives/1154106?utm_source=general&utm_medium=rss
- [블록미디어] 블록체인닷컴, 비트코인·이더리움 옵션 거래 출시…파생상품 확대 나선 이유는? (10-21 06:37) — https://www.blockmedia.co.kr/archives/1154102?utm_source=general&utm_medium=rss
- [Cointelegraph] Utah AG sues Kalshi, pursues profits from prediction market company (10-21 06:19) — https://cointelegraph.com/news/utah-lawsuit-kalshi-susquehanna-prediction-markets-illegal-bets?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] U.S. CFTC sets agenda for AI forum, exploring trading and agentic finance (10-21 06:12) — https://www.coindesk.com/policy/2026/10/20/u-s-cftc-sets-agenda-for-ai-forum-exploring-trading-and-agentic-finance
- [Cointelegraph] Bitwise, Hyperliquid seek SEC rule changes for token trading, airdrops (10-21 05:38) — https://cointelegraph.com/news/bitwise-hyperliquid-seek-sec-rule-changes-for-token-trading-airdrops?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Crypto’s 2026 shutdown wave claims 82 projects. What went wrong? (10-21 04:59) — https://cointelegraph.com/news/crypto-project-shutdowns-2026-what-went-wrong?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Crypto firms, Wall Street push SEC to revise Regulation Crypto Assets as comments close (10-21 04:19) — https://www.theblock.co/news/regulation/2026-10-20-sec-regulation-crypto-assets-comment-period-hyperliquid-sifma-aima-421444
- [Cointelegraph] Here’s what happened in crypto today (10-21 04:17) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Utah likens Kalshi to a ‘back-alley gambling den’ in lawsuit naming Susquehanna firms (10-21 04:12) — https://www.theblock.co/news/regulation/2026-10-20-utah-likens-kalshi-back-alley-gambling-den-lawsuit-naming-susquehanna-firms-421442
- [CoinDesk] OKX-ICE co-chair Andrew Cuomo calls corporate objections a ‘natural response’ to tokenized stock plans (10-21 03:26) — https://www.coindesk.com/business/2026/10/20/okx-ice-s-andrew-cuomo-calls-issuer-objections-a-natural-response-to-tokenized-stock-plans
- [The Block] JPMorgan issues first long-term bitcoin return forecast, projecting 10% annually (10-21 03:14) — https://www.theblock.co/news/markets/2026-10-20-jpmorgan-bitcoin-10-year-return-forecast-ltcma-421436
- [Cointelegraph] Strive closes $630M SATS IPO, leaves Bitcoin allocation unspecified (10-21 02:40) — https://cointelegraph.com/news/strive-closes-630m-sats-ipo-leaves-bitcoin-allocation-unspecified?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Bitcoin yield platform HoneyB developer raises $5 million at $30 million valuation (10-21 02:11) — https://www.theblock.co/news/deals/2026-10-20-bitcoin-yield-platform-honeyb-funding-valuation-421430
- [CoinDesk] The Coinbase allegations expose Bitcoin's corporate governance gap (10-21 02:02) — https://www.coindesk.com/opinion/2026/10/20/the-coinbase-allegations-expose-bitcoin-s-corporate-governance-gap
- [Cointelegraph] Injective, BDACS plan Korean won stablecoin settlement for tokenized assets (10-21 01:47) — https://cointelegraph.com/news/injective-bdacs-korean-won-stablecoin-tokenized-assets?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Stablecoin transfers quadruple to $891B as US banks expand adoption: Report (10-21 01:38) — https://cointelegraph.com/news/stablecoins-move-400m-an-hour-as-73-of-volume-occurs-outside-banking-hours-coinbase-report?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Ethereum staking hits record as yields fall and Solana activity grows: Bitwise (10-21 01:31) — https://www.theblock.co/news/ecosystems/2026-10-20-ethereum-solana-staking-record-yields-fall-bitwise-q3-421414
- [Cointelegraph] Alphabet, Microsoft add objections to OKX-ICE proposed tokenized stock platform (10-21 01:23) — https://cointelegraph.com/news/alphabet-microsoft-goldman-object-okx-ice-tokenized-stock?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] OKX is putting its money where its mouth is with new protection plan: Former NY Gov. Cuomo (10-21 01:20) — https://www.theblock.co/news/regulation/2026-10-20-okx-putting-money-where-mouth-is-new-protection-plan-former-ny-gov-cuomo-421421
- [Cointelegraph] Bitcoin price spikes to $83.3K as US stocks rise on Q3 earnings, oil falls (10-21 01:14) — https://cointelegraph.com/markets/bitcoin-price-spikes-to-833k-as-us-stocks-rise-on-q3-earnings-oil-falls?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Mastercard opens early access to AI agent payments following pilots with Coinbase, Base and Cloudflare (10-21 01:00) — https://www.theblock.co/news/business/2026-10-20-mastercard-opens-early-access-to-ai-agent-payments-following-pilots-with-coinbase-base-and-cloudflare-421406
- [The Block] Blockchain.com rolls out crypto options as it pursues US derivatives licenses (10-20 23:31) — https://www.theblock.co/news/markets/2026-10-20-blockchain-com-launches-options-trading-bitcoin-ether-sol-421326
- [CoinDesk] BlackRock seeks to shield bitcoin investors from losses after rival fund weathers 50% crash (10-20 23:28) — https://www.coindesk.com/markets/2026/10/20/blackrock-seeks-to-shield-bitcoin-investors-from-losses-after-rival-fund-weathers-50-crash
- [The Block] Injective partners with BDACS to bring Korean won stablecoin to RWA ecosystem (10-20 23:00) — https://www.theblock.co/news/markets/2026-10-20-injective-partners-bdacs-418883
- [CoinDesk] Kazakhstan court bars Coinbase, five others from unlicensed crypto services in Astana International Financial Centre (10-20 22:35) — https://www.coindesk.com/business/2026/10/20/kazakhstan-court-bars-coinbase-five-others-from-unlicensed-crypto-services-in-astana-international-financial-centre
- [Cointelegraph] Agents can trade 24/7 — but Yat Siu warns you could lose access at any time (10-20 22:30) — https://cointelegraph.com/magazine/ai-trade-sleep-yat-siu-warns-losing-agent?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] FINMA approves Switzerland’s first Bitcoin ETF for retail investors (10-20 22:10) — https://cointelegraph.com/news/finma-approves-switzerlands-first-bitcoin-etf-retail?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Stablecoins move over $400 million per hour on average as off-hours transfers dominate, Coinbase and The Block study finds (10-20 22:00) — https://www.theblock.co/news/web3/2026-10-20-stablecoins-move-400-million-per-hour-421111
- [CoinDesk] Microsoft, Alphabet and Goldman Sachs join objections to OKX-ICE tokenized stock trading (10-20 21:40) — https://www.coindesk.com/business/2026/10/19/microsoft-alphabet-and-goldman-sachs-join-objections-to-okx-ice-tokenized-stock-trading
- [Cointelegraph] Drift exploiter sends $61M ETH to Tornado Cash, holds $194M (10-20 21:38) — https://cointelegraph.com/news/drift-exploiter-eth-tornado-cash?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Tx launches USTX stablecoin to pull RWA liquidity onto its chain (10-20 21:30) — https://cointelegraph.com/news/tx-ustx-stablecoin-rwa-liquidity-chain?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Swiss regulator FINMA approves country’s first spot bitcoin ETF for retail investors (10-20 21:15) — https://www.theblock.co/news/regulation/2026-10-20-swiss-regulator-finma-approves-countrys-first-spot-bitcoin-etf-for-retail-investors-421127
- [Cointelegraph] Lloyds and Barclays among UK banks named in crypto transfer complaints, advocacy group says (10-20 21:13) — https://cointelegraph.com/news/uk-banks-crypto-transfer-complaints-stand-with-crypto?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] France's parliament approves vote to hit stablecoin trades with 31% capital gains tax (10-20 20:25) — https://www.coindesk.com/policy/2026/10/20/france-s-parliament-approves-vote-to-hit-crypto-to-stablecoin-trades-with-31-levy
- [Cointelegraph] Netflix FTX trailer was ‘enough to upset me’ in first 30 seconds: former FTX COO (10-20 20:23) — https://cointelegraph.com/news/netflix-ftx-trailer-upset-first-30-seconds-ftx-coo?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Equity weakness could damp demand for bitcoin after biggest ETF inflows in a month (10-20 20:14) — https://www.coindesk.com/daybook-us/2026/10/20/equity-weakness-could-damp-demand-for-bitcoin-after-biggest-etf-inflows-in-a-month
- [Cointelegraph] Kazakhstan court orders curbs on Coinbase, BingX and four others (10-20 20:12) — https://cointelegraph.com/news/kazakhstan-court-limits-coinbase-bingx-four?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] JPMorgan sees 10% annual bitcoin returns, topping stocks, bonds and gold over next decade (10-20 20:10) — https://www.coindesk.com/markets/2026/10/20/jpmorgan-sees-10-annual-bitcoin-returns-topping-stocks-bonds-and-gold-over-next-decade
- [CoinDesk] Bitcoin drops to $81,400 as Asian chip stocks tumble, options traders seek downside protection (10-20 19:22) — https://www.coindesk.com/markets/2026/10/20/bitcoin-drops-to-usd81-400-as-asian-chip-stocks-tumble-options-traders-seek-downside-protection
- [Cointelegraph] XRP 30-day exchange inflows pass 6B tokens as whales move to the sidelines (10-20 19:20) — https://cointelegraph.com/markets/xrp-30-day-exchange-inflows-pass-6b-tokens-as-whales-move-to-the-sidelines?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Mt. Gox pushes creditor repayment deadline to 2027 in sixth extension (10-20 19:20) — https://cointelegraph.com/news/mt-gox-creditor-repayment-deadline-extended-2027?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Live updates: Bitcoin cuts losses as stocks edge higher (10-20 19:14) — https://www.coindesk.com/markets/2026/10/20/live-updates-market-jitters-persist-as-the-ai-selloff-deepens
- [Cointelegraph] Bitget plans Thai crypto exchange acquisition weeks after $388M hack (10-20 19:00) — https://cointelegraph.com/news/bitget-plans-thai-crypto-exchange-acquisition-weeks-after-388m-hack?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] South Korean IPO slump adds to AI market jitters as Brent crude tops $111 (10-20 18:32) — https://www.coindesk.com/markets/2026/10/20/south-korean-ipo-plunge-deepens-ai-market-jitters-as-brent-tops-usd111

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