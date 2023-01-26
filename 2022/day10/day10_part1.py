import logging

level = logging.DEBUG
logging.basicConfig(level=level, format="%(message)s")


cpu_register_val = 1
cycle = 0
signal_strength_values = []
signal_strength_cycle_idx = [20, 60, 100, 140, 180, 220]
with open("day10_input", "r") as f:
    for index, line in enumerate(f):
        line = line.strip("\n")
        if line == "noop":
            cycle += 1
            if cycle in signal_strength_cycle_idx:
                signal_strength_values.append(cycle * cpu_register_val)
                logging.debug(f"inside adding signal strength {cycle}")
        else:
            command, value = line.split()
            value = int(value)
            for _ in range(2):
                cycle += 1
                if cycle in signal_strength_cycle_idx:
                    signal_strength_values.append(cycle * cpu_register_val)
                    logging.debug(f"inside adding signal strength {cycle}")
            cpu_register_val += value
        logging.debug(f"{line=} {cycle}")

print(sum(signal_strength_values))
