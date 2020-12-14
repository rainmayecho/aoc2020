from util import readfile
import re
from collections import defaultdict
from itertools import chain, combinations

LINE_REGEX = re.compile(r"(.*) = (.*)")

DAY = 14


def powerset(x):
    return list(chain.from_iterable(combinations(x, i) for i in range(len(x) + 1)))


def apply_mask(v, mask):
    res = 0
    for i, b in enumerate(reversed(mask)):
        if b == "X":
            res += v & (1 << i)
        elif b == "1":
            res += 1 << i
    return res


def apply_mask_indices(v, mask):
    res = 0
    arr = []
    for i, b in enumerate(reversed(mask)):
        if b == "X":
            arr.append(i)
        elif b == "1":
            res += 1 << i
        elif b == "0":
            res += v & (1 << i)
    if not arr:
        return [res]
    return powerset(arr)


def solve_1(data):
    mem = defaultdict(int)
    for line in data:
        lhs, rhs = LINE_REGEX.findall(line)[0]
        if "mask" in lhs:
            mask = rhs
        elif "mem" in lhs:
            mem[int(lhs[4:-1])] = apply_mask(int(rhs), mask)
    return sum(mem.values())


def solve_2(data):
    mem = defaultdict(int)
    for line in data:
        lhs, rhs = LINE_REGEX.findall(line)[0]
        if "mask" in lhs:
            mask = rhs
        elif "mem" in lhs:
            m1 = int(lhs[4:-1]) | int(mask.replace("X", "0"), 2)
            ps = apply_mask_indices(int(rhs), mask)
            for bits in ps:
                m2 = 0
                for b in bits:
                    m2 |= 1 << b
                mem[m1 ^ m2] = int(rhs)
    return sum(mem.values())


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = [line.rstrip() for line in f]
        print(solve_1(data))
        print(solve_2(data))
