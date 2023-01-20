import re


class Matrix:
    def __init__(self, matrix: list[list[str]]) -> None:
        self.matrix = matrix[:-1]

    def transpose(self):
        transposed_matrix = []

        for x in range(len(self.matrix[0])):
            transposed_row = []
            for y in range(len(self.matrix)):
                transposed_row.append(self.matrix[y][x])
            transposed_matrix.append(transposed_row)

        self.matrix = transposed_matrix
        return self

    def remove_inner_whitespaces(self):
        self.matrix = [list("".join(row).strip()) for row in self.matrix]
        return self

    def reverse(self):
        self.matrix = [row[::-1] for row in self.matrix]
        return self

    def __str__(self) -> str:
        output = []
        for row in self.matrix:
            output += row + ["\n"]
        return "".join(output)


stacks = []
with open("day5_input", "r") as f:
    input_part_flag = "L"
    cargo = None
    for line in f:
        if input_part_flag == "L":
            if line == "\n":
                input_part_flag = "I"
                cargo = (
                    Matrix(stacks)
                    .transpose()
                    .remove_inner_whitespaces()
                    .reverse()
                    .matrix
                )
                continue
            stacks.append(
                [line[i + 1] for i in range(0, len(line), 3 + 1)]
            )  # +1 in range step for skipping white space between items
        elif input_part_flag == "I":
            amount, from_pile, to_pile = map(int, re.findall(r"\d+", line))
            from_pile -= 1
            to_pile -= 1
            for number in range(amount):
                cargo[to_pile].append(cargo[from_pile].pop())

for array in cargo:
    print(array[-1], end="")
