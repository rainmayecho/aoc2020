from util import readfile
from functools import reduce

DAY = 13


def solve_1(t0, buses):
    B = [int(b) for b in buses if b != "x"]
    best, x = (float("inf")), None
    for b in B:
        d, r = divmod(t0, b)
        v = (b * d) + b
        if r == 0:
            return t0
        elif v < best:
            best = min(best, v)
            x = b
    return (best - t0) * x


def solve_2(t0, buses):
    def remainders(data):
        res = 0
        p = reduce(lambda a, b: a * b[1], data, 1)
        for k, n in data:
            y = p // n
            res += k * y * pow(y, n - 2, n)
            res %= p
        return res

    data = [(int(n) - i, int(n)) for i, n in enumerate(buses) if n != "x"]
    return remainders(data)


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        t0 = int(f.readline().rstrip())
        buses = f.readline().rstrip().split(",")
        print(solve_1(t0, buses))
        print(solve_2(t0, buses))
