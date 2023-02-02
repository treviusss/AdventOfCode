horizontal_pos = 0
depth = 0

with open("day2_input") as f:
    for line in f:
        command, value = line.split()
        value = int(value)
        if command == "forward":
            horizontal_pos += value
        elif command == "down":
            depth += value
        elif command == "up":
            depth -= value

print(horizontal_pos * depth)
