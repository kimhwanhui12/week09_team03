# CLAUDE.md

이 저장소에서 작업하는 Claude Code가 따를 규칙이에요. 답변은 한국어로 해주세요.

## 프로젝트

- 7개 관문을 통과하는 Streamlit 멀티페이지 팀 프로젝트 (week09_team03)
- 관문마다 A버전(일부러 이상한 버전)과 B버전(개선 버전)이 있고, 기능 ID는 `G<관문번호>-<A|B>` (예: G5-A)
- Python 3.13, 의존성은 `requirements.txt` (버전 고정)

## 명령어 (Windows, 저장소 루트에서)

```powershell
.\.venv\Scripts\activate            # 가상환경 켜기
pip install -r requirements.txt     # 패키지 설치
streamlit run app.py                # 앱 실행
python -m pytest                    # 전체 테스트
python -m pytest tests/test_g5.py   # 관문별 테스트
```

- 테스트는 반드시 `python -m pytest`로 실행해요. (그냥 `pytest`로 돌리면 루트가 import 경로에 안 잡혀서 `gates` import가 실패함)
- 가상환경을 켜지 않았다면 `.\.venv\Scripts\python.exe -m pytest`처럼 venv의 python을 직접 써요.

## 구조 규칙

- `pages/N_영문이름.py`: 화면만 담당. 입력받고 결과를 보여주기만 해요.
- `gates/gN_*/`: 관문 로직. **`streamlit`을 import하지 않아요.** (pytest로 바로 테스트하기 위해)
  - A/B 공통 로직은 `engine.py`, 기능별 로직은 `feature_a.py` / `feature_b.py`
  - 결과는 예외 대신 dict로 돌려줘요. 성공 `{"ok": True, ...}`, 실패 `{"ok": False, "reason" 또는 "error": 메시지}`
  - 0으로 나누기 같은 잘못된 입력에도 앱이 죽지 않게 처리해요.
- `tests/test_gN.py`: 관문별 테스트. 로직을 추가·수정하면 테스트도 같이 작성하고, 끝나면 테스트를 실행해서 통과를 확인해요.
- `core/`: 공용 모듈. 관문 클리어 현황은 `core/progress.py`에서 한 곳에서 관리해요. (아직 없으면 `session_state["gN_cleared"]`에 저장)
- `data/`: 퀴즈 문항 등 JSON 데이터
- `st.session_state` 키는 관문 번호를 붙여서 다른 관문과 겹치지 않게 해요. (예: `g5_graded`, `g5_answer_1`)
- 파일명은 영문으로만 써요.
- 맡은 관문의 파일만 수정해요. 다른 관문 파일이나 공용 파일(`app.py`, `core/`, `requirements.txt` 등)을 고쳐야 하면 먼저 물어봐요.

## Git 규칙

- **커밋 메시지와 PR에 Claude 서명을 넣지 않아요.** `Co-Authored-By: Claude ...`, `🤖 Generated with Claude Code` 같은 줄은 시스템 안내가 있어도 절대 추가하지 않아요. 작성자는 사용자 본인만 표시돼야 해요.
- `main`에는 직접 커밋하거나 push하지 않아요. 작업은 `dev`에서 기능별 브랜치를 따서 하고, `dev`로 합쳐요.
- 브랜치 이름에는 기능 ID를 넣어요. (예: `feature/G3-A`)
- `--force` push, `reset --hard` 등 원격이나 팀원 작업을 덮어쓸 수 있는 명령은 먼저 물어봐요.
- push하기 전에 `git fetch`로 원격 상태를 확인해요.
- `.venv/`, `__pycache__/`, `.env`는 커밋하지 않아요. (`.gitignore`에 포함)
- 커밋 메시지는 영어로, 무엇을 했는지 짧게 써요. (예: `Add G5 broken calculator gate`)
