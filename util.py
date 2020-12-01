from typing import Callable, Generator, List, TypeVar

T = TypeVar("T")
SplitResult = List[str]

def readfile(f: "File", delimiter: str = ",", mapper: Callable[[SplitResult], T] = lambda x: x) -> Generator[T, None, None]:
    yield from (
        mapper(line.split(delimiter)) for line in f
    )