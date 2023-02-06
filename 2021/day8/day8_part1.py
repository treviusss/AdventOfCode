from collections import defaultdict


def get_data(filename: str):
    with open(filename, "r") as f:
        return [line.strip("\n") for line in f]


def parse_data(data: list):
    return [[seq.strip() for seq in pattern.split("|")] for pattern in data]


def main():
    data = get_data("day8_input")
    data = parse_data(data)
    numbers = defaultdict(int)
    for signal_pattern, output in data:
        for chunk in output.split():
            numbers[len(chunk)] += 1
    answer = sum(value for key, value in numbers.items() if key in [2, 3, 4, 7])
    print(answer)


if __name__ == "__main__":
    main()
