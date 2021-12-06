#!/usr/bin/python3


def extract_coordinates(data):
    """Take input data and return list of parsed coordinates."""
    coordinates = []
    for line in data:
        from_, to_ = line.split(" -> ")[0], line.split(" -> ")[1]
        x1, y1 = from_.split(",")
        x2, y2 = to_.split(",")
        coordinates.append(list(map(int, (x1, y1, x2, y2))))
    return coordinates


def move_vertically(x1, y1, y2, grid):
    """Move vertically from y1 to y2 (x fixed)"""
    segment = y2 - y1
    for step in range(abs(segment) + 1):
        if segment > 0:
            grid[y1 + step][x1] += 1
        else:
            grid[y1 - step][x1] += 1
    return grid


def move_horizontally(x1, x2, y1, grid):
    """Move horizontally from x1 to x2 (y fixed)"""
    segment = x2 - x1
    for step in range(abs(segment) + 1):
        if segment > 0:
            grid[y1][x1 + step] += 1
        else:
            grid[y1][x1 - step] += 1
    return grid


def move_diagonally(x1, x2, y1, y2, grid):
    """Move diagonally from (x1, y1) -> (x2, y2)"""
    x_segment = x2 - x1
    y_segment = y2 - y1
    if x_segment > 0 and y_segment > 0:
        for step in range(abs(x_segment) + 1):
            grid[y1 + step][x1 + step] += 1
    if x_segment > 0 and y_segment < 0:
        for step in range(abs(x_segment) + 1):
            grid[y1 - step][x1 + step] += 1
    if x_segment < 0 and y_segment < 0:
        for step in range(abs(x_segment) + 1):
            grid[y1 - step][x1 - step] += 1
    if x_segment < 0 and y_segment > 0:
        for step in range(abs(x_segment) + 1):
            grid[y1 + step][x1 - step] += 1
    return grid


def map_vents_90degrees(coordinates):
    """--- Day 5: Hydrothermal Venture --- Map vertical/horizontal vents"""
    dim_length = max([max(row) for row in coordinates]) + 1  # 990 + 1
    grid = [[0] * dim_length for i in range(0, dim_length)]
    for coords in coordinates:
        # print(coords)
        x1, y1, x2, y2 = coords[0], coords[1], coords[2], coords[3]
        # check nature of movement (x1, y1) -> (x2, y2)
        vertical = True if x1 - x2 == 0 else False
        horizontal = True if y1 - y2 == 0 else False
        if vertical:  # iterate through rows (fixed x)
            grid = move_vertically(x1, y1, y2, grid)
        if horizontal:  # iterate through row's elements (fixed row)
            grid = move_horizontally(x1, x2, y1, grid)
    danger_areas = [1 if el >= 2 else 0 for row in grid for el in row]
    return grid, sum(danger_areas)


def map_vents_45degrees(grid, coordinates):
    """--- Part Two --- Add capability to map 45degree diagonals"""
    for coords in coordinates:
        x1, y1, x2, y2 = coords[0], coords[1], coords[2], coords[3]
        diagonally = True if abs(x2 - x1) - abs(y2 - y1) == 0 else False
        if diagonally:
            grid = move_diagonally(x1, x2, y1, y2, grid)
    danger_areas = [1 if el >= 2 else 0 for row in grid for el in row]
    return grid, sum(danger_areas)


def write_txt(file, path):
    """Wrapper to write 2d-array to text."""
    with open(path, "w") as f:
        for row in file:
            row = "".join(map(str, row))
            row = row.replace("0", ".")
            _ = f.write(row + "\n")


if __name__ == "__main__":
    with open("input/day5-test.txt", "r") as f:
        data = f.read().splitlines()
    coordinates = extract_coordinates(data)
    grid, points = map_vents_90degrees(coordinates)
    # write_txt(grid, "extras/day5-90deg.txt")
    print(f"Danger points w/2+ overlapping vents (90deg Grid): {points}")
    grid, points = map_vents_45degrees(grid, coordinates)
    # write_txt(grid, "extras/day5-full.txt")
    print(f"Danger points w/2+ overlapping vents (+45deg Grid): {points}")
