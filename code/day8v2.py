#!/usr/bin/python3


def rewire_display(signals, display):
    """--- Day 8: Seven Segment Search ---"""
    for signal in signals:
        if len(signal) == 2:
            one = signal
        if len(signal) == 4:
            four = signal
    rewired_display = []
    for d in display:
        if len(d) == 2:
            rewired_display.append(1)
        if len(d) == 3:
            rewired_display.append(7)
        if len(d) == 4:
            rewired_display.append(4)
        if len(d) == 7:
            rewired_display.append(8)
        if len(d) == 5:  # [2, 3, 5]
            if not list(set(one) - set(d)):
                rewired_display.append(3)
            elif len(list(set(four) - set(d))) == 1:
                rewired_display.append(5)
            else:
                rewired_display.append(2)
        if len(d) == 6:  # [0, 6, 9]
            if len(list(set(one) - set(d))) == 1:
                rewired_display.append(6)
            elif len(list(set(d) - set(one))) == 4:
                rewired_display.append(9)
            else:
                rewired_display.append(0)
    return rewired_display


if __name__ == "__main__":
    with open("test-input/day8.txt", "r") as f:
        data = f.read().splitlines()
        # data = f.readline()
    ted, sum_ = 0, 0
    for entry in data:
        signals = entry.split(" | ")[0].split(" ")
        display = entry.split(" | ")[1].split(" ")
        display = rewire_display(signals, display)
        ted += sum([1 for d in display if d in [1, 4, 7, 8]])
        sum_ += int("".join(list(map(str, display))))
    print(f"Part1 -- Count of decoded easy digits in the display: {ted}")
    print(f"Part2 -- Sum of all decoded digits in the display: {sum_}")
