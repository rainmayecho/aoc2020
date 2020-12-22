from util import readfile
from collections import deque, defaultdict

DAY = 22


def solve_1(data):
    players = [[], []]
    p = -1
    for line in data:
        if not line:
            continue
        if "Player" in line:
            p += 1
        else:
            players[p].append(int(line))
    p1, p2 = [list(v) for v in players]
    while p1 and p2:
        if p1[0] > p2[0]:
            p1.append(p1.pop(0))
            p1.append(p2.pop(0))
        else:
            p2.append(p2.pop(0))
            p2.append(p1.pop(0))

    print(sum((i + 1) * c for i, c in enumerate(reversed(max(p1, p2, key=len)))))

    def subgame(p1, p2, n=1):
        seen = defaultdict(set)
        winner = None
        r = 0
        while p1 and p2:
            r += 1
            if tuple(p1) in seen[1] or tuple(p2) in seen[2]:
                return 0
            if p1[0] < len(p1) and p2[0] < len(p2):
                x = subgame(list(p1[1 : p1[0] + 1]), list(p2[1 : p2[0] + 1]), n=n + 1)
                winner = p2 if x else p1
                other = p1 if x else p2
            elif p1[0] > p2[0]:
                winner = p1
                other = p2
            else:
                winner = p2
                other = p1
            seen[1].add(tuple(p1))
            seen[2].add(tuple(p2))
            winner.append(winner.pop(0))
            winner.append(other.pop(0))
        return (
            len(p2) > len(p1)
            if n > 1
            else sum((i + 1) * c for i, c in enumerate(reversed(max(p1, p2, key=len))))
        )

    return subgame(*players)


def solve_2(data):
    pass


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = [line.rstrip() for line in f]
        print(solve_1(data))
