# 코인 데일리 스냅샷

- 수집 시각: 2026-11-15 15:59 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 -2.9 / 3일 평균 -12.0 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | -62.5 |
| 파생·심리 | 30% | 30.0 |
| 밸류에이션 | 25% | 50.0 |
| 매크로 | 15% | -37.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.69 |
| 밸류에이션 | 가격÷STH-RP | +1 | +0 | 가격÷STH-RP 0.992 |
| 수급 | 현물 ETF 순유입 | -2 | -2 | 7거래일 연속 순유출 |
| 수급 | 거래소 순유입(7일) | -1 | -1 | 7일 순유입 분포 84백분위 |
| 수급 | 거래소 보유량(30일) | -1 | -1 | 30일 +1.64% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | -1 | -1 | 7일 +15.2% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 -0.0000% |
| 파생·심리 | RSI(14) | +2 | +2 | RSI 19.9 |
| 파생·심리 | 롱/숏 비율 | +0 | -2 | 롱/숏 분포 57백분위 |
| 파생·심리 | 미결제약정(OI) | +1 | +1 | OI 7일 -14.5%, 가격 -15.4% (레버리지 정리) |
| 파생·심리 | 옵션 스큐 | -1 | -1 | +7.97 (풋 우위 확대, 전일 +5.44) |
| 매크로 | 나스닥 | -1 | -1 | 50일선 아래 |
| 매크로 | DXY | -1 | -1 | 103.41, 20일 +1.5% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 159.88 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -4 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 25136.27 | 25366.09 | pt | 2026-11-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | 2.27 | 2.27 | % | 2026-11-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26350.07 | 26350.07 | pt | 2026-11-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 103.41 | 103.17 | pt | 2026-11-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.54 | 1.54 | % | 2026-11-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 159.875 | 159.734 | 엔 | 2026-11-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | 1.51 | 1.51 | % | 2026-11-13 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.08 | 4.02 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.87 | 2.79 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.65 | 3.44 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.12 | 3.03 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -4 | -4 |  | 2026-11-15 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 7.933 | 7.61 | % | 2026-11-15 06:57 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.206 | 2.2984 | 조$ | 2026-11-15 06:57 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | -185.5 | -284.0 | 백만$ | 2026-11-13 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 7거래일 연속 순유출 / 집계 기준일 2026-11-13 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -143.5 | -203.8 | 백만$ | 2026-11-13 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -1065.4 | -1438.1 | 백만$ | 2026-11-13 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | -7 | -5 | 일 | 2026-11-13 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 64118.79 | 68236.54 | USD | 2026-11-14 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 19.95 | 24.73 |  | 2026-11-14 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -15.36 | -9.9 | % | 2026-11-14 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.24 | 3.46 | 십억$ | 2026-11-14 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -14.47 | -10.62 | % | 2026-11-14 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 2.39 | 2.83 | 배 | 2026-11-14 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 56.7 | 90.0 | 백분위 | 2026-11-14 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | -0.0038 | 0.0047 | % | 2026-11-15 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | -0.0 | 0.0004 | % | 2026-11-15 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 44.35 | 41.99 |  | 2026-11-15 06:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 7.97 | 5.44 | vol pt | 2026-11-15 06:59 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-12-25, 콜 BTC-25DEC26-72000-C / 풋 BTC-25DEC26-60000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.6908 | 0.7119 |  | 2026-11-08 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 0.992 | 1.0008 |  | 2026-11-08 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 64335.0 | 68042.0 | $ | 2026-11-08 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 63821.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 16820.5 | 26738.3 | BTC | 2026-11-14 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 20196.6 | 28867.8 | BTC | 2026-11-14 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -2852.0 | -4017.0 | BTC | 2026-11-14 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 84.4 | 77.8 | 백분위 | 2026-11-14 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -3376.2 | -2129.5 | BTC | 2026-11-14 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | 1.64 | 1.8 | % | 2026-11-14 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2720719.0 | 2723962.0 | BTC | 2026-11-14 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (11-14 18:00 ~ 11-15 15:59 KST)

피드 상태: CoinDesk: 7건 / The Block: 3건 / Cointelegraph: 3건 / 블록미디어: 10건

