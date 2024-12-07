import sys
import itertools
rows = []
total = 0
with open(sys.argv[1]) as f:
    for line in f:
        (result, values) = line.strip().split(':')
        values = [int(x) for x in values.split()]
        result = int(result)
        rows.append((int(result), values))

ops = ['+', '*']
for row in rows:
    ops_for_row = []
    (result, values) = row
    ops_combos = list(itertools.product(ops, repeat=len(values) -1))
    for c in ops_combos:
        iter_val = values[0]
        c_idx = 0
        for i in range(1, len(values)):
            if c[c_idx] == "+":
                iter_val += values[i]
            else:
                iter_val *= values[i]
            c_idx += 1

        if iter_val == result:
            total += result
            break

print(total)
