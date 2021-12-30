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
        x_check = a.x1 <= b.x2 and a.x2 >= b.x1
        y_check = a.y1 <= b.y2 and a.y2 >= b.y1
        z_check = a.z1 <= b.z2 and a.z2 >= b.z1
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

            yield Cuboid(a.x1, c.x1, a.y1, a.y2, a.z1, a.z2)  # 1
            yield Cuboid(c.x2, a.x2, a.y1, a.y2, a.z1, a.z2)  # 0
            yield Cuboid(c.x1, c.x2, a.y1, c.y1, a.z1, a.z2)  # 1
            yield Cuboid(c.x1, c.x2, c.y2, a.y2, a.z1, a.z2)  # 0
            yield Cuboid(c.x1, c.x2, c.y1, c.y2, a.z1, c.z1)  # 1
            yield Cuboid(c.x1, c.x2, c.y1, c.y2, c.z2, a.z2)  # 1


if __name__ == "__main__":
    T = False
    test, actual = "test/day22", "input/day22"
    data = read_input(test) if T else read_input(actual)
    steps = [(row.split(" ")[0], integers(row)) for row in data]

reactor = []
for switch, step in steps:
    x1, x2, y1, y2, z1, z2 = step
    new_cuboid = Cuboid(x1, x2 + 1, y1, y2 + 1, z1, z2 + 1)
    reactor_temp = []
    for cuboid in reactor:
        for minikube in cuboid.subtract(new_cuboid):
            if minikube.volume():
                reactor_temp.append(minikube)
    reactor = reactor_temp
    if switch == "on":
        reactor.append(new_cuboid)

print(sum(c.volume() for c in reactor))
