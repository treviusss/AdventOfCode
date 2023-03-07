from itertools import combinations


def get_data(filename: str) -> list[int]:
    with open(filename, "r") as f:
        return [int(line.strip()) for line in f]


def part1(data: list[int], preamble=25) -> int:
    preamble += 1
    for i in range(len(data) - preamble + 1):
        chunk = data[i : i + preamble]
        num_to_check = chunk[-1]
        chunk = chunk[:-1]
        comb = [sum(pair) for pair in combinations(chunk, 2)]
        if num_to_check not in comb:
            return num_to_check
    return -1


def part2(data: list[int], target: int) -> list[int]:
    for chunk_size in range(2, len(data)):
        for i in range(len(data) - chunk_size + 1):
            chunk = data[i : i + chunk_size]
            if sum(chunk) == target:
                return chunk
    return []


def main() -> None:
    data = get_data("day9_input")
    ans1 = part1(data)
    ans2 = part2(data, ans1)
    ans2.sort()
    print(ans2[0] + ans2[-1])


if __name__ == "__main__":
    main()
