import sys
import itertools

sys.path.append('..')
from grid import TextGrid
g = TextGrid()
with open(sys.argv[1]) as f:
    for line in f:
        g.add_row(list(line.strip()))


antennas = []
while g.scan():
    v = g.value_at_current_pos()
    if v != '.':
        antennas.append((v, g.current_pos()))

def distance(pos1, pos2):
    (x1, y1) = pos1
    (x2, y2) = pos2

    return (x2 - x1, y2 - y1)


possible_locations = []
ant_groups = itertools.groupby(sorted(antennas, key= lambda y: y[0]), lambda x: x[0])
for key, ant_group in ant_groups:
    positions = [x[1] for x in ant_group] 
    print(key, positions)
    for c in itertools.product(positions, repeat=2):
        p1, p2 = (c)
        if p1 == p2:
            continue
        dx, dy = distance(p1, p2)
        for x, y in [p1, p2]:
            new_x = x + dx
            new_y = y + dy
            if new_x >= 0 and new_x < g.col_count() and new_y >=0 and new_y < g.row_count():
                new_loc = (new_x, new_y)
                if new_loc != p1 and new_loc != p2:
                    possible_locations.append((new_x, new_y))
print(len(set(possible_locations)))
            
