"""G5-B: 고정 3문제 채점, 중복 채점 차단"""

from gates.g5_calculator.engine import calculate

# (왼쪽 숫자, 화면 연산자, 오른쪽 숫자) -> 정답 4, 3, 27
PROBLEMS = [
    (7, "+", 3),
    (6, "×", 2),
    (9, "÷", 3),
]


def _to_number(value):
    """입력값을 숫자로 바꾼다. 비었거나 숫자가 아니면 None."""
    if value is None:
        return None
    try:
        return float(str(value).strip())
    except ValueError:
        return None


def grade(user_answers, already_graded):
    """3문제를 채점한다.

    이미 채점했으면 {"ok": False, "reason": ...}
    아니면 {"ok": True, "score", "total", "cleared"}
    """
    if already_graded:
        return {"ok": False, "reason": "이미 채점했어요. 재도전은 할 수 없어요."}

    answers = list(user_answers)
    score = 0
    for i, (a, op, b) in enumerate(PROBLEMS):
        expected = calculate(a, op, b)["result"]
        given = _to_number(answers[i]) if i < len(answers) else None
        if given is not None and given == expected:
            score += 1

    total = len(PROBLEMS)
    return {"ok": True, "score": score, "total": total, "cleared": score == total}