- [Cointelegraph] RWA protocol stUSDT winds down three years after $2.3B TVL peak (11-15 15:27) — https://cointelegraph.com/news/rwa-protocol-stusdt-winds-down-three-years-after-23b-tvl-peak?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 누가 비트코인 매도 버튼을 눌렀나? 미국에서 시작한 ‘블랙 위크엔드’ (11-15 15:06) — https://www.blockmedia.co.kr/archives/1166068?utm_source=general&utm_medium=rss
- [블록미디어] 비트코인 바닥은 어디? 호건 “2018년 침체기 닮아”…킬라, 3가지 시나리오(종합) (11-15 14:14) — https://www.blockmedia.co.kr/archives/1166066?utm_source=general&utm_medium=rss
- [블록미디어] [C리더스] 공화당과 손잡은 민주당 길리브랜드…크립토 규제 입법의 가교 (11-15 13:40) — https://www.blockmedia.co.kr/archives/1163485?utm_source=general&utm_medium=rss
- [블록미디어] [C리더스] 美 민주당의 크립토 협력파 파파스…클래리티법에 주목 (11-15 13:40) — https://www.blockmedia.co.kr/archives/1163426?utm_source=general&utm_medium=rss
- [블록미디어] [C리더스] “스테이블코인이 美 국채 수요 늘린다”…지니어스법 주도한 해거티 (11-15 13:40) — https://www.blockmedia.co.kr/archives/1163487?utm_source=general&utm_medium=rss
- [블록미디어] [C리더스] “은행 문턱 낮춰야”…크립토 기업 금융 접근권 강조한 앤디 바 (11-15 13:40) — https://www.blockmedia.co.kr/archives/1163428?utm_source=general&utm_medium=rss
- [블록미디어] [C리더스] 루미스 뒤 잇는 헤이그먼…와이오밍의 비트코인 정책 계승하나 (11-15 13:40) — https://www.blockmedia.co.kr/archives/1163434?utm_source=general&utm_medium=rss
- [블록미디어] [C리더스] “비트코인은 국가 필수자산”…美 전략비축 설계자 루미스의 퇴장 (11-15 13:40) — https://www.blockmedia.co.kr/archives/1163468?utm_source=general&utm_medium=rss
- [블록미디어] [C리더스] “가상자산은 특별하지 않다”…美 상원 복귀한 셰러드 브라운 (11-15 13:40) — https://www.blockmedia.co.kr/archives/1163449?utm_source=general&utm_medium=rss
- [블록미디어] [C리더스] 美 은행위원장 유력 워런 “부실한 크립토법, 없는 것보다 나빠”…감독 강화 예고 (11-15 13:40) — https://www.blockmedia.co.kr/archives/1163477?utm_source=general&utm_medium=rss
- [CoinDesk] XRP crashes to its lowest since November 2024 as money leaves crypto (11-15 11:50) — https://www.coindesk.com/markets/2026/11/15/xrp-crashes-to-its-lowest-since-november-2024-as-money-leaves-crypto
- [The Block] Kava Lend loses roughly $3.8 million to hack, sending KAVA token down nearly 40% (11-15 08:07) — https://www.theblock.co/news/defi/2026-11-14-kava-lend-loses-roughly-3-8-million-to-hack-sending-kava-token-down-nearly-40-440350
- [The Block] Louisiana AG calls CFTC chair an ‘obsequious standard bearer’ for prediction markets following agency lawsuit (11-15 04:06) — https://www.theblock.co/news/regulation/2026-11-14-louisiana-ag-calls-cftc-chair-an-obsequious-standard-bearer-for-prediction-markets-following-agency-lawsuit-440342
- [The Block] Bitcoin ETFs lose $1 billion for the second week in a row as crypto funds, except one, continue bleeding (11-15 02:50) — https://www.theblock.co/news/markets/2026-11-14-bitcoin-etfs-lose-1-billion-for-the-second-week-in-a-row-as-crypto-funds-except-one-continue-bleeding-440337
- [CoinDesk] Bitcoin crashes to 3-month low below $63,000 as analyst flags fourth capitulation wave (11-15 01:33) — https://www.coindesk.com/markets/2026/11/14/bitcoin-drifts-back-to-usd65-000-deep-value-zone-says-analyst
- [CoinDesk] Ethereum scaling project MegaETH slashes staff by 20% as it pursues AI business (11-15 01:33) — https://www.coindesk.com/business/2026/11/14/ethereum-scaling-project-megaeth-slashes-staff-by-20-as-it-pursues-ai-business
- [CoinDesk] Kazakhstan plans tokenized government bonds in first quarter after $22 million note sale (11-15 00:38) — https://www.coindesk.com/business/2026/11/14/kazakhstan-plans-tokenized-government-bonds-in-first-quarter-after-usd22-million-note-sale
- [CoinDesk] UK, Singapore, and Thailand central banks test cross-border FX settlement as stablecoins gain ground (11-15 00:00) — https://www.coindesk.com/policy/2026/11/14/uk-singapore-and-thailand-central-banks-test-cross-border-fx-settlement-as-stablecoins-gain-ground
- [CoinDesk] Britain could turn wasted Scottish wind power into bitcoin to cut its $1.3 billion grid bill (11-14 22:00) — https://www.coindesk.com/policy/2026/11/13/britain-could-turn-wasted-scottish-wind-power-into-bitcoin-to-cut-its-usd1-3-billion-grid-bill
- [CoinDesk] A behind the scenes force may amplify bitcoin and ether price volatility (11-14 21:57) — https://www.coindesk.com/markets/2026/11/14/a-behind-the-scenes-force-may-amplify-bitcoin-and-ether-price-volatility
- [Cointelegraph] Here’s what happened in crypto today (11-14 20:28) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Microsoft confirms global outage resolved, rules out cyberattack (11-14 19:34) — https://cointelegraph.com/news/microsoft-365-outage-resolved-cyberattack-ruled-out?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

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