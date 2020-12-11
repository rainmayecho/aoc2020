from util import readfile
from typing import List, Callable, Any, Generator, Tuple
from copy import deepcopy

DAY = 11


DIRECTIONS: List[Callable] = [
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y + 1),
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x - 1, y - 1),
    lambda x, y: (x - 1, y + 1),
    lambda x, y: (x + 1, y - 1),
    lambda x, y: (x + 1, y + 1),
]


def get_neighbors(
    cell: Tuple[int],
    grid: List[List[Any]],
    predicate: Callable[[int, int], bool] = lambda x, y: True,
) -> Generator[Tuple[int], None, None]:
    w, h = len(grid), len(grid[0])
    for step in DIRECTIONS:
        nx, ny = step(*cell)
        if nx >= 0 and nx < w and ny >= 0 and ny < h and predicate(nx, ny):
            yield grid[nx][ny]


def get_neighbors_far(
    cell: Tuple[int], grid: List[List[Any]]
) -> Generator[Tuple[int], None, None]:
    w, h = len(grid), len(grid[0])
    for step in DIRECTIONS:
        found = None
        prev_cell = cell
        while not found:
            nx, ny = step(*prev_cell)
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                break
            if nx >= 0 and nx < w and ny >= 0 and ny < h and grid[nx][ny] in ("#", "L"):
                found = grid[nx][ny]
            prev_cell = (nx, ny)
        yield found


def solve_1(data):
    h = len(data)
    w = len(data[0])

    grid = [list(row) for row in data]
    prev_state = "\n".join("".join(row) for row in grid)
    while True:
        new_grid = deepcopy(grid)
        for i in range(h):
            for j in range(w):
                if grid[i][j] == ".":
                    continue
                neighbors = list(get_neighbors((i, j), grid))
                if grid[i][j] == "L" and neighbors.count("#") == 0:
                    new_grid[i][j] = "#"
                elif grid[i][j] == "#" and neighbors.count("#") >= 4:
                    new_grid[i][j] = "L"

        state = "\n".join("".join(row) for row in new_grid)
        if state == prev_state:
            return state.count("#")
        prev_state = state
        grid = new_grid


def solve_2(data):
    h = len(data)
    w = len(data[0])

    grid = [list(row) for row in data]
    prev_state = "\n".join("".join(row) for row in grid)
    while True:
        new_grid = deepcopy(grid)
        for i in range(h):
            for j in range(w):
                if grid[i][j] == ".":
                    continue
                neighbors = list(get_neighbors_far((i, j), grid))
                if grid[i][j] == "L" and neighbors.count("#") == 0:
                    new_grid[i][j] = "#"
                elif grid[i][j] == "#" and neighbors.count("#") >= 5:
                    new_grid[i][j] = "L"

        state = "\n".join("".join(row) for row in new_grid)
        if state == prev_state:
            return state.count("#")
        prev_state = state
        grid = new_grid


if __name__ == "__main__":
    with open(f"{DAY}.in", "r") as f:
        data = [line.rstrip() for line in f]
        print(solve_1(list(data)))
        print(solve_2(list(data)))
