from collections import deque
from functools import reduce

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def get_data(filename: str) -> list[list[int]]:
    with open(filename, "r") as f:
        return [[int(digit) for digit in list(number.strip())] for number in f]


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


def find_basins_bfs(data: list) -> list:
    basins = []
    visited = set()

    for row in range(len(data)):
        for col in range(len(data[row])):
            if (row, col) not in visited and data[row][col] != 9:
                basin_size = 0
                queue = deque()
                queue.append((row, col))
                while queue:
                    (r, c) = queue.popleft()
                    if (r, c) in visited:
                        continue
                    visited.add((r, c))
                    basin_size += 1
                    for dr, dc in DIRECTIONS:
                        rr = r + dr
                        cc = c + dc
                        if (
                            len(data) > rr >= 0
                            and len(data[row]) > cc >= 0
                            and data[rr][cc] != 9
                        ):
                            queue.append((rr, cc))
                basins.append(basin_size)
    return basins


def find_basins_dfs(data: list) -> list:
    basins = []
    visited = set()

    for row in range(len(data)):
        for col in range(len(data[row])):
            if (row, col) not in visited and data[row][col] != 9:
                basin_size = 0
                queue = []
                queue.append((row, col))
                while queue:
                    print(f"current queue {queue}")
                    (r, c) = queue.pop()
                    if (r, c) in visited:
                        continue
                    visited.add((r, c))
                    basin_size += 1
                    for dr, dc in DIRECTIONS:
                        rr = r + dr
                        cc = c + dc
                        if (
                            len(data) > rr >= 0
                            and len(data[row]) > cc >= 0
                            and data[rr][cc] != 9
                        ):
                            queue.append((rr, cc))
                basins.append(basin_size)
    return basins


data = get_data("test_input")
low_points = find_low_points(data)
risk_level = sum(int(number) + 1 for number in low_points)
basins_bfs = sorted(find_basins_bfs(data), reverse=True)
answer_bfs = reduce(lambda x, y: x * y, basins_bfs[:3])
print(answer_bfs)
# basins_dfs = sorted(find_basins_dfs(data), reverse=True)
# answer_dfs = reduce(lambda x, y: x * y, basins_dfs[:3])
# print(answer_bfs == answer_dfs)
