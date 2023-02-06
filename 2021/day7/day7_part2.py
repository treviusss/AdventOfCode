def get_data(filename: str) -> list:
    with open(filename, "r") as f:
        return [int(number) for number in f.read().split(",")]


def brute_force(data: list):
    max_ = max(data)
    min_ = min(data)

    most_efficient = None
    for horizontal_pos in range(min_, max_ + 1):
        curr_fuel = 0
        for number in data:
            diff = abs(number - horizontal_pos)
            curr_fuel += (
                diff * (diff + 1) // 2
            )  # equation for sum of consecutive numbers
        if most_efficient is None or curr_fuel < most_efficient:
            most_efficient = curr_fuel
    return most_efficient


data = get_data("day7_input")
answer = brute_force(data)
print(answer)
