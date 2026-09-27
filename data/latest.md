# 코인 데일리 스냅샷

- 수집 시각: 2026-09-27 09:47 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 매수** → BTC 목표 비중 **80%** (전일 판정: 중립)
- 오늘 총점 26.4 / 3일 평균 25.7 / 오늘 구간 '매수'
- 판정 가능 지표 14/17개 (82%)
- '매수' 구간 2일 연속 → 판정 변경 (중립 → 매수)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | 83.3 |
| 파생·심리 | 30% | -10.0 |
| 밸류에이션 | 25% | 25.0 |
| 매크로 | 15% | -12.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.94 |
| 밸류에이션 | 가격÷STH-RP | +0 | +0 | 가격÷STH-RP 1.130 |
| 수급 | 현물 ETF 순유입 | +2 | +2 | 7거래일 연속 순유입 |
| 수급 | 거래소 순유입(7일) | +2 | +2 | 7일 순유입 분포 1백분위 |
| 수급 | 거래소 보유량(30일) | +1 | +1 | 30일 -0.67% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | 제외 | — | 7일 전 값 없음 |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0002% |
| 파생·심리 | RSI(14) | -1 | -1 | RSI 65.0 |
| 파생·심리 | 롱/숏 비율 | +0 | -1 | 롱/숏 분포 63백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +0 | OI 7일 -3.1%, 가격 +3.9% |
| 파생·심리 | 옵션 스큐 | -1 | +0 | +0.95 (풋 우위 확대, 전일 +0.62) |
| 매크로 | 나스닥 | +1 | +1 | 50일선 위 |
| 매크로 | DXY | -1 | -1 | 100.97, 20일 +1.8% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 157.19 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -1 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 27068.721 | 26939.369 | pt | 2026-09-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | 2.06 | 2.06 | % | 2026-09-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26169.53 | 26169.53 | pt | 2026-09-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 100.97 | 101.29 | pt | 2026-09-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.83 | 1.89 | % | 2026-09-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 157.185 | 158.811 | 엔 | 2026-09-26 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | 0.09 | 0.68 | % | 2026-09-26 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 3.71 | 3.54 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-09-11 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.76 | 2.79 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-09-11 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.7 | 3.72 | % | 2026-07-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-08-26 (점수 미반영: 발표 후 30일 경과) |
| A.매크로 | 근원 PCE 전년비 | 3.34 | 3.34 | % | 2026-07-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-08-26 (점수 미반영: 발표 후 30일 경과) |
| A.매크로 | 인플레이션 방향 합계 | -1 | -1 |  | 2026-09-27 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.324 | 6.355 | % | 2026-09-27 00:39 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.9035 | 2.8869 | 조$ | 2026-09-27 00:39 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | 134.5 | 190.6 | 백만$ | 2026-09-25 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 7거래일 연속 순유입 / 집계 기준일 2026-09-25 |
| B.자금흐름 | IBIT(블랙록) 순유입 | 97.0 | 162.6 | 백만$ | 2026-09-25 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | 2385.8 | 2684.4 | 백만$ | 2026-09-25 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | 7 | 6 | 일 | 2026-09-25 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 84416.65 | 84093.13 | USD | 2026-09-26 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 65.02 | 64.31 |  | 2026-09-26 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | 3.92 | 3.98 | % | 2026-09-26 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.12 | 3.16 | 십억$ | 2026-09-26 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -3.07 | 0.18 | % | 2026-09-26 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 1.28 | 1.33 | 배 | 2026-09-26 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 63.3 | 73.3 | 백분위 | 2026-09-26 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | -0.0009 | -0.0006 | % | 2026-09-27 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0002 | 0.0041 | % | 2026-09-27 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 34.9 | 34.76 |  | 2026-09-27 00:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 0.95 | 0.62 | vol pt | 2026-09-27 00:47 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-10-30, 콜 BTC-30OCT26-91000-C / 풋 BTC-30OCT26-79000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.9372 | 0.9259 |  | 2026-09-20 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.13 | 1.13 |  | 2026-09-20 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 74679.0 | 74401.0 | $ | 2026-09-20 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 84388.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 22970.3 | 19032.1 | BTC | 2026-09-25 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 30130.3 | 26693.5 | BTC | 2026-09-25 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -47162.9 | -41054.2 | BTC | 2026-09-25 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 1.1 | 2.2 | 백분위 | 2026-09-25 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -7160.0 | -7661.3 | BTC | 2026-09-25 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -0.67 | -0.6 | % | 2026-09-25 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2685119.0 | 2690689.0 | BTC | 2026-09-25 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (09-26 18:00 ~ 09-27 09:47 KST)

