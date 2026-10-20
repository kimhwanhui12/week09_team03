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

## 브랜치

- `main`: 배포/제출용
- `dev`: 개발용 — 작업은 `dev` 기준으로 진행
