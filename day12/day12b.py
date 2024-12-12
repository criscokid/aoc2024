import sys
sys.path.append('..')
from grid import TextGrid
g = TextGrid()

from collections import defaultdict, deque
import operator

with open(sys.argv[1]) as f:
    for line in f:
        g.add_row(list(line.strip("\n")))
        

nodes_seen = []
directions = {'right': (1, 0), 'down': (0, 1), 'left': (-1, 0), 'up': (0, -1)}

def flood_fill(start_pos):
    value_to_find = g.value_at(*start_pos)
    nodes = deque([start_pos])
    found_area = set()
    while not len(nodes) == 0:
        current_node = nodes.popleft()
        if g.value_at(*current_node) == value_to_find and current_node not in found_area:
            found_area.add(current_node)
            nodes_seen.append(current_node)
            for dir in directions.values():
                new_dir = tuple(map(operator.add, current_node, dir))
                nodes.append(new_dir)

    return found_area

areas = []
while g.scan():
    if g.current_pos() not in nodes_seen:
        area = flood_fill(g.current_pos())
        areas.append(area) 
            
for i in range(len(areas)):
    for p in areas[i]:
        g.set_value_at(p[0], p[1], i)

bounds = defaultdict(lambda: 0)
x_changes = []
for y in range(g.row_count()):
    row_changes = defaultdict(lambda: set())
    for x in range(-1, g.col_count() + 1):
        if g.value_at(x, y) != g.value_at(x + 1, y):
            key = g.value_at(x, y)
            row_changes[key].add((key, x))
            key = g.value_at(x + 1, y)
            row_changes[key].add((x, key))
    x_changes.append(dict(row_changes))

for c in range(len(areas)):
    last_seen = set()
    for xc in x_changes: 
        if c in xc:
            if xc[c] != last_seen:
                bounds["h" + str(c)] += len(xc[c] - last_seen)
            last_seen = xc[c]
y_changes = []
for x in range(g.col_count()):
    col_changes = defaultdict(lambda: set())
    for y in range(-1, g.row_count() + 1):
        if g.value_at(x, y) != g.value_at(x, y + 1):
            key = g.value_at(x, y)
            col_changes[key].add((key, y))
            key = g.value_at(x, y + 1)
            col_changes[key].add((y, key))
    y_changes.append(dict(col_changes))

for c in range(len(areas)):
    last_seen = set()
    for xc in y_changes: 
        if c in xc:
            if xc[c] != last_seen:
                bounds["v" + str(c)] += len(xc[c] - last_seen)
            last_seen = xc[c]
total = 0 
for a in areas:
    crop = g.value_at(*list(a)[0])
    sides = bounds["v" + str(crop)] + bounds["h" + str(crop)]
    total += sides * len(a)

print(total)
