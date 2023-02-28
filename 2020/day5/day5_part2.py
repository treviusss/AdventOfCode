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


def boarding_pass_parser(boarding_pass: str) -> tuple[int, int, int]:
    row_str, col_str = boarding_pass[:7], boarding_pass[7:]

    row = binary_search(row_str, 0, 127)
    col = binary_search(col_str, 0, 7)
    seat_id = row * 8 + col

    return row, col, seat_id


def test_boarding_pass_parser() -> None:
    assert boarding_pass_parser("BFFFBBFRRR") == (70, 7, 567)
    assert boarding_pass_parser("FFFBBBFRRR") == (14, 7, 119)
    assert boarding_pass_parser("BBFFBBFRLL") == (102, 4, 820)
    assert boarding_pass_parser("FBFBBFFRLR") == (44, 5, 357)


def find_highest_seat_id(data: list) -> int | None:
    highest_seat_id = None

    for boarding_pass in data:
        row, col, seat_id = boarding_pass_parser(boarding_pass)
        if highest_seat_id is None or seat_id > highest_seat_id:
            highest_seat_id = seat_id

    return highest_seat_id


def generate_seats_array(data: list) -> list[tuple[int, int, int]]:
    return [boarding_pass_parser(boarding_pass) for boarding_pass in data]


def main() -> None:
    data = get_data("day5_input")
    seats = sorted(generate_seats_array(data))
    seats_set = set(item[-1] for item in seats)
    all_poss_seats = set(range(seats[0][-1], seats[-1][-1] + 1))
    missing = all_poss_seats.difference(seats_set)
    print(missing)


if __name__ == "__main__":
    main()
