area = []

with open('santa2018.txt', 'r') as sp:
    for i in sp.readlines():
        i = i.replace('.','1').replace('|','2').replace('#','3')
        area.append(list(i.strip()))


def area_modifier(area):
    new_area = []
    area_len = len(area)
    for i in range(area_len):
        row = []
        for j in range(area_len):
            current = area[i][j]
            neighbours = ''
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    if (x<0 or x>=area_len) or (y<0 or y>=area_len) or (x==i and y==j):
                        pass
                    else:
                        neighbours+=area[x][y]
            if current == '1':
                if neighbours.count('2') >=3:
                    current = '2'
            elif current == '2':
                if neighbours.count('3') >=3:
                    current = '3'
            else:
                if neighbours.count('2') >=1 and neighbours.count('3') >=1:
                    pass
                else:
                    current = '1'
            row.append(current)
        new_area.append(row)
    return(new_area)

def area_counter(area):
    wooded = 0
    lumber = 0
    for x in range(len(area)):
        for y in range(len(area)):
            if area[x][y] == '2':
                wooded +=1
            if area[x][y] == '3':
                lumber +=1
    return wooded*lumber

def part_1(area):
    for i in range(10):
        area = area_modifier(area)
    return area_counter(area)

def part_2(area):
    visual = {}
    visual_2 = {}
    i = 0
    while True:
        area = area_modifier(area)
        c = area_counter(area)
        if c in visual.values():
            if c in visual_2.values():
                break
            visual_2[i] = c
        else:
            visual_2 = {}
        visual[i] = c
        i += 1
    a = next(iter(visual_2))
    pos = (1000000000 - a)%(i-a)
    return visual_2[a+pos-1]

print(part_1(area))
print(part_2(area))