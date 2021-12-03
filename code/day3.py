#!/usr/bin/python3

import numpy as np

# binary-string to decimal
# int("10110", 2)


def compute_power_consumption(data):
    """--- Day 3: Binary Diagnostic ---"""
    # base python3
    row_count = len(data)
    bit_size = len(data[0])  # 12 bits
    data2d = [list(row) for row in data]
    data2d_ = [list(map(int, row)) for row in data2d]
    totals = [sum(list(zip(*data2d_))[i]) for i in range(bit_size)]
    assert len(totals) == bit_size
    # print(totals)
    # [488, 499, 497, 506, 484, 485, 490, 501, 503, 483, 493, 515]
    gamma_rate = [1 if bit > row_count / 2 else 0 for bit in totals]
    epsilon_rate = [int(not _) for _ in gamma_rate]
    gamma_rate_ = "".join([str(x) for x in gamma_rate])
    epsilon_rate_ = "".join([str(x) for x in epsilon_rate])
    power_consumption = int(gamma_rate_, 2) * int(epsilon_rate_, 2)
    return power_consumption


def numpy_power_consumption(data):
    """--- Day 3: Binary Diagnostic --- numpy"""
    data2d = [list(row) for row in data]
    array2d = np.asarray(data2d, dtype=int)
    # array2d.shape
    gamma_rate = np.sum(array2d, axis=0) > array2d.shape[0] / 2
    epsilon_rate = ~gamma_rate
    gamma_rate_ = "".join(gamma_rate.astype(int).astype("str"))
    epsilon_rate_ = "".join(epsilon_rate.astype(int).astype("str"))
    power_consumption = int(gamma_rate_, 2) * int(epsilon_rate_, 2)
    return power_consumption


def life_support(data):
    """--- Part Two ---"""
    # data = [
    #     "00100",
    #     "11110",
    #     "10110",
    #     "10111",
    #     "10101",
    #     "01111",
    #     "00111",
    #     "11100",
    #     "10000",
    #     "11001",
    #     "00010",
    #     "01010",
    # ]
    o2gr = data  # oxygen generator rating
    co2sr = data  # carbon dioxide scrubber rating
    bit_tracker = 0
    while len(o2gr) > 1:
        o2gr2d_ = [list(map(int, row)) for row in o2gr]
        true_bit_count = sum(list(zip(*o2gr2d_))[bit_tracker])
        # most common bit
        mcb = "1" if true_bit_count >= len(o2gr) / 2 else "0"
        o2gr = [num for num in o2gr if num[bit_tracker] == mcb]
        bit_tracker += 1
        bit_tracker %= 12
    bit_tracker = 0
    while len(co2sr) > 1:
        co2sr2d_ = [list(map(int, row)) for row in co2sr]
        true_bit_count = sum(list(zip(*co2sr2d_))[bit_tracker])
        # least common bit
        lcb = "0" if true_bit_count >= len(co2sr) / 2 else "1"
        co2sr = [num for num in co2sr if num[bit_tracker] == lcb]
        bit_tracker += 1
        bit_tracker %= 12
    life_support_rating = int(o2gr[0], 2) * int(co2sr[0], 2)
    return life_support_rating


if __name__ == "__main__":
    file_path = "input/day3.txt"
    with open(file_path, "r") as f:
        data = f.read().splitlines()
    pc = compute_power_consumption(data)
    pc_n = numpy_power_consumption(data)
    ls = life_support(data)
    print(f"Power consumption = (gamma_r x epsilon_r)--python3: {pc}")
    print(f"Power consumption = (gamma_r x epsilon_r)--numpy: {pc_n}")
    print(f"Life-support rating = (o2gen x co2scrubb): {ls}")
