"""G5-A: 공개된 바뀐 연산 규칙대로 자유 계산"""

from gates.g5_calculator.engine import calculate


def run_free_calc(a, op, b):
    """숫자 2개와 화면 연산자를 받아 바뀐 규칙대로 계산한 결과를 돌려준다."""
    return calculate(a, op, b)
