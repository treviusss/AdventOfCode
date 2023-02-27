import itertools
from operator import mul

TARGET_VALUE = 2020


def get_data(filename: str) -> list[int]:
    with open(filename, "r") as f:
        return [int(line.strip()) for line in f]


def find_target_value_components(data: list[int]) -> tuple[int, int] | None:
    for index, item1 in enumerate(data):
        for _, item2 in enumerate(data, start=index + 1):
            if item1 + item2 == TARGET_VALUE:
                return item1, item2


def find_target_value_components2(
    data: list[int], n_components=2
) -> tuple[int, int] | None:
    combinations = itertools.combinations(data, n_components)
    for item1, item2 in combinations:
        if item1 + item2 == TARGET_VALUE:
            return item1, item2


def main():
    data = get_data("day1_input")
    values = find_target_value_components2(data)
    ans = mul(*values)
    print(ans)


if __name__ == "__main__":
    main()
