import sys
import operator
sys.path.append('..')
from grid import TextGrid
g = TextGrid()

found_nines = [] 

def follow_path(pos, previous_val = -1, previous_pos = None):
    current_value = g.value_at(*pos)
    if current_value == None:
        return
    if current_value == -1:
        return
    if previous_val == 8 and current_value == 9:
        found_nines.append(pos)
        return
    if current_value != previous_val + 1:
        return

    look_at = [(-1, 0), (0, -1), (1, 0), (0,1)]
    for dir in look_at:
        new_dir = tuple(map(operator.sub, pos, dir))
        if new_dir != previous_pos:
            follow_path(new_dir, current_value, pos)

with open(sys.argv[1]) as f:
    for line in f:
        parts = [int(x) if x != '.' else -1 for x in list(line.strip("\n"))]
        g.add_row(parts)

total = 0
while g.scan_until(0):
    follow_path(g.current_pos()) 
    total += len(set(found_nines))
    found_nines = []

print(total)

