from util import readfile

DAY = 6


def solve_1(data):
    n, buffer = 0, set()
    for line in data:
        if not line:
            n += len(buffer)
            buffer = set()
            continue
        buffer = {*buffer, *line}
    return n + len(buffer)


def union_intersect(buffer):
    u = set()
    for v in buffer:
        u = {*u, *v}
    for v in buffer:
        u &= {*v}
    return u


def solve_2(data):
    n, buffer = 0, []
    for line in data:
        if not line:
            n += len(union_intersect(buffer))
            buffer = []
            continue
        buffer.append(line)
    return n + len(union_intersect(buffer))


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = [line.rstrip() for line in f]
        print(solve_1(data))
        print(solve_2(data))
