import functools
import itertools
from operator import mul

TARGET_VALUE = 2020


def get_data(filename: str) -> list[int]:
    with open(filename, "r") as f:
        return [int(line.strip()) for line in f]


def find_target_value_components(data: list[int]):
    for index, item1 in enumerate(data):
        for _, item2 in enumerate(data, start=index + 1):
            if item1 + item2 == TARGET_VALUE:
                return item1, item2


def find_target_value_components2(data: list[int], n_components=2):
    combinations = itertools.combinations(data, n_components)
    for comb in combinations:
        if sum(comb) == TARGET_VALUE:
            return comb


def main():
    data = get_data("day1_input")
    values = find_target_value_components2(data, 3)
    ans = functools.reduce(mul, values, 1)
    print(ans)


if __name__ == "__main__":
    main()
