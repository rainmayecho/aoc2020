from typing import Any, Callable, Generator, List, Tuple, TypeVar

T = TypeVar("T")
SplitResult = List[str]
DIRECTIONS: List[Callable] = [
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y + 1),
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y - 1),
]


def readfile(
    f: "File", delimiter: str = ",", mapper: Callable[[SplitResult], T] = lambda x: x
) -> Generator[T, None, None]:
    yield from (mapper(line.split(delimiter)) for line in f)


def get_neighbors(
    cell: Tuple[int],
    grid: List[List[Any]],
    predicate: Callable[[int, int], bool] = lambda x, y: True,
) -> Generator[Tuple[int], None, None]:
    w, h = len(grid), len(grid[0])
    for step in DIRECTIONS:
        nx, ny = step(*cell)
        if nx >= 0 and nx < w and ny >= 0 and ny < h and predicate(nx, ny):
            yield nx, ny


if __name__ == "__main__":
    grid = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    assert list(map(lambda c: grid[c[0]][c[1]], get_neighbors((1, 1), grid))) == [
        1,
        5,
        7,
        3,
    ]
    assert list(
        map(
            lambda c: grid[c[0]][c[1]],
            get_neighbors((1, 1), grid, predicate=lambda x, y: grid[x][y] != 1),
        )
    ) == [5, 7, 3]
