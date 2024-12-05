import sys

sys.path.append('..')
from grid import TextGrid

total_xmas = 0
g = TextGrid()
with open(sys.argv[1]) as f:
    for line in f:
        g.add_row(list(line.strip()))


g.print()

while g.scan_until('A'):
    s = g.take_count_around(2)
    up_left = ''.join(s['up_left'])
    up_right = ''.join(s['up_right'])
    down_left = ''.join(s['down_left'])
    down_right = ''.join(s['down_right'])

    if (up_left == 'S' and down_right == 'M') or (up_left == 'M' and down_right == 'S'):
        if (up_right == 'M' and down_left == 'S') or (up_right == 'S' and down_left == 'M'):
            total_xmas += 1

print(total_xmas)
