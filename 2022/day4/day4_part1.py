class Solution:
    def __init__(self, file_name) -> None:
        self.overlapping_pairs_sum = 0
        self.process_input(file_name)

    def is_overlapping(self, start1: int, end1: int, start2: int, end2: int) -> bool:
        return start1 <= start2 and end1 >= end2 or start2 <= start1 and end2 >= end1

    def process_input(self, file_name: str) -> None:
        with open(file_name, "r") as f:
            for line in f:
                a, b, x, y = map(int, line.replace(",", "-").split("-"))
                if self.is_overlapping(a, b, x, y):
                    self.overlapping_pairs_sum += 1

    def __str__(self) -> str:
        return (
            f"There are {self.overlapping_pairs_sum} pairs that one range fully contain"
            " the other"
        )


solution = Solution("day4_input")
print(solution)
