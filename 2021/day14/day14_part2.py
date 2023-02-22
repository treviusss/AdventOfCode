from collections import Counter


def get_data(filename: str) -> list:
    with open(filename, "r") as f:
        return f.read().split("\n\n")


def parse_data(data: list) -> tuple[str, dict]:
    initial_string, pair_rules = data
    pair_rules_dict = {}

    for pair in pair_rules.strip().split("\n"):
        a, b = pair.split(" -> ")
        pair_rules_dict[a] = b

    return initial_string, pair_rules_dict


def calculate_polymer(start: str, pair_rules: dict, steps=10) -> Counter:
    pair_counter = Counter()
    for i in range(len(start) - 1):
        pair_counter[start[i] + start[i + 1]] += 1

    for step in range(steps):
        current_step_counter = Counter()
        for pair in pair_counter:
            current_step_counter[pair[0] + pair_rules[pair]] += pair_counter[pair]
            current_step_counter[pair_rules[pair] + pair[1]] += pair_counter[pair]
        pair_counter = current_step_counter

    return pair_counter


def main() -> None:
    data = get_data("day14_input")
    start_str, pair_rules = parse_data(data)
    polymer = calculate_polymer(start_str, pair_rules, steps=40)
    count = Counter()
    for pair in polymer:
        count[pair[0]] += polymer[pair]
    count[start_str[-1]] += 1
    ans = count.most_common()[0][1] - count.most_common()[-1][1]
    print(ans)


if __name__ == "__main__":
    main()
