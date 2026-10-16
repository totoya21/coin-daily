# 코인 데일리 스냅샷

- 수집 시각: 2026-10-16 10:07 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 -2.4 / 3일 평균 -2.6 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | -12.5 |
| 파생·심리 | 30% | -10.0 |
| 밸류에이션 | 25% | 25.0 |
| 매크로 | 15% | -12.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.96 |
| 밸류에이션 | 가격÷STH-RP | +0 | +0 | 가격÷STH-RP 1.110 |
| 수급 | 현물 ETF 순유입 | -1 | -1 | 5일 합 -374백만$ |
| 수급 | 거래소 순유입(7일) | -1 | -2 | 7일 순유입 분포 88백분위 |
| 수급 | 거래소 보유량(30일) | +1 | +1 | 30일 -1.17% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | +0 | +0 | 7일 -0.3% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0041% |
| 파생·심리 | RSI(14) | +0 | +0 | RSI 48.7 |
| 파생·심리 | 롱/숏 비율 | -1 | -2 | 롱/숏 분포 83백분위 |
| 파생·심리 | 미결제약정(OI) | +0 | +0 | OI 7일 +1.8%, 가격 +0.5% |
| 파생·심리 | 옵션 스큐 | -1 | +0 | +3.23 (풋 우위 확대, 전일 +2.41) |
| 매크로 | 나스닥 | +1 | +1 | 50일선 위 |
| 매크로 | DXY | -1 | -1 | 102.06, 20일 +1.8% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 158.16 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -2 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 26713.025 | 26692.869 | pt | 2026-10-15 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -1.77 | -3.07 | % | 2026-10-15 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26635.38 | 26628.39 | pt | 2026-10-15 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 102.062 | 102.55 | pt | 2026-10-15 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.84 | 1.89 | % | 2026-10-15 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 158.16 | 157.957 | 엔 | 2026-10-16 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | 0.06 | -0.23 | % | 2026-10-16 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.02 | 3.71 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-10-14 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.79 | 2.76 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-10-14 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.42 | 3.36 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.01 | 2.98 | % | 2026-08-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-09-30 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -2 | -2 |  | 2026-10-16 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 6.586 | 6.643 | % | 2026-10-16 01:01 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.782 | 2.7582 | 조$ | 2026-10-16 01:01 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | -261.5 | 175.6 | 백만$ | 2026-10-14 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 1거래일 연속 순유출 / 집계 기준일 2026-10-14 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -110.9 | 65.9 | 백만$ | 2026-10-14 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -374.2 | -599.8 | 백만$ | 2026-10-14 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | -1 | 1 | 일 | 2026-10-14 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 82131.46 | 81566.29 | USD | 2026-10-15 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 48.67 | 46.6 |  | 2026-10-15 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | 0.54 | -2.05 | % | 2026-10-15 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 3.36 | 3.32 | 십억$ | 2026-10-15 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | 1.81 | -0.72 | % | 2026-10-15 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 1.57 | 1.67 | 배 | 2026-10-15 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 83.3 | 96.7 | 백분위 | 2026-10-15 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.0043 | 0.0026 | % | 2026-10-16 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0041 | 0.0057 | % | 2026-10-16 00:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 38.68 | 38.89 |  | 2026-10-16 01:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 3.23 | 2.41 | vol pt | 2026-10-16 01:08 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-11-06, 콜 BTC-6NOV26-88000-C / 풋 BTC-6NOV26-78000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.9588 | 0.9304 |  | 2026-10-09 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 1.1102 | 1.0997 |  | 2026-10-09 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 74030.0 | 74182.0 | $ | 2026-10-09 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 82188.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 26132.0 | 21662.0 | BTC | 2026-10-14 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 26862.7 | 22054.1 | BTC | 2026-10-14 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | 3831.1 | 7368.1 | BTC | 2026-10-14 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 87.8 | 92.2 | 백분위 | 2026-10-14 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | -730.7 | -392.1 | BTC | 2026-10-14 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | -1.17 | -1.18 | % | 2026-10-14 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2675717.0 | 2676257.0 | BTC | 2026-10-14 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (10-15 18:00 ~ 10-16 10:07 KST)

