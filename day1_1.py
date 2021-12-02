def count_depth_increase():
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


if __name__ == "__main__":
    increased_measurements, line_counter = count_depth_increase()
    print(f"Measurements processed: {line_counter}")
    print(f"Measurements w/ increments: {increased_measurements}")
