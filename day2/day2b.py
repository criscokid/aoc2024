def getDirection(report):
    direction = 0
    if report[0] > report[1]:
        direction = -1
    else:
        direction = 1
    return direction

def testDirection(a, b, direction):
    if direction == -1:
        return a > b
    else:
        return b > a

def testChange(a, b):
    delta = abs(a-b)
    return delta <= 3 and delta >=1

def testAll(r):
    d = getDirection(r)
    for i in range(0, len(r)):
        if len(r) - 1 == i:
            break

        directionResult = testDirection(r[i], r[i+1], d)
        changeResult = testChange(r[i], r[i+1])
        # print(f"d:{directionResult}, c:{changeResult}")
        if not directionResult or not changeResult:
            return False
    return True

reports = []
with open("input1.txt") as f:
    for line in f:
        parts = [int(x) for x in line.strip("\n").split()]
        reports.append(parts)

safe = 0

for r in reports:
    result = testAll(r)
    if result:
        safe +=1
        continue
    
    for i in range(0, len(r)):
        result = testAll([x for idx, x in enumerate(r) if idx != i])
        if result:
            safe += 1
            break
print(safe)

