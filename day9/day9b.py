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
files = {}
gaps = [] 
d_idx = 0
for i in range(len(file_sizes)):
    files[i] = (file_sizes[i], d_idx)
    for j in range(file_sizes[i]):
        disk.append(i)
        d_idx += 1
    if len(free_space_blocks) > 0:
        space = free_space_blocks.popleft()
        if space > 0:
            gaps.append((space, d_idx))
        for j in range(space):
            disk.append('.')
            d_idx += 1

for f in range(len(files) - 1, -1, -1):
    length, f_location = files[f]
    for g_idx in range(len(gaps)):
        (g_size, g_location) = gaps[g_idx]
        if length <= g_size and g_location < f_location:
            for i in range(g_location, g_location + length):
                disk[i] = f
            for i in range(f_location, f_location + length):
                disk[i] = '.'
            if length == g_size:
                del gaps[g_idx]
            else:
                gaps[g_idx] = (g_size - length, g_location + length)
            break



total = 0
for i in range(len(disk)):
    if disk[i] == '.':
        continue

    total += i * disk[i]

print(total)
