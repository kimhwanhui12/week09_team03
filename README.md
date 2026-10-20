# week09_team03

Streamlit 단일 페이지 팀 프로젝트

## 개발 환경

- Python 3.13
- Streamlit 1.66.0 (`requirements.txt` 참고)

## 설치 및 실행 (Windows)

```powershell
# 1. 저장소 받기
git clone https://github.com/kimhwanhui12/week09_team03.git
cd week09_team03

# 2. 가상환경 만들고 켜기
python -m venv .venv
.\.venv\Scripts\activate

# 3. 패키지 설치
pip install -r requirements.txt

# 4. 실행
streamlit run app.py
```
## 설치 및 실행 (MacOS)

```zsh
# 1. 저장소 받기
git clone https://github.com/kimhwanhui12/week09_team03.git
cd week09_team03

# 2. 가상환경 만들고 켜기
python3 -m venv .venv
source .venv/bin/activate

# 3. 패키지 설치
pip install -r requirements.txt

# 4. 실행
streamlit run app.py
```
PowerShell에서 `activate` 실행이 막히면 아래 명령을 한 번 실행한 뒤 다시 시도하세요.

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## 폴더 구조

UI(`pages/`)와 로직(`gates/`)을 분리해요. 로직은 `streamlit`에 의존하지 않게 작성해서 pytest로 바로 테스트할 수 있게 합니다.

```
week09_team03/
├── app.py                 # 메인 진입점 (홈 / 관문 목록)
├── pages/                 # 관문별 화면 (UI만 담당)
├── gates/                 # 관문별 로직 (st 의존 X)
│   ├── g1_attendance/     # 1관문: 까다로운 출석봇
│   ├── g2_quiz/           # 2관문: 청개구리 퀴즈
│   ├── g3_notice/         # 3관문: 수상한 강의 공지
│   ├── g4_negotiation/    # 4관문: 팀플 빌런과 협상
│   ├── g5_calculator/     # 5관문: 고장난 계산기
│   ├── g6_memory/         # 6관문: 기말 범위 기억하기
│   └── g7_end_button/     # 7관문: 종강 버튼의 배신
├── core/                  # 공용 모듈 (세션 상태, 관문 진행 현황, 상수)
├── data/                  # 퀴즈 문항, 공지 목록, 단어 리스트 등 JSON 데이터
├── tests/                 # 관문별 테스트
├── .streamlit/            # Streamlit 설정 (config.toml)
├── requirements.txt
└── README.md
```

### 파일 작성 규칙

| 위치 | 규칙 | 예시 |
| --- | --- | --- |
| `pages/` | `숫자_영문이름.py` (숫자 순서대로 사이드바에 표시) | `pages/1_attendance_bot.py` |
| `gates/gN_*/` | 기능 ID별로 `feature_a.py`, `feature_b.py` + `__init__.py` | `gates/g1_attendance/feature_a.py` → G1-A |
| `tests/` | 관문 번호별 `test_gN.py` | `tests/test_g1.py` |

- 파일명은 한글 대신 영문을 써요. (Git·OS 환경에 따라 한글 파일명이 깨질 수 있음)
- 관문 클리어 여부는 각 관문에서 따로 관리하지 않고 `core/`의 공용 모듈에서 `st.session_state`로 한 곳에서 관리해요. (G7의 완료 검증·전체 초기화에서 사용)
- 빈 폴더를 Git에 올리기 위해 `.gitkeep`을 넣어뒀어요. 폴더에 실제 파일을 만들면 지워도 됩니다.

## 브랜치

- `main`: 배포/제출용
- `dev`: 개발용 — 작업은 `dev` 기준으로 진행
