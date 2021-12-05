#!/usr/bin/python3


if __name__ == "__main__":
    with open("input/day5-test.txt", "r") as f:
        data = f.read().splitlines()
    coordinates = []
    for line in data:
        from_, to_ = line.split(" -> ")[0], line.split(" -> ")[1]
        from_x, from_y = from_.split(",")
        to_x, to_y = to_.split(",")
        coordinates.append(list(map(int, (from_x, from_y, to_x, to_y))))
    dim_length = max([max(row) for row in coordinates]) + 1  # 990 + 1
    # min([min(row) for row in coordinates])  # 10
    # grid = [[0] * dim_length] * dim_length
    grid = [[0] * dim_length for i in range(0, dim_length)]
    for coords in coordinates:
        coords = coordinates[2]
        print(coords)
        x1, y1, x2, y2 = coords[0], coords[1], coords[2], coords[3]
        vertical = True if x1 - x2 == 0 else False
        horizontal = True if y1 - y2 == 0 else False
        if vertical:  # implies constant x == iteration through rows
            for step in range(y2 - y1 + 1):
                grid[y1 + step][x1] += 1
        if horizontal:  # implies constant y == iteration through row's cols
            for step in range(x2 - x1 + 1):
                grid[y1][x1 + step] += 1
    grid

with open("extras/day5-extras.txt", "w") as f:
    for row in grid:
        # f.write(str(row) + "\n")
        row = "".join(map(str, row))
        row = row.replace("0", ".")
        f.write(row + "\n")
