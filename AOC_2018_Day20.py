with open('santa2018.txt', 'r') as f:
    route = f.read()
    rx = route[1:]

directions = {'S': -1j ,'E': 1 ,'N': 1j ,'W': -1}

def builing_map(r, map={0:0}, pos=0, level=0):
    x_pos = pos
    x_level = level
    for element in r:
        if element in directions:
            pos += directions[element]
            if pos in map:
                level = map[pos]
            else:
                level += 1
                map[pos] = level
        elif element == '|':
            pos = x_pos
            level = x_level
        elif element == '(':
            builing_map(r, map, pos, level)
        elif element == ')':
            return
        else:
            print(map)
            return map

map = builing_map(iter(rx))

print(max(map.values()))
print(sum(1 for n in map.values() if n >= 1000))