import re
left = []
right = []

with open("input1.txt") as f:
    for line in f:
        parts = line.strip("\n").split()
        left.append(int(parts[0]))
        right.append(int(parts[1]))

left.sort()
right.sort()

sum = 0
for idx, l in enumerate(left):
    r = right[idx]
    sum += abs(l-r)

print(sum)
