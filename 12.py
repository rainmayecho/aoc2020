from util import readfile
from collections import deque

from math import pi
import math

DAY = 12


def rotate(p, angle):
    px, py = p
    return (
        math.cos(angle) * px - math.sin(angle) * py,
        math.sin(angle) * px + math.cos(angle) * py,
    )


def solve_1(data):
    DIRS = deque(["E", "S", "W", "N"])
    STEPS = {
        "E": lambda x, y, d: (x + d, y),
        "N": lambda x, y, d: (x, y - d),
        "W": lambda x, y, d: (x - d, y),
        "S": lambda x, y, d: (x, y + d),
    }

    ANGLES = {90: 1, 180: 2, 270: 3, 360: 4, -90: -1, -180: -2, -270: -3, -360: -4}

    D = "E"
    pos = (0, 0)
    for I in data:
        direction, val = I[0], I[1:]
        val = int(val)
        if direction in ("L", "R"):
            k = ANGLES[val * (-1 if direction == "R" else 1)]
            DIRS.rotate(k)
            D = DIRS[0]
        elif direction == "F":
            pos = STEPS[D](*pos, val)
        else:
            pos = STEPS[direction](*pos, val)
    a, b = pos
    return a + b


def solve_2(data):
    steps = {
        "E": lambda x, y, d: (x + d, y),
        "N": lambda x, y, d: (x, y + d),
        "W": lambda x, y, d: (x - d, y),
        "S": lambda x, y, d: (x, y - d),
    }
    wp = (10, 1)
    pos = (0, 0)
    for I in data:
        direction, val = I[0], int(I[1:])
        vr = val / 90 * pi / 2
        if direction == "F":
            dx, dy = wp
            pos = (pos[0] + (dx * val), pos[1] + (dy * val))
        elif direction in steps:
            wp = steps[direction](*wp, val)
        elif direction == "R":
            wp = rotate(wp, -vr)
        elif direction == "L":
            wp = rotate(wp, vr)
    a, b = pos
    return round(abs(a) + abs(b))


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = [line.rstrip() for line in f]
        print(solve_1(data))
        print(solve_2(data))
