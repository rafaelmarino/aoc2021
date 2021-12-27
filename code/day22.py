#!/usr/bin/python3

from utils import read_input, integers


def reboot_reactor(data):
    """--- Day 22: Reactor Reboot ---"""
    steps = [(row.split(" ")[0], integers(row)) for row in data]
    coords = set()
    for step in steps:
        # step = steps[0]
        on = True if step[0] == "on" else False
        x1, x2, y1, y2, z1, z2 = step[1]
        new_coords = {  # inclusive range. truncate from -50 to 50
            (x, y, z)
            for x in range(max(x1, -50), min(x2, 50) + 1)
            for y in range(max(y1, -50), min(y2, 50) + 1)
            for z in range(max(z1, -50), min(z2, 50) + 1)
        }
        if on:
            coords |= new_coords
        else:
            coords -= new_coords
    return len(coords)


if __name__ == "__main__":
    T = 0
    test, actual = "test/day22", "input/day22"
    data = read_input(test) if T else read_input(actual)


print(f"Part 1 -- On cubes after reboot: {reboot_reactor(data)}")
# print(f"{}")
