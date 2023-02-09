DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0), (1, -1), (1, 1), (-1, 1), (-1, -1)]
# U R D L UR DR DL UL


def get_data(filename: str) -> list[list[int]]:
    with open(filename, "r") as f:
        return [[int(number) for number in line.strip()] for line in f]


def get_octopus_flashes(data: list[list[int]], steps: int) -> int:
    flash_count = 0
    octopuses_state = data
    for step in range(steps):
        octopuses_state = [[number + 1 for number in row] for row in octopuses_state]
        for row in range(len(octopuses_state)):
            for col in range(len(octopuses_state[row])):
                if octopuses_state[row][col] >= 10:
                    octopuses_state, flash_count = flash(
                        octopuses_state, row, col, flash_count
                    )
        for row in range(len(octopuses_state)):
            for col in range(len(octopuses_state[row])):
                if octopuses_state[row][col] == -1:
                    octopuses_state[row][col] = 0
    return flash_count


def flash(data: list, row: int, col: int, flash_count: int) -> tuple:
    flash_count += 1
    data[row][col] = -1
    for dr, dc in DIRECTIONS:
        rr = row + dr
        cc = col + dc
        if 0 <= rr < len(data) and 0 <= cc < len(data[row]) and data[rr][cc] != -1:
            data[rr][cc] += 1
            if data[rr][cc] >= 10:
                data, flash_count = flash(data, rr, cc, flash_count)
    return data, flash_count


def main() -> None:
    data = get_data("day11_input")
    flashes = get_octopus_flashes(data, 100)
    print(flashes)


if __name__ == "__main__":
    main()
