FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}


def get_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [data.replace("\n", " ") for data in f.read().split("\n\n")]


def parse_data(data: list) -> list[str]:
    parsed_passport = []

    for passport in data:
        keys = []
        pairs = passport.split()
        for pair in pairs:
            key, values = pair.split(":")
            keys.append(key)
        parsed_passport.append(keys)

    return parsed_passport


def count_valid_passports(data: list) -> int:
    valid = 0

    for fields in data:
        fields = set(fields)
        if fields == FIELDS or (len(fields) == 7 and "cid" not in fields):
            valid += 1

    return valid


def main() -> None:
    data = get_data("day4_input")
    data = parse_data(data)
    ans = count_valid_passports(data)
    print(ans)


if __name__ == "__main__":
    main()
