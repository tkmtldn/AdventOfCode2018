"""Solution to Advent of Code 2018, Day 5 (https://adventofcode.com/2018/day/5)."""

with open('santa2018.txt', 'r') as aoc:
    ex = aoc.read()

def react(ex):
    num = 0
    while num < len(ex)-1:
        if ex[num].lower() == ex[num+1].lower() and ex[num] != ex[num+1]:
            ex=ex[:num]+ex[num+2:]
        else:
            num +=1
    return ex

def solution1(ex):
    while 1:
        a = len(ex)
        ex = react(ex)
        if a == len(ex):
            break
        react(ex)
    return len(ex)

def reacted2(element, ex):
    data = ex.replace(element, '').replace(element.upper(), '')
    return solution1(data)

def solution2(ex):
    alph = 'qwertyuiopasdfghjklzxcvbnm'
    min = 50000
    for element in alph:
        ans = reacted2(element, ex)
        if ans < min:
            min = ans
    return min

if __name__ == '__main__':
    print(solution1(ex))
    print(solution2(ex))