import functools
import operator
from dataclasses import dataclass


@dataclass
class Coordinates:
    row: int = 0
    col: int = 0


@dataclass
class Directions:
    right: int
    down: int


def get_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def traverse_forest(data: list, right: int, down: int):
    row_len = len(data)
    col_len = len(data[0])

    coords = Coordinates()
    directions = Directions(right, down)

    trees_encountered = 0

    while coords.row < row_len:
        if data[coords.row][coords.col % col_len] == "#":
            trees_encountered += 1
        coords.col += directions.right
        coords.row += directions.down

    return trees_encountered


def main() -> None:
    data = get_data("day3_input")
    slopes_to_check = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    ans = functools.reduce(
        operator.mul,
        (traverse_forest(data, right, down) for right, down in slopes_to_check),
    )
    print(ans)


if __name__ == "__main__":
    main()
