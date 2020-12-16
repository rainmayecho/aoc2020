from util import readfile
import re
from functools import partial
from collections import defaultdict

DAY = 16

RULE_REGEX = re.compile(r"(.*): (\d+)-(\d+) or (\d+)-(\d+)")
TICKET_REGEX = re.compile(r"")


def _rule(a, b, c, d, n):
    # print(n in {*range(a, b+1)})
    # print(n in {*range(c, d+1)})
    return n in {*range(a, b + 1)} or n in {*range(c, d + 1)}


def solve_1(data):
    i = 0
    rule_map, your, nearby = {}, None, []
    while True:
        line = data[i]
        if "or" in line:
            x = RULE_REGEX.findall(line)[0]
            key = x[0]
            a, b, c, d = list(map(int, x[1:]))
            rule_map[key] = partial(_rule, a, b, c, d)
        elif "your ticket" in line:
            i += 1
            your = list(map(int, data[i].split(",")))
        elif "nearby tickets" in line:
            i += 1
            while i < len(data):
                nearby.append(list(map(int, data[i].split(","))))
                i += 1
            break
        i += 1

    s = 0
    possible = defaultdict(set)
    excluded = defaultdict(lambda: {10, 11, 12})

    for ticket in nearby + [your]:
        for i, n in enumerate(ticket):
            if not any(rule(n) for rule in rule_map.values()):
                s += n
                break
            for k, rule in rule_map.items():
                v = rule(n)
                if v and i not in excluded[k]:
                    possible[k].add(i)
                elif not v:
                    excluded[k].add(i)
                    if i in possible[k]:
                        possible[k].remove(i)
    print(s)
    I = set()
    while any(len(v) > 1 for v in possible.values()):
        remove = set()
        for k, v in list(possible.items()):
            if len(v) == 1:
                remove |= v
                if "departure" in k:
                    I |= v
        for k in possible:
            possible[k] -= remove

    p = 1
    for i in I:
        p *= your[i]
    return p


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = [line.rstrip() for line in f]
        print(solve_1(data))
