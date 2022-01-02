from dataclasses import dataclass
from utils import read_input, integers


@dataclass(frozen=True)
class Cuboid:
    x1: int
    x2: int
    y1: int
    y2: int
    z1: int
    z2: int

    def volume(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1) * (self.z2 - self.z1)

    def intersects(a, b):
        x_check = a.x1 < b.x2 and a.x2 > b.x1
        y_check = a.y1 < b.y2 and a.y2 > b.y1
        z_check = a.z1 < b.z2 and a.z2 > b.z1
        return x_check and y_check and z_check

    def subtract(a, b):
        if not a.intersects(b):
            yield a
        else:
            c = Cuboid(
                min(max(b.x1, a.x1), a.x2),
                min(max(b.x2, a.x1), a.x2),
                min(max(b.y1, a.y1), a.y2),
                min(max(b.y2, a.y1), a.y2),
                min(max(b.z1, a.z1), a.z2),
                min(max(b.z2, a.z1), a.z2),
            )

            yield Cuboid(a.x1, c.x1, a.y1, a.y2, a.z1, a.z2)  # 1 0
            yield Cuboid(c.x2, a.x2, a.y1, a.y2, a.z1, a.z2)  # 0 1
            yield Cuboid(c.x1, c.x2, a.y1, c.y1, a.z1, a.z2)  # 1 0
            yield Cuboid(c.x1, c.x2, c.y2, a.y2, a.z1, a.z2)  # 0 1
            yield Cuboid(c.x1, c.x2, c.y1, c.y2, a.z1, c.z1)  # 1 1
            yield Cuboid(c.x1, c.x2, c.y1, c.y2, c.z2, a.z2)  # 1 1


if __name__ == "__main__":
    T = False
    test, actual = "test/day22", "input/day22"
    data = read_input(test) if T else read_input(actual)
    steps = [(row.split(" ")[0], integers(row)) for row in data]


def reboot_reactor(reboot_steps):
    """--- Part Two ---"""
    reactor = []
    for switch, step in reboot_steps:
        x1, x2, y1, y2, z1, z2 = step
        new_cuboid = Cuboid(x1, x2 + 1, y1, y2 + 1, z1, z2 + 1)
        reactor_temp = []
        for cuboid in reactor:
            for minikube in cuboid.subtract(new_cuboid):
                reactor_temp.append(minikube)
        reactor = reactor_temp
        if switch == "on":
            reactor.append(new_cuboid)
    return sum(c.volume() for c in reactor)


print(f"Part 2 -- On cubes after full reboot: {reboot_reactor(steps)}")
# Part 2 -- On cubes after full reboot: 1218645427221987

# blog post annotations
# a = Cuboid(10, 12 + 1, 10, 12 + 1, 10, 12 + 1)
# b = Cuboid(11, 13 + 1, 11, 13 + 1, 11, 13 + 1)
# c = Cuboid(9, 11 + 1, 9, 11 + 1, 9, 11 + 1)
# d = Cuboid(10, 10 + 1, 10, 10 + 1, 10, 10 + 1)

# a.intersects(d)
# a.volume()

# x_min, x_max = min([s[0] for _, s in steps]), max([s[1] for _, s in steps])
# y_min, y_max = min([s[2] for _, s in steps]), max([s[3] for _, s in steps])
# z_min, z_max = min([s[4] for _, s in steps]), max([s[5] for _, s in steps])
# print(f"x: {(x_min, x_max)}, y: {(y_min, y_max)}, z: {(z_min , z_max)}")
# # x: (-96513, 97051), y: (-99029, 95078), z: (-98435, 98668)
# x_sz = x_max - x_min + 1
# y_sz = y_max - y_min + 1
# z_sz = z_max - z_min + 1
# print(f"x_len: {x_sz}, y_len: {y_sz}, z_len: {z_sz}")
# # x_len: 193565, y_len: 194108, z_len: 197104
# print(f"max vol: {round((x_sz * y_sz * z_sz)/ 10 ** 15, 1)}")
# # 7.4 Quadrillion
# print(round(48 * (x_sz * y_sz * z_sz) / 1024 ** 5, 1))
# # ~ 316 PB
