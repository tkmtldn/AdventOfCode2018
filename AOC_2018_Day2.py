"""Solution to Advent of Code 2018, Day 2: Inventory Management System (https://adventofcode.com/2018/day/2)."""

santa = []
with open('santa2018.txt', 'r') as aoc:
    for i in aoc.readlines():
        santa.append(i)


def solution_1(santa):
    count2, count3 = 0, 0
    for element in santa:
        santa_letters = {}
        for i in element:
            santa_letters[i] = element.count(i)
        count2 += 1 if 2 in santa_letters.values() else 0
        count3 += 1 if 3 in santa_letters.values() else 0
    return (count2 * count3)


def solution_2(santa):
    santa.sort()
    santa_dict = {}
    for i in range (len(santa)-1):
        common, word = 0, ''
        for j in range(26):
            if santa[i][j] == santa[i+1][j]:
                common +=1
                word += santa[i][j]
        santa_dict[(word, santa[i], santa[i+1])] = common
    santa_value = max(santa_dict, key=santa_dict.get)
    return santa_value[0]


if __name__ == '__main__':
    print(solution_1(santa))
    print(solution_2(santa))