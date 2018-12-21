import time

puzzle_map = []
our_length = 148
with open('santa2018.txt', 'r') as stxt:
    rows = stxt.read().split("\n")
    for row in rows:
        row = [[i] for i in row.replace(' ','.').replace('\\', ')')]
        if len(row) < our_length:
            for k in range(our_length - len(row)):
                row.append(['.'])
        puzzle_map.append(row)

positions = set()
carts = []
dirs = '<^>v'

for i in range(len(puzzle_map)):
    for j in range(len(puzzle_map[3])):
        if (puzzle_map[i][j][0]) in dirs:
            carts.append((puzzle_map[i][j][0], 0, i, j))
            positions.add((i, j))

def move(puzzle_map, direction, junction, x, y):
    if direction == '<':
        next_pos = puzzle_map[x][y - 1][0]
        y -= 1
    elif direction == '^':
        next_pos = puzzle_map[x - 1][y][0]
        x -= 1
    elif direction == '>':
        next_pos = puzzle_map[x][y + 1][0]
        y += 1
    else:
        next_pos = puzzle_map[x + 1][y][0]
        x += 1
    if next_pos == '+':
        if junction % 3 == 0:
            direction = dirs[(dirs.index(direction) - 1) % 4]
            return (direction, junction + 1, x, y)
        elif junction % 3 == 1:
            return (direction, junction + 1, x, y)
        elif junction % 3 == 2:
            direction = dirs[(dirs.index(direction) + 1) % 4]
            return (direction, junction + 1, x, y)
        else:
            print('wrong junction')
    elif next_pos == '/':
        if direction == '<':
            direction = 'v'
        elif direction == '^':
            direction = '>'
        elif direction == '>':
            direction = '^'
        else:
            direction = '<'
    elif next_pos == ')':
        if direction == '<':
            direction = '^'
        elif direction == '^':
            direction = '<'
        elif direction == '>':
            direction = 'v'
        else:
            direction = '>'
    return (direction, junction, x, y)

#solution1
# m = True
# curr = []
# while m:
#     for i in range(len(carts)):
#         carts[i] = move(puzzle_map, carts[i][0], carts[i][1], carts[i][2], carts[i][3])
#         this = (carts[i][3], carts[i][2])
#         if this in curr:
#             print("Solution 1:", this)
#             m = False
#         curr.append(this)
#         if len(curr) > len(carts):
#             del curr[0]

#solution2
# carts_dict = {}
# range_dict = {}
active_carts = [n for n in range(len(carts))]
while len(active_carts) != 1:
    positions_after_turn = dict()
    this_turn = []
    to_remove = []
    for i in active_carts:
        carts[i] = move(puzzle_map, carts[i][0], carts[i][1], carts[i][2], carts[i][3])
        current_move = (carts[i][3], carts[i][2])
        positions_after_turn[i] = current_move
        if current_move in this_turn:
            to_remove.append(current_move)
        this_turn.append(current_move)
    if to_remove:
        for e in to_remove:
            for k, v in positions_after_turn.items():
                if v == e:
                    active_carts.remove(k)
print(positions_after_turn[active_carts[0]])
