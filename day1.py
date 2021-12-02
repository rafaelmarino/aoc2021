def count_single_increases():
    """AoC2021 -- Day1: Part1"""
    file_path = "input/day1.txt"
    line_counter, increase_counter = 0, 0
    with open(file_path, "r") as f:
        for line in f:
            line = int(line)
            line_counter += 1
            if line_counter == 1:
                prev_line = line
                continue
            if line > prev_line:
                increase_counter += 1
            prev_line = line
    return increase_counter, line_counter


def three_sliding_window():
    file_path = "input/day1.txt"
    line_counter, increase_counter = 0, 0
    window_sum_a, window_sum_b = 0, 0
    with open(file_path, "r") as f:
        for line in f:
            line = int(line)
            line_counter += 1
            if line_counter == 1:
                a = line
                continue
            if line_counter == 2:
                b = line
                continue
            if line_counter == 3:
                c = line
                continue
            window_sum_a = a + b + c
            window_sum_b = b + c + line
            if window_sum_b > window_sum_a:
                increase_counter += 1
            a, b, c = b, c, line
    return increase_counter


if __name__ == "__main__":
    increased_measurements, line_counter = count_single_increases()
    increased_three_sw = three_sliding_window()
    print(f"Measurements processed: {line_counter}")
    print(f"Measurements w/ increments: {increased_measurements}")
    print(f"Measurements w/3sw increments: {increased_three_sw}")
