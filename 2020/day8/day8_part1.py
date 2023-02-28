def get_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def process_data(data: list[str]) -> int:
    accumulator = 0
    i = 0
    visited = set()
    while True:
        if i in visited:
            break
        visited.add(i)

        curr_instruct, value = data[i].split()
        value = int(value)

        if curr_instruct == "acc":
            accumulator += value
            i += 1
        elif curr_instruct == "jmp":
            i += value
        elif curr_instruct == "nop":
            i += 1

    return accumulator


def main() -> None:
    data = get_data("day8_input")
    print(process_data(data))


if __name__ == "__main__":
    main()
