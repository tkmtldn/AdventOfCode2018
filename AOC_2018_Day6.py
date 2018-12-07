"""Solution to Advent of Code 2018, Day 6 (https://adventofcode.com/2018/day/6)."""

nb = 360
matrix = [[[] for i in range(nb)] for j in range(nb)]

with open('santa2018.txt', 'r') as aoc:
    ex = aoc.read()
for line in ex.split('\n'):
    a = line.split(', ')
    x, y = int(a[0]), int(a[1])
    for j in range(nb):
        for i in range(nb):
            matrix[i][j].append(abs(x-j)+abs(y-i))

count_area = 0

for i in range(len(matrix)):
    for j in range(len(matrix)):
        min_c = min(matrix[i][j])
        if sum(matrix[i][j]) < 10000:
            count_area +=1
        if matrix[i][j].count(min_c) >1:
            matrix[i][j] = 99
        else:
            matrix[i][j] = matrix[i][j].index(min_c)

borders = {}
for i in matrix[0]:
    if i not in borders.keys():
        borders[i] = 0
for i in matrix[-1]:
    if i not in borders.keys():
        borders[i] = 0
for j in range (1, len(matrix)-1):
    if matrix[j][0] not in borders.keys():
        borders[matrix[j][0]] = 0
    if matrix[j][-1] not in borders.keys():
        borders[matrix[j][0]] = 0

d={}
for element in matrix:
    for i in element:
        d[i] = d.get(i, 0) + 1
d2 = {}
for k, v in d.items():
    if k not in borders:
        d2[k] = v

if __name__ == '__main__':
    print(d2[max(d2, key=d2.get)])
    print(count_area)