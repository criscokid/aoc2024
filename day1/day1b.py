import re
left = []
right = []

with open("input1.txt") as f:
    for line in f:
        parts = re.split(r'\s+', line.strip("\n"))
        left.append(int(parts[0]))
        right.append(int(parts[1]))

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