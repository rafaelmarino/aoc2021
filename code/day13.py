#!/usr/bin/python3

import numpy as np

if __name__ == "__main__":
    test, actual = "test-input/day13.txt", "input/day13.txt"
    with open(actual, "r") as f:
        data = f.read().splitlines()
    paper = data[: data.index("")]
    paper = [list(map(int, coord.split(","))) for coord in paper]
    folds = data[data.index("") + 1 :]

    for fold in folds:
        max_x = max([coord[0] for coord in paper])
        max_y = max([coord[1] for coord in paper])
        dir, line = fold.split(" ")[-1].split("=")
        if dir == "y":
            top = [(x, y) for x, y in paper if y < int(line)]
            bottom = [(x, y) for x, y in paper if y > int(line)]
            to_add = [(x, max_y - y) for x, y in bottom]
            paper = set(top) | set(to_add)
        if dir == "x":
            left = [(x, y) for x, y in paper if x < int(line)]
            right = [(x, y) for x, y in paper if x > int(line)]
            to_add = [(max_x - x, y) for x, y in right]
            paper = set(left) | set(to_add)

    len(paper)

    max_x = max([coord[0] for coord in paper])
    max_y = max([coord[1] for coord in paper])
    grid = np.zeros((max_y + 1, max_x + 1)).astype(int)
    for coord in paper:
        y, x = coord
        grid[x, y] = 1

    def write_txt(file, path):
        """Write eight capital letters to text"""
        with open(path, "w") as f:
            for row in file:
                row = "".join(map(str, row))
                row = row.replace("0", " ")
                row = row.replace("1", "#")
                _ = f.write(row + "\n")

    write_txt(grid, "extras/day13.txt")
