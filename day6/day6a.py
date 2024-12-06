import sys

sys.path.append('..')
from grid import TextGrid

total_xmas = 0
g = TextGrid()
with open(sys.argv[1]) as f:
    for line in f:
        g.add_row(list(line.strip()))


g.print()

g.scan_until('^')
g.set_facing('up')

while g.next_facing_val() != None:
    if g.next_facing_val() == '.' or g.next_facing_val() == 'X':
        g.set_value_at_current_pos('X')
        g.move_facing()
        continue

    if g.next_facing_val() == '#':
        current_dir = g.facing_dir()
        if current_dir == 'up':
            g.set_facing('right')
        if current_dir == 'right':
            g.set_facing('down')
        if current_dir == 'down':
            g.set_facing('left')
        if current_dir == 'left':
            g.set_facing('up')
        continue

g.set_value_at_current_pos('X')
print()
g.print()

total_x = 0
data = g.current_data()

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 'X':
            total_x += 1

print(total_x)
