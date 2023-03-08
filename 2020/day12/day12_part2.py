from dataclasses import dataclass


@dataclass
class ShipDirection:
    direction: str
    value: int = 0


@dataclass
class WaypointDirection:
    direction: str
    value: int = 0


ROTATIONS = ["north", "east", "south", "west"]
ROTATIONS_INITIAL_MAP = {direction[0].upper(): direction for direction in ROTATIONS}


def get_data(filename: str) -> list[tuple[str, int]]:
    with open(filename, "r") as f:
        return [(line.strip()[0], int(line.strip()[1:])) for line in f]


# def move_ship(data: list[tuple[str, int]]) -> dict:
#     ship_directions = {direction: ShipDirection(direction) for direction in ROTATIONS}
#     waypoint_directions = {
#         direction: WaypointDirection(direction) for direction in ROTATIONS
#     }
#     waypoint_directions["east"].value = 10 + ship_directions["east"].value
#     waypoint_directions["north"].value = 1 + ship_directions["north"].value

#     ship_x = ship_directions["east"]
#     ship_y = ship_directions["north"]

#     waypoint_x = waypoint_directions["east"]
#     waypoint_y = waypoint_directions["north"]

#     for instruction, value in data:
#         if instruction == "F":
#             ship_x.value += value * waypoint_x.value
#             ship_y.value += value * waypoint_y.value
#         elif instruction == "R" or instruction == "L":
#             curr_index_x = ROTATIONS.index(waypoint_x.direction)
#             curr_index_y = ROTATIONS.index(waypoint_y.direction)

#             # Calculate direction after rotation either towards right or left
#             if instruction == "R":
#                 curr_dir_x = ROTATIONS[(curr_index_x + (value // 90)) % len(ROTATIONS)]
#                 curr_dir_y = ROTATIONS[(curr_index_y + (value // 90)) % len(ROTATIONS)]
#                 # to_discard = ROTATIONS[curr_index_y]
#             else:
#                 curr_dir_x = ROTATIONS[(curr_index_x - (value // 90)) % len(ROTATIONS)]
#                 curr_dir_y = ROTATIONS[(curr_index_y - (value // 90)) % len(ROTATIONS)]
#                 # to_discard = ROTATIONS[curr_index_x]

#             # Saving previous waypoints in order to change values in Waypoint objects
#             prev_waypoint_x = waypoint_x.value
#             prev_waypoint_y = waypoint_y.value

#             # Reset value in direction that is left
#             waypoint_directions[ROTATIONS[curr_index_x]].value = 0
#             waypoint_directions[ROTATIONS[curr_index_y]].value = 0

#             # Change East or West values in Waypoint objects
#             waypoint_x = waypoint_directions[curr_dir_x]
#             waypoint_x.value = prev_waypoint_x

#             # Change North or South values in Waypoint objects
#             waypoint_y = waypoint_directions[curr_dir_y]
#             waypoint_y.value = prev_waypoint_y

#             ship_x = ship_directions[curr_dir_x]
#             ship_y = ship_directions[curr_dir_y]
#         else:
#             curr_dir = ROTATIONS_INITIAL_MAP[instruction]
#             waypoint_directions[curr_dir].value += value
#         print(ship_directions, waypoint_directions, sep="\n")
#         print()
#     return ship_directions


def move_ship(data: list[tuple[str, int]]) -> tuple:
    waypoint_x = 10
    waypoint_y = 1
    ship_x = 0
    ship_y = 0

    for instruction, value in data:
        if instruction == "N":
            waypoint_y += value
        elif instruction == "E":
            waypoint_x += value
        elif instruction == "S":
            waypoint_y -= value
        elif instruction == "W":
            waypoint_x -= value
        elif instruction == "L":
            for _ in range(value // 90):
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
        elif instruction == "R":
            for _ in range(value // 90):
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
        elif instruction == "F":
            ship_x += value * waypoint_x
            ship_y += value * waypoint_y

    return ship_x, ship_y


def calculate_manhattan_distance(ship_location: tuple) -> int:
    return abs(ship_location[0]) + abs(ship_location[1])


def main() -> None:
    data = get_data("day12_input")
    dest_directions = move_ship(data)
    print(calculate_manhattan_distance(dest_directions))


if __name__ == "__main__":
    main()
