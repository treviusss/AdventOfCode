def get_data(filename: str) -> list[str]:
    with open(filename) as f:
        return [line.strip() for line in f]


def calculate_bits(data: list[str]) -> list[list[str]]:
    bits = []

    for column in range(len(data[0])):
        current_bits = []
        for row in range(len(data)):
            current_bits.append(data[row][column])
        bits.append(current_bits)

    return bits


def calculate_gamma_rate(data: list[list[str]]) -> int:
    return int(
        "".join(calculate_most_common(bits_array) for bits_array in data), base=2
    )


def calculate_epsilon_rate(gamma_rate: int) -> int:
    # epsilon is calculated by flipping bits of gamma rate value using XOR operation
    # with mask containing 12 ones
    mask = 0b111111111111
    return int(bin(gamma_rate ^ mask), base=2)


def calculate_most_common(lst: list):
    return max(set(lst), key=lst.count)


def main():
    data = get_data("day3_input")
    bits = calculate_bits(data)
    gamma_rate = calculate_gamma_rate(bits)
    epsilon_rate = calculate_epsilon_rate(gamma_rate)
    answer = gamma_rate * epsilon_rate
    print(answer)


if __name__ == "__main__":
    main()
