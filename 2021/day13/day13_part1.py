from copy import deepcopy


def get_data(filename: str) -> list:
    with open(filename, "r") as f:
        return f.read().split("\n\n")


def parse_data(data: list[str]) -> tuple[list[list[int]], list[tuple[str, int]]]:
    coords, instructions = data
    coords = [
        [int(numbers) for numbers in coord.split(",")] for coord in coords.split("\n")
    ]
    instructions = [
        [foo for foo in instr.split()[-1].split("=")]
        for instr in instructions.split("\n")
    ]
    instructions = [(direction, int(amount)) for direction, amount in instructions]

    return coords, instructions


def display_dots(coords_data: list) -> None:
    row_max = max(x for x, y in coords_data)
    col_max = max(y for x, y in coords_data)
    board = [[" " for row in range(row_max + 1)] for col in range(col_max + 1)]
    for x, y in coords_data:
        board[y][x] = "#"
    print(*board, sep="\n")


def paper_fold(coords_data: list, folding_instruction: list) -> list[list[int]]:
    board = deepcopy(coords_data)
    for direction, amount in folding_instruction:
        if direction == "x":
            for index, (x, y) in enumerate(board):
                if x > amount:
                    distance_from_axis = x - amount
                    new_x = x - 2 * distance_from_axis
                    board[index][0] = new_x
        elif direction == "y":
            for index, (x, y) in enumerate(board):
                if y > amount:
                    distance_from_axis = y - amount
                    new_y = y - 2 * distance_from_axis
                    board[index][1] = new_y
        break
    return board


def main() -> None:
    data = get_data("day13_input")
    coords, instructions = parse_data(data)
    board = paper_fold(coords, instructions)
    unique = set(tuple(arr) for arr in board)
    print(len(unique))
    # display_dots(board)


if __name__ == "__main__":
    main()
