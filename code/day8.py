#!/usr/bin/python3


def signal2display_hash(signals):
    """Create a map from mixed signals to the proper display (fea entry)"""
    signal2display = {segment: None for segment in "abcdefg"}
    two_three_five, zero_six_nine = [], []
    for signal in signals:
        if len(signal) == 2:
            one = signal
        if len(signal) == 3:
            seven = signal
        if len(signal) == 4:
            four = signal
        if len(signal) == 7:
            eight = signal
        if len(signal) == 5:
            two_three_five.append(signal)
        if len(signal) == 6:
            zero_six_nine.append(signal)
    seven_minus_one = list(set(seven) - set(one))[0]
    signal2display[seven_minus_one] = "a"  # 'b': 'aaaa'
    b_and_d = list(set(four) - set(seven))
    for b_or_d in b_and_d:
        # b_or_d = b_and_d[0]
        temp = sum([1 for signal in two_three_five if b_or_d in signal])
        if temp == 3:
            signal2display[b_or_d] = "d"  # 'e': 'dddd'
            dddd = b_or_d  # central segment
        if temp == 1:
            signal2display[b_or_d] = "b"  # 'f': 'bb'
            for signal in two_three_five:
                if b_or_d in signal:
                    five = signal
    two_or_three = two_three_five[:]
    two_or_three.remove(five)
    for signal in two_or_three:
        tmp_list = list(set(seven) - set(signal))
        if tmp_list:
            two = signal
            signal2display[tmp_list[0]] = "f"  # 'g': 'ff'
        else:
            three = signal
    for signal in zero_six_nine:
        tmp = list(set(eight) - set(signal))[0]
        if tmp == dddd:
            zero = signal
    six_or_nine = zero_six_nine[:]
    six_or_nine.remove(zero)
    for signal in six_or_nine:
        tmp_list = list(set(one) - set(signal))
        if tmp_list:
            # six = signal
            signal2display[tmp_list[0]] = "c"  # 'c': 'cc'
        # else:
        #     nine = signal
    # solved: one, two, three, four, five, seven, eight, zero, nine
    tmp = list(set(two) - set(five) - set(seven))[0]
    signal2display[tmp] = "e"  # 'a': 'ee'
    tmp = list(set(three) - set(seven) - set(four))[0]
    signal2display[tmp] = "g"  # 'd': 'gggg'
    return signal2display


def count_easy_digits(signal2display, display, proper_display):
    """--- Day 8: Seven Segment Search --- Part 1"""
    easy_digit_codes = [proper_display[n] for n in [1, 4, 7, 8]]
    easy_digits_count = 0
    for digit in display:
        decoded_digit = set([signal2display[i] for i in digit])
        if decoded_digit in easy_digit_codes:
            easy_digits_count += 1
    return easy_digits_count


def get_proper_display(signal2display, display, proper_display):
    """--- Part Two ---"""
    four_digits = []
    for digit in display:
        decoded_digit = set([signal2display[i] for i in digit])
        for k, value in proper_display.items():
            if decoded_digit == value:
                four_digits.append(k)
    # ['4', '3', '1', '5'] -> 4315
    return int("".join(list(map(str, four_digits))))


if __name__ == "__main__":
    with open("input/day8.txt", "r") as f:
        data = f.read().splitlines()
        # data = f.readline()
    proper_display = {
        0: set("abcefg"),
        1: set("cf"),
        2: set("acdeg"),
        3: set("acdfg"),
        4: set("bcdf"),
        5: set("abdfg"),
        6: set("abdefg"),
        7: set("acf"),
        8: set("abcdefg"),
        9: set("abcdfg"),
    }
    ted = 0  # total easy digits counter (part1)
    sum_ = 0  # sum of all proper displays (part2)
    for entry in data:
        signals = entry.split(" | ")[0].split(" ")
        display = entry.split(" | ")[1].split(" ")
        signal2display = signal2display_hash(signals)
        ted += count_easy_digits(signal2display, display, proper_display)
        # break
        sum_ += get_proper_display(signal2display, display, proper_display)
    print(f"Part1 -- Count of decoded easy digits in the display: {ted}")
    print(f"Part2 -- Sum of all decoded digits in the display: {sum_}")

# easy_digits = {2: 'one', 3: 'seven', 4: 'four',  7: 'eight'}
# hard_digits = {5: ['two', 'three', 'five'] , 6: ['zero', 'six', 'nine']}
