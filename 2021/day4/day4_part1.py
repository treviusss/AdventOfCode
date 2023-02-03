from collections import defaultdict


def get_data(filename: str) -> list:
    with open(filename) as f:
        content = f.read()
        return content.split("\n\n")


numbers, *boards = get_data("day4_input")
numbers = [int(number) for number in numbers.split(",")]
boards = [
    [[int(item) for item in row.split()] for row in board.splitlines()]
    for board in boards
]
bingo = defaultdict(list)


def check_win(bingo_board: dict):
    row_numbers = []
    column_numbers = []
    for board_index, board_hit in bingo_board.items():
        for row in range(len(boards[0])):
            for column in range(len(boards[0][0])):
                if (row, column) in board_hit:
                    row_numbers.append((row, column))
                if (column, row) in board_hit:
                    column_numbers.append((column, row))
            if len(row_numbers) == 5:
                return board_index, row_numbers
            elif len(column_numbers) == 5:
                return board_index, column_numbers
            else:
                row_numbers = []
                column_numbers = []
    return -1, []


def check_bingo(boards):
    for input_number in numbers:
        for board_index, board in enumerate(boards):
            for row_index, row in enumerate(board):
                for number_index, number in enumerate(row):
                    if number == input_number:
                        bingo[board_index].append((row_index, number_index))
                        check = check_win(bingo)
                        if check[0] != -1:
                            return input_number, check
    return -1, (-1, [])


last_number, (bingo_winning_index, bingo_winning_numbers_indices) = check_bingo(boards)
unmarked_numbers_sum = sum(
    boards[bingo_winning_index][row][column]
    for row in range(len(boards[bingo_winning_index]))
    for column in range(len(boards[bingo_winning_index][0]))
    if (row, column) not in bingo[bingo_winning_index]
)
answer = last_number * unmarked_numbers_sum
print(answer)
