#!/usr/bin/env python

import math
import re
from copy import deepcopy
from functools import reduce

with open(__file__, "r") as f:
    c = f.read()
    lines = c[c.rindex("🎅") + 1 : c.rindex("🐍")].rstrip().split("\n")

moons = list(map(lambda x: list(map(int, re.compile(r"-?\d+").findall(x))), lines))
velocity = [[0] * 3 for _ in range(len(moons))]


def signum(a, b):
    return 1 if a < b else (-1 if a > b else 0)


m = deepcopy(moons)

for i in range(1000):
    grav = [
        reduce(
            lambda a, b: list(
                map(sum, zip(a, map(lambda t: signum(t[0], t[1]), zip(m[j], b))))
            ),
            m,
            [0] * 3,
        )
        for j in range(4)
    ]

    for j in range(4):
        for k in range(3):
            velocity[j][k] += grav[j][k]
            m[j][k] += velocity[j][k]

pot = map(lambda x: sum(map(abs, x)), m)
kin = map(lambda x: sum(map(abs, x)), velocity)

part_one = sum(a * b for a, b in zip(pot, kin))
print(part_one)
assert part_one == 14606


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def period(pos):
    init_positions = tuple(pos)
    vel = (0, 0, 0, 0)
    t = 0

    while True:
        grav = [sum(map(lambda p: signum(pos[i], p), pos)) for i in range(len(pos))]
        vel = tuple(map(sum, zip(vel, grav)))
        pos = tuple(map(sum, zip(pos, vel)))

        t += 1

        if vel == (0, 0, 0, 0) and pos == init_positions:
            return t


periods = map(period, zip(*moons))
part_two = reduce(lambda a, p: lcm(a, p), periods, 1)
print(part_two)
assert part_two == 543673227860472

"""🎅<x=1, y=-4, z=3>
<x=-14, y=9, z=-4>
<x=-4, y=-6, z=7>
<x=6, y=-9, z=-11>
🐍"""
