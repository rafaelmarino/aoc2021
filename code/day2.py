#!/usr/bin/python3


def execute_route():
    """--- Day 2: Dive! ---"""
    file_path = "input/day2.txt"
    horizontal_pos, depth = 0, 0
    with open(file_path, "r") as f:
        for line in f:
            direction, unit = line.split(" ")
            unit = int(unit)
            if direction == "forward":
                horizontal_pos += unit
            if direction == "down":
                depth += unit
            if direction == "up":
                depth -= unit
    return horizontal_pos, depth


def execute_route2():
    """--- Day 2: Dive! ---"""
    file_path = "input/day2.txt"
    horizontal_pos, depth, aim = 0, 0, 0
    with open(file_path, "r") as f:
        for line in f:
            direction, unit = line.split(" ")
            unit = int(unit)
            if direction == "forward":
                horizontal_pos += unit
                depth += aim * unit
            if direction == "down":
                aim += unit
            if direction == "up":
                aim -= unit
    return horizontal_pos, depth


if __name__ == "__main__":
    hp, d = execute_route()
    hp2, d2 = execute_route2()
    print(f"Horizontal position x depth: {hp*d}")
    print(f"Horizontal position x depth: {hp2*d2}")
