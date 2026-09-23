# 코인 데일리 — GitHub 자동 수집 설치 가이드

PC 없이 GitHub 서버가 매일 09:30(KST)에 지표를 수집하고, 결과를 이 저장소의 `data/` 폴더에 저장합니다.
Claude 프로젝트에서 "실행해줘"라고 하면 Claude가 이 파일을 읽어 리포트를 만듭니다.

## 저장소에 들어가는 파일
- `coin_daily.py` 수집기 / `scoring.py` 점수 계산 / `config.json` 설정 / `requirements.txt`
- `.github/workflows/daily.yml` 매일 자동 실행 설정
- `data/` 수집 결과 (첫 실행 때 자동 생성)
- API 키는 저장소에 넣지 않고 GitHub Secrets에 넣습니다. 공개 저장소여도 키는 노출되지 않습니다.

## Secrets 이름 (Settings → Secrets and variables → Actions)
| 이름 | 필수 | 설명 |
|---|---|---|
| FRED_API_KEY | 필수 | CPI·PCE |
| COINGECKO_API_KEY | 권장 | 테더 도미넌스·TOTAL (없어도 대부분 작동) |
| ARKHAM_API_KEY | 선택 | 고래비율(근사), 고래 대량 이동 |

## 수동 실행
Actions 탭 → coin-daily → Run workflow → mode 선택
- `check`: 점검만 (결과 `data/check_report.md`, 기록 안 남김)
- `run`: 지금 바로 정식 수집

## 설정 바꾸기 (config.json)
- `derivatives_source`: 선물 데이터 거래소 (`okx` / `bybit` / `binance`). 점검 결과에서 접속되는 곳으로 고정
- `spot_source`: 현물 가격·RSI (`coinbase` / `binance`)
- `polymarket_fomc_slug`: 다음 FOMC 금리 인하 폴리마켓 마켓 주소 끝부분 (점수에 사용, 회의가 지나면 교체)
- `scoring`: 그룹 가중치, 판정 구간·목표 비중, 안전장치. 지표별 채점 기준은 `scoring.py`

## 참고
- GitHub 예약 실행은 서버 사정으로 10~30분 늦어질 수 있습니다.
- 60일 동안 저장소 활동이 없으면 예약 실행이 꺼지는데, 매일 결과를 저장하므로 자동으로 유지됩니다.
- 과거 비교가 필요한 지표(테더 도미넌스·폴리마켓 7일, 고래비율 30일)는 기록이 쌓일 때까지 점수에서 제외됩니다.
