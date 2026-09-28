# 코인 데일리 스냅샷

- 수집 시각: 2026-09-28 09:48 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 매수** → BTC 목표 비중 **80%** (전일 판정: 매수)
- 오늘 총점 23.1 / 3일 평균 25.3 / 오늘 구간 '매수'
- 판정 가능 지표 14/17개 (82%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | 83.3 |
| 파생·심리 | 30% | 0.0 |
| 밸류에이션 | 25% | 0.0 |
| 매크로 | 15% | -12.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.93 |
| 밸류에이션 | 가격÷STH-RP | -1 | +0 | 가격÷STH-RP 1.200 |
| 수급 | 현물 ETF 순유입 | +2 | +2 | 7거래일 연속 순유입 |
| 수급 | 거래소 순유입(7일) | +2 | +2 | 7일 순유입 분포 1백분위 |
| 수급 | 거래소 보유량(30일) | +1 | +1 | 30일 -0.55% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | 제외 | — | 7일 전 값 없음 |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0006% |
| 파생·심리 | RSI(14) | -1 | -1 | RSI 65.1 |
| 파생·심리 | 롱/숏 비율 | +0 | +0 | 롱/숏 분포 53백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +0 | OI 7일 -1.9%, 가격 +4.1% |
| 파생·심리 | 옵션 스큐 | +0 | -1 | +0.64 |
| 매크로 | 나스닥 | +1 | +1 | 50일선 위 |
| 매크로 | DXY | -1 | -1 | 100.97, 20일 +1.8% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 157.75 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -1 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 27068.721 | 26939.369 | pt | 2026-09-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | 2.06 | 2.06 | % | 2026-09-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26169.53 | 26169.53 | pt | 2026-09-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 100.97 | 101.29 | pt | 2026-09-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.83 | 1.83 | % | 2026-09-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 157.754 | 158.811 | 엔 | 2026-09-28 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | 0.45 | 0.09 | % | 2026-09-28 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 3.71 | 3.54 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-09-11 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.76 | 2.79 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-09-11 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.7 | 3.72 | % | 2026-07-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-08-26 (점수 미반영: 발표 후 30일 경과) |
| A.매크로 | 근원 PCE 전년비 | 3.34 | 3.34 | % | 2026-07-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-08-26 (점수 미반영: 발표 후 30일 경과) |
| A.매크로 | 인플레이션 방향 합계 | -1 | -1 |  | 2026-09-28 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.383 | 6.324 | % | 2026-09-28 00:42 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.8736 | 2.9035 | 조$ | 2026-09-28 00:42 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | 134.5 | 190.6 | 백만$ | 2026-09-25 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 7거래일 연속 순유입 / 집계 기준일 2026-09-25 |
| B.자금흐름 | IBIT(블랙록) 순유입 | 97.0 | 162.6 | 백만$ | 2026-09-25 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | 2385.8 | 2385.8 | 백만$ | 2026-09-25 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | 7 | 7 | 일 | 2026-09-25 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 84462.14 | 84416.65 | USD | 2026-09-27 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 65.13 | 65.02 |  | 2026-09-27 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | 4.07 | 3.92 | % | 2026-09-27 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.11 | 3.12 | 십억$ | 2026-09-27 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -1.93 | -3.07 | % | 2026-09-27 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 1.25 | 1.21 | 배 | 2026-09-27 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 53.3 | 63.3 | 백분위 | 2026-09-27 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.0046 | -0.0011 | % | 2026-09-28 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0006 | 0.0002 | % | 2026-09-28 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 35.19 | 34.9 |  | 2026-09-28 00:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 0.64 | 0.95 | vol pt | 2026-09-28 00:48 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-10-30, 콜 BTC-30OCT26-91000-C / 풋 BTC-30OCT26-79000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.9336 | 0.9372 |  | 2026-09-21 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.2 | 1.13 |  | 2026-09-21 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 70258.0 | 74679.0 | $ | 2026-09-21 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 84309.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 11569.7 | 22970.3 | BTC | 2026-09-26 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 17514.6 | 30130.3 | BTC | 2026-09-26 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -51621.6 | -47162.9 | BTC | 2026-09-26 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 1.1 | 1.1 | 백분위 | 2026-09-26 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -5944.9 | -7160.0 | BTC | 2026-09-26 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -0.55 | -0.67 | % | 2026-09-26 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2682221.0 | 2685119.0 | BTC | 2026-09-26 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (09-27 18:00 ~ 09-28 09:48 KST)

피드 상태: CoinDesk: 2건 / The Block: 2건 / Cointelegraph: 3건 / 블록미디어: 10건

- [블록미디어] [개장시황] 코스피, 美 금리 부담 속 하락 출발…7000선은 지켜 (09-28 09:21) — https://www.blockmedia.co.kr/archives/1144780?utm_source=general&utm_medium=rss
- [Cointelegraph] THORChain under fire over Bitget, ETH evolves beyond blockchain: Hodler’s Digest (09-28 08:43) — https://cointelegraph.com/magazine/thorchain-under-fire-over-bitget-hack-eth-is-beyond-blockchain-now?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] [코인시황] 비트코인, 8만4000달러대 횡보…유가 상승에 투심 부담 (09-28 08:20) — https://www.blockmedia.co.kr/archives/1144746?utm_source=general&utm_medium=rss
- [블록미디어] AI 거품론·고용 불안에 숨고르기…이번 주 미 증시 좌우할 3대 변수 (09-28 07:33) — https://www.blockmedia.co.kr/archives/1144722?utm_source=general&utm_medium=rss
- [The Block] Onchain analyst links $18.4 million in Robinhood Chain memecoin extractions to single rug-pull operation (09-28 07:02) — https://www.theblock.co/news/defi/2026-09-27-onchain-analyst-links-18-4-million-in-robinhood-chain-memecoin-extractions-to-single-rug-pull-operation-416960
- [블록미디어] 8번 모두 맞힌 침체 경고음…美 장·단기 금리 역전 임박에 금융시장 긴장 (09-28 07:02) — https://www.blockmedia.co.kr/archives/1144718?utm_source=general&utm_medium=rss
- [블록미디어] 잠긴 비트코인 다중서명 지갑 구출할까…보안·유출 갈림길 선 ‘BIP138’ (09-28 06:40) — https://www.blockmedia.co.kr/archives/1144715?utm_source=general&utm_medium=rss
- [블록미디어] 펌프펀, 퀘벡서 무등록 영업 지정… “하루아침에 자산 묶일 수도” (09-28 06:11) — https://www.blockmedia.co.kr/archives/1144712?utm_source=general&utm_medium=rss
- [블록미디어] [뉴욕 코인시황] ETF 자금 몰린 비트코인 85K 눈앞…9만달러 향하나, PCE가 변수 (09-28 05:42) — https://www.blockmedia.co.kr/archives/1144709?utm_source=general&utm_medium=rss
- [The Block] ‘It’s really not just a blockchain anymore’: Vitalik Buterin maps Ethereum’s path to 2030 (09-27 23:35) — https://www.theblock.co/news/ecosystems/2026-09-27-its-really-not-just-a-blockchain-anymore-vitalik-buterin-maps-ethereums-path-to-2030-416953
- [CoinDesk] Vitalik Buterin maps Ethereum’s shift beyond a blockchain in sweeping 2030 vision (09-27 23:29) — https://www.coindesk.com/tech/2026/09/27/vitalik-buterin-maps-ethereum-s-shift-beyond-a-blockchain-in-sweeping-2030-vision
- [Cointelegraph] Australia asks OpenAI, Anthropic chiefs to Senate inquiry on rogue hack: Report (09-27 21:46) — https://cointelegraph.com/news/australia-summons-openai-anthropic-chiefs-to-senate-inquiry-on-health-data-hack-report?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 피델리티 “비트코인 10만달러 신호 떴다…8만달러 이중바닥” (09-27 21:16) — https://www.blockmedia.co.kr/archives/1144701?utm_source=general&utm_medium=rss
- [CoinDesk] How months of work on the Clarity Act all fell apart (09-27 21:00) — https://www.coindesk.com/news-analysis/2026/09/27/how-months-of-work-on-the-clarity-act-all-fell-apart
- [블록미디어] 중국이 AI 멸망론에 미온적인 세 가지 이유–NYT (09-27 20:59) — https://www.blockmedia.co.kr/archives/1144698?utm_source=general&utm_medium=rss
- [블록미디어] “AI 버블 붕괴, 일어날 일이 일어날 때”–WSJ (09-27 19:39) — https://www.blockmedia.co.kr/archives/1144688?utm_source=general&utm_medium=rss
- [Cointelegraph] Riot Platforms repays $200M credit facility, releases collateral (09-27 18:57) — https://cointelegraph.com/news/riot-platforms-repays-200m-credit-facility-releases-collateral?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

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