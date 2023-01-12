# class approach for training
PRIORITY: dict[str, int] = {chr(number + 96): number for number in range(1, 27)}
PRIORITY.update(
    {
        key.upper(): value + 26 for key, value in PRIORITY.items()
    }
)
class Solution:
    
    def __init__(self, file: str):
        self.priority_sum = 0 
        self.process_input(file)

    def process_input(self, input_file: str):
        with open(input_file, "r") as f:
            for line in f:
                line = line.strip('\n')
                first_compartment = set(line[:len(line) // 2])
                second_compartment = set(line[len(line) // 2:])
                intersection = first_compartment.intersection(second_compartment)
                
                for item in intersection:
                    self.priority_sum += PRIORITY.get(item, 0)
                    

    def __str__(self):
        return f"The sum of the priorities of items is {self.priority_sum}"

    
solution = Solution("day3_input")
print(solution)

