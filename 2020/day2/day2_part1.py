import re
from typing import NamedTuple


class PasswordValidator(NamedTuple):
    range_condition: range
    character: str
    password: str


def get_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def parse_data(data: list) -> list:
    regexp = re.compile("(\d+)-(\d+)")
    parsed_data = []

    for line in data:
        condition, password = line.split(":")
        password = password.strip()
        char_range, char = condition.split(" ")
        lower_bound, upper_bound = [
            int(number)
            for number in regexp.match(char_range).groups()
            if number is not None
        ]
        entry = PasswordValidator(range(lower_bound, upper_bound + 1), char, password)
        parsed_data.append(entry)

    return parsed_data


def validate_password(data: PasswordValidator) -> bool:
    return data.password.count(data.character) in data.range_condition


def main() -> None:
    data = get_data("day2_input")
    data = parse_data(data)
    ans = sum(validate_password(item) for item in data)
    print(ans)


if __name__ == "__main__":
    main()
