#!/usr/bin/python3

if __name__ == "__main__":
    test, actual = "test-input/day13.txt", "input/day13.txt"
    with open(actual, "r") as f:
        data = f.read().splitlines()
    paper = data[: data.index("")]
    paper = [list(map(int, coord.split(","))) for coord in paper]
    folds = data[data.index("") + 1 :]

    for fold in folds[0]:
        max_x = max([coord[0] for coord in paper])
        max_y = max([coord[1] for coord in paper])
        dir, line = folds[0].split(" ")[-1].split("=")
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
