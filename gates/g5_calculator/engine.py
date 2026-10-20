"""G5 공통 계산 엔진: 화면의 연산자를 바뀐 규칙대로 계산한다."""

# 화면에 보이는 연산자 -> 실제로 수행하는 연산
RULES = {
    "+": "-",
    "-": "+",
    "×": "÷",
    "÷": "×",
}

RULE_LABELS = {
    "+": "뺄셈",
    "-": "덧셈",
    "×": "나눗셈",
    "÷": "곱셈",
}


def calculate(a, op, b):
    """바뀐 규칙으로 a op b를 계산한다.

    성공: {"ok": True, "result": 숫자}
    실패: {"ok": False, "error": 메시지}  (0으로 나누기, 모르는 연산자)
    """
    if op not in RULES:
        return {"ok": False, "error": f"지원하지 않는 연산자예요: {op}"}

    actual = RULES[op]
    if actual == "-":
        result = a - b
    elif actual == "+":
        result = a + b
    elif actual == "×":
        result = a * b
    else:
        if b == 0:
            return {"ok": False, "error": "0으로 나눌 수 없어요."}
        result = a / b

    if isinstance(result, float) and result.is_integer():
        result = int(result)
    return {"ok": True, "result": result}
