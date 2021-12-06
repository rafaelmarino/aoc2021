#!/usr/bin/python3


if __name__ == "__main__":
    with open("input/day5.txt", "r") as f:
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
    m_grid = [[0] * dim_length for i in range(0, dim_length)]  # manhattan
    e_grid = [[0] * dim_length for i in range(0, dim_length)]  # euclidean
    for coords in coordinates:
        # coords = coordinates[1]
        # print(coords)
        x1, y1, x2, y2 = coords[0], coords[1], coords[2], coords[3]
        vertical = True if x1 - x2 == 0 else False
        horizontal = True if y1 - y2 == 0 else False
        diagonal = True if abs(x2 - x1) - abs(y2 - y1) == 0 else False
        if vertical:  # constant x; iterate through rows
            segment = y2 - y1
            for step in range(abs(segment) + 1):
                if segment > 0:
                    m_grid[y1 + step][x1] += 1
                    e_grid[y1 + step][x1] += 1
                else:
                    m_grid[y1 - step][x1] += 1
                    e_grid[y1 - step][x1] += 1
        if horizontal:  # constant y; iterate through row's cols
            segment = x2 - x1
            for step in range(abs(segment) + 1):
                if segment > 0:
                    m_grid[y1][x1 + step] += 1
                    e_grid[y1][x1 + step] += 1
                else:
                    m_grid[y1][x1 - step] += 1
                    e_grid[y1][x1 - step] += 1
        if diagonal:  # iterate through both rows and cols
            x_segment = x2 - x1
            y_segment = y2 - y1
            for step in range(abs(x_segment) + 1):
                if x_segment > 0 and y_segment > 0:
                    e_grid[y1 + step][x1 + step] += 1
                if x_segment > 0 and y_segment < 0:
                    e_grid[y1 - step][x1 + step] += 1
                if x_segment < 0 and y_segment < 0:
                    e_grid[y1 - step][x1 - step] += 1
                if x_segment < 0 and y_segment > 0:
                    e_grid[y1 + step][x1 - step] += 1
    # m_grid
    danger_areas_m = [1 if elem >= 2 else 0 for row in m_grid for elem in row]
    sum(danger_areas_m)
    # e_grid
    danger_areas_e = [1 if elem >= 2 else 0 for row in e_grid for elem in row]
    sum(danger_areas_e)

    # return sum(dangerous_mask)

with open("extras/day5-extras.txt", "w") as f:
    g = [m_grid, e_grid]
    grid = g[1]
    for row in grid:
        # grid[0]
        # f.write(str(row) + "\n")
        row = "".join(map(str, row))
        row = row.replace("0", ".")
        _ = f.write(row + "\n")
