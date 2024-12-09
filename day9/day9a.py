import sys
from collections import deque

input = []
with open(sys.argv[1]) as f:
    input = [int(x) for x in list(f.read().strip())]

file_sizes = []
free_space_blocks = []

for i in range(len(input)):
    if i % 2 == 0:
        file_sizes.append(input[i])
    else:
        free_space_blocks.append(input[i])
disk = []
free_space_blocks = deque(free_space_blocks)

for i in range(len(file_sizes)):
    for j in range(file_sizes[i]):
        disk.append(i)
    if len(free_space_blocks) > 0:
        for j in range(free_space_blocks.popleft()):
            disk.append(-1)

r_idx = len(disk) - 1

for i in range(len(disk)):
    if r_idx == i:
        break
    while disk[r_idx] == -1:
        r_idx -= 1
    if disk[i] == -1:
        disk[i], disk[r_idx] = disk[r_idx], disk[i]
        r_idx -= 1

total = 0
for i in range(len(disk)):
    if disk[i] == -1:
        break

    total += i * disk[i]

print(total)
