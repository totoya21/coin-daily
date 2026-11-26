# 코인 데일리 스냅샷

- 수집 시각: 2026-11-26 17:46 KST
- 결과: 성공 38 / 실패·검증필요 2 / 수동 1 (전체 41)
- 모든 값은 아래 '출처' 열의 고정 소스에서 가져온 값이다. '이전'은 소스가 준 직전값 또는 지난 수집값.

## 점수 (스크립트 계산 — 리포트에서 재계산하지 말 것)

- **판정: 중립** → BTC 목표 비중 **60%** (전일 판정: 중립)
- 오늘 총점 13.1 / 3일 평균 9.0 / 오늘 구간 '중립'
- 판정 가능 지표 14/17개 (82%)

| 그룹 | 가중치 | 그룹 점수 |
|---|---|---|
| 수급 | 30% | -62.5 |
| 파생·심리 | 30% | 62.5 |
| 밸류에이션 | 25% | 75.0 |
| 매크로 | 15% | -37.5 |

| 그룹 | 지표 | 점수 | 어제 | 근거 |
|---|---|---|---|---|
| 밸류에이션 | MVRV Z | +1 | +1 | MVRV Z 0.28 |
| 밸류에이션 | 가격÷STH-RP | +2 | +1 | 가격÷STH-RP 0.842 |
| 수급 | 현물 ETF 순유입 | -2 | -2 | 6거래일 연속 순유출 |
| 수급 | 거래소 순유입(7일) | -1 | +0 | 7일 순유입 분포 89백분위 |
| 수급 | 거래소 보유량(30일) | -1 | -1 | 30일 +0.69% (±0.5% 미만은 0점) |
| 수급 | 고래비율(근사) | 제외 | — | 값 없음 |
| 수급 | 테더 도미넌스(7일) | -1 | -1 | 7일 +3.7% (±3% 미만은 0점) |
| 파생·심리 | 펀딩비 | +1 | +1 | 3회 평균 0.0068% |
| 파생·심리 | RSI(14) | +2 | +2 | RSI 27.4 |
| 파생·심리 | 롱/숏 비율 | +1 | +0 | 롱/숏 분포 30백분위 |
| 파생·심리 | 미결제약정(OI) | +1 | +1 | OI 7일 -12.6%, 가격 -4.1% (레버리지 정리) |
| 파생·심리 | 옵션 스큐 | 제외 | -1 | 값 없음 |
| 매크로 | 나스닥 | -1 | -1 | 50일선 아래 |
| 매크로 | DXY | -1 | -1 | 103.75, 20일 +1.7% (상승) |
| 매크로 | USD/JPY | +0 | +0 | 159.16 |
| 매크로 | CPI·PCE | -1 | -1 | 둔화−재가속 합계 -4 |
| 매크로 | 폴리마켓 금리인하 | 제외 | — | FOMC 마켓 미설정 또는 값 없음 |

## 지표

