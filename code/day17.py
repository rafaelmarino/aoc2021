#!/usr/bin/python3

from utils import integers


def take_step(x, y, vx, vy):
    """--- Day 17: Trick Shot ---"""
    x += vx
    y += vy
    if vx > 0:
        vx -= 1
    if vx <= -1:
        vx += 1
    vy -= 1
    return x, y, vx, vy


def will_hit(vx, vy):
    """--- Part Two ---"""
    x, y = 0, 0
    while x <= x2 and y >= y1:  # while probe has chance to reach target
        x, y, vx, vy = take_step(x, y, vx, vy)
        if x1 <= x <= x2 and y1 <= y <= y2:
            return True  # target area touched
    return False  # probe never touches the target area at (vx, vy)


if __name__ == "__main__":
    test, actual = "test-input/day17.txt", "input/day17.txt"
    with open(test, "r") as f:
        # data = f.read().splitlines()
        data = f.readline()
    x1, x2, y1, y2 = integers(data)


print(y1 * (y1 + 1) // 2)
# print(sum(range(abs(y1))))
print(sum(will_hit(vx, vy) for vx in range(x2 + 1) for vy in range(y1, -y1)))
