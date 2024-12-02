import sys

with open(sys.argv[1]) as f:
    for line in f:
        parts = [int(x) for x in line.strip("\n").split()]

