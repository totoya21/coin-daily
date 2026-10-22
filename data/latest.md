# 코인 데일리 스냅샷

- 수집 시각: 2026-10-22 10:11 KST
- 결과: 성공 34 / 실패·검증필요 5 / 수동 1 (전체 40)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 16.0 / 3일 평균 2.8 / 오늘 구간 '중립'
- 판정 가능 지표 14/17개 (82%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | 12.5 |
| 파생·심리 | 30% | 20.0 |
| 밸류에이션 | 25% | 25.0 |
| 매크로 | 15% | 0.0 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.94 |
| 밸류에이션 | 가격÷STH-RP | +0 | +0 | 가격÷STH-RP 1.102 |
| 수급 | 현물 ETF 순유입 | +1 | +1 | 5일 합 +211백만$ |
| 수급 | 거래소 순유입(7일) | -1 | -1 | 7일 순유입 분포 84백분위 |
| 수급 | 거래소 보유량(30일) | +1 | +1 | 30일 -1.46% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | +0 | +0 | 7일 -3.0% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0020% |
| 파생·심리 | RSI(14) | +0 | +0 | RSI 56.7 |
| 파생·심리 | 롱/숏 비율 | +1 | -1 | 롱/숏 분포 17백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +0 | OI 7일 +6.4%, 가격 +3.0% |
| 파생·심리 | 옵션 스큐 | +0 | -1 | +2.88 |
| 매크로 | 나스닥 | +1 | -1 | 50일선 위 |
| 매크로 | DXY | -1 | -1 | 101.70, 20일 +0.6% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 158.14 |
| 매크로 | CPI·PCE | 제외 | -1 | 발표 후 30일 이내 지표 없음 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 26702.857 | 26424.82 | pt | 2026-10-21 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | 0.04 | -2.87 | % | 2026-10-21 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26627.56 | 26622.41 | pt | 2026-10-21 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 101.697 | 101.73 | pt | 2026-10-21 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 0.59 | 1.18 | % | 2026-10-21 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 158.14 | 158.268 | 엔 | 2026-10-22 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | 0.12 | -0.04 | % | 2026-10-22 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 |  | 4.02 |  |  | fail | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | Expecting value: line 1 column 1 (char 0) |
| A.매크로 | 근원 CPI 전년비 |  | 2.79 |  |  | fail | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | Expecting value: line 1 column 1 (char 0) |
| A.매크로 | PCE 전년비 |  | 3.42 |  |  | fail | [FRED](https://fred.stlouisfed.org/series/PCEPI) | Expecting value: line 1 column 1 (char 0) |
| A.매크로 | 근원 PCE 전년비 |  | 3.01 |  |  | fail | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | Expecting value: line 1 column 1 (char 0) |
| B.자금흐름 | 테더 도미넌스 | 6.447 | 6.532 | % | 2026-10-22 01:09 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.8296 | 2.7898 | 조$ | 2026-10-22 01:09 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | 23.2 | 526.6 | 백만$ | 2026-10-20 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 2거래일 연속 순유입 / 집계 기준일 2026-10-20 |
| B.자금흐름 | IBIT(블랙록) 순유입 | 29.9 | 665.2 | 백만$ | 2026-10-20 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | 211.0 | 363.4 | 백만$ | 2026-10-20 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | 2 | 1 | 일 | 2026-10-20 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 84024.67 | 82938.26 | USD | 2026-10-21 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 56.71 | 52.63 |  | 2026-10-21 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | 3.01 | -0.2 | % | 2026-10-21 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.53 | 3.19 | 십억$ | 2026-10-21 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | 6.44 | -1.35 | % | 2026-10-21 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 1.17 | 1.21 | 배 | 2026-10-21 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 16.7 | 70.0 | 백분위 | 2026-10-21 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | -0.0047 | 0.0034 | % | 2026-10-22 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.002 | 0.0053 | % | 2026-10-22 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 37.12 | 37.21 |  | 2026-10-22 01:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 2.88 | 3.43 | vol pt | 2026-10-22 01:11 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-11-27, 콜 BTC-27NOV26-92000-C / 풋 BTC-27NOV26-79000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.9432 | 0.9213 |  | 2026-10-15 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.102 | 1.0932 |  | 2026-10-15 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 76581.0 | 75900.0 | $ | 2026-10-15 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 84392.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 22038.2 | 16537.6 | BTC | 2026-10-20 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 21756.0 | 15578.3 | BTC | 2026-10-20 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | 1173.4 | 499.1 | BTC | 2026-10-20 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 84.4 | 84.4 | 백분위 | 2026-10-20 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | 282.2 | 959.3 | BTC | 2026-10-20 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -1.46 | -1.36 | % | 2026-10-20 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2681408.0 | 2680975.0 | BTC | 2026-10-20 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (10-21 18:00 ~ 10-22 10:11 KST)

피드 상태: CoinDesk: 12건 / The Block: 11건 / Cointelegraph: 21건 / 블록미디어: 10건

- [블록미디어] XRP, 11월 말 4달러 전망 나왔다…7차례 막힌 저항선 돌파가 관건 (10-22 09:51) — https://www.blockmedia.co.kr/archives/1154711?utm_source=general&utm_medium=rss
- [Cointelegraph] PHP Foundation admits ‘structural failure’ delayed critical security fix (10-22 09:44) — https://cointelegraph.com/news/php-foundation-admits-structural-failure-delayed-critical-security-fix?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] [개장시황] 코스피, 전날 3%대 급등 후 숨고르기…5700선 등락 (10-22 09:20) — https://www.blockmedia.co.kr/archives/1154700?utm_source=general&utm_medium=rss
- [블록미디어] 김민석 “디지털자산 과세 연내 결론…정부에 최종 점검 요청” (10-22 09:10) — https://www.blockmedia.co.kr/archives/1154692?utm_source=general&utm_medium=rss
- [The Block] Aerodrome and Velodrome merge to launch Aero across seven blockchain networks (10-22 09:00) — https://www.theblock.co/news/defi/2026-10-21-aerodrome-velodrome-merge-aero-421514
- [블록미디어] [코인시황] 비트코인 8만4000달러 돌파…美 기술주 반등에 상승세 (10-22 08:13) — https://www.blockmedia.co.kr/archives/1154682?utm_source=general&utm_medium=rss
- [블록미디어] 비트코인 반등에 파생시장 55조원 몰렸다…레버리지 투자 다시 꿈틀 (10-22 08:13) — https://www.blockmedia.co.kr/archives/1154677?utm_source=general&utm_medium=rss
- [블록미디어] 美 스테이블코인 규제 완화에 업계 환호…은행권은 “예금 이탈” 반발 (10-22 07:41) — https://www.blockmedia.co.kr/archives/1154670?utm_source=general&utm_medium=rss
- [블록미디어] 머스크 “미국 5경원 빚, AI·로봇만이 해법”…비트코인 대안론도 부상 (10-22 07:15) — https://www.blockmedia.co.kr/archives/1154663?utm_source=general&utm_medium=rss
- [블록미디어] 트럼프, 10억달러 동결 발표… ‘디지털자산’ 직접 언급 피해 (10-22 06:54) — https://www.blockmedia.co.kr/archives/1154661?utm_source=general&utm_medium=rss
- [Cointelegraph] American Bankers Association: OCC’s GENIUS rules ‘undermine’ US Congress (10-22 06:53) — https://cointelegraph.com/news/american-bankers-association-occ-genius-rules-stablecoins?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 스페이스X·테슬라 합병 추진…기업가치 4655조원 ‘초대형 AI 공룡’ 탄생하나 (10-22 06:43) — https://www.blockmedia.co.kr/archives/1154658?utm_source=general&utm_medium=rss
- [블록미디어] [뉴욕 금·채권·달러] FOMC 앞두고 혼조…미 국채금리 5.12%·금 4139달러 상승 (10-22 06:31) — https://www.blockmedia.co.kr/archives/1154654?utm_source=general&utm_medium=rss
- [Cointelegraph] Tether backs Bolivian fintech bringing USDT payments to food delivery and banking (10-22 05:26) — https://cointelegraph.com/news/tether-backs-bolivian-fintech-bringing-usdt-payments-to-food-delivery-and-banking?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Trump didn‘t mention ‘crypto’ once in White House cybercrime roundtable (10-22 05:19) — https://cointelegraph.com/news/white-house-cybercrime-roundtable-donald-trump-crypto-ventures?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Here’s what happened in crypto today (10-22 05:10) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Robinhood single-stock perps could be a ‘strong positive’ for HOOD shares, Mizuho says (10-22 03:54) — https://www.theblock.co/news/business/2026-10-21-robinhood-single-stock-perpetual-futures-mizuho-survey-421639
- [The Block] American Bankers Association accuses OCC of undermining Congress with final stablecoin rewards rule (10-22 02:59) — https://www.theblock.co/news/regulation/2026-10-21-american-bankers-association-accuses-occ-undermining-congress-stablecoin-rewards-rule-421629
- [Cointelegraph] Cardano Foundation urges EU against expanding MiCA rules to DeFi and staking (10-22 02:57) — https://cointelegraph.com/news/cardano-foundation-urges-eu-against-expanding-mica-rules-to-defi-and-staking?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] UK financial watchdog opens consultations for DeFi guidance, crypto laws (10-22 02:25) — https://cointelegraph.com/news/uk-fca-consultations-defi-crypto-laws?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Treasury Secretary Bessent likens GENIUS Act to Lincoln-era banking reform (10-22 02:10) — https://cointelegraph.com/news/occ-finalizes-stablecoin-rules-genius-act-bessent?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Dataline raises $10.6 million for decentralized data network for AI agents, plans ICO (10-22 01:44) — https://www.theblock.co/news/deals/2026-10-21-dataline-decentralized-data-network-ai-agents-funding-ico-421596
- [CoinDesk] Trump to throw spotlight on overseas crypto abuses at White House event (10-22 01:23) — https://www.coindesk.com/policy/2026/10/21/trump-to-throw-spotlight-on-overseas-crypto-abuses-in-white-house-event
- [Cointelegraph] Chainlink, Cardano, other blockchain groups push SEC for clearer crypto rules (10-22 01:09) — https://cointelegraph.com/news/chainlink-cardano-and-other-blockchain-groups-push-sec-for-clearer-crypto-rules?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] How a16z-backed DATA is rethinking its blockchain strategy after $30 million Sui deal (10-22 00:22) — https://www.coindesk.com/business/2026/10/21/how-a16z-backed-data-is-rethinking-its-blockchain-strategy-after-usd30-million-sui-deal
- [Cointelegraph] Bitcoin price tags $84.6K as US stocks head higher on SpaceX Q3 earnings beat (10-22 00:13) — https://cointelegraph.com/markets/bitcoin-price-tags-846k-as-us-stocks-head-higher-on-spacex-q3-earnings-beat?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Grayscale expands in-kind subscriptions to 10 crypto ETFs and trusts (10-22 00:12) — https://www.theblock.co/news/markets/2026-10-21-grayscale-expands-in-kind-subscriptions-10-crypto-etfs-421559
- [CoinDesk] Bybit will look for big broker partnerships to take on Robinhood in the U.S. (10-22 00:09) — https://www.coindesk.com/business/2026/10/16/bybit-will-look-for-big-broker-partnerships-to-take-on-robinhood-in-the-u-s
- [CoinDesk] Crypto Long & Short: Why real-world assets need fixed-rate loans onchain (10-22 00:00) — https://www.coindesk.com/coindesk-indices/2026/10/21/crypto-long-and-short-why-real-world-assets-need-fixed-rate-loans-onchain
- [The Block] Anza’s Alpenglow goes live on Solana, cutting finality to 150 milliseconds (10-21 23:24) — https://www.theblock.co/news/ecosystems/2026-10-21-anzas-alpenglow-goes-live-on-solana-cutting-finality-to-150-milliseconds-421508
- [Cointelegraph] Solana’s Alpenglow launches on mainnet, targets 99% faster finality (10-21 22:57) — https://cointelegraph.com/news/solanas-alpenglow-launches-mainnet-99-faster-finality?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Big Tech’s eMudhra fixes may leave crypto bots exposed, CertiK warns (10-21 22:31) — https://cointelegraph.com/news/certik-warning-crypto-emudhra-flaw-risks?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] 5 alternatives to Ledger to store your Bitcoin (10-21 22:30) — https://cointelegraph.com/magazine/5-alternatives-to-ledger-to-store-your-bitcoin?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Standard Chartered signs definitive agreements to acquire Zodia Custody (10-21 21:44) — https://www.theblock.co/news/business/2026-10-21-standard-chartered-signs-definitive-agreements-to-acquire-zodia-custody-421535
- [Cointelegraph] OCC finalizes GENIUS Act rules for stablecoin issuers and custody (10-21 21:26) — https://cointelegraph.com/news/occ-finalizes-genius-act-rules-stablecoin-issuers-custody?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Why centralized exchanges refuse to list legacy crypto tokens without explicit SEC immunity (10-21 21:12) — https://www.coindesk.com/policy/2026/10/21/why-centralized-exchanges-refuse-to-list-legacy-crypto-tokens-without-explicit-sec-immunity
- [CoinDesk] Japanese visitors may be able to pay with yen stablecoins in South Korea under Shinhan-SBI pact (10-21 21:10) — https://www.coindesk.com/business/2026/10/21/japanese-visitors-may-be-able-to-pay-with-yen-stablecoins-in-south-korea-under-shinhan-sbi-pact
- [Cointelegraph] Standard Chartered signs definitive deal to acquire Zodia Custody (10-21 21:06) — https://cointelegraph.com/news/standard-chartered-acquire-zodia-custody-uk?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Dogecoin wallet, app teams unite in push to give DOGE more everyday uses (10-21 21:00) — https://www.coindesk.com/tech/2026/10/21/dogecoin-wallet-app-teams-unite-in-push-to-give-doge-more-everyday-uses
- [The Block] Dogecoin Labs launches as DOGE ecosystem seeks growth beyond meme-driven demand (10-21 21:00) — https://www.theblock.co/news/business/2026-10-21-dogecoin-labs-launch-mydoge-dogeos-such-app-421469
- [The Block] Bitcoin volatility nears 2026 lows as traders brace for Fed decision and US midterms (10-21 20:55) — https://www.theblock.co/news/markets/2026-10-21-bitcoin-volatility-nears-2026-lows-as-traders-brace-for-fed-decision-and-us-midterms-421524
- [CoinDesk] Bitcoin risk management grows more popular as the 'just bet on price' era fades (10-21 20:15) — https://www.coindesk.com/daybook-us/2026/10/21/bitcoin-risk-management-grows-more-popular-as-the-just-bet-on-price-era-fades
- [The Block] First out the gate: OCC debuts final rule implementing Trump-signed GENIUS Act (10-21 20:01) — https://www.theblock.co/news/regulation/2026-10-21-occ-final-rule-implementing-trump-signed-genius-act-421470
- [CoinDesk] OCC's final rule to start fresh in weighing stablecoin rewards against GENIUS Act ban (10-21 20:00) — https://www.coindesk.com/policy/2026/10/21/occ-s-final-rule-to-start-fresh-in-weighing-stablecoin-rewards-against-genius-act-ban
- [The Block] BitGo launches innovation unit to design crypto’s next breakout application (10-21 20:00) — https://www.theblock.co/news/business/2026-10-21-bitgo-launches-research-unit-421502
- [Cointelegraph] PancakeSwap TVL tops $380M as major fee overhaul heads to vote (10-21 19:50) — https://cointelegraph.com/markets/pancakeswap-tvl-jumps-19-percent-fee-overhaul?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] France proposes liability for crypto exchanges offering DeFi access (10-21 19:46) — https://cointelegraph.com/news/france-liability-crypto-exchange-defi-access?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin ‘top buyers’ halt BTC price upside with $87.7K now key: Glassnode (10-21 19:39) — https://cointelegraph.com/markets/bitcoin-top-buyers-halt-btc-price-upside-with-877k-now-key-glassnode?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Crypto rises with Asian tech stocks, zcash extends gain after setting upgrade date (10-21 19:34) — https://www.coindesk.com/markets/2026/10/21/crypto-rises-with-asian-tech-stocks-zcash-extends-gain-after-setting-upgrade-date
- [CoinDesk] Live updates: Bitcoin holds above $84,000 as Middle East worries resurface (10-21 19:30) — https://www.coindesk.com/markets/2026/10/21/live-updates-bitcoin-clings-to-usd82-500-as-spacex-results-lift-stock-futures
- [Cointelegraph] Shinhan, SBI make Japan-Korea tourist spending a test case for yen stablecoins (10-21 19:22) — https://cointelegraph.com/news/shinhan-sbi-japan-korea-travel-yen-stablecoin?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Zcash rallies 12% as developers finalize NU7 activation height (10-21 19:15) — https://cointelegraph.com/markets/zcash-zec-rallies-12-percent-nu7-mainnet-upgrade?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Drift exploiter sends $109M in Ether to Tornado Cash in 2 days (10-21 19:13) — https://cointelegraph.com/news/drift-exploiter-moves-109m-eth-tornado-cash-2-days?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] SpaceX and Tesla explore merger that would unite more than 30,000 bitcoin (10-21 18:23) — https://www.coindesk.com/markets/2026/10/21/spacex-and-tesla-explore-merger-that-would-unite-more-than-30-000-bitcoin

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

- CPI 전년비 (FRED): Expecting value: line 1 column 1 (char 0)
- 근원 CPI 전년비 (FRED): Expecting value: line 1 column 1 (char 0)
- PCE 전년비 (FRED): Expecting value: line 1 column 1 (char 0)
- 근원 PCE 전년비 (FRED): Expecting value: line 1 column 1 (char 0)
- 고래비율(근사) (Arkham + Coin Metrics): Arkham 키 없음