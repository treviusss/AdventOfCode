from collections import Counter


def get_data(filename: str) -> list[str]:
    with open(filename) as f:
        return [line.strip() for line in f]


def calculate_oxygen_rating(data: list[str]):
    current_data = data[:]
    for column in range(len(current_data[0])):
        current_bits = []
        for row in range(len(current_data)):
            current_bits.append(current_data[row][column])
        if len(current_data) == 1:
            return current_data
        most_common = calculate_most_common(current_bits)
        current_data = [bits for bits in current_data if bits[column] == most_common]
    return current_data


def calculate_co2(data: list[str]):
    current_data = data[:]
    for column in range(len(current_data[0])):
        current_bits = []
        for row in range(len(current_data)):
            current_bits.append(current_data[row][column])
        if len(current_data) == 1:
            return current_data
        most_common = calculate_most_common(current_bits)
        current_data = [bits for bits in current_data if bits[column] != most_common]
    return current_data


def calculate_most_common(lst: list):
    counter = Counter(lst)
    if counter["1"] == counter["0"]:
        return "1"
    return counter.most_common(1)[0][0]


def main():
    data = get_data("day3_input")
    oxygen = calculate_oxygen_rating(data)
    co2 = calculate_co2(data)
    answer = int(oxygen[0], base=2) * int(co2[0], base=2)
    print(answer)


if __name__ == "__main__":
    main()
