OPENING_BRACKETS = ["(", "[", "{", "<"]
CLOSING_BRACKETS = [")", "]", "}", ">"]
MATCHING_BRACKETS = {
    opening: closing for opening, closing in zip(OPENING_BRACKETS, CLOSING_BRACKETS)
}
BRACKET_POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def get_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def find_corrupted_lines(data: list) -> list:
    corrupted_lines = []

    for line in data:
        corrupted = False
        index = 0
        bracket_stack = []
        while not corrupted and index < len(line):
            if line[index] in OPENING_BRACKETS:
                bracket_stack.append(line[index])
            elif line[index] in CLOSING_BRACKETS:
                if MATCHING_BRACKETS.get(bracket_stack[-1]) == line[index]:
                    bracket_stack.pop()
                else:
                    corrupted_lines.append(line[: index + 1])
                    corrupted = True
            index += 1

    return corrupted_lines


def calculate_corrupted_lines_score(corrupted_list: list) -> int:
    return sum(BRACKET_POINTS[line[-1]] for line in corrupted_list)


def main() -> None:
    data = get_data("day10_input")
    corrupted_lines = find_corrupted_lines(data)
    corrupted_lines_score = calculate_corrupted_lines_score(corrupted_lines)
    print(corrupted_lines_score)


if __name__ == "__main__":
    main()
