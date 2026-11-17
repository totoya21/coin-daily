# 코인 데일리 스냅샷

- 수집 시각: 2026-11-17 17:19 KST
- 결과: 성공 39 / 실패·검증필요 1 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 0.1 / 3일 평균 1.4 / 오늘 구간 '중립'
- 판정 가능 지표 15/17개 (88%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | -62.5 |
| 파생·심리 | 30% | 40.0 |
| 밸류에이션 | 25% | 50.0 |
| 매크로 | 15% | -37.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.65 |
| 밸류에이션 | 가격÷STH-RP | +1 | +1 | 가격÷STH-RP 0.975 |
| 수급 | 현물 ETF 순유입 | -2 | -2 | 7거래일 연속 순유출 |
| 수급 | 거래소 순유입(7일) | -1 | +0 | 7일 순유입 분포 83백분위 |
| 수급 | 거래소 보유량(30일) | -1 | -1 | 30일 +1.19% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | -1 | -1 | 7일 +12.5% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +2 | 3회 평균 0.0040% |
| 파생·심리 | RSI(14) | +2 | +2 | RSI 23.9 |
| 파생·심리 | 롱/숏 비율 | +0 | +0 | 롱/숏 분포 67백분위 |
| 파생·심리 | 미결제약정(OI) | +1 | +1 | OI 7일 -22.5%, 가격 -13.9% (레버리지 정리) |
| 파생·심리 | 옵션 스큐 | +0 | +0 | +4.43 |
| 매크로 | 나스닥 | -1 | -1 | 50일선 아래 |
| 매크로 | DXY | -1 | -1 | 103.57, 20일 +1.8% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 159.22 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -4 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 24509.76 | 25136.27 | pt | 2026-11-16 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -2.94 | 2.27 | % | 2026-11-16 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 26310.13 | 26350.07 | pt | 2026-11-16 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 103.571 | 103.55 | pt | 2026-11-17 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.81 | 1.47 | % | 2026-11-17 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 159.216 | 159.78 | 엔 | 2026-11-17 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | 0.78 | 0.76 | % | 2026-11-17 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.08 | 4.02 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.87 | 2.79 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.65 | 3.44 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.12 | 3.03 | % | 2026-09-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-10-29 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -4 | -4 |  | 2026-11-17 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 7.885 | 7.989 | % | 2026-11-17 08:15 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.217 | 2.1892 | 조$ | 2026-11-17 08:15 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | -185.5 | -284.0 | 백만$ | 2026-11-13 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 7거래일 연속 순유출 / 집계 기준일 2026-11-13 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -143.5 | -203.8 | 백만$ | 2026-11-13 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -1065.4 | -1065.4 | 백만$ | 2026-11-13 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | -7 | -7 | 일 | 2026-11-13 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 64816.79 | 65315.35 | USD | 2026-11-16 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 23.91 | 24.52 |  | 2026-11-16 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -13.88 | -12.63 | % | 2026-11-16 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 2.99 | 3.03 | 십억$ | 2026-11-16 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -22.52 | -20.83 | % | 2026-11-16 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 2.78 | 2.82 | 배 | 2026-11-16 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 66.7 | 66.7 | 백분위 | 2026-11-16 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.0014 | 0.0045 | % | 2026-11-17 08:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.004 | -0.0001 | % | 2026-11-17 08:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 43.67 | 42.49 |  | 2026-11-17 08:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐(풋IV−콜IV) | 4.43 | 5.5 | vol pt | 2026-11-17 08:20 UTC | ok | [Deribit](https://www.deribit.com/options/BTC) | 만기 2026-12-25, 콜 BTC-25DEC26-72000-C / 풋 BTC-25DEC26-60000-P. 양수면 하방 헤지 수요 우위 |
| D.온체인 | MVRV Z-Score | 0.6457 | 0.6928 |  | 2026-11-10 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 0.9751 | 0.993 |  | 2026-11-10 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 66601.0 | 65649.0 | $ | 2026-11-10 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 64943.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 28742.8 | 17218.7 | BTC | 2026-11-16 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 26181.8 | 29230.6 | BTC | 2026-11-16 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -3090.7 | -10243.0 | BTC | 2026-11-16 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 83.3 | 58.9 | 백분위 | 2026-11-16 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | 2561.0 | -12011.9 | BTC | 2026-11-16 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | 1.19 | 1.16 | % | 2026-11-16 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2711617.0 | 2708826.0 | BTC | 2026-11-16 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (11-16 18:00 ~ 11-17 17:19 KST)

피드 상태: CoinDesk: 17건 / The Block: 20건 / Cointelegraph: 22건 / 블록미디어: 10건

- [블록미디어] 금, 5%대 국채 수익률에 ‘고전’…2015년 이후 최악의 해 (11-17 17:08) — https://www.blockmedia.co.kr/archives/1166883?utm_source=general&utm_medium=rss
- [블록미디어] CNN·BBC·줌까지 악성코드 노출…178개 기관서 코인 송금 주소 ‘바꿔치기’ 공격 (11-17 16:54) — https://www.blockmedia.co.kr/archives/1166947?utm_source=general&utm_medium=rss
- [The Block] Grayscale says crypto pullback offers ‘compelling entry points’ as bitcoin falls to $64,000 (11-17 16:39) — https://www.theblock.co/news/markets/2026-11-17-grayscale-compelling-entry-points-bitcoin-442083
- [CoinDesk] Bitcoin could slide into the $50,000s as Fed rate hike bets build, Wintermute says (11-17 16:38) — https://www.coindesk.com/markets/2026/11/17/bitcoin-could-slide-into-the-usd50-000s-as-fed-rate-hike-bets-build-wintermute-says
- [블록미디어] [마감시황] 코스피, 외인 ‘팔자’에  5000선 아래로…9개월 만에 최저 (11-17 15:58) — https://www.blockmedia.co.kr/archives/1166897?utm_source=general&utm_medium=rss
- [CoinDesk] Cardano Foundation seeks $5 million from treasury using ADA price 33% above market (11-17 15:54) — https://www.coindesk.com/tech/2026/11/17/cardano-foundation-seeks-usd5-million-from-treasury-using-ada-price-33-above-market
- [The Block] Cathie Wood’s Ark Invest loads up on crypto stocks while selling $85 million in Nvidia (11-17 15:35) — https://www.theblock.co/news/business/2026-11-17-ark-invest-buys-crypto-stocks-sells-nvidia-442080
- [Cointelegraph] Ex-Robinhood engineer pleads guilty to $125K Hyperliquid trading scheme (11-17 15:35) — https://cointelegraph.com/news/ex-robinhood-engineer-pleads-guilty-125k-crypto-trading-fraud?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 前 영국 총리 “‘야키모토 나카소리’가 비트코인 운영자냐”…업계 반박 불거져 (11-17 15:30) — https://www.blockmedia.co.kr/archives/1166871?utm_source=general&utm_medium=rss
- [Cointelegraph] Here’s what happened in crypto today (11-17 15:00) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 두나무 적자 전환에도…네이버 합병 몸값 15조 ‘요지부동’ (11-17 14:48) — https://www.blockmedia.co.kr/archives/1166850?utm_source=general&utm_medium=rss
- [The Block] CZ denies Binance sold crypto, Bitwise sees Solana at $1,100 by 2031, and more (11-17 14:45) — https://www.theblock.co/newsletters/the-daily/2026-11-17-cz-binance-bitwise-solana-more-crypto-news-441584
- [CoinDesk] Wells Fargo's reported BlackRock bitcoin ETF holdings double to $2.35 billion (11-17 14:37) — https://www.coindesk.com/markets/2026/11/17/wells-fargo-s-reported-blackrock-bitcoin-etf-holdings-double-to-usd2-35-billion
- [블록미디어] CFTC ‘파생상품 거래소’ 인가 따낸 백팩, 솔라나 지갑에서 종합 금융 플랫폼으로 진화 (11-17 14:35) — https://www.blockmedia.co.kr/archives/1166852?utm_source=general&utm_medium=rss
- [블록미디어] 트웬티원도 16개월 만에 비트코인 매수…BTC DAT 3사, 서로 다른 축적 전략 (종합) (11-17 14:10) — https://www.blockmedia.co.kr/archives/1166841?utm_source=general&utm_medium=rss
- [CoinDesk] Ripple-backed Evernorth has written down its pre-listing XRP holdings by 60% (11-17 14:02) — https://www.coindesk.com/markets/2026/11/17/ripple-backed-evernorth-has-written-down-its-pre-listing-xrp-holdings-by-60
- [블록미디어] 이더리움 1800달러도 위태…선물 미결제약정 70% 급감, ‘찐바닥’ 신호일까 (11-17 13:43) — https://www.blockmedia.co.kr/archives/1166840?utm_source=general&utm_medium=rss
- [블록미디어] 美 대형은행 AI 위험노출 1조달러…연준, 금융권 연쇄 손실 경고 (11-17 13:01) — https://www.blockmedia.co.kr/archives/1166821?utm_source=general&utm_medium=rss
- [블록미디어] 비트코인 추가 하락 경고한 맷 호건…앤트로픽 IPO 이후 반등론과 엇갈린 전망 (11-17 12:55) — https://www.blockmedia.co.kr/archives/1166829?utm_source=general&utm_medium=rss
- [Cointelegraph] Trezor customer data exposed in 3rd partner breach this year (11-17 12:46) — https://cointelegraph.com/news/trezor-customer-data-exposed-in-3rd-partner-breach-this-year?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Hackers inject credit card, crypto-stealing malware into 178 major websites (11-17 10:02) — https://cointelegraph.com/news/hackers-inject-malware-into-178-major-websites?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Nvidia shares fall 4% as board reportedly rules out Huang return (11-17 08:50) — https://cointelegraph.com/news/nvidia-shares-fall-4-as-board-reportedly-rules-out-huang-return?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] CFTC backs blockchain-based derivatives infrastructure as Backpack, tZERO win approvals (11-17 08:27) — https://www.theblock.co/news/regulation/2026-11-16-cftc-blockchain-derivatives-exchange-approval-backpack-tzero-441591
- [Cointelegraph] Custodia Bank loses Supreme Court bid for direct Fed payment access (11-17 07:54) — https://cointelegraph.com/news/custodia-bank-loses-supreme-court-bid-for-direct-fed-payment-access?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] German lawmakers back crypto freezes outside criminal cases (11-17 07:46) — https://cointelegraph.com/news/german-lawmakers-back-crypto-freezes-outside-criminal-cases?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Binance hack may push institutions to outside custody, FalconX exec says (11-17 07:19) — https://cointelegraph.com/news/binance-hack-institutional-crypto-custody-falconx?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Former Robinhood engineer pleads guilty to insider trading scheme on Hyperliquid (11-17 06:51) — https://www.coindesk.com/markets/2026/11/16/former-robinhood-engineer-pleads-guilty-to-insider-trading-scheme-on-hyperliquid
- [The Block] Trezor hit by another shipping partner data leak, affecting 27,000 Skladon orders (11-17 06:44) — https://www.theblock.co/news/business/2026-11-16-trezor-hit-another-shipping-partner-data-leak-affecting-27000-skladon-orders-441524
- [Cointelegraph] Bitmine edges toward 5% of ETH supply as treasuries report buys amid market slump (11-17 05:45) — https://cointelegraph.com/markets/bitmine-nears-5-eth-supply-treasuries-report-buys-amid-market-slump?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Democratic senators warn SEC’s tokenized stock exemption has illicit finance gaps (11-17 05:44) — https://www.theblock.co/news/regulation/2026-11-16-democratic-senators-warn-secs-tokenized-stock-exemption-illicit-finance-gaps-441432
- [CoinDesk] Bitcoin risks falling below $60,000 as Nvidia earnings threaten to deepen crypto sell-off (11-17 05:35) — https://www.coindesk.com/markets/2026/11/16/bitcoin-risks-falling-below-usd60-000-as-nvidia-earnings-threaten-to-deepen-crypto-sell-off
- [The Block] Peraire-Bueno brothers acquitted of wire fraud in $25 million Ethereum MEV case (11-17 05:30) — https://www.theblock.co/news/regulation/2026-11-16-peraire-bueno-brothers-acquitted-ethereum-mev-wire-fraud-441425
- [The Block] Bitwise sees Solana reaching $1,100 by 2031 in bull case as onchain trading grows (11-17 05:27) — https://www.theblock.co/news/markets/2026-11-16-bitwise-solana-price-prediction-1100-2031-441407
- [Cointelegraph] Boris Johnson says UK must lead blockchain development despite crypto doubts (11-17 05:18) — https://cointelegraph.com/news/boris-johnson-uk-must-lead-blockchain-development-despite-crypto-doubts?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Coinbase and Broadridge propose standard for tokenized stock disclosures (11-17 04:56) — https://cointelegraph.com/news/coinbase-broadridge-tokenized-stock-shareholder-notices?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Solflare CEO says AI security reviews are essential, touts ‘bunker mode’ and MoneyGram deal (11-17 03:59) — https://www.theblock.co/news/defi/2026-11-16-solflare-ceo-ai-security-reviews-bunker-mode-moneygram-441396
- [CoinDesk] U.S. Senate Democrats tell CFTC to back off its demand prediction markets defy bans (11-17 03:54) — https://www.coindesk.com/policy/2026/11/16/u-s-senate-democrats-tell-cftc-to-back-off-its-demand-prediction-markets-defy-bans
- [The Block] Winklevoss-backed Cypherpunk buys Zcash dip as mining debut delivers $2.6 million operating profit (11-17 03:43) — https://www.theblock.co/news/business/2026-11-16-winklevoss-cypherpunk-buys-zcash-dip-mining-debut-delivers-2-6-million-operating-profit-441392
- [Cointelegraph] Nvidia turmoil tests Bitcoin miners’ AI funding plans (11-17 03:07) — https://cointelegraph.com/news/nvidia-turmoil-tests-bitcoin-miners-ai-funding-plans?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Standard Chartered says Japan’s bond tokenization plans could help drive RWA market to $2 trillion (11-17 02:54) — https://www.theblock.co/news/web3/2026-11-16-japan-tokenized-government-bonds-standard-chartered-rwa-2-trillion-441384
- [Cointelegraph] Safe wallet reportedly loses $6.5M as Zodiac suspects key compromise (11-17 02:49) — https://cointelegraph.com/news/safe-wallet-reportedly-loses-millions-after-key-compromise?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Privacy on Solana is ‘non-negotiable’ for institutional adoption, Mert Mumtaz says (11-17 02:22) — https://www.theblock.co/news/ecosystems/2026-11-16-privacy-solana-non-negotiable-institutional-adoption-mert-mumtaz-says-441363
- [The Block] Supreme Court rejects Custodia Bank’s bid for Fed master account (11-17 02:15) — https://www.theblock.co/news/regulation/2026-11-16-supreme-court-rejects-custodia-banks-bid-for-fed-master-account-441376
- [The Block] Boris Johnson backs tokenization months after likening bitcoin to a ‘Ponzi scheme’ (11-17 01:49) — https://www.theblock.co/news/regulation/2026-11-16-boris-johnson-backs-tokenization-months-after-bitcoin-to-ponzi-scheme-441368
- [CoinDesk] Lighter suspends all withdrawals after $10.4 million crypto exploit (11-17 01:41) — https://www.coindesk.com/tech/2026/11/16/lighter-suspends-all-withdrawals-after-usd10-4-million-crypto-exploit
- [Cointelegraph] Bitcoin price fails to hold $65K as US stocks drop further on AI nerves (11-17 01:26) — https://cointelegraph.com/markets/bitcoin-price-fails-to-hold-65k-us-stocks-drop-on-ai-nerves?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] DeFi Development Corp. adds 9,482 SOL as CHAD dividend streak hits 31 days (11-17 01:16) — https://www.theblock.co/news/markets/2026-11-16-defi-development-solana-treasury-2-62-million-sol-441361
- [CoinDesk] Brazil's central bank faces backlash over stablecoin money laundering remarks (11-17 00:54) — https://www.coindesk.com/business/2026/11/16/brazil-s-central-bank-faces-backlash-over-stablecoin-money-laundering-remarks
- [CoinDesk] German parliament proposes crypto seizures without criminal charges (11-17 00:44) — https://www.coindesk.com/policy/2026/11/16/german-parliament-proposes-crypto-seizures-without-criminal-charges
- [The Block] Tom Lee says Ethereum’s ‘waterfall decline in price’ defies fundamentals as Bitmine adds 7,653 ETH (11-17 00:00) — https://www.theblock.co/news/business/2026-11-16-tom-lee-ethereum-waterfall-decline-price-defies-fundamentals-bitmine-adds-7653-eth-440904
- [The Block] Layer 2 Scaling Explained (11-16 23:56) — https://www.theblock.co/learn/basics/layer-2-scaling-explained-436103
- [Cointelegraph] Zelle picks Solana for ZelleUSD stablecoin and international payments (11-16 23:55) — https://cointelegraph.com/news/zelle-solana-zelleusd-stablecoin-international-payments?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Bitwise CIO says bitcoin may fall further in the near term but still calls it the best risk-adjusted trade of the next decade (11-16 23:52) — https://www.theblock.co/news/markets/2026-11-16-bitwise-cio-says-bitcoin-may-fall-further-in-the-near-term-but-still-calls-it-the-best-risk-adjusted-trade-of-the-next-decade-440901
- [Cointelegraph] Lighter recovers $5M after $10M exploit linked to compromised API keys (11-16 23:19) — https://cointelegraph.com/news/lighter-dex-pauses-withdrawals-10m-exploit?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Banks are banning AI agents over security... and competition concerns (11-16 22:30) — https://cointelegraph.com/magazine/banks-are-banning-ai-agents-over-security-and-competition-concerns?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Strategy buys $33M in Bitcoin, spends $228M on STRC buybacks (11-16 22:29) — https://cointelegraph.com/news/strategy-buy-485-bitcoin-228-million-strc-buyback?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] ‘This dip could use a little orange’: Michael Saylor’s Strategy buys another 485 BTC for $33 million as bitcoin tumbles (11-16 22:13) — https://www.theblock.co/news/business/2026-11-16-this-dip-could-use-a-little-orange-michael-saylor-strategy-bitcoin-tumbles-440886
- [CoinDesk] Solana drops ‘beta’ label after more than six years (11-16 22:03) — https://www.coindesk.com/tech/2026/11/16/solana-drops-beta-label-after-more-than-six-years
- [Cointelegraph] Binance Pay Later offers credit backed by Bitcoin, Ether and BNB holdings (11-16 22:00) — https://cointelegraph.com/news/binance-pay-later-crypto-backed-credit?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Old crypto feud reignites: Why OKX's Star Xu blames Binance for two years of October crashes (11-16 21:55) — https://www.coindesk.com/markets/2026/11/16/bitcoin-s-slide-reopens-an-old-feud-between-crypto-s-most-powerful-founders

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