| 그룹 | 지표 | 값 | 이전 | 단위 | 데이터 기준 | 상태 | 출처 | 메모 |
|---|---|---|---|---|---|---|---|---|
| A.매크로 | 나스닥 종합지수 | 23585.801 | 23733.539 | pt | 2026-11-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 5거래일 변화율 | -3.46 | -2.45 | % | 2026-11-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) |  |
| A.매크로 | 나스닥 50일 이평 | 25978.69 | 26026.54 | pt | 2026-11-25 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/%5EIXIC) | 종가가 이평 위면 추세 양호 |
| A.매크로 | 달러인덱스(DXY) | 103.754 | 103.67 | pt | 2026-11-26 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | DXY 20거래일 변화율 | 1.68 | 1.78 | % | 2026-11-26 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/DX-Y.NYB) |  |
| A.매크로 | USD/JPY | 159.155 | 159.262 | 엔 | 2026-11-26 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | USD/JPY 5거래일 변화율 | -0.14 | -0.07 | % | 2026-11-26 | ok | [Yahoo Finance](https://finance.yahoo.com/quote/JPY%3DX) |  |
| A.매크로 | CPI 전년비 | 4.08 | 4.02 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPIAUCSL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | 근원 CPI 전년비 | 2.87 | 2.79 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/CPILFESL) | FRED 갱신일 2026-11-10 (발표 후 30일 이내) |
| A.매크로 | PCE 전년비 | 3.84 | 3.67 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPI) | FRED 갱신일 2026-11-25 (발표 후 30일 이내) |
| A.매크로 | 근원 PCE 전년비 | 3.26 | 3.14 | % | 2026-10-01 | ok | [FRED](https://fred.stlouisfed.org/series/PCEPILFE) | FRED 갱신일 2026-11-25 (발표 후 30일 이내) |
| A.매크로 | 인플레이션 방향 합계 | -4 | -4 |  | 2026-11-26 | ok | [FRED](https://fred.stlouisfed.org/) | 최근 발표 지표 중 전년비 둔화 +1 / 재가속 −1의 합 |
| B.자금흐름 | 테더 도미넌스 | 8.254 | 8.46 | % | 2026-11-26 08:39 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) | 상승=위험회피 / TradingView USDT.D와 계산 방식 다름 |
| B.자금흐름 | 전체 시가총액(TOTAL) | 2.1047 | 2.0595 | 조$ | 2026-11-26 08:39 UTC | ok | [CoinGecko](https://www.coingecko.com/en/global-charts) |  |
| B.자금흐름 | BTC 현물 ETF 순유입(전체) | -231.6 | -569.7 | 백만$ | 2026-11-24 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) | 6거래일 연속 순유출 / 집계 기준일 2026-11-24 |
| B.자금흐름 | IBIT(블랙록) 순유입 | -175.3 | -509.3 | 백만$ | 2026-11-24 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 5거래일 순유입 합계 | -2359.1 | -2367.5 | 백만$ | 2026-11-24 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| B.자금흐름 | ETF 연속일수(+유입/−유출) | -6 | -5 | 일 | 2026-11-24 | ok | [TFTC (SoSoValue·Farside 집계)](https://www.tftc.io/bitcoin-etf-flows) |  |
| C.파생·가격 | BTC 일봉 종가 | 60383.51 | 59740.87 | USD | 2026-11-25 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | RSI(14, 일봉) | 27.45 | 24.77 |  | 2026-11-25 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) | 70↑ 과매수 / 30↓ 과매도 |
| C.파생·가격 | BTC 7일 가격 변화율 | -4.13 | -7.91 | % | 2026-11-25 | ok | [Coinbase 현물](https://www.coinbase.com/price/bitcoin) |  |
| C.파생·가격 | 선물 미결제약정(OI) | 2.72 | 2.69 | 십억$ | 2026-11-25 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | OI 7일 변화율 | -12.62 | -8.85 | % | 2026-11-25 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 달러 기준 OI라 가격 변동이 섞여 있음 |
| C.파생·가격 | 롱/숏 계정비율 | 2.46 | 2.71 | 배 | 2026-11-25 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 1 초과면 롱 우위 |
| C.파생·가격 | 롱/숏 계정비율 분포 위치 | 30.0 | 46.7 | 백분위 | 2026-11-25 | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | OKX 선물 최근 30일 분포 기준. 높을수록 롱 쏠림 |
| C.파생·가격 | 펀딩비(최근 1회) | 0.0067 | 0.01 | % | 2026-11-26 08:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) | 0.05%↑ 과열 |
| C.파생·가격 | 펀딩비 최근 3회 평균 | 0.0068 | 0.0048 | % | 2026-11-26 08:00 UTC | ok | [OKX 선물](https://www.okx.com/trade-swap/btc-usdt-swap) |  |
| C.파생·가격 | DVOL(BTC 내재변동성) | 50.97 | 54.26 |  | 2026-11-26 08:00 UTC | ok | [Deribit](https://www.deribit.com/statistics/BTC/volatility-index) |  |
| C.파생·가격 | 옵션 25델타 스큐 |  | 9.05 |  |  | fail | [Deribit](https://www.deribit.com/options/BTC) | 429 Client Error: Too Many Requests for url: https://www.deribit.com/api/v2/public/ticker?instrument_name=BTC-25DEC26-52000-P |
| D.온체인 | MVRV Z-Score | 0.2776 | 0.3085 |  | 2026-11-19 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 0 이하 역사적 매수구간 / 7 이상 과열 |
| D.온체인 | 단기보유자 MVRV | 0.8422 | 0.8532 |  | 2026-11-19 | ok | [BGeometrics](https://charts.bgeometrics.com/) |  |
| D.온체인 | 단기보유자 실현가(STH-RP) | 71560.0 | 70078.0 | $ | 2026-11-19 | ok | [BGeometrics](https://charts.bgeometrics.com/) | 가격 ÷ STH-MVRV로 계산 (가격 60268.0$). 가격이 위면 강세 유지 |
| D.온체인 | 거래소 BTC 유입 | 29540.1 | 25236.8 | BTC | 2026-11-25 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 유출 | 27199.9 | 25269.8 | BTC | 2026-11-25 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 | -1776.2 | -9423.4 | BTC | 2026-11-25 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 순유입 7일 합 분포 위치 | 88.9 | 60.0 | 백분위 | 2026-11-25 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 최근 90일 분포 기준. 높을수록 매도 압력 |
| D.온체인 | 거래소 BTC 순유입 | 2340.2 | -33.0 | BTC | 2026-11-25 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) | 양수=매도 압력 / 음수=축적 |
| D.온체인 | 거래소 보유량 30일 변화율 | 0.69 | 0.83 | % | 2026-11-25 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 거래소 BTC 보유량 | 2712502.0 | 2709516.0 | BTC | 2026-11-25 | ok | [Coin Metrics 커뮤니티](https://charts.coinmetrics.io/crypto-data/) |  |
| D.온체인 | 채굴자→거래소 유입 |  |  |  |  | manual | [수동 확인](https://cryptoquant.com/asset/btc/chart/miner-flows) | 무료 소스 없음 → 수동 확인 목록 참고 |
| D.온체인 | 고래비율(근사) |  |  |  |  | fail | [Arkham + Coin Metrics](https://intel.arkm.com/) | Arkham 키 없음 |

## 지난밤 뉴스 (11-25 18:00 ~ 11-26 17:46 KST)

피드 상태: CoinDesk: 16건 / The Block: 20건 / Cointelegraph: 23건 / 블록미디어: 10건

- [블록미디어] 비트코인 ‘역대급 손절’의 함정?…”대규모 내부 이체에 매도세 과대평가 우려” (11-26 17:30) — https://www.blockmedia.co.kr/archives/1171063?utm_source=general&utm_medium=rss
- [CoinDesk] $7 billion of bitcoin options expire Friday, and the biggest bets look starkly different from October (11-26 17:01) — https://www.coindesk.com/markets/2026/11/26/usd7-billion-of-bitcoin-options-expire-friday-and-the-biggest-bets-look-starkly-different-from-october
- [블록미디어] ‘63억달러 해킹’에 규제 고삐 당긴다…영국, 디파이 플랫폼에도 인가 요구 (11-26 17:00) — https://www.blockmedia.co.kr/archives/1171029?utm_source=general&utm_medium=rss
- [CoinDesk] Zcash developers want users to move $300 million out of an older privacy system (11-26 16:09) — https://www.coindesk.com/tech/2026/11/26/zcash-developers-want-users-to-move-usd300-million-out-of-an-older-privacy-system
- [블록미디어] ‘승부수’인가 ‘무리수’인가… 피델리티, 체인링크 현물 ETF 증권신고서 제출 (11-26 16:01) — https://www.blockmedia.co.kr/archives/1171000?utm_source=general&utm_medium=rss
- [블록미디어] [마감시황] 코스피, 4800선 넘봤지만…개인 1조 매도에 0.29% 상승 그쳐 (11-26 15:57) — https://www.blockmedia.co.kr/archives/1171040?utm_source=general&utm_medium=rss
- [블록미디어] 미국 차기 상원 은행위원장 유력 후보 워런, SEC에 디지털자산 규제 완화 철회 요구 (11-26 15:40) — https://www.blockmedia.co.kr/archives/1170985?utm_source=general&utm_medium=rss
- [The Block] Europe’s only spot bitcoin ETF starts trading in Switzerland, BIT says (11-26 15:30) — https://www.theblock.co/news/markets/2026-11-26-swiss-bitcoin-etf-bbit-begins-trading-europes-only-446724
- [CoinDesk] Over 1,000 Bitcoin miners were tricked into working for a thief by a fake internet route (11-26 15:19) — https://www.coindesk.com/markets/2026/11/26/hackers-hijacked-1-000-plus-bitcoin-mines-in-one-second-by-faking-internet-routes
- [블록미디어] 차기 금융서비스위원장 유력 후보 워터스 “트럼프 디지털자산 부패 조사할 것” (11-26 15:05) — https://www.blockmedia.co.kr/archives/1170967?utm_source=general&utm_medium=rss
- [Cointelegraph] Here’s what happened in crypto today (11-26 15:00) — https://cointelegraph.com/news/what-happened-in-crypto-today?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 비트코인·이더리움 ETF 동반 ‘순유출’ 지속…11월 한 달에만 9조원 증발했다 (11-26 15:00) — https://www.blockmedia.co.kr/archives/1170974?utm_source=general&utm_medium=rss
- [Cointelegraph] UK regulator plans tighter DeFi rules, citing $6.3B Binance hack: Report (11-26 14:53) — https://cointelegraph.com/news/uk-fca-defi-regulation-binance-hack?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Fidelity files for Chainlink ETF, Musk’s X wins ruling in alleged bitcoin content-farm case, and more (11-26 14:45) — https://www.theblock.co/newsletters/the-daily/2026-11-26-fidelity-chainlink-etf-musk-x-ruling-alleged-bitcoin-content-farm-case-more-crypto-news-446755
- [블록미디어] 앤트로픽 CEO, IPO로 2억8000만달러 현금화…주가는 공모가 하회 (11-26 14:45) — https://www.blockmedia.co.kr/archives/1170965?utm_source=general&utm_medium=rss
- [CoinDesk] Ripple is worth $90 a share to one fund and $300 to another, SEC filings show (11-26 14:30) — https://www.coindesk.com/markets/2026/11/26/ripple-is-worth-usd90-a-share-to-one-fund-and-usd300-to-another-sec-filings-show
- [Cointelegraph] Sky proposes emergency vote on $25M transfer amid liquidity stress (11-26 14:29) — https://cointelegraph.com/news/sky-emergency-vote-25m-transfer-stusds-liquidity-stress?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [블록미디어] 비밀번호 관리 서비스 ‘1패스워드’ 해킹…창펑자오 “모든 비밀번호 바꿔라” (11-26 14:22) — https://www.blockmedia.co.kr/archives/1170952?utm_source=general&utm_medium=rss
- [The Block] Galaxy walks back bitcoin’s June-bottom call, warns of deeper losses below $58,525 (11-26 14:16) — https://www.theblock.co/news/markets/2026-11-26-galaxy-walks-back-bitcoin-bottom-call-446786
- [블록미디어] 금융위, 거래소 상장 책임 ‘증권신고서’급으로 강화…알트코인 상폐 잇따르나 (11-26 14:15) — https://www.blockmedia.co.kr/archives/1170953?utm_source=general&utm_medium=rss
- [Cointelegraph] 1Password hacker stole customer names and emails, but vaults safe (11-26 13:55) — https://cointelegraph.com/news/1password-hacker-stole-customer-names-and-emails-but-vaults-safe?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] Bill to lock up U.S. government bitcoin for 20 years advances to full House (11-26 13:46) — https://www.coindesk.com/policy/2026/11/26/strategic-bitcoin-reserve-bill-to-lock-up-u-s-government-held-bitcoin-for-20-years-goes-to-full-house
- [Cointelegraph] Senate Democrats urge SEC to scrap crypto, tokenized stock exemptions (11-26 13:24) — https://cointelegraph.com/news/senate-democrats-urge-sec-to-scrap-crypto-tokenized-stock-exemptions?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] House Committee advances Strategic Bitcoin Reserve bill with narrow path to passage (11-26 12:03) — https://www.theblock.co/news/regulation/2026-11-25-house-committee-advances-strategic-bitcoin-reserve-bill-446778
- [The Block] LayerZero adds Samsung Card, Kakao Pay, ZAN as validators for upcoming Zero blockchain (11-26 11:22) — https://www.theblock.co/news/business/2026-11-25-layerzero-kakaopay-samsung-446770
- [Cointelegraph] AI labs likely sitting on cryptography ‘bombshells,’ computer scientist says (11-26 10:33) — https://cointelegraph.com/news/ai-labs-likely-sitting-on-cryptography-bombshells-computer-scientist-says?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Sens. Warren, Van Hollen lead push to scrap SEC’s Regulation Crypto and innovation exemption (11-26 07:20) — https://www.theblock.co/news/regulation/2026-11-25-warren-van-hollen-lead-push-scrap-sec-regulation-crypto-innovation-exemption-446756
- [Cointelegraph] Switzerland clears 57 jurisdictions for crypto tax data sharing (11-26 06:53) — https://cointelegraph.com/news/switzerland-clears-57-jurisdictions-crypto-tax-data-sharing?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Braiins warns of Bitcoin mining attacks affecting over 1,000 sites (11-26 06:22) — https://cointelegraph.com/news/braiins-warns-bitcoin-mining-attacks-affecting-1000-sites?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Why ECB collateral eligibility could boost demand for tokenized bonds (11-26 06:11) — https://cointelegraph.com/news/why-ecb-collateral-eligibility-could-boost-demand-tokenized-bonds?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Bitcoin miners hit by hashrate hijacking attack exploiting unencrypted connections (11-26 04:37) — https://www.theblock.co/news/ecosystems/2026-11-25-bitcoin-miners-hit-hashrate-hijacking-attack-exploiting-unencrypted-connections-446723
- [The Block] Fidelity files for spot Chainlink ETF with planned Nasdaq listing (11-26 04:32) — https://www.theblock.co/news/business/2026-11-25-fidelity-chainlink-etf-nasdaq-listing-446735
- [Cointelegraph] Ethereum Foundation backs Keccak-256 to counter quantum, AI threats (11-26 03:54) — https://cointelegraph.com/news/ethereum-foundation-keccak-256-counter-quantum-ai-threats?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] French Senate blocks new crypto tax and wallet list critics called a kidnapping risk (11-26 03:24) — https://www.coindesk.com/business/2026/11/25/french-senate-blocks-new-crypto-tax-and-wallet-list-critics-called-a-kidnapping-risk
- [The Block] Justice Department takes aim at billions in crypto fraud proceeds in historic ‘largest ever crackdown’ (11-26 03:05) — https://www.theblock.co/news/regulation/2026-11-25-justice-department-takes-aim-billions-crypto-fraud-proceeds-largest-ever-crackdown-446711
- [The Block] Nvidia agrees to $290 million settlement over crypto mining disclosures amid Jensen Huang turmoil (11-26 03:00) — https://www.theblock.co/news/regulation/2026-11-25-nvidia-290-million-settlement-crypto-mining-class-action-446709
- [Cointelegraph] US inflation rises to 3.8% ahead of December Fed meeting, clouding crypto outlook (11-26 02:53) — https://cointelegraph.com/markets/us-inflation-rises-december-fed-meeting-clouding-crypto-outlook?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [CoinDesk] 'This time actually seems different': Crypto veterans brace for more pain as bitcoin tumbles (11-26 02:38) — https://www.coindesk.com/markets/2026/11/25/this-time-actually-seems-different-crypto-veterans-brace-for-more-pain-as-bitcoin-tumbles
- [Cointelegraph] Bitcoin falls toward $57K amid US tariff fears, hot PCE data as Nasdaq drops 4% (11-26 02:33) — https://cointelegraph.com/markets/bitcoin-falls-57k-us-tariff-pce-data-nasdaq-drops?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Bitcoin falls below $58,000 as CoinShares’ Butterfill sees ‘tail end of the bear market’ (11-26 02:26) — https://www.theblock.co/news/markets/2026-11-25-bitcoin-falls-below-58000-coinshares-butterfill-sees-tail-end-bear-market-446678
- [Cointelegraph] Nvidia agrees to $290M settlement over crypto mining revenue disclosures (11-26 02:19) — https://cointelegraph.com/news/nvidia-agrees-290m-settlement-crypto-mining-revenue-disclosures?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] FCC authorizes SpaceX to deploy 1M satellites for orbital AI data centers (11-26 02:10) — https://cointelegraph.com/news/fcc-authorizes-spacex-1m-satellites-orbital-ai-data-centers?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Hyperliquid’s HYPE will join bitcoin, ether and more in Franklin Templeton’s crypto ETF (11-26 01:54) — https://www.theblock.co/news/markets/2026-11-25-franklin-templeton-ezpz-etf-adds-hyperliquid-hype-446686
- [CoinDesk] EU bank watchdog seeks European Commission rules for crypto firms offering DeFi lending (11-26 01:02) — https://www.coindesk.com/policy/2026/11/25/eu-bank-watchdog-seeks-european-commission-rules-for-crypto-firms-offering-defi-lending
- [CoinDesk] Ukrainian lawmakers pass crypto tax and regulation bill expected to bring in $330 million (11-26 01:02) — https://www.coindesk.com/business/2026/11/25/ukrainian-lawmakers-pass-crypto-tax-and-regulation-bill-expected-to-bring-in-usd330-million
- [The Block] Aave Labs publicly launches savings app as balances top $63 million (11-26 01:00) — https://www.theblock.co/news/defi/2026-11-25-aave-labs-publicly-launches-savings-app-as-balances-top-63-million-446674
- [CoinDesk] Crypto Long & Short: Bitcoin investors can’t keep ignoring Japan (11-26 00:59) — https://www.coindesk.com/coindesk-indices/2026/11/25/crypto-long-and-short-bitcoin-investors-can-t-keep-ignoring-japan
- [The Block] NovaTech founders ordered to pay $1.3 billion over crypto Ponzi scheme targeting Haitian investors (11-26 00:02) — https://www.theblock.co/news/regulation/2026-11-25-novatech-founders-ordered-pay-1-3-million-crypto-ponzi-scheme-haitian-investors-446643
- [CoinDesk] South Korean crypto exchange Bithumb warns of phishing after deeper October breach probe (11-25 23:47) — https://www.coindesk.com/tech/2026/11/25/south-korean-crypto-exchange-bithumb-warns-of-phishing-after-deeper-october-breach-probe
- [The Block] Ukraine passes crypto market law, with $332 million revenue target (11-25 23:35) — https://www.theblock.co/news/regulation/2026-11-25-ukraine-passes-crypto-market-law-with-332-million-revenue-target-446182
- [Cointelegraph] Ex-FTX COO calls out Netflix over CZ’s ‘Asian mafia’ portrayal (11-25 23:21) — https://cointelegraph.com/news/ftx-coo-netflix-portrayal-binance-founder-racist?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] Bit Digital repays $50 million to Galaxy after selling 29,825 ETH (11-25 23:15) — https://www.theblock.co/news/business/2026-11-25-bit-digital-repays-50-million-to-galaxy-after-selling-29825-eth-446164
- [Cointelegraph] Ukraine passes bill to legalize crypto and tax profits at 23% (11-25 22:02) — https://cointelegraph.com/news/ukraine-passes-bill-crypto-regulation-tax?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [The Block] UniCredit offers bitcoin exposure to Italian retail clients with capital protection at maturity (11-25 21:24) — https://www.theblock.co/news/business/2026-11-25-unicredit-offers-bitcoin-exposure-to-italian-retail-clients-with-capital-protection-at-maturity-446150
- [CoinDesk] Fed’s preferred inflation gauge lands with a December rate increase already priced in (11-25 21:18) — https://www.coindesk.com/daybook-us/2026/11/25/fed-s-preferred-inflation-gauge-lands-with-a-december-rate-increase-already-priced-in
- [The Block] ‘Don’t mess with X,’ Elon Musk says after platform secures default judgment in alleged bitcoin content-farm case (11-25 21:14) — https://www.theblock.co/news/regulation/2026-11-25-dont-mess-with-x-elon-musk-says-after-platform-secures-default-judgment-in-alleged-bitcoin-content-farm-case-446151
- [CoinDesk] Ether, DeFi fall twice as hard as bitcoin as equities selloff resumes (11-25 20:57) — https://www.coindesk.com/markets/2026/11/25/ether-defi-fall-twice-as-hard-as-bitcoin-as-equities-selloff-resumes
- [CoinDesk] Italy’s UniCredit launches six-year bitcoin certificate with gains capped at 65% (11-25 20:51) — https://www.coindesk.com/business/2026/11/25/italy-s-unicredit-debuts-six-year-bitcoin-certificate-with-100-capital-protection-and-65-cap
- [Cointelegraph] Japan’s SBI, SMFG launch Solana venture for stablecoins, tokenization (11-25 20:49) — https://cointelegraph.com/news/sbi-smfg-solana-global-stablecoin-tokenization?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound
- [Cointelegraph] Hong Kong launches tokenized debt platform with 24-hour settlement (11-25 20:31) — https://cointelegraph.com/news/hong-kong-central-bank-platform-tokenized-debt-securities?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound

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

- 옵션 25델타 스큐 (Deribit): 429 Client Error: Too Many Requests for url: https://www.deribit.com/api/v2/public/ticker?instrument_name=BTC-25DEC26-52000-P
- 고래비율(근사) (Arkham + Coin Metrics): Arkham 키 없음