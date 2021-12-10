#!/usr/bin/python3


def p1():
    """--- Day 10: Syntax Scoring ---"""
    return


def p2():
    """--- Part Two ---"""
    return


if __name__ == "__main__":
    with open("input/day10.txt", "r") as f:
        data = f.read().splitlines()
        # data = f.readline()
    matching_characters = {"(": ")", "[": "]", "{": "}", "<": ">"}
    stack = []
    first_illegal_characters = []
    for line in data:
        # line = data[2]
        for symbol in line:
            if symbol in matching_characters.keys():  # opening char
                stack.append(symbol)
            elif stack and matching_characters[stack[-1]] == symbol:
                _ = stack.pop()
            else:
                first_illegal_characters.append(symbol)
                break  # stop: a single character corrupts entire line

    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    error_score = sum([points[c] for c in first_illegal_characters])

    print(f"{error_score}")
    # print(f"{}")
