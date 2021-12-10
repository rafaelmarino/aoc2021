#!/usr/bin/python3


def parse_navigation_subsystem(data):
    """--- Day 10: Syntax Scoring ---"""
    matching_characters = {"(": ")", "[": "]", "{": "}", "<": ">"}
    first_illegal_characters = []
    # incomplete_lines = []
    completion_seqs = []  # seq of chars that would complete the lines
    for line in data:
        stack = []
        corrupt_line = False
        # line = data[2]
        for symbol in line:
            if symbol in matching_characters.keys():  # opening char
                stack.append(symbol)
            elif stack and matching_characters[stack[-1]] == symbol:
                _ = stack.pop()
            else:
                first_illegal_characters.append(symbol)
                corrupt_line = True
                break  # stop: a single char corrupts the entire line
        if not corrupt_line:  # ie incomplete
            # incomplete_lines.append(line)
            seq = [matching_characters[c] for c in stack[::-1]]
            completion_seqs.append(seq)
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    error_score = sum([points[c] for c in first_illegal_characters])
    return error_score, completion_seqs


def compute_autocomplete_score(completion_seqs):
    """--- Part Two ---"""
    points = {")": 1, "]": 2, "}": 3, ">": 4}
    total_scores = []
    for seq in completion_seqs:
        total_score = 0
        for symbol in seq:
            total_score *= 5
            total_score += points[symbol]
        total_scores.append(total_score)
    total_scores.sort()
    return total_scores[len(total_scores) // 2]  # middle score


if __name__ == "__main__":
    with open("input/day10.txt", "r") as f:
        data = f.read().splitlines()
        # data = f.readline()
    error_score, completion_seqs = parse_navigation_subsystem(data)
    ac_score = compute_autocomplete_score(completion_seqs)

    print(f"Part 1 -- Total syntax error score: {error_score}")
    print(f"Part 2 -- Autocompletion iddle score: {ac_score}")
