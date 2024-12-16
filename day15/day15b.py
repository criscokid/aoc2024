import sys
import operator

sys.path.append('..')
from day15.day15a import can_move_in_dir
from grid import TextGrid
g = TextGrid()

dirs = {'^': (0, -1), '>': (1, 0), "v": (0, 1), "<": (-1, 0)}
reverse_dir = {(0, -1): '^', (1, 0): '>', (0, 1): "v", (-1, 0): "<"}

path = []


def line_expansion(line):
    new_line = []
    for c in line:
        if c == '#':
            new_line.extend(['#', '#'])
        elif c == 'O':
            new_line.extend(['[', ']'])
        elif c == '.':
            new_line.extend(['.', '.'])
        else:
            new_line.extend(['@', '.'])
    return new_line


grid = True
with open(sys.argv[1]) as f:
    for line in f:
        if line.strip() == "":
            grid = False

        parts = list(line.strip("\n"))
        if grid:
            parts = list(line.strip("\n"))
            g.add_row(line_expansion(parts))
        else:
            for p in parts:
                path.append(dirs[p])
g.print()

def can_box_move_in_dir(pos, dir):
    #left: we would be on the right side of the box
    if dir == (-1, 0):
        current_pos = pos
        current_val = g.value_at(*current_pos)
        while current_val != '#':
            current_pos = tuple(map(operator.add, (-2, 0), current_pos))
            current_val = g.value_at(*current_pos)
            if current_val == '.':
                return True
        return False

    #move right, we hit the left sid eof the box
    if dir == (1, 0):
        current_pos = pos
        current_val = g.value_at(*current_pos)
        while current_val != '#':
            current_pos = tuple(map(operator.add, (2, 0), current_pos))
            current_val = g.value_at(*current_pos)
            if current_val == '.':
                return True
        return False
    #up and down, we have to check y above both boxes
    (pos_x, pos_y) = pos
    (dir_x, dir_y) = dir
    value_at_pos = g.value_at(*pos)
    new_left_x_pos = new_right_x_pos = 0
    new_y_pos = pos_y + dir_y
    if value_at_pos == '[':
        new_left_x_pos = pos_x + dir_x
        new_right_x_pos = pos_x + dir_x + 1
    else:
        new_left_x_pos = pos_x + dir_x
        new_right_x_pos = pos_x + dir_x - 1
    if g.value_at(new_left_x_pos, new_y_pos) == '.' and g.value_at(new_right_x_pos, new_y_pos) == '.':
        return True
    if g.value_at(new_left_x_pos, new_y_pos) == '#' and g.value_at(new_right_x_pos, new_y_pos) == '#':
        return False
    left_check = None
    right_check = None
    if g.value_at(new_left_x_pos, new_y_pos) == '.':
        left_check = True 
    else:
        left_check = can_box_move_in_dir((new_left_x_pos, new_y_pos), dir)
    if g.value_at(new_right_x_pos, new_y_pos) == '.':
        right_check = True
    else:
        right_check = can_box_move_in_dir((new_right_x_pos, new_y_pos), dir)
    return left_check and right_check

def box_move_in_dir(pos, dir):
    if can_box_move_in_dir(pos, dir):
        if dir == (-1, 0):
            left_side = tuple(map(operator.add, (-2, 0), pos))
            right_side = tuple(map(operator.add, (-1, 0), pos))

            if g.value_at(*left_side) == ']':
                box_move_in_dir(left_side, dir)
            g.set_value_at(left_side[0], left_side[1], '[')
            g.set_value_at(right_side[0], right_side[1], ']')
            g.set_value_at(pos[0], pos[1], '.')
            return
        if dir == (1, 0):
            left_side = tuple(map(operator.add, (1, 0), pos))
            right_side = tuple(map(operator.add, (2, 0), pos))

            if g.value_at(*right_side) == '[':
                box_move_in_dir(right_side, dir)
            g.set_value_at(left_side[0], left_side[1], '[')
            g.set_value_at(right_side[0], right_side[1], ']')
            g.set_value_at(pos[0], pos[1], '.')
            return

        value_at_pos = g.value_at(*pos)
        left_side = None
        right_side = None
        current_left_side = None
        current_right_side = None
        if value_at_pos == '[':
            left_side = tuple(map(operator.add, pos, dir))
            right_side = tuple(map(operator.add, (pos[0] + 1, pos[1]), dir))
            current_left_side = pos
            current_right_side = (pos[0] + 1, pos[1])
        else:
            left_side = tuple(map(operator.add, (pos[0] - 1, pos[1]), dir))
            right_side = tuple(map(operator.add, pos, dir))
            current_left_side = (pos[0] - 1, pos[1])
            current_right_side = pos 
        
        if g.value_at(*left_side) in ['[', ']']:
            box_move_in_dir(left_side, dir)
        if g.value_at(*right_side) in ['[', ']']:
            box_move_in_dir(right_side, dir)

        g.set_value_at(left_side[0], left_side[1], '[')
        g.set_value_at(right_side[0], right_side[1], ']')
        g.set_value_at(current_left_side[0], current_left_side[1], '.')
        g.set_value_at(current_right_side[0], current_right_side[1], '.')

    
        
def move_in_dir(pos, dir):
    (pos_x, pos_y) = pos
    (dir_x, dir_y) = dir
    new_pos_x = pos_x + dir_x
    new_pos_y = pos_y + dir_y
    box_moved = False

    if new_pos_x < 0 or new_pos_x >= g.col_count() or new_pos_y < 0 or new_pos_y >= g.row_count():
        return (False, box_moved)

    if g.value_at(new_pos_x, new_pos_y) == "#":
        return (False, box_moved)

    if g.value_at(new_pos_x, new_pos_y) in ['[', ']']:
        box_move_in_dir((new_pos_x, new_pos_y), dir)
        box_moved = True

    if g.value_at(new_pos_x, new_pos_y) == ".":
        old_value = g.value_at(pos_x, pos_y)
        g.set_value_at(pos_x, pos_y, ".")
        g.set_value_at(new_pos_x, new_pos_y, old_value)
        return (True, box_moved)

    return (False, box_moved)

g.scan_until('@')
current_pos = g.current_pos()
i = 1
#problem at step 310
for p in path:
    print(i, reverse_dir[p])
    i+=1
    (success, moved_box) = move_in_dir(current_pos, p)
    if success:
        current_pos = tuple(map(operator.add, current_pos, p))
    g.print()
    if moved_box:
        input()

g.move_to_pos(-1, 0)

total = 0
while g.scan_until('['):
    (x, y) = g.current_pos()
    total += y * 100 + x

print(total)
