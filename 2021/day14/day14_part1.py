from collections import Counter, defaultdict


def get_data(filename: str) -> list:
    with open(filename, "r") as f:
        return f.read().split("\n\n")


def parse_data(data: list) -> tuple[str, dict]:
    initial_string, pair_rules = data
    pair_rules_dict = {}

    for pair in pair_rules.split("\n"):
        if pair:
            a, b = pair.split(" -> ")
            pair_rules_dict[a] = b

    return initial_string, pair_rules_dict


def calculate_polymer(start: str, pair_rules: dict, steps=10) -> list[str]:
    template = list(start)
    altered_template = []

    for step in range(steps):
        for i in range(len(template) - 1):
            curr_chunk = "".join(template[i : i + 2])
            if curr_chunk in pair_rules:
                altered_template.append(curr_chunk[0])
                altered_template.append(pair_rules[curr_chunk])
        altered_template.append(template[-1])
        template = altered_template
        altered_template = []

    return template


def main() -> None:
    data = get_data("day14_input")
    start_str, pair_rules = parse_data(data)
    polymer = calculate_polymer(start_str, pair_rules)
    count = Counter(polymer)
    ans = count.most_common()[0][1] - count.most_common()[-1][1]
    print(ans)


if __name__ == "__main__":
    main()
