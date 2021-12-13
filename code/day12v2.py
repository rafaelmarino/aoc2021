#!/usr/bin/python3

from collections import defaultdict


if __name__ == "__main__":
    test1, test2 = "test-input/day12-1.txt", "test-input/day12-2.txt"
    test3, actual = "test-input/day12-3.txt", "input/day12.txt"
    with open(actual, "r") as f:
        data = f.read().splitlines()

    adj_list = defaultdict(list)
    for u, v in [uv.strip().split("-") for uv in data]:
        adj_list[u].append(v)
        adj_list[v].append(u)

    def traverse(can_twice, a="start", seen={"start"}):
        if a == "end":
            yield 1
        else:
            for b in adj_list[a]:
                if b.islower():
                    if b not in seen:
                        yield from traverse(can_twice, b, seen | {b})
                    elif can_twice and b not in {"start", "end"}:
                        yield from traverse(False, b, seen)
                else:
                    yield from traverse(can_twice, b, seen)


print(f"Part 1 -- {sum(traverse(can_twice=False))}")
print(f"Part 2 -- {sum(traverse(can_twice=True))}")
