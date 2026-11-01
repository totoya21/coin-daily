# 코인 데일리 스냅샷

- 수집 시각: 2026-11-01 15:39 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 -0.5 / 3일 평균 10.5 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | 0.0 |
| 파생·심리 | 30% | -10.0 |
| 밸류에이션 | 25% | 25.0 |
| 매크로 | 15% | -25.0 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.77 |
| 밸류에이션 | 가격÷STH-RP | +0 | +0 | 가격÷STH-RP 1.024 |
| 수급 | 현물 ETF 순유입 | -1 | +2 | 5일 합 -203백만$ |
| 수급 | 거래소 순유입(7일) | +1 | +1 | 7일 순유입 분포 18백분위 |
| 수급 | 거래소 보유량(30일) | +0 | +1 | 30일 -0.47% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | +0 | +0 | 7일 +1.9% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +0 | +1 | 3회 평균 0.0100% |
| 파생·심리 | RSI(14) | +1 | +1 | RSI 35.5 |
| 파생·심리 | 롱/숏 비율 | -2 | -2 | 롱/숏 분포 93백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +0 | OI 7일 +11.2%, 가격 -4.1% |
| 파생·심리 | 옵션 스큐 | +0 | -1 | +5.34 |
| 매크로 | 나스닥 | -1 | -1 | 50일선 아래 |
| 매크로 | DXY | +0 | +0 | 101.88, 20일 -0.1% |
| 매크로 | USD/JPY | +0 | +0 | 157.80 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -3 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 25437.0 | 26184.721 | pt | 2026-10-30 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -2.0 | -2.0 | % | 2026-10-30 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26574.14 | 26574.14 | pt | 2026-10-30 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 101.88 | 102.04 | pt | 2026-10-30 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | -0.05 | -0.05 | % | 2026-10-30 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 157.804 | 157.833 | 엔 | 2026-10-30 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | 0.84 | 0.84 | % | 2026-10-30 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.02 | 3.71 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-10-14 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.79 | 2.76 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-10-14 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.65 | 3.44 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.12 | 3.03 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -3 | -3 |  | 2026-11-01 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.801 | 6.854 | % | 2026-11-01 06:39 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.6356 | 2.6215 | 조$ | 2026-11-01 06:39 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | -643.3 | 17.1 | 백만$ | 2026-10-30 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 1거래일 연속 순유출 / 집계 기준일 2026-10-30 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -233.7 | 12.8 | 백만$ | 2026-10-30 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -202.6 | 302.8 | 백만$ | 2026-10-30 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | -1 | 4 | 일 | 2026-10-30 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 77423.98 | 77180.42 | USD | 2026-10-31 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 35.53 | 34.29 |  | 2026-10-31 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -4.14 | -4.81 | % | 2026-10-31 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.71 | 3.68 | 십억$ | 2026-10-31 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | 11.22 | 7.53 | % | 2026-10-31 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 2.61 | 2.65 | 배 | 2026-10-31 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 93.3 | 100.0 | 백분위 | 2026-10-31 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.01 | 0.01 | % | 2026-11-01 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.01 | 0.0085 | % | 2026-11-01 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 39.66 | 40.59 |  | 2026-11-01 06:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 5.34 | 5.56 | vol pt | 2026-11-01 06:39 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-11-27, 콜 BTC-27NOV26-84000-C / 풋 BTC-27NOV26-73000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.7668 | 0.7585 |  | 2026-10-31 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.0236 | 1.0201 |  | 2026-10-31 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 75616.0 | 75590.0 | $ | 2026-10-31 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 77401.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 6752.5 | 32430.5 | BTC | 2026-10-31 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 10502.4 | 26836.1 | BTC | 2026-10-31 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -30624.8 | -26670.3 | BTC | 2026-10-31 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 17.8 | 20.0 | 백분위 | 2026-10-31 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -3749.8 | 5594.4 | BTC | 2026-10-31 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -0.47 | -0.59 | % | 2026-10-31 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2665092.0 | 2666040.0 | BTC | 2026-10-31 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (10-31 18:00 ~ 11-01 15:39 KST)

피드 상태: CoinDesk: 11건 / The Block: 2건 / Cointelegraph: 7건 / 블록미디어: 10건

