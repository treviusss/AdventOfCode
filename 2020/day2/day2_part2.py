from typing import NamedTuple


class PasswordValidator(NamedTuple):
    positions: list[int]
    character: str
    password: str


def get_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def parse_data(data: list) -> list:
    parsed_data = []

    for line in data:
        condition, password = line.split(":")
        password = password.strip()
        positions, char = condition.split(" ")
        positions = [int(num) for num in positions.split("-")]
        entry = PasswordValidator(positions, char, password)
        parsed_data.append(entry)

    return parsed_data


def validate_password(data: PasswordValidator) -> bool:
    found = 0
    for pos in data.positions:
        if data.password[pos - 1] == data.character:
            found += 1
    if found == 1:
        return True
    return False


def main():
    data = get_data("day2_input")
    data = parse_data(data)
    ans = sum(validate_password(item) for item in data)
    print(ans)


if __name__ == "__main__":
    main()
