#!/usr/bin/python3

import re
from utils import read_input, integers
from collections import defaultdict
from itertools import combinations


def can_explode_check(temp):
    """Determine if a snailfish number can be exploded"""
    proper_pairs = re.findall(pair_p, temp)
    counter = defaultdict(int)  # tracks right split index for duplicate pairs
    for pair in proper_pairs:
        counter[pair] += 1
        n = counter[pair]
        groups = temp.split(pair)
        before, after = pair.join(groups[:n]), pair.join(groups[n:])
        lbc = len(re.findall(left_bracket, before))  # left bracket count
        rbc = len(re.findall(right_bracket, before))
        can_explode = True if lbc - rbc >= 4 else False
        if can_explode:
            return pair, before, after, True
    return pair, before, after, False


def can_split_check(temp):
    """Determine if a snailfish number can be split"""
    return True if any(ele >= 10 for ele in integers(temp)) else False


def add_and_reduce(running_sum, num):
    """--- Day 18: Snailfish ---"""
    temp = "[" + running_sum + "," + num + "]"
    # print(temp)
    pair, before, after, can_explode = can_explode_check(temp)
    can_split = can_split_check(temp)
    while can_explode or can_split:
        if can_explode:
            if integers(before):
                num = integers(before)[-1]
                new_num = str(num + integers(pair)[0])
                before = new_num.join(before.rsplit(str(num), 1))
            if integers(after):
                num = integers(after)[0]
                new_num = str(num + integers(pair)[1])
                after = after.replace(str(num), new_num, 1)
            temp = before + "0" + after
            # print(f"afterExplodeOn--{pair}--", temp)
            pair, before, after, can_explode = can_explode_check(temp)
            can_split = can_split_check(temp)
            continue
        if can_split:
            num = [n for n in integers(temp) if n >= 10][0]
            before, after = temp.split(str(num), 1)
            # (15 // 2, 15 // 2 + (15 % 2 > 0)) round down, round up
            to_insert = str([num // 2, num // 2 + (num % 2 > 0)]).replace(" ", "")
            temp = before + to_insert + after
            # print(f"afterSplitOn--{num}--", temp)
            pair, before, after, can_explode = can_explode_check(temp)
            can_split = can_split_check(temp)
    return temp


def compute_mag(running_sum):
    """Compute the magnitude of a reduced snailfish number"""
    # running_sum = "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
    mag = running_sum
    while re.findall(pair_p, mag):
        for pair in re.findall(pair_p, mag):
            left_num, right_num = integers(pair)
            new_num = left_num * 3 + right_num * 2
            mag = mag.replace(pair, str(new_num))
        # break
    return mag


if __name__ == "__main__":
    test = True
    data = read_input("test/day18") if test else read_input("input/day18")
    pair_p = r"\[\d+,\d+\]"
    left_bracket, right_bracket = r"\[", r"\]"
    running_sum = data[0]
    for num in data[1:]:  # data[1:2]
        # num = data[1:2][0]
        # print(num)
        running_sum = add_and_reduce(running_sum, num)
        # print(running_sum)
        # print(can_explode, can_split)
    total_mag = compute_mag(running_sum)

    max_ = 1
    for num1, num2 in combinations(data, 2):
        mag1 = compute_mag(add_and_reduce(num1, num2))
        mag2 = compute_mag(add_and_reduce(num2, num1))
        max_ = max(map(int, [max_, mag1, mag2]))

print(f"Part 1 -- Reduced number total magnitude: {total_mag}")
print(f"Part 2 -- Reduced number max magnitude: {max_}")
