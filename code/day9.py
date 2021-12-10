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


def compute_three_largest_basins():
    """--- Part Two ---"""
    return


if __name__ == "__main__":
    matrix = np.genfromtxt("test-input/day9.txt", delimiter=1, dtype=int)
    low_points = extract_low_points(matrix)
    risk = (low_points + 1).sum()

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                self.dfs(grid, i, j)
                count += 1
    return count


def dfs(self, grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
        return
    grid[i][j] = "#"
    self.dfs(grid, i + 1, j)
    self.dfs(grid, i - 1, j)
    self.dfs(grid, i, j + 1)
    self.dfs(grid, i, j - 1)

    print(f"Part 1 -- Total risk from all low points: {risk}")
    # print(f"{}")
