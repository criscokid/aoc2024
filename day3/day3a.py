import sys
import re

mul_instruction = r"(mul\(\d+,\d+\))"
data = ""
with open(sys.argv[1]) as f:
   data = f.read()

matches = re.findall(mul_instruction, data)
print(matches)

sum = 0
for m in matches:
    numbers = re.findall(r"\d+", m)
    values = [int(x) for x in numbers]
    sum += values[0] * values[1]

print(sum)
