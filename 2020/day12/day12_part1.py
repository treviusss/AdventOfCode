from dataclasses import dataclass


@dataclass
class CardinalDirection:
    direction: str
    value: int = 0


ROTATIONS = ["north", "east", "south", "west"]
ROTATIONS_INITIAL_MAP = {direction[0].upper(): direction for direction in ROTATIONS}


def get_data(filename: str) -> list[tuple[str, int]]:
    with open(filename, "r") as f:
        return [(line.strip()[0], int(line.strip()[1:])) for line in f]


def move_ship(data: list[tuple[str, int]]) -> dict[str, CardinalDirection]:
    ship_directions = {
        direction: CardinalDirection(direction) for direction in ROTATIONS
    }
    current_facing_dir = ship_directions["east"]

    for instruction, value in data:
        if instruction == "F":
            current_facing_dir.value += value
        elif instruction == "R" or instruction == "L":
            curr_index = ROTATIONS.index(current_facing_dir.direction)

            if instruction == "R":
                curr_dir = ROTATIONS[(curr_index + (value // 90)) % len(ROTATIONS)]
            else:
                curr_dir = ROTATIONS[(curr_index - (value // 90)) % len(ROTATIONS)]

            current_facing_dir = ship_directions[curr_dir]
        else:
            curr_dir = ROTATIONS_INITIAL_MAP[instruction]
            ship_directions[curr_dir].value += value

    return ship_directions


def calculate_manhattan_distance(data: dict[str, CardinalDirection]) -> int:
    y_directions = abs(data["north"].value - data["south"].value)
    x_directions = abs(data["east"].value - data["west"].value)
    return x_directions + y_directions


def main() -> None:
    data = get_data("day12_input")
    dest_directions = move_ship(data)
    print(calculate_manhattan_distance(dest_directions))


if __name__ == "__main__":
    main()
