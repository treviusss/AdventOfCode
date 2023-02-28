import re
from collections import defaultdict


def get_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def parse_bags(data: list[str]) -> defaultdict:
    bags = defaultdict(list)

    for line in data:
        bag_color, bag_content = line.split(" bags contain ")
        if "no other" in bag_content:
            continue
        else:
            match = re.compile(r"(\d+) (\w+ \w+)")
            inner_bags = match.findall(bag_content)
            for amount, inner_bag_color in inner_bags:
                bags[bag_color].append((int(amount), inner_bag_color))

    return bags


def count_bags(target_bag="shiny gold") -> int:
    ans = 1
    for amount, bag in bags[target_bag]:
        result = amount * count_bags(bag)
        ans += result
    return ans


def main() -> None:
    global bags
    data = get_data("day7_input")
    bags = parse_bags(data)
    print(count_bags() - 1)


if __name__ == "__main__":
    main()
