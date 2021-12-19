#!/usr/bin/python3

import re
from utils import read_input

"""
To reduce a snailfish number, you must repeatedly do the first action in this list that applies to the snailfish number:
- If any pair is nested inside four pairs, the leftmost such pair explodes.
- If any regular number is 10 or greater, the leftmost such regular number splits.
"""


def f():
    """--- Day 18: Snailfish ---"""
    pass


if __name__ == "__main__":
    test = True
    data = read_input("test/day18") if test else read_input("input/day18")
    # len(data)

    running_sum = data[0]
    for num in data[1:2]:
        # num = data[1:2][0]
        print(num)
        temp = "[" + running_sum + "," + num + "]"
        temp

    integers(temp)
    pair = r"\[[0-9],[0-9]\]"
    opening_bracket = r"\["
    re.findall(opening_bracket, temp)
    proper_pairs = re.findall(pair, temp)
    [(m.start(0), m.end(0)) for m in re.finditer(pair, temp)]

# 11//2 + (11 % 2 > 0)  # round up
