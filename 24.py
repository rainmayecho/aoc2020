from util import readfile
from collections import defaultdict

DAY = 24

DIRS = {
    "ne": lambda n: n + complex(1, 1),
    "e": lambda n: n + complex(2, 0),
    "se": lambda n: n + complex(1, -1),
    "sw": lambda n: n + complex(-1, -1),
    "w": lambda n: n + complex(-2, 0),
    "nw": lambda n: n + complex(-1, 1),
}

WHITE = 0
BLACK = 1


def neighbors(cell):
    yield from (step(cell) for step in DIRS.values())


def simulate(space):
    freq = defaultdict(int)
    for cell, v in [(cell, v) for cell, v in space.items() if v]:
        for nb in neighbors(cell):
            freq[nb] += 1
    next_space = defaultdict(int)
    for cell, nc in freq.items():
        if space[cell] == BLACK and nc in (0, 1, 2):
            next_space[cell] = BLACK
        elif space[cell] != BLACK and nc == 2:
            next_space[cell] = BLACK
    return next_space


def count(space, color=BLACK):
    return sum(v == color for v in space.values())


def solve_1(data):
    inc = defaultdict(int)
    for line in data:
        cur = complex(0, 0)
        i = 0
        while i < len(line):
            c = line[i]
            if c in ("n", "s"):
                i += 1
                c += line[i]
            cur = DIRS[c](cur)
            i += 1
        inc[cur] ^= 1
    return sum(v for v in inc.values())


def solve_2(data):
    space = defaultdict(int)
    for line in data:
        cur = complex(0, 0)
        i = 0
        while i < len(line):
            c = line[i]
            if c in ("n", "s"):
                i += 1
                c += line[i]
            cur = DIRS[c](cur)
            i += 1
        space[cur] ^= 1

    for i in range(1, 101):
        space = simulate(space)
    return count(space)


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = [line.rstrip() for line in f]
        print(solve_1(data))
        print(solve_2(data))
