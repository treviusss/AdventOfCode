import logging
from functools import reduce
from operator import mul

level = logging.INFO
logging.basicConfig(level=level, format="%(message)s")


def get_data(file_name: str) -> list[str]:
    with open(file_name, "r", encoding="utf-8") as f:
        return [line.strip("\n") for line in f]


def is_visible(nearby_trees: list[list[int]], current_tree: int) -> bool:
    return not (
        all(any(tree >= current_tree for tree in section) for section in nearby_trees)
    )


def scenic_score(nearby_trees: list[list[int]], current_tree: int) -> int:
    score = []
    for index, section in enumerate(nearby_trees):
        if index % 2 == 0:
            section = section[::-1]
        direction_score = 0
        logging.debug(f"{index=} {section=}")
        for tree in section:
            if tree < current_tree:
                direction_score += 1
            if tree >= current_tree:
                direction_score += 1
                break
        score.append(direction_score)
    logging.debug(f"{current_tree=} {nearby_trees=} {score=}")
    return reduce(mul, score)


def traverse_trees(data: list) -> int:
    highest_scenic_score = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            row_len = len(data) - 1
            col_len = len(data[row]) - 1
            if row == 0 or col == 0 or row == row_len or col == col_len:
                continue
            curr_tree = int(data[row][col])
            nearby_row = list(map(list, [data[row][:col], data[row][col + 1 :]]))
            nearby_column = [
                column[col] for column in data
            ]  # transpose matrix to have column as row
            nearby_column = [
                nearby_column[:row],
                nearby_column[row + 1 :],
            ]  # slice column to exclude current tree
            nearby_trees = [
                [int(number) for number in neighbour]
                for neighbour in nearby_row + nearby_column
            ]
            current_score = scenic_score(nearby_trees, curr_tree)
            if current_score > highest_scenic_score:
                highest_scenic_score = current_score
            # logging.debug(f"{row=} {col=} {curr_tree=} {nearby_trees=}")

    return highest_scenic_score


if __name__ == "__main__":
    data = get_data("day8_input")
    answer = traverse_trees(data)
    print(answer)
