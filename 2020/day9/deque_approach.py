from collections import deque
from itertools import combinations


def get_data(filename: str) -> list[int]:
    with open(filename, "r") as f:
        return [int(line.strip()) for line in f]


def task1(data: list[int], size=25) -> int:
    d = deque(data[:size], size)

    for val in data[size:]:
        sums = {a + b for a, b in combinations(d, 2)}
        if val not in sums:
            return val
        d.append(val)
    return -1


def task2(data: list[int], target: int) -> deque:
    for size in range(2, len(data)):

        d = deque(data[:size], size)

        for val in data[size:]:
            sums = sum(d)
            if sums == target:
                return d
            d.append(val)

    return deque()


data = get_data("day9_input")
answer1 = task1(data)
answer2 = task2(data, answer1)
answer2 = sorted(answer2)
print(answer1)
print(answer2[0] + answer2[-1])
