from collections import defaultdict


def get_data(filename: str):
    with open(filename, "r") as f:
        return [line.strip("\n") for line in f]


def parse_data(data: list):
    return [[seq.strip() for seq in pattern.split("|")] for pattern in data]


def decode(data: list):
    count = []
    for array in data:

        numbers = defaultdict(set)
        five_chars = []
        six_chars = []
        signal_patterns, output = array
        signal_patterns = signal_patterns.split()
        signal_patterns.sort(key=len)

        for pattern in signal_patterns:
            if len(pattern) == 2:
                numbers[1] = set(pattern)
            elif len(pattern) == 3:
                numbers[7] = set(pattern)
            elif len(pattern) == 4:
                numbers[4] = set(pattern)
            elif len(pattern) == 7:
                numbers[8] = set(pattern)
            elif len(pattern) == 5:
                five_chars.append(set(pattern))
            elif len(pattern) == 6:
                six_chars.append(set(pattern))

        # find number 3
        number_3 = [
            pattern
            for pattern in five_chars
            if len(numbers[1].intersection(pattern)) == 2
        ][0]
        numbers[3] = number_3
        five_chars.remove(number_3)

        # find number 9
        number_9 = [
            pattern
            for pattern in six_chars
            if len(numbers[3].intersection(pattern)) == 5
        ][0]
        numbers[9] = number_9
        six_chars.remove(number_9)

        # find number 0
        number_0 = [
            pattern
            for pattern in six_chars
            if len(numbers[7].intersection(pattern)) == 3
        ][0]
        numbers[0] = number_0
        six_chars.remove(number_0)

        # find number 6
        numbers[6] = six_chars[0]

        # find number 5
        number_5 = [
            pattern
            for pattern in five_chars
            if len(numbers[6].intersection(pattern)) == 5
        ][0]
        numbers[5] = number_5
        five_chars.remove(number_5)

        # find number 2
        numbers[2] = five_chars[0]

        # compare words from output section and find corresponding number
        current_output = []
        for word in output.split():
            for key, value in numbers.items():
                if set(word) == value:
                    current_output.append(key)
        count.append(int("".join(str(number) for number in current_output)))

    return sum(count)


def main():
    data = get_data("day8_input")
    data = parse_data(data)
    answer = decode(data)
    print(answer)


if __name__ == "__main__":
    main()
