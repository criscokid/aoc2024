import sys
import re

bots = []
with open(sys.argv[1]) as f:
    for line in f:
        parts = re.findall(r"([\d-]+)", line.strip())
        parts = [int(x) for x in parts]
        bots.append(tuple(parts))

board_x = int(sys.argv[2])
board_y = int(sys.argv[3])

mid_x = int(board_x / 2 - 0.5)
mid_y = int(board_y / 2 - 0.5)
print("mid points", mid_x, mid_y)

quads = {1: 0, 2: 0, 3: 0, 4: 0}
for bot in bots:
    (x_pos, y_pos, move_x, move_y) = bot
    for i in range(100):
        x_pos += move_x
        if(x_pos >= board_x):
            x_pos = (x_pos - board_x)
        if(x_pos < 0):
            x_pos = board_x + x_pos
        y_pos += move_y
        if(y_pos >= board_y):
            y_pos = (y_pos - board_y)
        if(y_pos < 0):
            y_pos = board_y + y_pos
    if(x_pos < mid_x and y_pos < mid_y):
        quads[1] += 1
    elif(x_pos > mid_x and y_pos < mid_y):
        quads[2] += 1
    elif(x_pos < mid_x and y_pos > mid_y):
        quads[3] += 1
    elif(x_pos > mid_x and y_pos > mid_y):
        quads[4] += 1
total = 1
for v in quads.values():
    total *= v

print(total)



