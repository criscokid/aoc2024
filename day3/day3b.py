import sys
import re

mul_instruction = r"(mul\(\d+,\d+\)|don't\(\)|do\(\))"
data = ""
with open(sys.argv[1]) as f:
   data = f.read()

matches = re.findall(mul_instruction, data)
print(matches)

sum = 0
should_mul = True
for m in matches:
   if m[0:2] == "mu" and should_mul:
      numbers = re.findall(r"\d+", m)
      values = [int(x) for x in numbers]
      sum += values[0] * values[1]
      continue

   if m[0:3] == "don":
      should_mul = False
      continue
   
   if m[0:3] == "do(":
      should_mul = True

print(sum)
