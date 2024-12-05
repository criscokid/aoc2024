import sys
import math

rules = {}
data = []

ruleSection =  True
with open(sys.argv[1]) as f:
    for line in f:
        if line.strip() == "":
            ruleSection = False
            continue

        if ruleSection:
            parts = [int(x) for x in line.strip().split('|')]
            if parts[0] in rules:
                rules[parts[0]].append(parts[1])
            else:
                rules[parts[0]] = [parts[1]]
        else:
            parts = [int(x) for x in line.strip().split(',')]
            data.append(parts)
for k in rules.keys():
    rules[k].sort()


valids = []

for line in data:
    valid = True
    for i in range(len(line)):
        if not valid:
            break
        current_page = line[i]
        if current_page in rules:
            for j in range(i, -1, -1):
                if line[j] in rules[current_page]:
                    valid = False
                    break
    if valid:
        valids.append(line)

print(valids)
sum = 0
for v in valids:
    mid = (len(v) - 1)/2
    sum += v[math.floor(mid)]

print(sum)





