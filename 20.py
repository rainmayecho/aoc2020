from collections import defaultdict, deque
from util import readfile
from copy import deepcopy, copy
from itertools import product

import re


DAY = 20


def rotate(arr):
    return list(zip(*arr))[::-1]


def flip(arr):
    return [row[::-1] for row in arr]


def solve_1(data):
    tiles = {}
    i = 0
    L = len(data)
    while i < L:
        line = data[i]
        if "Tile" in line:
            _id = int(line.split(" ")[1][:-1])
            tile = []
            i += 1
            while i < L:
                line = data[i]
                if not line:
                    tiles[_id] = tile
                    break
                row = list(line)
                tile.append(row)
                i += 1
        i += 1

    A = defaultdict(set)
    for k, v in tiles.items():
        _arr = deepcopy(v)
        for n in range(4):
            z = "".join(_arr[0])
            A[z].add(k)
            A[z[::-1]].add(k)
            _arr = rotate(_arr)

    counts = defaultdict(int)
    seen = set()
    for k, v in A.items():
        if len(v) >= 2:
            for _id in v:
                counts[_id] += 1
            seen.add(k)
            seen.add(k[::-1])
    p = 1
    corners = []
    for n, c in counts.items():
        if c == 4:
            corners.append(n)
            p *= n
    print(p, corners)


class Tile:
    def __init__(self, _id, _data):
        self.id = _id
        self.__original = _data

    @property
    def flipped(self):
        return Tile(self.id, flip(self.__original))

    @property
    def data(self):
        return copy(self.__original)

    @staticmethod
    def __top(arr):
        return "".join(arr[0])

    @staticmethod
    def __bottom(arr):
        return "".join(arr[-1])

    @staticmethod
    def __left(arr):
        return "".join(arr[i][0] for i in range(len(arr)))

    @staticmethod
    def __right(arr):
        return "".join(arr[i][-1] for i in range(len(arr)))

    @property
    def top(self):
        return self.__top(self.__original)

    @property
    def bottom(self):
        return self.__bottom(self.__original)

    @property
    def left(self):
        return self.__left(self.__original)

    @property
    def right(self):
        return self.__right(self.__original)

    @property
    def rotations(self):
        arr = deepcopy(self.__original)
        for _ in range(4):
            yield Tile(self.id, copy(arr))
            arr = rotate(arr)
        arr = flip(self.__original)
        for _ in range(4):
            yield Tile(self.id, copy(arr))
            arr = rotate(arr)

    def __repr__(self):
        return f"<Tile {self.id}>"

    def __str__(self):
        return "\n".join("".join(row) for row in self.__original) + "\n"


class Image:
    def __init__(self, rows_of_tiles):
        self.__data = []
        for tile_row in rows_of_tiles:
            for i in range(1, len(tile_row[0].data) - 1):
                row = []
                for tile in tile_row:
                    row.extend(tile.data[i][1:-1])
                self.__data.append(row)

    @staticmethod
    def compare(a, b, mask):
        d = []
        for i, row in enumerate(b):
            r = []
            for j, c in enumerate(row):
                r.append(c if (i, j) in mask else " ")
            d.append(r)
        return Image.pprint(a) == Image.pprint(d)

    @staticmethod
    def scan(data, pattern):
        target = [list(r) for r in pattern.split("\n")]
        mask = {
            (i, j)
            for j in range(len(target[0]))
            for i in range(len(target))
            if target[i][j] == "#"
        }
        h, w = len(data), len(data[0])
        wh, ww = len(target), len(target[0])
        assert h > wh and w > ww
        n = 0
        for i in range(h - wh):
            for j in range(w - ww):
                window = []
                for row in data[i : i + wh]:
                    window.append(row[j : j + ww])
                if Image.compare(target, window, mask):
                    n += 1
        return n

    @property
    def rotations(self):
        arr = deepcopy(self.__data)
        for _ in range(4):
            yield arr
            yield flip(arr)
            arr = rotate(arr)

    @staticmethod
    def pprint(data):
        s = "\n".join("".join(row) for row in data) + "\n"
        return s

    def __str__(self):
        return "\n".join("".join(row) for row in self.__data) + "\n"


def solve_2(data):
    tiles = {}
    i = 0
    L = len(data)
    while i < L:
        line = data[i]
        if "Tile" in line:
            _id = int(line.split(" ")[1][:-1])
            tile = []
            i += 1
            while i < L:
                line = data[i]
                if not line:
                    tiles[_id] = Tile(_id, tile)
                    break
                row = list(line)
                tile.append(row)
                i += 1
        i += 1

    S = int(len(tiles) ** 0.5)
    img = [[None] * S for _ in range(S)]

    result = None
    monster = """                  #
#    ##    ##    ###
 #  #  #  #  #  #   """
    C = monster.count("#")

    def construct(i, j, seen):
        nonlocal img
        nonlocal tiles
        nonlocal result
        if i == S:
            if not result:
                result = Image(deepcopy(img))
                total = str(result).count("#")
                ans = float("inf")
                for rotated in result.rotations:
                    n = total - (Image.scan(rotated, monster) * C)
                    ans = min(ans, n)
                print(ans)
            return
        elif j == S:
            construct(i + 1, 0, seen)
            return

        for _id, tile in tiles.items():
            if _id in seen:
                continue

            for rotated_tile in tile.rotations:
                x = 1
                if i:
                    x &= rotated_tile.top == img[i - 1][j].bottom
                if j:
                    x &= rotated_tile.left == img[i][j - 1].right
                if x:
                    img[i][j] = rotated_tile
                    seen.add(_id)
                    construct(i, j + 1, seen)
                    seen.remove(_id)

    construct(0, 0, set())


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = [line.rstrip() for line in f]
        print(solve_1(data))
        print(solve_2(data))
