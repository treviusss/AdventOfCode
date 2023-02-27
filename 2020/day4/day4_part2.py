import re
from abc import ABC, abstractmethod


class Validate(ABC):
    @abstractmethod
    def validate_field(self, field) -> None:
        pass


class ValidateYear(Validate):
    def __init__(self, lower_bound: int, upper_bound: int) -> None:
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def validate_field(self, field) -> bool:
        match = re.match(r"\d{4}", field)
        result = None
        if match:
            try:
                year = int(match.group())
                result = self.lower_bound <= year <= self.upper_bound
            except TypeError as e:
                raise e
        if result is not None:
            return result
        return False


class ValidateHeight(Validate):
    def __init__(self) -> None:
        self.cm_lower_bound = 150
        self.cm_upper_bound = 193
        self.in_lower_bound = 59
        self.in_upper_bound = 76

    def validate_field(self, field) -> bool:
        match = re.match(r"(\d+)(cm|in)", field)
        if match:
            try:
                height = int(match.group(1))
            except TypeError as e:
                raise e

            if match.group(2) == "cm":
                return self.cm_lower_bound <= height <= self.cm_upper_bound

            if match.group(2) == "in":
                return self.in_lower_bound <= height <= self.in_upper_bound

        return False


class ValidateHairColor(Validate):
    def validate_field(self, field) -> bool:
        match = re.match(r"#[a-f0-9]{6}", field)
        if match:
            return True
        return False


class ValidateEyeColor(Validate):
    def validate_field(self, field) -> bool:
        eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return field in eye_colors


class ValidatePassportID(Validate):
    def validate_field(self, field) -> bool:
        # match = re.match(r"\b\d{9}\b", field)
        # if match:
        #     return True
        # return False
        return len(field) == 9 and all(char.isdigit() for char in field)


def get_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [data.replace("\n", " ") for data in f.read().split("\n\n")]


def parse_data(data: list) -> list[dict[str, str]]:
    parsed_passports = []

    for passport in data:
        current_passport = {}
        pairs = passport.split()
        for pair in pairs:
            key, value = pair.split(":")
            current_passport[key] = value
        parsed_passports.append(current_passport)

    return parsed_passports


def count_valid_passports(data: list) -> int:
    valid = 0

    for passport in data:
        keys = 0
        valid_data = 0
        for key, value in passport.items():
            if key == "cid":
                continue
            keys += 1
            valid_obj = FIELDS[key]
            if valid_obj.validate_field(value):
                valid_data += 1
        if keys == valid_data == len(FIELDS):
            valid += 1

    return valid


def main() -> None:
    global FIELDS
    FIELDS = {
        "byr": ValidateYear(1920, 2002),
        "iyr": ValidateYear(2010, 2020),
        "eyr": ValidateYear(2020, 2030),
        "hgt": ValidateHeight(),
        "hcl": ValidateHairColor(),
        "ecl": ValidateEyeColor(),
        "pid": ValidatePassportID(),
    }
    data = get_data("day4_input")
    data = parse_data(data)
    print(count_valid_passports(data))


if __name__ == "__main__":
    main()
