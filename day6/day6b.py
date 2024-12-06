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
start_pos = g.current_pos()

main_path = []

while g.next_facing_val() != None:
    if g.next_facing_val() == '.' or g.next_facing_val() == '^':
        main_path.append(g.current_pos())
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

main_path.append(g.current_pos())
block_pos = 0


for pos in set(main_path[1:]):
    g.set_facing('up')
    x, y = pos
    g.move_to_pos(*start_pos)
    g.set_value_at(x, y, '#')
    turns = []
    while g.next_facing_val() != None:
        if g.next_facing_val() != '#':
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
            if (g.current_pos(), current_dir, g.facing_dir()) in turns:
                block_pos += 1
                break
            turns.append((g.current_pos(), current_dir, g.facing_dir()))
    
    g.set_value_at(x, y, '.')

print(block_pos)
