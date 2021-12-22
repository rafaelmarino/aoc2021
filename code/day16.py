#!/usr/bin/python3
from utils import read_input_line, cat


def compute_spv(tid, bits, spv):
    """--- Part Two ---"""
    if tid == 0:
        return (bits, sum(spv))
    if tid == 1:
        prod = 1
        for v in spv:
            prod *= v
        return (bits, prod)
    if tid == 2:
        return (bits, min(spv))
    if tid == 3:
        return (bits, max(spv))
    if tid == 5:
        return (bits, 1 if spv[0] > spv[1] else 0)
    if tid == 6:
        return (bits, 1 if spv[0] < spv[1] else 0)
    if tid == 7:
        return (bits, 1 if spv[0] == spv[1] else 0)


def parse(bits):
    """--- Day 16: Packet Decoder ---"""
    global sumofversions
    version, bits = int(bits[:3], 2), bits[3:]  # read & cut off bits
    sumofversions += version
    tid, bits = int(bits[:3], 2), bits[3:]
    if tid == 4:  # literal value packet
        value = ""
        while True:
            cont_ = bits[0]
            value += bits[1:5]
            bits = bits[5:]
            if cont_ == "0":
                break
        return (bits, int(value, 2))
    else:  # operator packet, contains 1 or more subpackets
        ltid, bits = bits[0], bits[1:]  # length type id
        spvs = []  # subpacket_values
        if ltid == "0":
            subpackets_len, bits = int(bits[:15], 2), bits[15:]
            subpackets = bits[:subpackets_len]
            bits = bits[subpackets_len:]
            while subpackets:
                subpackets, sub_value = parse(subpackets)
                spvs.append(sub_value)
        elif ltid == "1":
            subpackets_count, bits = int(bits[:11], 2), bits[11:]
            for _ in range(subpackets_count):
                bits, sub_value = parse(bits)
                spvs.append(sub_value)
        return compute_spv(tid, bits, spvs)


if __name__ == "__main__":
    T = 0
    test, actual = "test/day16", "input/day16"
    hex_ = read_input_line(test) if T else read_input_line(actual)
    bits = cat(f"{int(x, 16):04b}" for x in hex_)
    sumofversions = 0

outer_packet_value = parse(bits)[1]
print(f"{sumofversions}")
print(f"{outer_packet_value}")
