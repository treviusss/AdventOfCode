def get_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def binary_search(input_str: str, low: int, high: int) -> int:
    mid = (low + high) // 2

    for char in input_str:
        if char == "F" or char == "L":
            high = mid
        elif char == "B" or char == "R":
            low = mid + 1
        mid = (low + high) // 2

    return mid


def check_boarding_pass(boarding_pass: str) -> tuple[int, int, int]:
    row_str, col_str = boarding_pass[:7], boarding_pass[7:]

    row = binary_search(row_str, 0, 127)
    col = binary_search(col_str, 0, 7)
    seat_id = row * 8 + col

    return row, col, seat_id


def test_check_boarding_pass() -> None:
    assert check_boarding_pass("BFFFBBFRRR") == (70, 7, 567)
    assert check_boarding_pass("FFFBBBFRRR") == (14, 7, 119)
    assert check_boarding_pass("BBFFBBFRLL") == (102, 4, 820)
    assert check_boarding_pass("FBFBBFFRLR") == (44, 5, 357)


def find_highest_seat_id(data: list) -> int | None:
    highest_seat_id = None

    for boarding_pass in data:
        row, col, seat_id = check_boarding_pass(boarding_pass)
        if highest_seat_id is None or seat_id > highest_seat_id:
            highest_seat_id = seat_id

    return highest_seat_id


def main() -> None:
    data = get_data("day5_input")
    test_check_boarding_pass()
    print(find_highest_seat_id(data))


if __name__ == "__main__":
    main()
