from util import readfile
from collections import defaultdict

DAY = 21


def solve_1(data):
    G = defaultdict(set)
    I = defaultdict(int)
    for line in data:
        line = line.replace("(", "").replace(")", "")
        ingredients, allergens = line.split(" contains ")
        ingredients = ingredients.split(" ")
        allergens = allergens.split(", ")
        for i in ingredients:
            I[i] += 1
        for a in allergens:
            if not a in G:
                G[a] = {*ingredients}
            else:
                G[a] &= {*ingredients}
    n = 0
    for i, c in I.items():
        if not any(i in a for a in G.values()):
            n += c
    res = {}
    while any(len(v) >= 1 for v in G.values()):
        remove = set()
        for k, v in list(G.items()):
            if len(v) == 1:
                res[[*v][0]] = k
                remove |= v
        for k in G:
            G[k] -= remove
    return ",".join(e[0] for e in sorted(res.items(), key=lambda e: e[1]))


def solve_2():
    pass


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = [line.rstrip() for line in f]
        print(solve_1(data))
