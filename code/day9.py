#!/usr/bin/python3


import numpy as np


def extract_low_points(matrix):
    """--- Day 9: Smoke Basin ---"""
    # pad matrix with 9s to allow rolling (up/down rows; left/right cols)
    m = np.pad(matrix, pad_width=(1, 1), mode="constant", constant_values=9)
    row_mask = (np.roll(m, 1, 0) > m) & (np.roll(m, -1, 0) > m)
    col_mask = (np.roll(m, 1, 1) > m) & (np.roll(m, -1, 1) > m)
    local_minima_conditions = (row_mask & col_mask)[1:-1, 1:-1]  # crop
    low_points = np.extract(local_minima_conditions, matrix)
    return low_points


def traverse_sccs(grid):
    """--- Part Two ---"""

    def dfs(grid, i, j):
        out_of_bounds_i = i < 0 or i >= len(grid)
        out_of_bounds_j = j < 0 or j >= len(grid[0])
        if out_of_bounds_i or out_of_bounds_j or grid[i][j] == 9:
            return
        grid[i][j] = 9  # mark as visited
        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i, j - 1)

    nines_ = (grid == 9).sum()
    scc_count = 0  # count of strongly connected components aka basins
    ncs = []  # node counts per SCC
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 9:  # if node not visited
                dfs(grid, i, j)
                scc_count += 1
                # just visited = all visited - initial nodes - prev visited
                ncs.append((grid == 9).sum() - nines_ - sum(ncs))
    return ncs


if __name__ == "__main__":
    matrix = np.genfromtxt("input/day9.txt", delimiter=1, dtype=int)
    low_points = extract_low_points(matrix)
    risk = (low_points + 1).sum()
    scc_node_counts = sorted(traverse_sccs(matrix[:]), reverse=True)
    top3_areas = np.prod(scc_node_counts[:3])
    print(f"Part 1 -- Total risk from all low points: {risk}")
    print(f"Part 2 -- Area of top 3 SCCs (basins) {top3_areas}")
