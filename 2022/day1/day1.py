with open("day1_input", "r") as f:
    elf_calories_sum = 0
    elf_number = 1
    elves = []

    for line in f:
        if line == "\n":
            elves.append((elf_number, elf_calories_sum))
            elf_calories_sum = 0
            elf_number += 1
        else:
            elf_calories_sum += int(line)

    top_elf = max(elves)
    top_elves = sorted(elves, key=lambda x: x[1], reverse=True)
    top3_elves_total = sum(calories for index, calories in top_elves[:3])
    
    print(top3_elves_total)

