from collections import defaultdict
from typing import Any

MAX_DIR_SIZE = 100_000
MIN_DISC_SPACE = 30_000_000
AVAILABLE_DISC_SPACE = 70_000_000


def get_data(file_name: str) -> list[str]:
    with open(file_name, "r", encoding="utf-8") as f:
        return [line.strip("\n") for line in f]


def traverse_file_tree(input_to_parse: list[str]) -> defaultdict[Any, int]:
    """
    Updates file hierarchy dictionary where key is parent dictionary
    and value is dictionary
    """

    hierarchy = defaultdict(int)
    path = []

    for line in input_to_parse:
        line = line.split(" ")
        if line[1] == "cd":
            if line[2] == "..":
                path.pop()
            else:
                path.append(line[2])
        elif line[1] == "ls":
            continue
        elif line[0] == "dir":
            continue
        else:
            size = int(line[0])
            for idx in range(len(path) + 1):
                hierarchy["/".join(path[:idx])] += size

    return hierarchy


def solution(dirs: dict) -> list:
    answer = []
    root_size = dirs["/"]
    free_space = AVAILABLE_DISC_SPACE - root_size
    for key, value in dirs.items():
        if value >= (MIN_DISC_SPACE - free_space):
            answer.append(value)
    answer.sort()
    return answer[0]


if __name__ == "__main__":
    data = get_data("day7_input")
    hierarchy = traverse_file_tree(data)
    answer = solution(hierarchy)
    print(answer)
