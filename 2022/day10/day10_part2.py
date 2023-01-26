import logging

level = logging.INFO
logging.basicConfig(level=level, format="%(message)s")

CRT_WIDTH = 40
LIT_PIXEL = "#"
DARK_PIXEL = "."

crt_row = []
sprite_pos = [0, 1, 2]
cycle = 0


def update_crt_row() -> None:
    crt_row.append(LIT_PIXEL if cycle % CRT_WIDTH in sprite_pos else DARK_PIXEL)


with open("day10_input", "r") as f:
    for line in f:
        line = line.strip("\n")
        if line == "noop":
            update_crt_row()
            cycle += 1
            logging.debug(f"{line=} {cycle=} {sprite_pos=} {crt_row=}")
        else:
            command, value = line.split()
            value = int(value)
            for _ in range(2):
                update_crt_row()
                cycle += 1
            sprite_pos = [(pos + value) for pos in sprite_pos]
            logging.debug(f"{line=} {cycle=} {sprite_pos=} {crt_row=}")

for i in range(len(crt_row) // CRT_WIDTH):
    print("".join(crt_row[i * CRT_WIDTH : (i + 1) * CRT_WIDTH]))
