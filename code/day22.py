#!/usr/bin/python3

from __future__ import annotations
from typing import List

# from itertools import product
from utils import read_input, integers
from math import prod


def initialize_reactor(steps):
    """--- Day 22: Reactor Reboot ---"""
    coords = set()
    for step in steps:
        on = True if step[0] == "on" else False
        x1, x2, y1, y2, z1, z2 = step[1]
        new_coords = {  # inclusive range. truncate from -50 to 50
            (x, y, z)
            for x in range(max(x1, -50), min(x2, 50) + 1)
            for y in range(max(y1, -50), min(y2, 50) + 1)
            for z in range(max(z1, -50), min(z2, 50) + 1)
        }
        if on:
            coords |= new_coords
        else:
            coords -= new_coords
    return len(coords)


class Cuboid:
    """A cuboid (i.e., rectangular prism) contains many 1x1x1 cubes"""

    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1, self.x2 = x1, x2
        self.y1, self.y2 = y1, y2
        self.z1, self.z2 = z1, z2
        self.coords = [x1, x2, y1, y2, z1, z2]

    def vol(self) -> int:
        self.vol_ = prod(
            [
                self.x2 - self.x1,
                self.y2 - self.y1,
                self.z2 - self.z1,
            ]
        )
        return self.vol_

    def intersects(self, Other: Cuboid) -> bool:
        x_check = self.x1 <= Other.x2 - 1 and self.x2 - 1 >= Other.x1
        y_check = self.y1 <= Other.y2 - 1 and self.y2 - 1 >= Other.y1
        z_check = self.z1 <= Other.z2 - 1 and self.z2 - 1 >= Other.z1
        return x_check and y_check and z_check

    def contains(self, Other: Cuboid) -> bool:
        x_check = self.x1 <= Other.x1 and self.x2 >= Other.x2
        y_check = self.y1 <= Other.y1 and self.y2 >= Other.y2
        z_check = self.z1 <= Other.z1 and self.z2 >= Other.z2
        return x_check and y_check and z_check

    def subtract(self, Other: Cuboid) -> List[Cuboid]:
        if not self.intersects(Other):
            return [self]  # nothing to subtract
        elif Other.contains(self):
            return []  # cuboid_a completely deleted
        xs = sorted((self.x1, self.x2, Other.x1, Other.x2))
        ys = sorted((self.y1, self.y2, Other.y1, Other.y2))
        zs = sorted((self.z1, self.z2, Other.z1, Other.z2))

        ret = []
        for x0, x1 in zip(xs, xs[1:]):
            for y0, y1 in zip(ys, ys[1:]):
                for z0, z1 in zip(zs, zs[1:]):
                    cube = Cuboid(x0, x1, y0, y1, z0, z1)
                    if self.contains(cube) and not cube.intersects(Other):
                        ret.append(cube)
        return ret


if __name__ == "__main__":
    T = 0
    test, actual = "test/day22", "input/day22"
    data = read_input(test) if T else read_input(actual)
    steps = [(row.split(" ")[0], integers(row)) for row in data]


def compute(steps: list) -> int:
    cubes: list[Cuboid] = []
    for on, step in steps:
        step = [num + 1 if i % 2 == 1 else num for i, num in enumerate(step)]
        cuboid = Cuboid(*step)
        cubes = [part for cube in cubes for part in cube.subtract(cuboid)]
        if on == "on":
            cubes.append(cuboid)
        # print(sum(cube.vol() for cube in cubes))
    return sum(cube.vol() for cube in cubes)


print(compute(steps))

# # volume = 0
# on, coords_a = steps[0]
# on, coords_b = steps[1]
# on, coords_c = steps[2]
# on, coords_d = steps[3]
# # x1, x2, y1, y2, z1, z2 = step
# cuboid_a = Cuboid(*coords_a)
# cuboid_b = Cuboid(*coords_b)
# cuboid_c = Cuboid(*coords_c)
# cuboid_d = Cuboid(*coords_d)
# cuboid_X = Cuboid(15, 20, 15, 20, 15, 20)

# cuboid_a.coords, cuboid_b.coords, cuboid_c.coords, cuboid_d.coords
# cuboid_X.coords
# assert cuboid_a.intersects(cuboid_b)
# cuboid_a.intersects(cuboid_d)
# assert not cuboid_a.intersects(cuboid_X)
# assert cuboid_a.contains(cuboid_a) and cuboid_b.contains(cuboid_b)
# # print(len(cuboid_a.subtract(cuboid_b)))
# # print(sum([C.vol() for C in cuboid_a.subtract(cuboid_b)]))
# cuboid_b.subtract(cuboid_a)
# assert cuboid_a.subtract(cuboid_X)[0] == cuboid_a

# cuboid_a.vol()
# cuboid_b.vol()
# cuboid_d.vol()
# 19+27 = 46  # 19 unique on cuboid_b, 8 overlap
# 27-19 = 8

# minikubes_a = list(
#     product(
#         range(cuboid_a.x1, cuboid_a.x2 + 1),
#         range(cuboid_a.y1, cuboid_a.y2 + 1),
#         range(cuboid_a.z1, cuboid_a.z2 + 1),
#     ),
# )
# minikubes_b = list(
#     product(
#         range(cuboid_d.x1, cuboid_d.x2 + 1),
#         range(cuboid_d.y1, cuboid_d.y2 + 1),
#         range(cuboid_d.z1, cuboid_d.z2 + 1),
#     ),
# )

# dif = set(minikubes_a).difference(set(minikubes_b))
# len(dif), dif
# intersection = set(minikubes_a).intersection(set(minikubes_b))
# len(intersection), intersection


# cuboid.vol()
# reboot_cuboids = []
# for step in steps:
#     pass


# print(f"Part 1 -- On cubes after initialization: {initialize_reactor(steps)}")
# print(f"Part 2 -- On cubes after full reboot: {reboot_reactor(steps)}")


"""
rebooted_cuboids = []
for step in steps:
    cuboid_b = Cuboid(step)
    processed_cuboids = []
    for cuboid_a in rebooted_cuboids:
        # Cases for cuboid_a - cuboid_b:
        - If cuboid_b contains cuboid_a:
            continue
        - Elif cuboid_a intersects cuboid_b:
            cuboid_a = Subtract(cuboid_b from cuboid_a)
            processed_cuboids.append(cuboid_a)
    if cuboid_b.on:
        processed_cuboids.append(cuboid_b)
    rebooted_cuboids = processed_cuboids

Try recursion. When the command is 'on' the resulting number of cubes is all the cubes that were already on, plus all the cubes in the region being turned on, minus all the cubes that were already on in that region (so that they aren't double-counted
"""
