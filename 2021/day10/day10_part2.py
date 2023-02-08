OPENING_BRACKETS = ["(", "[", "{", "<"]
CLOSING_BRACKETS = [")", "]", "}", ">"]
MATCHING_BRACKETS = {
    opening: closing for opening, closing in zip(OPENING_BRACKETS, CLOSING_BRACKETS)
}
BRACKET_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def get_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def find_incomplete_lines(data: list) -> list:
    incomplete_lines = []

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
                    corrupted = True
                    bracket_stack = []
            index += 1
        if bracket_stack:
            incomplete_lines.append(bracket_stack)

    return incomplete_lines


def complement_lines(lines: list) -> list[list[str]]:
    return [[MATCHING_BRACKETS[bracket] for bracket in line[::-1]] for line in lines]


def complemented_lines_score(complemented_list: list) -> list:
    lines_score = []

    for line in complemented_list:
        score = 0
        for bracket in line:
            score *= 5
            score += BRACKET_POINTS[bracket]
        lines_score.append(score)

    return lines_score


def find_middle_score(score_list: list) -> int:
    return sorted(score_list)[len(score_list) // 2]


def main():
    data = get_data("day10_input")
    incomplete_lines = find_incomplete_lines(data)
    complemented_lines = complement_lines(incomplete_lines)
    score = complemented_lines_score(complemented_lines)
    middle_score = find_middle_score(score)
    print(middle_score)


if __name__ == "__main__":
    main()
