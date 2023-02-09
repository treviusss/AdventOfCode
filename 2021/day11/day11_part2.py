DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0), (1, -1), (1, 1), (-1, 1), (-1, -1)]
# U R D L UR DR DL UL


def get_data(filename: str) -> list[list[int]]:
    with open(filename, "r") as f:
        return [[int(number) for number in line.strip()] for line in f]


def find_simultaneously_flash_step(data: list[list[int]], step_limit=9999) -> int:
    octopuses_state = data
    step = 1
    while step <= step_limit:
        all_flash = True
        octopuses_state = [[number + 1 for number in row] for row in octopuses_state]
        for row in range(len(octopuses_state)):
            for col in range(len(octopuses_state[row])):
                if octopuses_state[row][col] >= 10:
                    octopuses_state = flash(octopuses_state, row, col)
        for row in range(len(octopuses_state)):
            for col in range(len(octopuses_state[row])):
                if octopuses_state[row][col] == -1:
                    octopuses_state[row][col] = 0
                else:
                    all_flash = False
        if all_flash:
            return step
        step += 1
    return -1


def flash(data: list, row: int, col: int) -> list:
    data[row][col] = -1
    for dr, dc in DIRECTIONS:
        rr = row + dr
        cc = col + dc
        if 0 <= rr < len(data) and 0 <= cc < len(data[row]) and data[rr][cc] != -1:
            data[rr][cc] += 1
            if data[rr][cc] >= 10:
                data = flash(data, rr, cc)
    return data


def main() -> None:
    data = get_data("day11_input")
    all_flash_step = find_simultaneously_flash_step(data)
    if all_flash_step != -1:
        print(all_flash_step)


if __name__ == "__main__":
    main()
