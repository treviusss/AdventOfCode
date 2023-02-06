from collections import Counter


def get_data(filename: str) -> list:
    with open(filename, "r") as f:
        return f.read().splitlines()


def parse_data(data: list) -> list:
    return [
        [[int(item) for item in group.split(",")] for group in line.split(" -> ")]
        for line in data
    ]


def get_lines(data: list):
    vents = Counter()
    for pairs in data:
        (x1, y1), (x2, y2) = pairs
        if x1 == x2 or y1 == y2:
            diff_x = x2 - x1
            diff_y = y2 - y1
            sign_x = 1 if diff_x > 0 else (-1 if diff_x < 0 else 0)
            sign_y = 1 if diff_y > 0 else (-1 if diff_y < 0 else 0)

            for value in range(max(abs(diff_x), abs(diff_y)) + 1):
                x = x1 + value * sign_x
                y = y1 + value * sign_y
                vents[(x, y)] += 1
    return vents


data = get_data("day5_input")
data = parse_data(data)
lines = get_lines(data)
overlap = sum(1 for key, value in lines.items() if value >= 2)
print(overlap)
