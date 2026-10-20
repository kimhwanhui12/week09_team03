import streamlit as st

from gates.g5_calculator.engine import RULE_LABELS, RULES
from gates.g5_calculator.feature_a import run_free_calc
from gates.g5_calculator.feature_b import PROBLEMS, grade

OPERATORS = list(RULES.keys())


def mark_cleared():
    """core/progress.py가 있으면 거기에, 없으면 session_state에 G5 클리어를 기록한다."""
    try:
        from core import progress
    except ImportError:
        progress = None

    for name in ("mark_cleared", "set_cleared", "clear_gate"):
        func = getattr(progress, name, None)
        if callable(func):
            func("G5")
            return
    st.session_state["g5_cleared"] = True


st.session_state.setdefault("g5_graded", False)
st.session_state.setdefault("g5_result", None)

st.title("관문 5: 고장난 계산기")

st.warning(
    "**바뀐 연산 규칙**  \n"
    + "  \n".join(f"화면의 `{op}` 는 실제로 **{RULE_LABELS[op]}**" for op in OPERATORS)
    + "  \n0으로 나누면 에러 메시지가 나와요."
)

version = st.radio("버전", ["A버전", "B버전"], horizontal=True)

if version == "A버전":
    st.subheader("G5-A: 자유 계산")
    col_a, col_op, col_b = st.columns([2, 1, 2])
    a = col_a.number_input("첫 번째 숫자", value=0.0, format="%g")
    op = col_op.selectbox("연산자", OPERATORS)
    b = col_b.number_input("두 번째 숫자", value=0.0, format="%g")

    if st.button("계산"):
        res = run_free_calc(a, op, b)
        if res["ok"]:
            st.success(f"{a:g} {op} {b:g} = **{res['result']:g}**")
        else:
            st.error(res["error"])

else:
    st.subheader("G5-B: 3문제 채점")
    graded = st.session_state["g5_graded"]

    answers = []
    for i, (a, op, b) in enumerate(PROBLEMS, start=1):
        answers.append(
            st.text_input(f"문제 {i}: {a} {op} {b} = ?", key=f"g5_answer_{i}", disabled=graded)
        )

    if st.button("제출", disabled=graded):
        res = grade(answers, st.session_state["g5_graded"])
        if res["ok"]:
            st.session_state["g5_graded"] = True
            st.session_state["g5_result"] = res
            if res["cleared"]:
                mark_cleared()
        else:
            st.session_state["g5_result"] = res
        st.rerun()

    result = st.session_state["g5_result"]
    if result:
        if not result["ok"]:
            st.error(result["reason"])
        elif result["cleared"]:
            st.success(f"점수: {result['score']} / {result['total']} — 관문 5 완료!")
        else:
            st.error(f"점수: {result['score']} / {result['total']} — 재도전은 할 수 없어요.")
