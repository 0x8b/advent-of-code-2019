#!/usr/bin/env python

import re
from collections import Counter

with open(__file__, "r") as f:
    c = f.read()
    lower, upper = map(int, c[c.rindex("🎅") + 1 : c.rindex("🐍")].rstrip().split("-"))

part_one = 0
part_two = 0

for i in range(lower, upper + 1):
    if (s := str(i)) == "".join(sorted(s)):
        if re.compile(r"(\d)\1").search(s):
            part_one += 1

        if 2 in Counter(s).values():
            part_two += 1

print(part_one)
assert part_one == 1675

print(part_two)
assert part_two == 1142

"""🎅172930-683082
🐍"""
