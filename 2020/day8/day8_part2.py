from typing import Container

INSTRUCTIONS = {"jmp": "nop", "nop": "jmp"}


def get_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def process_data(data: list[str]) -> int:
    orig_data = data
    swap_indexes = get_instructions_indexes(data, INSTRUCTIONS.keys())
    accumulator = 0

    for index in swap_indexes:
        i = 0
        accumulator = 0
        data = orig_data.copy()

        # Change operation to opposite
        instr, _ = data[index].split()
        new_instr = INSTRUCTIONS[instr]
        data[index] = data[index].replace(instr, new_instr)

        visited = set()
        while True:
            if i in visited:
                break
            visited.add(i)

            try:
                curr_instruct, value = data[i].split()
            except IndexError:
                return accumulator

            value = int(value)

            if curr_instruct == "acc":
                accumulator += value
                i += 1
            elif curr_instruct == "jmp":
                i += value
            elif curr_instruct == "nop":
                i += 1

    return accumulator


def get_instructions_indexes(data: list[str], instructions: Container) -> list[int]:
    return [index for index, line in enumerate(data) if line.split()[0] in instructions]


def main() -> None:
    data = get_data("day8_input")
    print(process_data(data))


if __name__ == "__main__":
    main()
