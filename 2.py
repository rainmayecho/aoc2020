from util import readfile
from collections import Counter

DAY = 2

def solve_1(data):
    res = 0
    for rule, password in data:
        R, c = rule
        l, r = list(map(int, R.split("-")))
        d = Counter(password)
        if d.get(c, 0) >= l and d.get(c, 0) <= r:
            res += 1
    return res


def solve_2(data):
    res = 0
    for rule, password in data:
        R, c = rule
        l, r = list(map(int, R.split("-")))
        if (password[l-1] == c) ^ (password[r-1] == c):
            res += 1
    return res

if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = list(readfile(f, delimiter=": ", mapper=lambda x: [x[0].split(" "), x[1].rstrip()]))
        print(solve_1(data))
        print(solve_2(data))