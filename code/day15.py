#!/usr/bin/python3

# import numpy as np
from heapq import heappop, heappush
from utils import *


def dijkstras(grid, start, end):
    """--- Day 15: Chiton ---"""
    heap, seen, dist = [(0, start)], set(), {start: 0}
    while heap:
        cost, cur = heappop(heap)  # cur_0 = [0, (0, 0)]
        seen.add(cur)
        if cur == end:
            return cost

        for n in neighbours(*cur):
            if n not in grid or n in seen:
                continue
            new_cost = cost + grid[n]
            # non-existing elements in heapq are considered to be infinite
            if n not in dist or new_cost < dist[n]:
                dist[n] = new_cost
                heappush(heap, (new_cost, n))
    assert False, "No path found"


if __name__ == "__main__":
    test, actual = "test-input/day15.txt", "input/day15.txt"
    with open(actual, "r") as f:
        g = [[int(x) for x in line.strip()] for line in f]
    SX, SY = len(g[0]), len(g)  # size of x, size of y
    grid1 = grid_to_dict(g)  # {(0, 0): 1, ... , (SX-1, SY-1): x}

    grid2 = {}  # part2
    for (x, y), val in grid1.items():
        for i in range(5):
            for j in range(5):
                grid2[(SX * i + x, SY * j + y)] = (val + i + j - 1) % 9 + 1

    # _, val = list(grid1.items())[0]
    # val = 8
    # result = []
    # for i in range(5):
    #     for j in range(5):
    #         result.append((val + i + j - 1) % 9 + 1)
    # the (-1 % +1) guarantee that no grid value is Zero. 9%9==0
    # [result[i : i + 5] for i in range(0, len(result), 5)]
    # [
    #     [8, 9, 1, 2, 3],
    #     [9, 1, 2, 3, 4],
    #     [1, 2, 3, 4, 5],
    #     [2, 3, 4, 5, 6],
    #     [3, 4, 5, 6, 7],
    # ]

print("Part 1", dijkstras(grid1, (0, 0), (SX - 1, SY - 1)))
print("Part 2", dijkstras(grid2, (0, 0), (SX * 5 - 1, SY * 5 - 1)))
