#!/usr/bin/env python

import math
from collections import defaultdict
from itertools import product
from operator import itemgetter

with open(__file__, "r") as f:
    c = f.read()
    space = list(zip(*c[c.rindex("🎅") + 1 : c.rindex("🐍")].rstrip().split("\n")))


def get_count(p, q):
    if p[0] == q[0]:
        return abs(p[1] - q[1])

    if p[1] == q[1]:
        return abs(p[0] - q[0])

    return math.gcd(abs(p[0] - q[0]), abs(p[1] - q[1]))


d = defaultdict(int)
side = len(space[0])

for p in product(range(side), repeat=2):
    if space[p[0]][p[1]] != "#":
        continue

    for q in product(range(side), repeat=2):
        if space[q[0]][q[1]] != "#" or (p[0] == q[0] and p[1] == q[1]):
            continue

        c = get_count(p, q)

        dx = (q[0] - p[0]) // c
        dy = (q[1] - p[1]) // c

        d[p] += 1 == sum(
            space[p[0] + dx * i][p[1] + dy * i] == "#" for i in range(1, c + 1)
        )

part_one = max(d.values())
print(part_one)
assert part_one == 282

sx, sy = max(d.items(), key=itemgetter(1))[0]
refvec = (0, 1)


# https://stackoverflow.com/questions/41855695
def clockwise(vector):
    length = math.hypot(vector[0], vector[1])

    if length == 0:
        return -math.pi, 0

    normalized = (vector[0] / length, vector[1] / length)
    dotprod = normalized[0] * refvec[0] + normalized[1] * refvec[1]
    diffprod = refvec[1] * normalized[0] - refvec[0] * normalized[1]
    angle = math.atan2(diffprod, dotprod)

    if angle < 0:
        return 2 * math.pi + angle, length

    return angle, length


grid = map(lambda p: (p[0] - sx, -(p[1] - sy)), product(range(side), repeat=2))

sorted_positions = sorted(grid, key=clockwise)[1:]


def remap(p):
    x, y = p
    return (x + sx, -y + sy)


asteroids = [p for p in sorted_positions if space[remap(p)[0]][remap(p)[1]] == "#"]

counter = 0
last_angle = 0
i = 0

while asteroids:
    if i > len(asteroids) - 1:
        i = 0

    x, y = asteroids[i]
    a = math.atan2(y, x)

    if last_angle == a:
        i += 1
        continue

    pt = asteroids.pop(i)
    counter += 1
    last_angle = a

    if counter == 200:
        part_two = 100 * remap(pt)[0] + remap(pt)[1]
        break

print(part_two)
assert part_two == 1008

"""🎅###..#.##.####.##..###.#.#..
#..#..###..#.......####.....
#.###.#.##..###.##..#.###.#.
..#.##..##...#.#.###.##.####
.#.##..####...####.###.##...
##...###.#.##.##..###..#..#.
.##..###...#....###.....##.#
#..##...#..#.##..####.....#.
.#..#.######.#..#..####....#
#.##.##......#..#..####.##..
##...#....#.#.##.#..#...##.#
##.####.###...#.##........##
......##.....#.###.##.#.#..#
.###..#####.#..#...#...#.###
..##.###..##.#.##.#.##......
......##.#.#....#..##.#.####
...##..#.#.#.....##.###...##
.#.#..#.#....##..##.#..#.#..
...#..###..##.####.#...#..##
#.#......#.#..##..#...#.#..#
..#.##.#......#.##...#..#.##
#.##..#....#...#.##..#..#..#
#..#.#.#.##..#..#.#.#...##..
.#...#.........#..#....#.#.#
..####.#..#..##.####.#.##.##
.#.######......##..#.#.##.#.
.#....####....###.#.#.#.####
....####...##.#.#...#..#.##.
🐍"""
