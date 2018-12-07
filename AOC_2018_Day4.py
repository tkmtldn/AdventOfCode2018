"""Solution to Advent of Code 2018, Day 4 (https://adventofcode.com/2018/day/4)."""

import re
from datetime import datetime

santa = []
with open('santa2018.txt', 'r') as aoc:
    for i in aoc.readlines():
        x = re.search('\[(.*)\](.*)', i)
        timestamp = datetime.strptime(x.group(1), '%Y-%m-%d %H:%M')
        santa.append([timestamp, x.group(2).strip()])
santa.sort()

def solution(santa):
    gtime = {}
    gtime_shifts = {}

    for i in santa:
        x = i[-1].split()
        if x[0] == 'Guard':
            current_guard = x[1]
            gtime_shifts[current_guard] = gtime_shifts.get(current_guard, [0 for k in range(60)])
        elif x[0] == 'falls':
            begin = i[0].time().minute
        elif x[0] == 'wakes':
            sleep = i[0].time().minute
            sleep_min = sleep - begin
            gtime[current_guard] = gtime.get(current_guard, 0) + sleep_min
            for i in range(begin,sleep):
                gtime_shifts[current_guard][i] +=1

    guard_max = max(gtime, key=gtime.get)
    answer1 = int(guard_max[1:]) * gtime_shifts[guard_max].index(max(gtime_shifts[guard_max]))

    max_of_max = 0
    for k, v in gtime_shifts.items():
        for i in v:
            if i > max_of_max:
                max_of_max = i
                guard_of_max = k
    answer2 = int(guard_of_max[1:]) * gtime_shifts[guard_of_max].index(max(gtime_shifts[guard_of_max]))

    return answer1, answer2

if __name__ == '__main__':
    print(solution(santa))