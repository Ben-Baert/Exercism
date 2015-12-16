import re

WORD_TO_OPERATOR = {
    "plus" : "+",
    "minus" : "-",
    "multiplied by" : "*",
    "divided by" : "//"
}

def apply_operators(word_problem):
    for word, operator in WORD_TO_OPERATOR.items():
        word_problem = word_problem.replace(word, operator)
    return word_problem

def apply_order_brackets(word_problem):
    return re.sub(r"([\-0-9]+[\s\+\-\*\/]+[\-0-9]+)", r"(\1)", word_problem, count=1)

def calculate(word_problem):
    try:
        return eval(apply_order_brackets(apply_operators(word_problem[8:-1])))
    except Exception:
        raise ValueError