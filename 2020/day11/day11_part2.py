DIR = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
# UP, UP-RIGHT, RIGHT, DOWN-RIGHT, DOWN, DOWN-LEFT, LEFT, UP-LEFT, UP


def get_data(filename: str) -> list[list[str]]:
    with open(filename, "r") as f:
        return [[char for char in line.strip()] for line in f]


def display_layout(data: list[list[str]]) -> None:
    for row in range(len(data)):
        for col in range(len(data[row])):
            print(data[row][col], end="")
        print()


def occupied_seats(data: list[list[str]]) -> tuple[int, int]:
    i = 0
    prev_occupied_seats = []
    prev_empty_seats = []

    while True:
        occupied_seats: list[tuple] = []
        empty_seats: list[tuple] = []
        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] == ".":
                    continue
                occupied_adjacent_seats = 0
                for dr, dc in DIR:
                    multiplier = 1
                    while True:
                        rr = dr * multiplier + row
                        cc = dc * multiplier + col
                        if 0 <= rr < len(data) and 0 <= cc < len(data[row]):
                            if data[rr][cc] == "#":
                                occupied_adjacent_seats += 1
                                break
                            if data[rr][cc] == "L":
                                break
                            multiplier += 1
                        else:
                            break
                if occupied_adjacent_seats == 0:
                    occupied_seats.append((row, col))
                if data[row][col] == "#" and occupied_adjacent_seats >= 5:
                    empty_seats.append((row, col))
        for x, y in occupied_seats:
            data[x][y] = "#"
        for x, y in empty_seats:
            data[x][y] = "L"
        # display_layout(data)
        if prev_empty_seats == empty_seats and prev_occupied_seats == occupied_seats:
            break

        prev_empty_seats = empty_seats
        prev_occupied_seats = occupied_seats
        i += 1

    count_occupied_seats = sum(row.count("#") for row in data)
    return i, count_occupied_seats


def main() -> None:
    data = get_data("day11_input")
    i, count_occupied_seats = occupied_seats(data)
    print(i, count_occupied_seats)


if __name__ == "__main__":
    main()
