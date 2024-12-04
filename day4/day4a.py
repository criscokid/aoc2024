import sys
import re

sys.path.append('..')
from grid import TextGrid

xmas_re = r"XMAS"

g = TextGrid()
with open(sys.argv[1]) as f:
    for line in f:
        g.add_row(list(line.strip()))


g.print()

search_strings = []
search_strings.extend([''.join(x) for x in g.rows()])
search_strings.extend([''.join(x) for x in g.cols()])
for i in range(1, g.row_count()):
    x = i
    y = 0
    diag_vals = []
    while x < g.col_count() and y < g.row_count():
        diag_vals.append(g.value_at(x, y))
        x += 1
        y += 1
    search_strings.append(''.join(diag_vals))

for i in range(g.col_count()):
    x = 0
    y = i
    diag_vals = []
    while x < g.col_count() and y < g.row_count():
        diag_vals.append(g.value_at(x, y))
        x += 1
        y += 1
    search_strings.append(''.join(diag_vals))

for i in range(g.row_count()):
    x = g.col_count() - 1
    y = i
    diag_vals = []
    while x >= 0 and y < g.row_count():
        diag_vals.append(g.value_at(x, y))
        x -= 1
        y += 1
    search_strings.append(''.join(diag_vals))


for i in range(g.col_count() - 1, -1, -1):
    x = 0
    y = i
    diag_vals = []
    while x < g.col_count() and y >= 0:
        diag_vals.append(g.value_at(x, y))
        x += 1
        y -= 1
    search_strings.append(''.join(diag_vals))

total_xmas = 0
for r in [x for x in search_strings if len(x) > 3]:
    total_xmas += len(re.findall(xmas_re, r))
    total_xmas += len(re.findall(xmas_re, r[::-1]))
print(total_xmas)
