from util import readfile
from collections import deque

DAY = 18

OPERATORS = {"*": 1, "+": 2}


def solve_1(data):
    def _eval(out):
        s = []
        for token in reversed(out):
            if token.isdigit():
                s.append(token)
            elif token in OPERATORS:
                a, b = list(map(int, (s.pop(), s.pop())))
                if token == "*":
                    s.append(a * b)
                else:
                    s.append(a + b)
        return s[0]

    s = 0
    for exp in data:
        tokens = exp.replace("(", "( ").replace(")", " )").split(" ")
        ops = []
        res = deque([])
        for token in tokens:
            if token == "(":
                ops.append(token)
            elif token == ")":
                while ops[-1] != "(":
                    res.appendleft(ops.pop())
                if ops and ops[-1] == "(":
                    ops.pop()
            if token.isdigit():
                res.appendleft(token)
            elif token in OPERATORS:
                while (
                    ops
                    and ops[-1] in OPERATORS
                    and OPERATORS[ops[-1]] >= OPERATORS[token]
                    and ops[-1] != "("
                ):
                    res.appendleft(ops.pop())
                ops.append(token)
        while ops:
            res.appendleft(ops.pop())

        s += _eval(res)
    return s


def solve_2(data):
    pass


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = [line.rstrip() for line in f]
        print(solve_1(data))
