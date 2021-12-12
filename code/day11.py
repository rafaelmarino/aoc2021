#!/usr/bin/python3

import numpy as np
import itertools


def take_steps(matrix, steps=210):
    """--- Day 11: Dumbo Octopus ---"""
    pad_ = np.NAN
    m = np.pad(matrix, pad_width=1, mode="constant", constant_values=pad_)
    # create adjacency grid programmatically
    adj = [c for c in itertools.product([-1, 0, 1], repeat=2) if c != (0, 0)]
    # assert len(adj) == 8 and sum([i + j for (i, j) in adj]) == 0
    total_flashes = 0
    for step in range(steps):
        m += 1
        while np.any(np.where(m >= 10)):  # while any cell ready to flash
            fcs = np.transpose(np.where((m) >= 10))
            total_flashes += len(fcs)  # flash
            m[np.where(m >= 10)] = np.NINF  # switch off
            for coords in fcs:
                for (x_, y_) in adj:  # propagate flash to adj box
                    x, y = coords
                    x += x_
                    y += y_
                    m[x, y] += 1
        m[np.where(m == np.NINF)] = 0  # switch all flashed octopi to 0
        if step == 99:  # part1
            flashes_at_step100 = total_flashes
        if m[1:-1, 1:-1].sum() == 0:  # part2
            step_all_flash = step + 1
            break
    return flashes_at_step100, step_all_flash


if __name__ == "__main__":
    # test1, test2 = "test-input/day11-mini.txt", "test-input/day11.txt"
    actual = "input/day11.txt"
    matrix = np.genfromtxt(actual, delimiter=1, dtype=float)
    flashes100, step_all_flash = take_steps(matrix, 300)
    print(f"Part 1 -- Flash count after 100 steps: {flashes100}")
    print(f"Part 2 -- First step all octopi flash together: {step_all_flash}")
