
with open("input1.txt") as f:
    for line in f:
        parts = [int(x) for x in line.strip("\n").split()]
        left.append(parts[0])
        right.append(parts[1])


