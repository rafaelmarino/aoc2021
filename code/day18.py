#!/usr/bin/python3

import re
from utils import read_input, integers
from collections import defaultdict


def can_explodef(temp):
    """Determine if a snailfish number can be exploded"""
    proper_pairs = re.findall(pair_p, temp)
    counter = defaultdict(int)
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


def can_splitf(temp):
    """Determine if a snailfish number can be split"""
    return True if any(ele >= 10 for ele in integers(temp)) else False


if __name__ == "__main__":
    test = False
    data = read_input("test/day18") if test else read_input("input/day18")
    pair_p = r"\[\d+,\d+\]"
    left_bracket, right_bracket = r"\[", r"\]"
    running_sum = data[0]
    for num in data[1:]:  # data[1:2]
        # num = data[1:2][0]
        # print(num)
        temp = "[" + running_sum + "," + num + "]"
        # print(temp)
        pair, before, after, can_explode = can_explodef(temp)
        can_split = can_splitf(temp)
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
                pair, before, after, can_explode = can_explodef(temp)
                can_split = can_splitf(temp)
                continue
            if can_split:
                num = [n for n in integers(temp) if n >= 10][0]
                before, after = temp.split(str(num), 1)
                # (15 // 2, 15 // 2 + (15 % 2 > 0)) round down, round up
                to_insert = str([num // 2, num // 2 + (num % 2 > 0)]).replace(" ", "")
                temp = before + to_insert + after
                # print(f"afterSplitOn--{num}--", temp)
                pair, before, after, can_explode = can_explodef(temp)
                can_split = can_splitf(temp)
        running_sum = temp
        # print(running_sum)
        # print(can_explode, can_split)


# temp = [[9, 1], [1, 9]]

# re.findall(pair_p, temp)
pair_p

# temp = "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]"
mag = temp
while re.findall(pair_p, mag):
    for pair in re.findall(pair_p, mag):
        left_num, right_num = integers(pair)
        mag = mag.replace(pair, str(left_num * 3 + right_num * 2))
    # break

print(mag)
