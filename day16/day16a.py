import operator
import sys

sys.path.append('..')
from grid import TextGrid
g = TextGrid()
from collections import deque
dirs = {(0, -1), (1, 0), (0, 1), (-1, 0)}
path = []

with open(sys.argv[1]) as f:
    for line in f:
        g.add_row(list(line.strip()))

g.print()

g.scan_until('S')
nodes = deque()
nodes.append((g.current_pos(), (1,0), 0, []))
totals = []


def get_possible_turns(current_pos, seen_nodes):
    avaliable_dirs = []
    for d in dirs:
        test_pos = tuple(map(operator.add, current_pos, d))
        if g.value_at(*test_pos) in ['.', 'E'] and test_pos not in seen_nodes:
            avaliable_dirs.append(d)

    return avaliable_dirs

while len(nodes) > 0:
    current_node = nodes.popleft()
    (current_pos, current_dir, current_total, seen_nodes) = current_node

    if g.value_at(*current_pos) == 'E':
        totals.append(current_total)
        continue

    if current_pos in seen_nodes:
        continue


    possible_dirs = get_possible_turns(current_pos, seen_nodes)

    if len(possible_dirs) == 0:
        continue

    seen_nodes.append(current_pos)

    for d in possible_dirs:
        next_pos = tuple(map(operator.add, current_pos, d))
        additional_cost =  1 if d == current_dir else 1001
        nodes.append((next_pos, d, current_total + additional_cost, seen_nodes))
print()
g.print()
print(min(totals))
