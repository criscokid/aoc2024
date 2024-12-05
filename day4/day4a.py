import sys

sys.path.append('..')
from grid import TextGrid

total_xmas = 0
g = TextGrid()
with open(sys.argv[1]) as f:
    for line in f:
        g.add_row(list(line.strip()))


g.print()

while g.scan_until('X'):
    surrounding = g.take_count_around(4)
    strings = [''.join(x) for x in surrounding.values() if len(x) == 3]
    for s in strings:
        if s == "MAS":
            total_xmas += 1




print(total_xmas)
