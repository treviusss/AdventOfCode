import logging
from collections import deque

level = logging.INFO
logging.basicConfig(level=level, format="%(messsage)s")

START_CHAR = "S"
END_CHAR = "E"

DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_data(file_name: str) -> list[str]:
    with open(file_name, "r", encoding="utf-8") as f:
        return [line.strip("\n") for line in f]


def find_start(data: list, target) -> deque[tuple[tuple[int, int], int]]:
    queue = deque()
    for index_row, number_row in enumerate(data):
        for index_col, number_col in enumerate(data[index_row]):
            if number_col == target:
                queue.append(((index_row, index_col), 0))
    return queue


def transform_char_into_numbers(data) -> list[list[int]]:
    # transform each letter in input data to corresponding number in alphabet starting
    # with "a" as 1, "b" as 2 etc. assuming startign point S is the lowest elevation,
    # same as "a", and E is the highest elevation same as "z"
    row_len = len(data)
    col_len = len(data[0])

    char_into_number_array = [[0 for _ in range(col_len)] for _ in range(row_len)]
    for row_idx in range(row_len):
        for col_idx in range(col_len):
            if data[row_idx][col_idx] == START_CHAR:
                char_into_number_array[row_idx][col_idx] = 1
            elif data[row_idx][col_idx] == END_CHAR:
                char_into_number_array[row_idx][col_idx] = 26
            else:
                char_into_number_array[row_idx][col_idx] = (
                    ord(data[row_idx][col_idx]) - ord("a") + 1
                )

    return char_into_number_array


def breadth_first_search(data: list, transformed_data: list):
    row_len = len(data)
    col_len = len(data[0])
    queue = find_start(
        data, "a"
    )  # filling the queue with coords of the lowest elevation hence string "a"

    visited = set()
    while queue:
        (row_coord, col_coord), distance = queue.popleft()
        if (row_coord, col_coord) in visited:
            continue
        # otherwise
        visited.add((row_coord, col_coord))

        if data[row_coord][col_coord] == END_CHAR:
            return distance

        for dir_row, dir_col in DIR:
            new_row_coord = row_coord + dir_row
            new_col_coord = col_coord + dir_col
            if (
                0 <= new_row_coord < row_len
                and 0 <= new_col_coord < col_len
                and transformed_data[new_row_coord][new_col_coord] - 1
                <= transformed_data[row_coord][col_coord]
            ):
                queue.append(((new_row_coord, new_col_coord), distance + 1))
    return -1


def main():
    data = get_data("day12_input")
    number_array = transform_char_into_numbers(data)
    answer = breadth_first_search(data, number_array)
    print(answer)


if __name__ == "__main__":
    main()
