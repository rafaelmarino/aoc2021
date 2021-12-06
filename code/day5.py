#!/usr/bin/python3


def move_vertically(x1, y1, y2, m_grid, e_grid):
    """Move vertically across both grids."""
    segment = y2 - y1
    for step in range(abs(segment) + 1):
        if segment > 0:
            m_grid[y1 + step][x1] += 1
            e_grid[y1 + step][x1] += 1
        else:
            m_grid[y1 - step][x1] += 1
            e_grid[y1 - step][x1] += 1
    return m_grid, e_grid


def move_horizontally(x1, x2, y1, m_grid, e_grid):
    """Move horizontally across both grids."""
    segment = x2 - x1
    for step in range(abs(segment) + 1):
        if segment > 0:
            m_grid[y1][x1 + step] += 1
            e_grid[y1][x1 + step] += 1
        else:
            m_grid[y1][x1 - step] += 1
            e_grid[y1][x1 - step] += 1
    return m_grid, e_grid


def move_diagonally(x1, x2, y1, y2, e_grid):
    """Move diagonally across both grids."""
    x_segment = x2 - x1
    y_segment = y2 - y1
    if x_segment > 0 and y_segment > 0:
        for step in range(abs(x_segment) + 1):
            e_grid[y1 + step][x1 + step] += 1
    if x_segment > 0 and y_segment < 0:
        for step in range(abs(x_segment) + 1):
            e_grid[y1 - step][x1 + step] += 1
    if x_segment < 0 and y_segment < 0:
        for step in range(abs(x_segment) + 1):
            e_grid[y1 - step][x1 - step] += 1
    if x_segment < 0 and y_segment > 0:
        for step in range(abs(x_segment) + 1):
            e_grid[y1 + step][x1 - step] += 1
    return e_grid


def map_hydrothermal_vents(data):
    """--- Day 5: Hydrothermal Venture ---"""
    coordinates = []
    for line in data:
        from_, to_ = line.split(" -> ")[0], line.split(" -> ")[1]
        x1, y1 = from_.split(",")
        x2, y2 = to_.split(",")
        coordinates.append(list(map(int, (x1, y1, x2, y2))))
    dim_length = max([max(row) for row in coordinates]) + 1  # 990 + 1
    # min([min(row) for row in coordinates])  # 10
    m_grid = [[0] * dim_length for i in range(0, dim_length)]  # manhattan
    e_grid = [[0] * dim_length for i in range(0, dim_length)]  # euclidean
    for coords in coordinates:
        # print(coords)
        x1, y1, x2, y2 = coords[0], coords[1], coords[2], coords[3]
        # check nature of movement (x1, y1) -> (x2, y2)
        vertically = True if x1 - x2 == 0 else False
        horizontally = True if y1 - y2 == 0 else False
        diagonally = True if abs(x2 - x1) - abs(y2 - y1) == 0 else False
        if vertically:  # constant x; iterate through rows (fixed x)
            m_grid, e_grid = move_vertically(x1, y1, y2, m_grid, e_grid)
        if horizontally:  # constant y; iterate through row's cols (fixed row)
            m_grid, e_grid = move_horizontally(x1, x2, y1, m_grid, e_grid)
        if diagonally:  # iterate through both rows and cols
            e_grid = move_diagonally(x1, x2, y1, y2, e_grid)
    danger_areas_m = [1 if el >= 2 else 0 for row in m_grid for el in row]
    danger_areas_e = [1 if el >= 2 else 0 for row in e_grid for el in row]
    # return m_grid, e_grid, sum(danger_areas_m), sum(danger_areas_e)
    return sum(danger_areas_m), sum(danger_areas_e)


if __name__ == "__main__":
    with open("input/day5-test.txt", "r") as f:
        data = f.read().splitlines()
    m_danger, e_danger = map_hydrothermal_vents(data)
    print(f"Danger points w/2+ overlapping vents (Manhattan Grid): {m_danger}")
    print(f"Danger points w/2+ overlapping vents (Euclidean Grid): {e_danger}")

# export grids for test cases
# file_paths = ["extras/day5-manhattan.txt", "extras/day5-euclidean.txt"]
# for path in file_paths:
#     with open(path, "w") as f:
#         if path == "extras/day5-manhattan.txt":
#             grid = m_grid
#         else:
#             grid = e_grid
#         for row in grid:
#             # f.write(str(row) + "\n")
#             row = "".join(map(str, row))
#             row = row.replace("0", ".")
#             _ = f.write(row + "\n")
