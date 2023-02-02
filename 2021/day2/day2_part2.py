horizontal_pos = 0
depth = 0
aim = 0

with open("day2_input") as f:
    for line in f:
        command, value = line.split()
        value = int(value)
        if command == "forward":
            horizontal_pos += value
            depth += aim * value
        elif command == "down":
            aim += value
        elif command == "up":
            aim -= value

print(horizontal_pos * depth)
