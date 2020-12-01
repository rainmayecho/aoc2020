from util import readfile
from typing import List

DAY = 1

def _twosum(nums: List[int], target: int = 2020):
    seen = set()
    for n in data:
        if target - n in seen:
            return n * (target - n)
        seen.add(n)

def _threesum(nums: List[int], target: int = 2020):
    seen = set()
    for i, n in enumerate(nums):
        for m in nums[i+1:]:
            x = target - n - m
            if x in seen:
                return (x * n * m)
            seen.add(m)


def solve_1(data: List[int], target: int = 2020):
    return _twosum(data)

def solve_2(data: List[int], target: int = 2020):
    return _threesum(data)


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = list(readfile(f, mapper=lambda x: int(x[0])))
        print(f"Part 1: {solve_1(data)}")
        print(f"Part 2: {solve_2(data)}")