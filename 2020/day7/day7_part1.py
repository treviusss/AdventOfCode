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
                bags[inner_bag_color].append(bag_color)

    return bags


def dfs_bags(bags: dict[str, list[str]]) -> set:
    visited = set()
    Q = ["shiny gold"]

    while Q:
        color = Q.pop()
        if color in visited:
            continue
        visited.add(color)
        for bag in bags[color]:
            Q.append(bag)

    return visited


def main() -> None:
    data = get_data("day7_input")
    bags = parse_bags(data)
    ans = dfs_bags(bags)
    print(len(ans) - 1)


if __name__ == "__main__":
    main()
