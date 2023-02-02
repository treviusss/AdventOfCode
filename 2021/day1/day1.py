import timeit
from collections import deque
from itertools import islice


def part_one_first_solution():
    previous_measurement = None
    increase_number = 0
    with open("day1_input") as f:
        for line in f:
            line = int(line)
            if previous_measurement is None:
                previous_measurement = line
            elif previous_measurement < line:
                previous_measurement = line
                increase_number += 1
            else:
                previous_measurement = line
    return increase_number


def part_one_second_solution():
    input_data = [int(number) for number in open("day1_input")]
    result = sum(y > x for x, y in zip(input_data, input_data[1:]))
    return result


def part_two():
    measurement = deque()
    increase_number = 0
    with open("day1_input") as f:
        for line in f:
            line = int(line)
            measurement.append(line)
            if len(measurement) == 4:
                if sum(islice(measurement, 0, 3)) < sum(islice(measurement, 1, 4)):
                    increase_number += 1
                measurement.popleft()

    return increase_number


print(part_two())

# first_solution_time = min(
#     timeit.repeat(
#         "part_one_first_solution()",
#         setup="from __main__ import part_one_first_solution",
#         number=1000,
#     )
# )

# second_solution_time = min(
#     timeit.repeat(
#         "part_one_second_solution()",
#         setup="from __main__ import part_one_second_solution",
#         number=1000,
#     )
# )
# print(first_solution_time, second_solution_time)
