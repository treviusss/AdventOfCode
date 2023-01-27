# from dataclasses import dataclass

# @dataclass
# class Monkey:
#     id: int
#     items: list
#     worry_level: int
#     test: int

import logging
import re
from math import floor
from operator import add, mul, pow
from typing import Any

level = logging.INFO
logging.basicConfig(level=level, format="%(message)s")

OPERATORS = {"*": mul, "+": add, "**": pow}
WORRY_LEVEL_BORED = 3


def parse_input_data(filename: str) -> dict[int, Any]:
    monkeys = {}

    with open(filename, "r") as f:
        monkey_number = 0
        for line in f:
            if line == "\n":
                continue
            key, value = line.split(":")
            key = key.lower().strip()
            value = value.strip()

            if key.startswith("monkey"):
                _, monkey_num = key.split()
                monkey_number = int(monkey_num)
                monkeys[monkey_number] = {}
                monkeys[monkey_number]["inspect"] = 0

            elif key.startswith("starting"):
                items = [int(item) for item in value.split(", ")]
                monkeys[monkey_number]["items"] = items

            elif key.startswith("operation"):
                value = re.sub(r"old \* old", r"old ** 2", value)
                match_operation = re.search(r"(\+|\*+)\s(\d+)", value)
                monkeys[monkey_number]["operation"] = match_operation.group(1), int(
                    match_operation.group(2)
                )
                # logging.debug(f"OPERATION {value=} {match_operation.group(1)=}")

            elif key.startswith("test"):
                match_test = re.search(r"\d+", value)
                monkeys[monkey_number]["test"] = int(match_test.group())
                # logging.debug(f"TEST {value=} {int(match_test.group())=}")

            elif key.startswith("if true"):
                match_if_true = re.search(r"\d+", value)
                monkeys[monkey_number]["test_true"] = int(match_if_true.group(0))
                # logging.debug(f"TRUE CONDITION {value=} {match=}")

            elif key.startswith("if false"):
                match_if_false = re.search(r"\d+", value)
                monkeys[monkey_number]["test_false"] = int(match_if_false.group(0))
                # logging.debug(f"FALSE CONDITION {value=} {match=}")

    return monkeys


def monkey_inspect(
    monkey_data: dict[int, dict[str, Any]], rounds: int = 20
) -> dict[int, dict[str, Any]]:
    monkey_data = monkey_data
    for _ in range(rounds):
        logging.debug(f"ROUND {_}\n\n")
        for monkey_index, monkey_values in monkey_data.items():
            for item in monkey_values["items"][:]:
                monkey_data[monkey_index]["inspect"] += 1
                current_item = monkey_values["items"][0]
                logging.debug(
                    f"CURRENT {monkey_index=} {monkey_values=} {current_item=}"
                )
                current_item = OPERATORS[monkey_values["operation"][0]](
                    current_item, monkey_values["operation"][1]
                )
                logging.debug(f"AFTER OPERATION {current_item=}")
                current_item = floor(current_item / WORRY_LEVEL_BORED)
                logging.debug(f"AFTER DIVISION BY 3 AND ROUNDING {current_item=}")
                if current_item % monkey_values["test"] == 0:
                    dest_monkey = monkey_data[monkey_values["test_true"]]
                    dest_monkey["items"].append(current_item)
                else:
                    dest_monkey = monkey_data[monkey_values["test_false"]]
                    dest_monkey["items"].append(current_item)
                monkey_values["items"].pop(0)
    logging.debug(f"{monkey_data}")
    return monkey_data


def main():
    monkeys = parse_input_data("day11_input")
    monkeys = monkey_inspect(monkeys)
    two_most_active = mul(*sorted(value["inspect"] for value in monkeys.values())[-2:])
    print(two_most_active)


if __name__ == "__main__":
    main()
