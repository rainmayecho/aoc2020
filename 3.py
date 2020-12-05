from util import readfile

DAY = 3

R = 3
D = 1


def solve_1(data):
    c = 3
    x = 0
    L = len(data[0])
    for row in data[1:]:
        x += int(row[c] == "#")
        c += R
        c %= L
    return x


def solve_2(data):
    L = len(data[0])
    H = len(data)
    p = 1
    for (right, down) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        i = down
        x = 0
        c = right
        while i < H:
            row = data[i]
            x += int(row[c] == "#")
            c += right
            c %= L
            i += down
        p *= x
    return p


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = list(readfile(f, mapper=lambda x: x[0].rstrip()))
        print(solve_1(data))
        print(solve_2(data))