- [블록미디어] 바이낸스, 단계적 출금 재개–네번째 공식 발표 (11-01 13:28) — https://www.blockmedia.co.kr/archives/1159649?utm_source=general&utm_medium=rss
- [블록미디어] 스페이스X 공모가 밑돌아도…CZ “장기 보유 최고 종목” (11-01 13:02) — https://www.blockmedia.co.kr/archives/1159645?utm_source=general&utm_medium=rss
- [블록미디어] 바이낸스, 해킹 손실 60억달러 보전…보전율 90% (11-01 12:10) — https://www.blockmedia.co.kr/archives/1159641?utm_source=general&utm_medium=rss
- [블록미디어] JP모건, 장기 전망에 비트코인 첫 포함…연 10% 제시 (11-01 11:51) — https://www.blockmedia.co.kr/archives/1159639?utm_source=general&utm_medium=rss
- [블록미디어] 바이낸스 해킹 불똥…넥스트테크, 비트코인 매도 검토 (11-01 11:25) — https://www.blockmedia.co.kr/archives/1159636?utm_source=general&utm_medium=rss
- [블록미디어] 이더리움 2360달러 돌파시 바이낸스 해커는 어떻게 나올까? 에이브 청산의 역설 (11-01 11:05) — https://www.blockmedia.co.kr/archives/1159623?utm_source=general&utm_medium=rss
- [블록미디어] 이더리움 ETF, 23거래일 연속 순유출…출시 이후 최장 (11-01 10:38) — https://www.blockmedia.co.kr/archives/1159627?utm_source=general&utm_medium=rss
- [블록미디어] 칼시, 민주당 상원 장악 확률 72%로 평가 (11-01 10:33) — https://www.blockmedia.co.kr/archives/1159628?utm_source=general&utm_medium=rss
- [블록미디어] 트럼프 “바이낸스 해킹, 北 소행이면 논의”…외교·안보 사안으로 확산하나 (11-01 10:12) — https://www.blockmedia.co.kr/archives/1159621?utm_source=general&utm_medium=rss
- [CoinDesk] FBI confirms North Korea's role in $6 billion Binance hack, asks DeFi community to block BTC, ETH, SOL addresses (11-01 10:10) — https://www.coindesk.com/policy/2026/10/31/fbi-confirms-north-korea-s-role-in-usd6-billion-binance-hack-asks-defi-community-to-block-btc-eth-sol-addresses
- [블록미디어] 비트코인 공포지수 한 달 새 70→36…바닥 판단은 일러 (11-01 09:41) — https://www.blockmedia.co.kr/archives/1159619?utm_source=general&utm_medium=rss
- [CoinDesk] Bitcoin's white paper turns 18, and small businesses are still paying for the bailouts it answered (11-01 03:00) — https://www.coindesk.com/opinion/2026/10/31/bitcoin-s-white-paper-turns-18-and-small-businesses-are-still-paying-for-the-bailouts-it-answered
- [CoinDesk] A stolen iPhone, $14,000 in losses and London's crypto theft problem (11-01 01:09) — https://www.coindesk.com/business/2026/11/01/a-stolen-iphone-usd14-000-in-losses-and-london-s-crypto-theft-problem
- [CoinDesk] Traders are already placing leveraged bets on Anthropic’s IPO using crypto contracts (11-01 01:00) — https://www.coindesk.com/business/2026/10/31/traders-are-already-placing-leveraged-bets-on-anthropic-s-ipo-using-crypto-contracts
- [Cointelegraph] Binance says 90% of stolen assets replenished, targets Sunday withdrawals (11-01 00:36) — https://cointelegraph.com/news/binance-hack-90-percent-replenished?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Hackers hijack a dozen DeFi websites, all registered with Name.com, and steal about $138,000 (11-01 00:26) — https://www.theblock.co/news/defi/2026-10-31-hackers-hijack-a-dozen-defi-websites-all-registered-with-name-com-and-steal-about-138000-432251
- [Cointelegraph] Bitcoin held up better than expected after Binance hack, Strive CEO says (11-01 00:26) — https://cointelegraph.com/markets/bitcoin-binance-hack-strive-ceo?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Binance says it has replaced 90% of stolen crypto after massive $6.3 billion breach (11-01 00:24) — https://www.coindesk.com/business/2026/10/31/binance-says-it-has-replaced-90-of-stolen-crypto-after-massive-usd6-3-billion-breach
- [Cointelegraph] Here’s what happened in crypto today (11-01 00:09) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Institutions embrace crypto staking despite shrinking yields (11-01 00:00) — https://www.coindesk.com/business/2026/10/26/institutions-embrace-crypto-staking-despite-shrinking-yields
- [CoinDesk] Uber tests how tokenization can put idle cash to work with HSBC, Franklin Templeton (10-31 23:40) — https://www.coindesk.com/business/2026/10/31/uber-tests-how-tokenization-can-put-idle-cash-to-work-with-hsbc-franklin-templeton
- [Cointelegraph] Bitcoin turns 18: Has the original rebel grown up? (10-31 23:27) — https://cointelegraph.com/magazine/bitcoin-turns-18-has-the-original-rebel-grown-up?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] As big bitcoin miners chase AI profits, individuals get another shot at the rewards (10-31 23:00) — https://www.coindesk.com/tech/2026/10/31/as-big-bitcoin-miners-chase-ai-profits-individuals-get-another-shot-at-the-rewards
- [Cointelegraph] Texas brothers sentenced to 15 years in prison for armed crypto robbery, kidnapping (10-31 22:37) — https://cointelegraph.com/news/texas-brothers-sentenced-to-15-years-in-prison-for-armed-crypto-robbery-kidnapping?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Chainalysis says hacker using ‘offensive agentic techniques’ accessed its customers’ names and emails (10-31 22:27) — https://www.theblock.co/news/business/2026-10-31-chainalysis-says-hacker-using-offensive-agentic-techniques-accessed-its-customers-names-and-emails-432244
- [CoinDesk] 18 years in, what has Bitcoin truly done? (10-31 22:00) — https://www.coindesk.com/opinion/2026/10/31/18-years-in-what-has-bitcoin-truly-done
- [CoinDesk] A Nasdaq-listed company may sell $450 million bitcoin, citing Binance hack and quantum fears (10-31 21:49) — https://www.coindesk.com/markets/2026/10/31/a-nasdaq-listed-company-may-sell-usd450-million-bitcoin-citing-binance-hack-and-quantum-fears
- [CoinDesk] The $6.3 billion Binance hack paradox: Centralization made the hack possible, but also saved $3 billion (10-31 21:00) — https://www.coindesk.com/business/2026/10/31/the-usd6-3-billion-binance-hack-paradox-centralization-made-the-hack-possible-but-also-saved-usd3-billion
- [Cointelegraph] Blockchain investigator Chainalysis hit by cybersecurity incident (10-31 20:22) — https://cointelegraph.com/news/blockchain-investigator-chainalysis-hit-by-cybersecurity-incident?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Binance $6.3B record hack sparks pre-election political clashes (10-31 18:58) — https://cointelegraph.com/news/binance-63b-record-hack-sparks-pre-election-political-chatter?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

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