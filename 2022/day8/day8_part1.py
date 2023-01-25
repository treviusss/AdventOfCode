import logging

level = logging.DEBUG
logging.basicConfig(level=level, format="%(message)s")


def is_visible(nearby_trees: list[list[int]], current_tree: int) -> bool:
    return not (
        all(any(tree >= current_tree for tree in section) for section in nearby_trees)
    )


def get_data(file_name: str) -> list[str]:
    with open(file_name, "r", encoding="utf-8") as f:
        return [line.strip("\n") for line in f]


def count_visible_trees(data: list) -> int:
    edge_visible_trees = len(data[0]) * 2 + (len(data[0]) - 2) * 2
    inner_visibile_trees = 0

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

            # logging.debug(f"{row=} {col=} {curr_tree=} {nearby_trees=}")
            tree_visibility = is_visible(nearby_trees, curr_tree)
            inner_visibile_trees += tree_visibility
            # logging.debug(f"{tree_visibility=} {inner_visibile_trees=}")

    logging.debug(f"{edge_visible_trees=} {inner_visibile_trees=}")
    trees_sum = edge_visible_trees + inner_visibile_trees
    return trees_sum


if __name__ == "__main__":
    data = get_data("day8_input")
    answer = count_visible_trees(data)
    print(answer)
