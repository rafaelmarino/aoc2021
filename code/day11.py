#!/usr/bin/python3

import numpy as np
import itertools

from numpy.core.fromnumeric import repeat


def p1():
    """--- Day 11: Dumbo Octopus ---"""
    return


def p2():
    """--- Part Two ---"""
    return


if __name__ == "__main__":
    test1, test2 = "test-input/day11-mini.txt", "test-input/day11.txt"
    actual = "input/day11.txt"
    matrix = np.genfromtxt(actual, delimiter=1, dtype=float)
    pad_ = np.NAN
    m = np.pad(matrix, pad_width=1, mode="constant", constant_values=pad_)
    # create adjacency grid programmatically
    adj = [c for c in itertools.product([-1, 0, 1], repeat=2) if c != (0, 0)]
    assert len(adj) == 8 and sum([i + j for (i, j) in adj]) == 0
    steps = 100
    total_flashes = 0
    for step in range(steps):
        m += 1
        # total_flashes += len(np.transpose(np.where(m >= 10)))
        while np.any(np.where(m >= 10)):  # while any cell ready to flash
            fcs = np.transpose(np.where((m) >= 10))  # coords to flash
            total_flashes += len(fcs)  # flash
            m[np.where(m >= 10)] = np.NINF  # switch off
            for coords in fcs:
                for (x_, y_) in adj:  # propagate flash to 8-box adj cells
                    x, y = coords
                    x += x_
                    y += y_
                    m[x, y] += 1
        m[np.where(m == np.NINF)] = 0  # switch all flashed octopi to 0
    total_flashes

    #
    # m[6, 6] = 100
    # c = 0
    # while np.any(np.where(m >= 10)):
    #     m[6,6] -= 1
    #     c += 1
    # c
    # m

    print(f"Part 1 -- Flash count after {steps} steps: {total_flashes}")
    # print(f"{}")
