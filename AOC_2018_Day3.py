"""Solution to Advent of Code 2018, Day 3: No Matter How You Slice It (https://adventofcode.com/2018/day/3)."""
import re

santa = []
with open('santa2018.txt', 'r') as aoc:
    for i in aoc.readlines():
        abc = re.findall(r'(\d+,\d+):.(\d+x\d+)', i)
        a, b = abc[0][0].split(',')
        c, d = abc[0][1].split('x')
        santa.append([int(a), int(b), int(c), int(d)])

smap = [[0 for i in range(1000)] for j in range(1000)]
for t in santa:
    for x in range(t[0], t[0] + t[2]):
        for y in range(t[1], t[1] + t[3]):
            smap[x][y] += 1

def solution1(smap):
    ans = 0
    for row in smap:
        for column in row:
            if column > 1:
                ans += 1
    return ans

def solution2(santa, smap):
    ans = 0
    for t in santa:
        mark = True
        for x in range(t[0], t[0]+t[2]):
            for y in range(t[1], t[1]+t[3]):
                if smap[x][y] >1:
                    mark = False
        if mark:
            ans = santa.index(t)+1
    return ans

if __name__ == '__main__':
    print(solution1(smap))
    print(solution2(santa, smap))