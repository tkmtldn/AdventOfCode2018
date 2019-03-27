# https://adventofcode.com/2018/day/10

import re

tries = 10730 #I tried 20000, but try #10727 was the best (so, the answer on question 2 is # of our best try)

with open("santa2018.txt", 'r+') as st:
    stt = [l.rstrip('n') for l in st]
    stt =[[int(i) for i in re.findall(r'-?\d+', l)] for l in stt]

val = {}
ans = []
ansx = []
ansy = []
for i in range(tries):
    minx = min(x + i * vx for (x, y, vx, vy) in stt)
    maxx = max(x + i * vx for (x, y, vx, vy) in stt)
    miny = min(y + i * vy for (x, y, vx, vy) in stt)
    maxy = max(y + i * vy for (x, y, vx, vy) in stt)
    val[i] = (maxx - minx + maxy - miny)
    if i == 10727:
        print(minx, maxx, miny, maxy)
        for (x, y, vx, vy) in stt:
            x = x + i * vx
            y = y + i * vy
            ans.append([x,y])
            ansx.append(x)
            ansy.append(y)

for k,v in val.items():
    if v == min(val.values()):
        print(k, v)


mapa = [[' ' for x in range(200)] for y in range(200)]
for element in ans:
    mapa[element[1]][element[0]] = '#'
for x in range (0,200):
    for y in range(0,200):
        if y not in ansx:
            mapa[x][y] = '*'
        if x not in ansy:
            mapa[x][y] = '*'

for t in mapa:
    line = ''.join(t)
    line = line.replace('*',' ')
    print(line)
