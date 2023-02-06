def get_data(filename: str) -> list:
    with open(filename, "r") as f:
        return [int(number) for number in f.read().split(",")]


def lanternfish_simulation(data: list, days=80):
    lanternfishes = data[:]
    for day in range(days):
        temp_lanternfishes = []
        new_fishes = 0
        for fish in lanternfishes:
            curr_fish = fish - 1
            if curr_fish < 0:
                curr_fish = 6
                new_fishes += 1
            temp_lanternfishes.append(curr_fish)
        if new_fishes:
            temp_lanternfishes.extend(new_fishes * [8])
        lanternfishes = temp_lanternfishes
    return lanternfishes


data = get_data("day6_input")
lanternfish = lanternfish_simulation(data)
print(lanternfish.__len__())
