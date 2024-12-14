import sys
from dataclasses import dataclass, field
import numpy as np

@dataclass
class Button:
    x: int = 0
    y: int = 0

@dataclass
class Game:
    total_x: int = 0
    total_y: int = 0
    button_a: Button = field(default_factory=Button)
    button_b: Button = field(default_factory=Button)

games = []
g = Game()
with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith("Button A:"):
            parts = line.strip().split()
            x = int(parts[2].replace("X+", "").replace(",", ""))
            y = int(parts[3].replace("Y+", ""))
            g.button_a = Button(x, y)
        if line.startswith("Button B:"):
            parts = line.strip().split()
            x = int(parts[2].replace("X+", "").replace(",", ""))
            y = int(parts[3].replace("Y+", ""))
            g.button_b = Button(x, y)
        if line.startswith("Prize"):
            parts = line.strip().split()
            x = int(parts[1].replace(",", "").replace("X=", ""))
            y = int(parts[2].replace("Y=", ""))
            g.total_x = x
            g.total_y = y
        if line.strip() == '':
            games.append(g)
            g = Game()
            continue
games.append(g)


total = 0
for g in games:
    buttons = [[g.button_a.x, g.button_b.x], [g.button_a.y, g.button_b.y]]
    n_a, n_b = np.linalg.solve(buttons, [g.total_x, g.total_y])
    if np.isclose(n_a, round(n_a)) and np.isclose(n_b, round(n_b)):
        total += round(n_a) * 3 + round(n_b)

print(total)
