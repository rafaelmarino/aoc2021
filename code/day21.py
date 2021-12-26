#!/usr/bin/python3


from utils import read_input
from itertools import cycle, product
from collections import Counter
from functools import lru_cache


def play_deterministic_die(p1, p2, sc1=0, sc2=0):
    """--- Day 21: Dirac Dice ---"""
    die = cycle(range(1, 101))
    p1s_turn = True
    roll_counter = 0
    while max(sc1, sc2) < 1000:
        three_rolls = sum([next(die) for _ in range(3)])
        roll_counter += 3
        if p1s_turn:
            p1 = (p1 + three_rolls) % 10 or 10  # fixes 10 % 10 = 0
            sc1 += p1
        else:
            p2 = (p2 + three_rolls) % 10 or 10
            sc2 += p2
        p1s_turn = not p1s_turn
    return min(sc1, sc2) * roll_counter


@lru_cache(maxsize=None)
def play_dirac_die(p1, p2, sc1=0, sc2=0):
    """--- Part Two ---"""
    if sc2 >= 21:  # check most recently computed roll/score
        return 0, 1
    w1, w2 = 0, 0
    for roll_sum, freq in dice_freq.items():
        new_p1 = (p1 + roll_sum) % 10 or 10
        new_sc1 = sc1 + new_p1
        p2w, p1w = play_dirac_die(p2, new_p1, sc2, new_sc1)
        w1 += freq * p1w
        w2 += freq * p2w
    return w1, w2


if __name__ == "__main__":
    T = False
    test, actual = "test/day21", "input/day21"
    data = read_input(test) if T else read_input(actual)
    p1, p2 = [int(position[-1]) for position in data]
    part1 = play_deterministic_die(p1, p2)
    dice_freq = Counter(sum(p) for p in product((1, 2, 3), repeat=3))
    part2 = max(play_dirac_die(p1, p2))


print(f"Part 1 -- (LosingPlayerScore)*(rollCount): {part1}")
print(f"Part 2 -- Find player with more universe wins has: {part2} wins")
