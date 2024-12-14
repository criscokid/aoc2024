import sys
import re
import numpy as np
from PIL import Image

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

quads = {1: 0, 2: 0, 3: 0, 4: 0}

def move_bot(x_pos, y_pos, move_x, move_y):
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
    return (x_pos, y_pos)


for j in range(10000):
    pixels = np.zeros((board_x, board_y, 3), dtype=np.uint8)
    for i in range(len(bots)):
        (x_pos, y_pos, move_x, move_y) = bots[i]
        (x_pos, y_pos) = move_bot(x_pos, y_pos, move_x, move_y)
        pixels[x_pos, y_pos] = [0, 255, 0]
        bots[i] = (x_pos, y_pos, move_x, move_y)

    img = Image.fromarray(pixels)
    img.save(f"images/{j}.png")

    
