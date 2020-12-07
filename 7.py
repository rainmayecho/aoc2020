from util import readfile
from collections import defaultdict
import re

DAY = 7

LINE_REGEX = re.compile(r"(.*) contain (\d+.*,?)+")


def solve_1(data):
    G = defaultdict(set)
    for line in data:
        _d = LINE_REGEX.findall(line)
        if not _d:
            continue
        k, details = _d[0]
        for d in details.split(","):
            b = " ".join(d.lstrip().split(" ")[1:]).replace(".", "")
            if not b[-1] == "s":
                b += "s"
            G[k].add(b)
    target = "shiny gold bags"
    found = set()

    def dfs(k, seen, path=[]):
        if k in seen:
            return
        seen.add(k)
        if target in G[k]:
            found.add(path[0])
            return
        if k in G:
            for _k in G[k]:
                s = seen | {k}
                dfs(_k, s, path=path + [_k])

    for k in list(G.keys()):
        dfs(k, set(), path=[k])
    return len(found), G


def solve_2(data):
    G = defaultdict(set)
    for line in data:
        _d = LINE_REGEX.findall(line)
        if not _d:
            continue
        k, details = _d[0]
        for d in details.split(","):
            b = " ".join(d.lstrip().split(" ")[1:]).replace(".", "")
            x = int(d.lstrip().split(" ")[0])
            if not b[-1] == "s":
                b += "s"
            G[k].add((b, x))

    target = "shiny gold bags"

    def dfs(k):
        if not len(G[k]):
            return 0
        return sum((v[1] + v[1] * dfs(v[0])) for v in G[k])

    n = dfs(target)
    return n


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = [line.rstrip() for line in f]
        n, G = solve_1(data)
        print(n)
        print(solve_2(data))
