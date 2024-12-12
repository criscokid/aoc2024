import sys
import math
import functools

values = []

with open(sys.argv[1]) as f:
        values = [int(x) for x in f.read().strip("\n").split()]

def numDigits(n):
    return int(math.log10(n)) + 1    

@functools.lru_cache(maxsize=None)
def process(val, iteration = 25):
    if iteration == 0:
        return 1

    if val == 0:
        return process(1, iteration - 1)
     
    elif numDigits(val) % 2 == 0:
        str_value = str(val)
        midPoint = len(str_value)//2
        left = int(str_value[0:midPoint])
        right = int(str_value[midPoint:])
        t = process(left, iteration - 1)
        t += process(right, iteration - 1)
        return t
    else:
        return process(val * 2024, iteration - 1)

total = 0
for v in values:
    total += process(v, 75)
print(total)

