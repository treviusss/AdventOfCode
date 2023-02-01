# Based on solution by https://www.youtube.com/@jonathanpaulson5053

from functools import cmp_to_key


def compare(value1, value2):
    if isinstance(value1, int) and isinstance(value2, int):
        if value1 < value2:
            return -1
        elif value1 == value2:
            return 0
        else:
            return 1
    elif isinstance(value1, list) and isinstance(value2, list):
        i = 0
        while i < len(value1) and i < len(value2):
            current_item = compare(value1[i], value2[i])
            if current_item == 1:
                return 1
            if current_item == -1:
                return -1
            i += 1
        if i == len(value1) and i < len(value2):
            return -1
        elif i < len(value1) and i == len(value2):
            return 1
        else:
            return 0
    elif isinstance(value1, int) and isinstance(value2, list):
        return compare([value1], value2)
    else:
        return compare(value1, [value2])


with open("day13_input") as f:
    data = f.read().strip()
answer1 = 0
data = [line for line in data.split("\n\n")]
pairs = []
for i, group in enumerate(data):
    p1, p2 = group.split("\n")
    p1 = eval(p1)
    p2 = eval(p2)
    pairs.append(p1)
    pairs.append(p2)
    if compare(p1, p2) == -1:
        answer1 += i + 1

# https://docs.python.org/3/howto/sorting.html#comparison-functions
pairs += [[[2]], [[6]]]
sorted_pairs = sorted(pairs, key=cmp_to_key(compare))
answer2 = (sorted_pairs.index([[2]]) + 1) * (sorted_pairs.index([[6]]) + 1)
print(answer1)
print(answer2)
