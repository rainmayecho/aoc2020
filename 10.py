from util import readfile
from functools import lru_cache

DAY = 10


def solve_1(data):
    data.sort()
    prev, i = 0, 0
    a, b = 0, 0
    while i < len(data):
        x = data[i]
        diff = x - prev
        if diff == 1:
            a += 1
        elif diff == 3:
            b += 1
        prev = x
        i += 1
    return a * (b + 1)


def solve_2(data):
    n = data[-1]
    d = [1] + [0] * n
    for v in data:
        d[v] = d[v - 3] + d[v - 2] + d[v - 1]
    return d[-1]


if __name__ == "__main__":
    with open(f"{DAY}test.in", "r") as f:
        data = [int(line.rstrip()) for line in f]
        print(solve_1(data))
        print(solve_2(data))
