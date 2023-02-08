DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def get_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def find_low_points(data: list) -> list:
    low_points = []

    for row in range(len(data)):
        for col in range(len(data[0])):
            curr_number = data[row][col]
            neighbours = [
                data[row + dr][col + dc]
                for dr, dc in DIRECTIONS
                if len(data) > row + dr >= 0 and len(data[0]) > col + dc >= 0
            ]
            check_neighbours = [number for number in neighbours if curr_number < number]
            if len(check_neighbours) == len(neighbours):
                low_points.append(curr_number)

    return low_points


data = get_data("day9_input")
low_points = find_low_points(data)
risk_level = sum(int(number) + 1 for number in low_points)
print(risk_level)
