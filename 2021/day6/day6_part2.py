from collections import Counter, defaultdict


def get_data(filename: str) -> list:
    with open(filename, "r") as f:
        return [int(number) for number in f.read().split(",")]


def lanternfish_simulation(data: list, days=80):
    fishes = Counter(data)
    for day in range(days):
        temp_fishes = defaultdict(int)
        for fish, amount in fishes.items():
            if fish == 0:
                temp_fishes[6] += amount
                temp_fishes[8] += amount
            else:
                temp_fishes[fish - 1] += amount
        fishes = temp_fishes
    return sum(fishes.values())


data = get_data("day6_input")
lanternfish = lanternfish_simulation(data, days=256)
print(lanternfish)
