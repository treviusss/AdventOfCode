from collections import Counter


def get_data(filename: str) -> list[int]:
    with open(filename, "r") as f:
        return [int(line.strip()) for line in f]


def answer(data: list[int], start: int = 0) -> list[int]:
    diffs = []
    current = start
    adapters = sorted(data)

    for adapter_rating in adapters:
        diff = adapter_rating - current
        if 1 <= diff <= 3:
            diffs.append(diff)
        current = adapter_rating

    diffs.append(3)  # add builtin adapter

    return diffs


def main() -> None:
    data = get_data("day10_input")
    diffs = answer(data)
    counter = Counter(diffs)
    print(counter[1] * counter[3])


if __name__ == "__main__":
    main()
