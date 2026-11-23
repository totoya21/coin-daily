# 코인 데일리 스냅샷

- 수집 시각: 2026-11-23 17:01 KST
- 결과: 성공 38 / 실패·검증필요 2 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 12.5 / 3일 평균 10.0 / 오늘 구간 '중립'
- 판정 가능 지표 14/17개 (82%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | -37.5 |
| 파생·심리 | 30% | 62.5 |
| 밸류에이션 | 25% | 50.0 |
| 매크로 | 15% | -50.0 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.37 |
| 밸류에이션 | 가격÷STH-RP | +1 | +1 | 가격÷STH-RP 0.874 |
| 수급 | 현물 ETF 순유입 | -2 | -2 | 3거래일 연속 순유출 |
| 수급 | 거래소 순유입(7일) | +0 | +1 | 7일 순유입 분포 36백분위 |
| 수급 | 거래소 보유량(30일) | +0 | -1 | 30일 +0.49% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | -1 | -1 | 7일 +4.2% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +2 | 3회 평균 0.0011% |
| 파생·심리 | RSI(14) | +2 | +2 | RSI 26.7 |
| 파생·심리 | 롱/숏 비율 | +1 | +1 | 롱/숏 분포 27백분위 |
| 파생·심리 | 미결제약정(OI) | +1 | +1 | OI 7일 -6.3%, 가격 -6.4% (레버리지 정리) |
| 파생·심리 | 옵션 스큐 | 제외 | -1 | 값 없음 |
| 매크로 | 나스닥 | -2 | -2 | 5일 -10.0% 급락 |
| 매크로 | DXY | -1 | -1 | 103.59, 20일 +1.6% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 159.06 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -4 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 22617.73 | 23879.199 | pt | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -10.02 | -10.02 | % | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26113.44 | 26113.44 | pt | 2026-11-20 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 103.591 | 103.81 | pt | 2026-11-23 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.6 | 1.96 | % | 2026-11-23 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 159.055 | 159.707 | 엔 | 2026-11-23 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | -0.45 | -0.11 | % | 2026-11-23 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.08 | 4.02 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.87 | 2.79 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.65 | 3.44 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.12 | 3.03 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -4 | -4 |  | 2026-11-23 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 8.327 | 8.478 | % | 2026-11-23 07:58 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.0907 | 2.052 | 조$ | 2026-11-23 07:58 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | -582.2 | -306.4 | 백만$ | 2026-11-19 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 3거래일 연속 순유출 / 집계 기준일 2026-11-19 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -541.1 | -148.7 | 백만$ | 2026-11-19 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -1306.0 | -1306.0 | 백만$ | 2026-11-19 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | -3 | -3 | 일 | 2026-11-19 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 61163.01 | 60086.0 | USD | 2026-11-22 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 26.74 | 22.58 |  | 2026-11-22 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -6.36 | -6.29 | % | 2026-11-22 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 2.84 | 2.82 | 십억$ | 2026-11-22 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -6.32 | -12.92 | % | 2026-11-22 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 2.15 | 2.22 | 배 | 2026-11-22 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 26.7 | 20.0 | 백분위 | 2026-11-22 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | -0.0005 | 0.0015 | % | 2026-11-23 08:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0011 | -0.0028 | % | 2026-11-23 08:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 49.02 | 57.68 |  | 2026-11-23 08:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐 |  | 9.05 |  |  | fail | [Deribit](https://www.deribit.com/options/BTC) | 429 Client Error: Too Many Requests for url: https://www.deribit.com/api/v2/public/ticker?instrument_name=BTC-25DEC26-54000-C |
| D.온체인 | MVRV Z-Score | 0.3666 | 0.3784 |  | 2026-11-16 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 0.8736 | 0.8747 |  | 2026-11-16 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 69945.0 | 68735.0 | $ | 2026-11-16 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 61104.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 14441.8 | 37664.0 | BTC | 2026-11-22 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 13517.4 | 49689.5 | BTC | 2026-11-22 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -20583.1 | -24870.2 | BTC | 2026-11-22 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 35.6 | 28.9 | 백분위 | 2026-11-22 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | 924.4 | -515.4 | BTC | 2026-11-22 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | 0.49 | 1.3 | % | 2026-11-22 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2699121.0 | 2698129.0 | BTC | 2026-11-22 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (11-22 18:00 ~ 11-23 17:01 KST)

피드 상태: CoinDesk: 7건 / The Block: 5건 / Cointelegraph: 7건 / 블록미디어: 10건

- [블록미디어] 이더리움 글램스터담 내년으로 연기…개발자 “구조적 문제 반복” (11-23 17:00) — https://www.blockmedia.co.kr/archives/1169274?utm_source=general&utm_medium=rss
- [CoinDesk] Crypto thieves are using online ads to infect iPhones with a single tap, research finds (11-23 16:45) — https://www.coindesk.com/tech/2026/11/23/moldyroost-malvertizing-campaign-uses-one-tap-iphone-hacks-to-hunt-crypto-wallet-keys-research-shows
- [CoinDesk] This Swedish bitcoin treasury firm lost 30 BTC trading part of its own stack (11-23 16:18) — https://www.coindesk.com/markets/2026/11/23/this-swedish-bitcoin-treasury-firm-lost-30-btc-trading-part-of-its-own-stack
- [The Block] Ark buys $146 million in Anthropic shares last week, trims Ethereum and Solana Staking ETF holdings (11-23 16:12) — https://www.theblock.co/news/business/2026-11-23-ark-buys-146-million-worth-anthropic-since-debut-444866
- [블록미디어] 63억달러 해킹에도 이더리움 안 떠났다…바이낸스 출금량 ‘역대 최저’ (11-23 16:07) — https://www.blockmedia.co.kr/archives/1169361?utm_source=general&utm_medium=rss
- [블록미디어] [마감시황] 코스피, AI 회의론에 3%대 급락…4700선 턱걸이 (11-23 15:54) — https://www.blockmedia.co.kr/archives/1169355?utm_source=general&utm_medium=rss
- [블록미디어] 솔라나 거래 실패 가능성 커졌다…새 보안 규칙에 구형 앱 비상 (11-23 15:51) — https://www.blockmedia.co.kr/archives/1169307?utm_source=general&utm_medium=rss
- [블록미디어] 지난주 비트코인·이더리움 ETF서 14.7억달러 이탈…블랙록 하루 최대 유출 (11-23 15:33) — https://www.blockmedia.co.kr/archives/1169301?utm_source=general&utm_medium=rss
- [블록미디어] 디지털자산기본법 정부안 내일 공개…‘늦어도 내년 1월 통과’ 문턱 넘을까 (11-23 15:33) — https://www.blockmedia.co.kr/archives/1169330?utm_source=general&utm_medium=rss
- [CoinDesk] Cardano holders are turning down a $4 million request for running its flagship event (11-23 15:15) — https://www.coindesk.com/markets/2026/11/23/cardano-holders-are-turning-down-a-usd4-million-request-for-running-its-flagship-event
- [블록미디어] 골드만삭스 “삼성·SK하이닉스 목표가 낮췄다…메모리 가격 급락 경고” (11-23 15:13) — https://www.blockmedia.co.kr/archives/1169323?utm_source=general&utm_medium=rss
- [Cointelegraph] Here’s what happened in crypto today (11-23 15:00) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 미국 연준 ‘빅스텝’ 전망 사라졌다…12월 금리동결 가능성 등장 (11-23 15:00) — https://www.blockmedia.co.kr/archives/1169318?utm_source=general&utm_medium=rss
- [The Block] Spot bitcoin ETFs shed $1.8 billion in past week as outflows become ‘structural’: analysts (11-23 14:47) — https://www.theblock.co/news/markets/2026-11-23-spot-bitcoin-etfs-shed-1-79-billion-in-past-week-444857
- [CoinDesk] Bitcoin sold for $17,000 on Kraken's Canadian dollar market, and the trades stand (11-23 14:42) — https://www.coindesk.com/markets/2026/11/23/bitcoin-sold-for-usd17-000-on-kraken-s-canadian-dollar-market-and-the-trades-stand
- [블록미디어] 금 2.6% 급반등에도 비트코인은 약세장…’디지털 금’ 위상 흔들 (11-23 14:10) — https://www.blockmedia.co.kr/archives/1169306?utm_source=general&utm_medium=rss
- [CoinDesk] Market rout kills 50 basis points December Fed rate hike bets (11-23 13:45) — https://www.coindesk.com/markets/2026/11/23/market-rout-kills-50-basis-points-december-fed-rate-hike-bets
- [블록미디어] 블룸버그 맥글론 “비트코인 1만달러 추락 전망…도지코인은 가치 0에 수렴” (11-23 13:45) — https://www.blockmedia.co.kr/archives/1169294?utm_source=general&utm_medium=rss
- [Cointelegraph] Trump renews call for Nvidia to rehire Jensen Huang as CEO (11-23 12:37) — https://cointelegraph.com/news/trump-renews-call-for-nvidia-to-rehire-jensen-huang-as-ceo?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Billionaire Bill Ackman warns Fed will make a rate ‘mistake’ in December (11-23 11:47) — https://cointelegraph.com/markets/billionaire-bill-ackman-warns-fed-rate-hikes-could-trigger-recession?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Half of wallets on Trump’s dinner list got tokens from non-US exchanges (11-23 09:53) — https://cointelegraph.com/news/half-wallets-trumps-dinner-list-got-tokens-from-non-us-exchanges?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] A $2 million exploit leads to a $3.7 million free-for-all as traders empty Fusionist’s ACE bridge (11-23 08:17) — https://www.theblock.co/news/defi/2026-11-22-a-2-million-exploit-leads-to-a-3-7-million-free-for-all-as-traders-empty-fusionists-ace-bridge-444838
- [Cointelegraph] Will Bitcoin’s big rebound hold? More tampered Ledgers found: Hodler’s Digest (11-23 07:47) — https://cointelegraph.com/magazine/will-bitcoins-big-rebound-hold-more-tampered-ledgers-found-hodlers-digest?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Trump to host second memecoin dinner tonight with TRUMP down 99% from peak (11-23 05:58) — https://www.theblock.co/news/ecosystems/2026-11-22-trump-to-host-second-memecoin-dinner-tonight-with-trump-down-99-from-peak-444828
- [CoinDesk] More on the pending oversight hearings: State of Crypto (11-23 04:30) — https://www.coindesk.com/
- [The Block] Chainflip’s losses climb to $12 million after protocol discloses 122.9 BTC theft, offers hacker bounty (11-23 03:58) — https://www.theblock.co/news/defi/2026-11-22-chainflips-losses-climb-to-12-million-after-protocol-discloses-122-9-btc-theft-offers-hacker-bounty-444829
- [Cointelegraph] The future of onchain FX could start with users, not institutional liquidity (11-22 23:30) — https://cointelegraph.com/opinion/future-onchain-fx-could-start-with-users-not-institutional-liquidity?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin's quantum security challenge extends to bridges, custodians and millions of coins (11-22 23:00) — https://www.coindesk.com/tech/2026/11/22/bitcoin-s-quantum-security-challenge-extends-to-bridges-custodians-and-millions-of-coins
- [Cointelegraph] Bitcoin briefly drops to $17K on Kraken, exchange upholds trades (11-22 18:33) — https://cointelegraph.com/news/bitcoin-17k-kraken-canadian-dollar-market-trades-stand?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

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