from dataclasses import dataclass
from enum import IntEnum


@dataclass
class Coordinates:
    row: int = 0
    col: int = 0


class Directions(IntEnum):
    RIGHT = 3
    DOWN = 1


def get_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def traverse_forest(data: list) -> int:
    row_len = len(data)
    col_len = len(data[0])
    coords = Coordinates()
    trees_encountered = 0

    while coords.row < row_len:
        if data[coords.row][coords.col % col_len] == "#":
            trees_encountered += 1
        coords.col += Directions.RIGHT
        coords.row += Directions.DOWN

    return trees_encountered


def main() -> None:
    data = get_data("day3_input")
    trees = traverse_forest(data)
    print(trees)


if __name__ == "__main__":
    main()
