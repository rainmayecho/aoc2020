from util import readfile
from collections import deque

DAY = 9


def _twosum(nums, target: int = 2020):
    seen = set()
    for n in data:
        if target - n in seen:
            return True
        seen.add(n)


def solve_1(data):
    window = deque(data[:25])
    for n in data[25:]:
        if not _twosum(window, target=n):
            return n
        window.popleft()
        window.append(n)


def solve_2(n, data):
    for i in range(len(data)):
        for j in range(i, len(data)):
            if sum(data[i:j]) == n:
                return min(data[i:j]) + max(data[i:j])


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = [int(line.rstrip()) for line in f]
        n = solve_1(data)
        print(n)
        print(solve_2(n, data))
