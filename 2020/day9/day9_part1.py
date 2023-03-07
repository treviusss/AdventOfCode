from itertools import combinations


def get_data(filename: str) -> list[int]:
    with open(filename, "r") as f:
        return [int(line.strip()) for line in f]


def answer(data: list[int], preamble=25) -> int:
    preamble += 1
    for i in range(len(data) - preamble + 1):
        chunk = data[i : i + preamble]
        num_to_check = chunk[-1]
        chunk = chunk[:-1]
        comb = [sum(pair) for pair in combinations(chunk, 2)]
        if num_to_check not in comb:
            return num_to_check
    return -1


def main() -> None:
    data = get_data("day9_input")
    print(answer(data))


if __name__ == "__main__":
    main()
