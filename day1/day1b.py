import re
left = []
right = []

with open("input1.txt") as f:
    for line in f:
        parts = [int(x) for x in line.strip("\n").split()]
        left.append(parts[0])
        right.append(parts[1])

left.sort()
right.sort()

sum = 0
occurences = {}

for r in right:
    if r in occurences:
        occurences[r] += 1
    else:
        occurences[r] = 1

for l in left:
    score = 0
    if l in occurences:
        score = l * occurences[l]
    sum += score

print(sum)
