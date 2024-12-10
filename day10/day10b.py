import sys
import operator
sys.path.append('..')
from grid import TextGrid
g = TextGrid()


def follow_path(pos, previous_val = -1, previous_pos = None):
    current_value = g.value_at(*pos)
    if current_value == None:
        return 0
    if current_value == -1:
        return 0
    if previous_val == 8 and current_value == 9:
        return 1
    if current_value != previous_val + 1:
        return 0
    
    v = 0
    look_at = [(-1, 0), (0, -1), (1, 0), (0,1)]
    for dir in look_at:
        new_dir = tuple(map(operator.sub, pos, dir))
        if new_dir != previous_pos:
            v += follow_path(new_dir, current_value, pos)

    return v

with open(sys.argv[1]) as f:
    for line in f:
        parts = [int(x) if x != '.' else -1 for x in list(line.strip("\n"))]
        g.add_row(parts)

total = 0
g.move_to_pos(-1, -1)
while g.scan_until(0):
    total += follow_path(g.current_pos()) 

print(total)

