import sys
import operator

sys.path.append('..')
from grid import TextGrid
g = TextGrid()

dirs = {'^': (0, -1), '>': (1, 0), "v": (0, 1), "<": (-1, 0)}
path = []

grid = True
with open(sys.argv[1]) as f:
    for line in f:
        if line.strip() == "":
            grid = False

        parts = list(line.strip("\n"))
        if grid:
            parts = list(line.strip("\n"))
            g.add_row(parts)
        else:
            for p in parts:
                path.append(dirs[p])
       
def can_move_in_dir(pos, dir):
    (pos_x, pos_y) = pos
    (dir_x, dir_y) = dir
    new_pos_x = pos_x + dir_x
    new_pos_y = pos_y + dir_y

    if new_pos_x < 0 or new_pos_x >= g.col_count() or new_pos_y < 0 or new_pos_y >= g.row_count():
        return False

    if g.value_at(new_pos_x, new_pos_y) == "#":
        return False

    if g.value_at(new_pos_x, new_pos_y) == "O":
        if not can_move_in_dir((new_pos_x, new_pos_y), dir):
            return False

    if g.value_at(new_pos_x, new_pos_y) == ".":
        old_value = g.value_at(pos_x, pos_y)
        g.set_value_at(pos_x, pos_y, ".")
        g.set_value_at(new_pos_x, new_pos_y, old_value)
        return True 

g.scan_until('@')
current_pos = g.current_pos()
for p in path:
    if can_move_in_dir(current_pos, p):
        current_pos = tuple(map(operator.add, current_pos, p))

g.move_to_pos(-1, 0)

total = 0
while g.scan_until('O'):
    (x, y) = g.current_pos()
    total += y * 100 + x

print(total)
