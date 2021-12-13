#!/usr/bin/python3

from collections import defaultdict


if __name__ == "__main__":
    test1, test2 = "test-input/day12-1.txt", "test-input/day12-2.txt"
    test3, actual = "test-input/day12-3.txt", "input/day12.txt"
    with open(actual, "r") as f:
        data = f.read().splitlines()

    d = defaultdict(list)
    for u, v in [uv.strip().split("-") for uv in data]:
        d[u].append(v)
        d[v].append(u)
    # d.default_factory = None  # return to regular dic
    d

    def dfs(visited_caves=set(), start="start", end="end"):
        """--- Day 12: Passage Pathing ---"""
        counter = 0
        for node in d[start]:
            if node == "start":
                continue
            if start.islower():
                visited_caves = visited_caves | {start}
            if node == end:  # path found
                counter += 1
            elif node in visited_caves:
                continue
            else:
                counter += dfs(visited_caves, start=node)
        return counter

    print(f"Part 1 -- {dfs()}")
    # print(f"Part 2 -- {}")
