#!/usr/bin/python3

from collections import Counter


def insertion(pairs, chars):
    p = Counter()
    for (a, b), times in pairs.items():
        e = rules[a + b]  # single element to insert
        p[a + e] += times
        p[e + b] += times
        chars[e] += times
    return p


def solve(poly, steps):
    """--- Day 14: Extended Polymerization ---"""
    pairs = Counter(a + b for a, b in zip(poly, poly[1:]))  # defaults to 1
    chars = Counter(poly)
    for _ in range(steps):
        pairs = insertion(pairs, chars)
    return max(chars.values()) - min(chars.values())


if __name__ == "__main__":
    test, actual = "test-input/day14.txt", "input/day14.txt"
    with open(actual, "r") as f:
        data = f.read().splitlines()

    poly, _, *rules = data
    rules = dict(r.split(" -> ") for r in rules)

print(f"Part 1 -- {solve(poly, 10)}")
print(f"Part 2 -- {solve(poly, 40)}")
