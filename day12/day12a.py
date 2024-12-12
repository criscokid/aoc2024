import sys
sys.path.append('..')
from grid import TextGrid
g = TextGrid()

from collections import deque
import operator

with open(sys.argv[1]) as f:
    for line in f:
        g.add_row(list(line.strip("\n")))
        

nodes_seen = []

def flood_fill(start_pos):
    value_to_find = g.value_at(*start_pos)
    nodes = deque([start_pos])
    found_area = set()
    while not len(nodes) == 0:
        current_node = nodes.popleft()
        if g.value_at(*current_node) == value_to_find and current_node not in found_area:
            found_area.add(current_node)
            nodes_seen.append(current_node)
            look_at = [(-1, 0), (0, -1), (1, 0), (0,1)]
            for dir in look_at:
                new_dir = tuple(map(operator.add, current_node, dir))
                nodes.append(new_dir)

    return found_area

areas = []
while g.scan():
    if g.current_pos() not in nodes_seen:
        area = flood_fill(g.current_pos())
        areas.append(area) 

def find_edge_total(nodes):
    crop = g.value_at(*nodes[0])
    edges = []
    for n in nodes:
        look_at = [(-1, 0), (0, -1), (1, 0), (0,1)]
        for dir in look_at:
            new_dir = tuple(map(operator.add, n, dir))
            if g.value_at(*new_dir) != crop:
                edges.append(new_dir)
    return len(edges)

total = 0
for a in areas:
    edges = find_edge_total(list(a))
    total += len(a) * edges

print(total)
