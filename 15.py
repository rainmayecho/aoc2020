from util import readfile
from collections import defaultdict, deque

DAY = 15


def solve_1():
    inp = "9,19,1,6,0,5,4"
    inp = list(map(int, inp.split(",")))
    ms = defaultdict(list)
    for i, n in enumerate(inp):
        ms[n].append(i + 1)

    res = list(inp)
    prev = deque(inp[-2:])
    offset = len(inp) + 1
    for i in range(30000000 - len(inp)):
        indices = ms[prev[-1]]
        if len(indices) == 1:
            n = 0
        else:
            n = indices[-1] - indices[-2]
        ms[n].append(i + offset)
        res.append(n)
        prev.append(n)
        prev.popleft()
    return res[-1]


def solve_2():
    pass


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        print(solve_1())
