#!/usr/bin/python3


def map_hydrothermal_vents(data):
    """--- Day 5: Hydrothermal Venture ---"""
    coordinates = []
    for line in data:
        from_, to_ = line.split(" -> ")[0], line.split(" -> ")[1]
        from_x, from_y = from_.split(",")
        to_x, to_y = to_.split(",")
        coordinates.append(list(map(int, (from_x, from_y, to_x, to_y))))
    dim_length = max([max(row) for row in coordinates]) + 1  # 990 + 1
    # min([min(row) for row in coordinates])  # 10
    m_grid = [[0] * dim_length for i in range(0, dim_length)]  # manhattan
    e_grid = [[0] * dim_length for i in range(0, dim_length)]  # euclidean
    for coords in coordinates:
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
    danger_areas_m = [1 if elem >= 2 else 0 for row in m_grid for elem in row]
    danger_areas_e = [1 if elem >= 2 else 0 for row in e_grid for elem in row]
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
#             # grid[0]
#             # f.write(str(row) + "\n")
#             row = "".join(map(str, row))
#             row = row.replace("0", ".")
#             _ = f.write(row + "\n")