피드 상태: CoinDesk: 10건 / The Block: 11건 / Cointelegraph: 20건 / 블록미디어: 10건

- [블록미디어] 카프리올 CEO “양자 보안 합의 시 비트코인 50% 급등 가능” (10-16 09:58) — https://www.blockmedia.co.kr/archives/1152329?utm_source=general&utm_medium=rss
- [Cointelegraph] MSCI adopts index exclusion rules that could oust Strategy (10-16 09:48) — https://cointelegraph.com/news/msci-adopts-index-exclusion-rules-that-could-oust-strategy?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] [개장시황] 코스피, 저가 매수에 1%대 반등 출발…삼전·하이닉스 동반 강세 (10-16 09:13) — https://www.blockmedia.co.kr/archives/1152328?utm_source=general&utm_medium=rss
- [Cointelegraph] Australia releases draft bill to adopt OECD crypto tax reporting framework (10-16 08:34) — https://cointelegraph.com/news/australia-releases-draft-bill-to-adopt-oecd-crypto-tax-reporting-framework?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] [코인시황] 비트코인, 美 국채금리 하락·증시 반등에 8만2000달러선 회복 (10-16 08:23) — https://www.blockmedia.co.kr/archives/1152310?utm_source=general&utm_medium=rss
- [블록미디어] 인젝티브 10% 급등…블록체인 수익성 지표서 솔라나·이더리움 제쳤다 (10-16 08:10) — https://www.blockmedia.co.kr/archives/1152307?utm_source=general&utm_medium=rss
- [블록미디어] 슈퍼폼, 토큰화 주식 수익 구조 공개…청산 위험 자동 관리 (10-16 08:03) — https://www.blockmedia.co.kr/archives/1151796?utm_source=general&utm_medium=rss
- [Cointelegraph] Scammer loses $4.8M stored on tampered Ledgers: Asia Express (10-16 07:42) — https://cointelegraph.com/magazine/scammer-loses-48m-stored-on-tampered-ledgers-asia-express?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 스트래티지, MSCI 지수 퇴출 위기…최대 16조원 매도 폭탄 우려 (10-16 07:35) — https://www.blockmedia.co.kr/archives/1152303?utm_source=general&utm_medium=rss
- [The Block] MSCI finalizes index rules that put Strategy, crypto treasury firms at risk of exclusion (10-16 07:15) — https://www.theblock.co/news/business/2026-10-15-msci-rules-could-exclude-strategy-mstr-from-indexes-418729
- [블록미디어] 사기범도 털렸다…변조된 레저 지갑에 480만달러 날려 (10-16 06:56) — https://www.blockmedia.co.kr/archives/1152298?utm_source=general&utm_medium=rss
- [블록미디어] 비트코인 신규 매수…주요 상장사 2곳이 독식 (10-16 06:44) — https://www.blockmedia.co.kr/archives/1152293?utm_source=general&utm_medium=rss
- [The Block] Farcaster acquired by Balaji’s Network School, with new ‘social smart contract’ for users (10-16 06:41) — https://www.theblock.co/news/ecosystems/2026-10-15-network-school-acquires-farcaster-from-neynar-418720
- [블록미디어] 비트코인 8만달러 매수벽 소진에도 반등…글래스노드 “하단 지지력 다시 약화” (10-16 06:24) — https://www.blockmedia.co.kr/archives/1152285?utm_source=general&utm_medium=rss
- [블록미디어] [뉴욕 금·채권·달러] 미국 물가 상승에도 달러·국채금리 동반 하락…금값 1.57%↑ (10-16 06:21) — https://www.blockmedia.co.kr/archives/1152280?utm_source=general&utm_medium=rss
- [Cointelegraph] Binance.US seeks $1B valuation in potential $100M funding round: Report (10-16 05:21) — https://cointelegraph.com/news/binance-us-funding-valuation-billion?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Here’s what happened in crypto today (10-16 04:37) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] At the White House, crypto policy vacancy looms large (10-16 03:48) — https://www.coindesk.com/news-analysis/2026/10/15/at-the-white-house-crypto-policy-vacancy-looms-large
- [Cointelegraph] Ex-Trump crypto adviser profited after helping pass stablecoin bill: WSJ (10-16 02:14) — https://cointelegraph.com/news/bo-hines-donald-trump-crypto-advisor-nxum-tether-conflict?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Sweden revisits digital krona as ECB advances digital euro plans (10-16 01:49) — https://cointelegraph.com/news/sweden-riksbank-digital-krona-cbdc-legislation?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] CleanSpark and BitFuFu see bitcoin production slip in September as Canaan remains flat (10-16 01:06) — https://www.theblock.co/news/business/2026-10-15-cleanspark-bitfufu-bitcoin-production-slip-september-canaan-remains-flat-418686
- [The Block] Multiliquid, a settlement platform for tokenized assets, raises $8 million (10-16 01:00) — https://www.theblock.co/news/deals/2026-10-15-multiliquid-tokenized-assets-funding-418693
- [The Block] DeFi Development boosts CHAD dividend to 14% amid push to grow Solana holdings (10-16 00:48) — https://www.theblock.co/news/markets/2026-10-15-defi-development-chad-dividend-rate-14-418694
- [Cointelegraph] Mastercard brings stablecoin balances into traditional banking and card payments (10-16 00:46) — https://cointelegraph.com/news/mastercard-bvnk-global-money-platform-stablecoins?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Bitcoin slips under $80K after US PPI gains most in four years (10-16 00:10) — https://cointelegraph.com/markets/bitcoin-price-breaks-under-80k-after-us-ppi-gains-most-in-over-4-years?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Crypto for Advisors: Wall Street is done waiting on Congress for crypto rules (10-16 00:00) — https://www.coindesk.com/coindesk-indices/2026/10/15/crypto-for-advisors-wall-street-is-done-waiting-on-congress-for-crypto-rules
- [The Block] Ripple Prime adds RWA swaps referencing perpetual futures listed on Hyperliquid (10-15 23:43) — https://www.theblock.co/news/business/2026-10-15-ripple-prime-rwa-swaps-perpetual-futures-hyperliquid-418681
- [The Block] Starknet opens seven-day vote on independent Layer 1 over quantum risks (10-15 23:26) — https://www.theblock.co/news/ecosystems/2026-10-15-starknet-opens-seven-day-vote-on-independent-layer-1-over-quantum-risks-418673
- [Cointelegraph] Russia to ban direct peer-to-peer crypto trades starting July 2027 (10-15 23:22) — https://cointelegraph.com/news/russia-ban-p2p-crypto-trades-july-2027?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Nasdaq-listed Tron sets up $200M ATM share offering to fuel TRX acquisitions (10-15 23:16) — https://cointelegraph.com/news/nasdaq-tron-200m-atm-offering-fuel-trx-acquisitions?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Bitwise CIO argues bitcoin will benefit whether AI booms or busts (10-15 23:01) — https://www.theblock.co/news/markets/2026-10-15-bitwise-cio-argues-bitcoin-will-benefit-whether-ai-booms-or-busts-418668
- [Cointelegraph] Can the SEC and CFTC’s pro-crypto rules be overturned? Legal opinion (10-15 22:30) — https://cointelegraph.com/magazine/can-the-sec-and-cftcs-pro-crypto-rules-be-overturned-legal-opinion?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Helius CEO Mert Mumtaz joins NEAR Foundation Council (10-15 22:00) — https://www.theblock.co/news/business/2026-10-15-helius-ceo-mert-mumtaz-joins-near-foundation-council-418656
- [CoinDesk] How Brooklyn prosecutors and the FBI took down a massive crypto fraud network targeting Russian speakers (10-15 21:35) — https://www.coindesk.com/business/2026/10/15/how-brooklyn-prosecutors-and-the-fbi-took-down-a-massive-crypto-fraud-network-targeting-russian-speakers
- [Cointelegraph] HEX token sellers erase $160M following reports of founder Richard Schueler arrest (10-15 21:12) — https://cointelegraph.com/news/hex-token-erases-160m-reports-founder-schuelers-arrest?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Under pressure, Ledger unveils plan to turn its crypto hardware wallet into a smartphone (10-15 21:00) — https://www.coindesk.com/tech/2026/10/15/under-pressure-ledger-unveils-plan-to-turn-its-crypto-hardware-wallet-into-a-smartphone
- [The Block] Ledger unveils Atom Android device with Solana Mobile integration and new tamper protections amid investigation into modified wallets (10-15 21:00) — https://www.theblock.co/news/business/2026-10-15-ledger-atom-solana-mobile-418644
- [Cointelegraph] Ledger’s answer to wallet tampering costs $849 and ships next year (10-15 21:00) — https://cointelegraph.com/news/ledger-new-hardware-device-asia-wallet-tampering?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bitcoin, copper, stocks, yields all fall; gold rises (10-15 20:15) — https://www.coindesk.com/daybook-us/2026/10/15/bitcoin-copper-stocks-yields-all-fall-gold-rises
- [The Block] EBA designates Circle’s USDC as the EU’s first ‘significant’ e-money token (10-15 20:10) — https://www.theblock.co/news/regulation/2026-10-15-eba-designates-circles-usdc-as-the-eus-first-significant-e-money-token-418637
- [CoinDesk] Altcoins lead crypto declines as Asian stocks drop; bitcoin little changed since midnight (10-15 19:52) — https://www.coindesk.com/markets/2026/10/15/bitcoin-holds-above-usd80-000-as-an-asian-stock-rout-drags-altcoins-lower
- [Cointelegraph] White House crypto council chief Patrick Witt steps down (10-15 19:41) — https://cointelegraph.com/news/white-house-crypto-council-director-steps-down?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Starknet opens vote on potential Ethereum L2 exit over quantum risks (10-15 19:22) — https://cointelegraph.com/news/starknet-vote-ethereum-l2-exit-post-quantum-l1?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Live updates: Bitcoin bounces back to $82,000 after first fall below $80,000 in one month (10-15 19:16) — https://www.coindesk.com/business/2026/10/15/live-updates-bitcoin-back-under-usd81-000-as-ai-selloff-worsens
- [CoinDesk] Hyperliquid founder wants U.S. oversight of trading platforms, not his blockchain (10-15 19:00) — https://www.coindesk.com/policy/2026/10/15/hyperliquid-founder-wants-u-s-oversight-of-trading-platforms-not-his-blockchain
- [Cointelegraph] Bitget, Liquid exploits push Q3 crypto hacks toward $1.2B (10-15 19:00) — https://cointelegraph.com/news/bitget-liquid-exploits-push-crypto-hacks-near-12b-q3?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Australia’s financial watchdog seeks stiffer rules for crypto exchanges ahead of licensing deadline (10-15 18:53) — https://www.coindesk.com/policy/2026/10/15/australia-s-financial-watchdog-seeks-stiffer-rules-for-crypto-exchanges-ahead-of-licensing-deadline
- [Cointelegraph] Bitcoin dips to $80.1K as KOSPI closes at its lowest since April (10-15 18:48) — https://cointelegraph.com/markets/bitcoin-dips-korea-kospi-lowest-close-since-april?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Thailand crypto ETFs may see slow start despite new rules: CoinShares (10-15 18:36) — https://cointelegraph.com/news/thailand-crypto-etfs-slow-start-new-rules-coinshares?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Hex founder Richard Heart arrested in Istanbul, Turkish media report (10-15 18:20) — https://www.coindesk.com/policy/2026/10/15/hex-founder-richard-heart-arrested-in-istanbul-turkish-media-report
- [Cointelegraph] Babylon advances native Bitcoin lending proposal on Aave V4 (10-15 18:14) — https://cointelegraph.com/news/babylon-native-bitcoin-collateral-aave-v4-proposal?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

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