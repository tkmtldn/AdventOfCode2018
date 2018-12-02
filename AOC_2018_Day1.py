"""Solution to Advent of Code 2018, Day 1: Chronal Calibration (https://adventofcode.com/2018/day/1)."""

santa = []
with open('santa2018.txt', 'r') as aoc:
    for i in aoc.readlines():
        santa.append(int(i))


def solution_1(santa):
    return sum(santa)

def solution_2(santa):
    count = 0
    attempts = set()
    t = 0
    while True:
        count += int(santa[t % len(santa)])
        t += 1
        if count in attempts:
            return count
        attempts.add(count)

if __name__ == '__main__':
    print(solution_1(santa))
    print(solution_2(santa))