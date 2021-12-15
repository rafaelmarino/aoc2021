#!/usr/bin/python3


from collections import defaultdict


def f1():
    """--- Day 14: Extended Polymerization ---"""
    pass


if __name__ == "__main__":
    test, actual = "test-input/day14.txt", "input/day14.txt"
    with open(actual, "r") as f:
        data = f.read().splitlines()

    temp, rules = data[0], data[2:]
    rules_d = {}
    for rule in rules:
        left, right = rule.split(" -> ")
        rules_d[left] = left[0] + right + left[1]

    steps = 10
    for step in range(steps):
        overlaps = [(E + temp[i + 1]) for i, E in enumerate(temp[:-1])]
        for i, overlap in enumerate(overlaps):
            overlaps[i] = rules_d[overlap]
        temp = "".join([o[:-1] for o in overlaps]) + overlaps[-1][-1]
    # len(temp)

    counts = defaultdict(int)
    for E in temp:
        counts[E] += 1

    max_E = max(counts.keys(), key=counts.get)
    min_E = min(counts.keys(), key=counts.get)

    diff = counts[max_E] - counts[min_E]
    diff

    # print(f"Part 1 -- Dots after the first fold in the paper: {p1}")
    # print(f"Part 2 -- Dots after all the folds: {len(folded_paper)}")
