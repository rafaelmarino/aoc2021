#!/usr/bin/python3


from utils import read_input
from itertools import cycle

"""--- Day 21: Dirac Dice ---"""
"""--- Part Two ---"""

if __name__ == "__main__":
    T = True
    test, actual = "test/day21", "input/day21"
    data = read_input(test) if T else read_input(actual)


def play_die(sc1 = 0, sc2 = 0):
    pass

sc1, sc2 = 0, 0
p1, p2 = 9, 6
die = cycle(range(1, 101))

p1s_turn = True
roll_counter = 0
while sc1 < 1000 and sc2 < 1000:
    three_rolls = sum([next(die) for _ in range(3)])
    roll_counter += 3
    if p1s_turn:
        p1 = (p1 + three_rolls) % 10 or 10
        sc1 += p1
    else:
        p2 = (p2 + three_rolls) % 10 or 10
        sc2 += p2
    p1s_turn = not p1s_turn

min(sc1, sc2) * roll_counter




print(f"{}")
print(f"{}")
