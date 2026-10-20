import pytest

from gates.g5_calculator.engine import calculate
from gates.g5_calculator.feature_a import run_free_calc
from gates.g5_calculator.feature_b import PROBLEMS, grade


@pytest.mark.parametrize(
    "a, op, b, expected",
    [
        (7, "+", 3, 4),    # + 는 뺄셈
        (7, "-", 3, 10),   # - 는 덧셈
        (6, "×", 2, 3),    # × 는 나눗셈
        (9, "÷", 3, 27),   # ÷ 는 곱셈
    ],
)
def test_swapped_operators(a, op, b, expected):
    res = calculate(a, op, b)
    assert res == {"ok": True, "result": expected}


def test_division_by_zero_returns_error():
    res = calculate(5, "×", 0)
    assert res["ok"] is False
    assert "0" in res["error"]


def test_unknown_operator_returns_error():
    assert calculate(1, "%", 2)["ok"] is False


def test_free_calc_uses_swapped_rules():
    assert run_free_calc(2.5, "÷", 2) == {"ok": True, "result": 5}
    assert run_free_calc(1, "×", 0)["ok"] is False


def test_problems_are_fixed():
    assert PROBLEMS == [(7, "+", 3), (6, "×", 2), (9, "÷", 3)]


def test_grade_all_correct_clears():
    res = grade(["4", "3", "27"], already_graded=False)
    assert res == {"ok": True, "score": 3, "total": 3, "cleared": True}


def test_grade_accepts_numbers_and_spaces():
    assert grade([4, " 3 ", "27.0"], already_graded=False)["cleared"] is True


def test_grade_partial_wrong_does_not_clear():
    res = grade(["10", "3", "abc"], already_graded=False)
    assert res == {"ok": True, "score": 1, "total": 3, "cleared": False}


def test_grade_empty_answers():
    res = grade(["", None, ""], already_graded=False)
    assert res["score"] == 0
    assert res["cleared"] is False


def test_grade_blocks_duplicate_grading():
    res = grade(["4", "3", "27"], already_graded=True)
    assert res["ok"] is False
    assert "reason" in res
    assert "score" not in res
