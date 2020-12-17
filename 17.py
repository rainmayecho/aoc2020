from util import readfile
from copy import deepcopy
from collections import defaultdict
from itertools import product

DAY = 17

inp = """##..####
.###....
#.###.##
#....#..
...#..#.
#.#...##
..#.#.#.
.##...#."""

ACTIVE = "#"


def neighbors(cell, size=3):
    def step(delta):
        return tuple(a + b for a, b in zip(delta, cell))

    yield from (
        step(delta) for delta in product(range(-1, 2), repeat=size) if any(delta)
    )


def simulate(space, size):
    freq = defaultdict(int)
    for cell, v in [(cell, v) for cell, v in space.items() if v == "#"]:
        for nb in neighbors(cell, size=size):
            freq[nb] += 1

    next_space = defaultdict(lambda: ".")
    for cell, nc in freq.items():
        if space[cell] == ACTIVE and nc in (2, 3):
            next_space[cell] = ACTIVE
        elif space[cell] != ACTIVE and nc == 3:
            next_space[cell] = ACTIVE
    return next_space


def solve_1(inp, size):
    space = defaultdict(lambda: ".")
    for i, row in enumerate(inp.split("\n")):
        for j, v in enumerate(row):
            space[(0, i, j)] = v
    for _ in range(6):
        space = simulate(space, size)
    return sum(int(v == "#") for v in space.values())


def solve_2(inp, size):
    space = defaultdict(lambda: ".")
    for i, row in enumerate(inp.split("\n")):
        for j, v in enumerate(row):
            space[(0, i, j, 0)] = v
    for _ in range(6):
        space = simulate(space, size)
    return sum(int(v == "#") for v in space.values())


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        print(solve_1(inp, 3))
        print(solve_2(inp, 4))