피드 상태: CoinDesk: 4건 / The Block: 2건 / Cointelegraph: 3건 / 블록미디어: 10건

- [블록미디어] 써클 아크에 AI 신원 확인 도입…USDC 전환 전 사기 위험 점검 (09-27 09:46) — https://www.blockmedia.co.kr/archives/1144649?utm_source=general&utm_medium=rss
- [블록미디어] 솔라나 알펜글로우, 개발망도 가동…거래 확정 0.1초 목표(종합) (09-27 09:14) — https://www.blockmedia.co.kr/archives/1144644?utm_source=general&utm_medium=rss
- [블록미디어] 캐시 우드, 오픈AI·스페이스X 담은 펀드 토큰화…블록체인에 기록 (09-27 08:16) — https://www.blockmedia.co.kr/archives/1144640?utm_source=general&utm_medium=rss
- [블록미디어] 세일러 스트래티지 회장 “은행이 비트코인 맡고 담보대출도 허용해야” (09-27 07:43) — https://www.blockmedia.co.kr/archives/1144637?utm_source=general&utm_medium=rss
- [블록미디어] 바이낸스, 써클에 1억달러 투자… ‘5년 동맹’ 체결 (09-27 06:50) — https://www.blockmedia.co.kr/archives/1144635?utm_source=general&utm_medium=rss
- [블록미디어] 크라켄 모회사 페이워드, 통합 금융 플랫폼 구축 (09-27 06:30) — https://www.blockmedia.co.kr/archives/1144632?utm_source=general&utm_medium=rss
- [블록미디어] 애플, 탭틱엔진 특허 소송 패소… “57억달러 배상” (09-27 06:28) — https://www.blockmedia.co.kr/archives/1144630?utm_source=general&utm_medium=rss
- [블록미디어] 테더, 미 국채 1100억달러 보유…미 정부 ‘파트너’ 되나 (09-27 06:24) — https://www.blockmedia.co.kr/archives/1144628?utm_source=general&utm_medium=rss
- [블록미디어] [뉴욕 코인시황] 트럼프, 이란 휴전안 거부…비트코인 8.3만달러대 후퇴 (09-27 06:20) — https://www.blockmedia.co.kr/archives/1144625?utm_source=general&utm_medium=rss
- [블록미디어] “스페이스X, AI 잠재력 주목”…모건스탠리, 목표가 300달러 (09-27 05:11) — https://www.blockmedia.co.kr/archives/1144623?utm_source=general&utm_medium=rss
- [The Block] Bitcoin ETFs turn positive for 2026 with $2.4 billion weekly inflow, their largest since October (09-27 02:24) — https://www.theblock.co/news/markets/2026-09-26-bitcoin-etfs-turn-positive-for-2026-with-2-4-billion-weekly-inflow-their-largest-since-october-416944
- [The Block] Kalshi loses appeal over Ohio and Tennessee sports betting laws, widening circuit split (09-27 00:17) — https://www.theblock.co/news/regulation/2026-09-26-kalshi-loses-appeal-over-ohio-and-tennessee-sports-betting-laws-widening-circuit-split-416937
- [CoinDesk] Kraken’s parent Payward is betting billions on becoming financial infrastructure, not just a crypto exchange (09-26 23:00) — https://www.coindesk.com/business/2026/09/26/kraken-s-parent-payward-is-betting-billions-on-becoming-financial-infrastructure-not-just-a-crypto-exchange
- [Cointelegraph] Kalshi loses appeal, setting up potential Supreme Court case (09-26 22:21) — https://cointelegraph.com/news/kalshi-loses-appeal-setting-up-potential-supreme-court-case?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Binance deal gives Circle a boost in stablecoin race with Tether, analysts say (09-26 22:00) — https://www.coindesk.com/business/2026/09/26/binance-deal-gives-circle-a-boost-in-stablecoin-race-with-tether-analysts-say
- [CoinDesk] Bitget hacker moves $83 million in stolen XRP that Ripple cannot freeze (09-26 21:56) — https://www.coindesk.com/markets/2026/09/26/bitget-hacker-moves-usd83-million-in-stolen-xrp-that-ripple-cannot-freeze
- [Cointelegraph] Here’s what happened in crypto today (09-26 21:17) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin could soon get Zcash-style 'shielded' privacy without changing its rules (09-26 21:00) — https://www.coindesk.com/tech/2026/09/25/bitcoin-could-soon-get-zcash-style-shielded-privacy-without-changing-its-rules
- [Cointelegraph] SEC Commissioner Hester Peirce to leave post on Oct. 2 (09-26 18:02) — https://cointelegraph.com/news/sec-commissioner-hester-peirce-to-leave-post-on-oct-2?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

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