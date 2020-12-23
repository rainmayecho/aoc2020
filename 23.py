from util import readfile
from collections import deque

DAY = 23

inp = "916438275"
# inp = "389125467"


def solve_1():
    l = list(map(int, inp))
    _min = 1
    _max = 9
    cups = deque(l)
    cur = cups[0]
    for i in range(100):
        three = []
        while cups[0] != cur:
            cups.rotate(-1)
        dest = cups[0] - 1
        cups.rotate(-1)
        for _ in range(3):
            three.append(cups.popleft())
        cur = cups[0]
        while dest < _min or dest > _max or dest in three:
            dest -= 1
            if dest < _min:
                dest = _max

        while cups[0] != dest:
            cups.rotate(-1)

        l = cups.popleft()
        for c in reversed(three):
            cups.appendleft(c)
        cups.appendleft(l)
    while cups[0] != 1:
        cups.rotate(1)

    cups.popleft()
    return "".join(map(str, cups))


N = int(1e6)
M = int(1e7)


def solve_2():
    L = list(map(int, inp))
    ll = len(L)
    cups = L[0:1] + [0] * ll
    for i in range(ll):
        cups[L[i]] = L[i + 1] if i + 1 < ll else 10
    for i in range(10, N):
        cups.append(i + 1)
    cups += [cups[0], N, 1]
    for _ in range(M):
        cur = cups[0]
        nc = cups[cur]
        three = []
        for _ in range(3):
            three.append(nc)
            nc = cups[nc]
        cups[cur] = nc
        dest = (cur - 1) or N
        while dest in three:
            dest = (dest - 1) or N
        t = cups[dest]
        cups[dest] = three[0]
        cups[three[-1]] = t
        cups[0] = nc
    return cups[1] * cups[cups[1]]


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        print(solve_1())
        print(solve_2())
