https://adventofcode.com/2018/day/11

n = 300
serial = 2866


mapa = [[0 for x in range(n)] for y in range(n)]
for i in range(n):
    for j in range(n):
        rack = i+11
        mapa[i][j] = int(str((rack*(j+1)+serial)*rack)[-3])-5


def solution1(mapa, n):
    max_power = 0
    coord_x, coord_y = 0, 0
    for i in range(n-2):
        for j in range(n-2):
            sum = mapa[i][j]+mapa[i][j+1]+mapa[i][j+2]+mapa[i+1][j]+mapa[i+1][j+1]+mapa[i+1][j+2]+mapa[i+2][j]+mapa[i+2][j+1]+mapa[i+2][j+2]
            if sum > max_power:
                max_power = sum
                coord_x = i + 1
                coord_y = j + 1
    return coord_x, coord_y

def solution2(mapa):
    max_power = 0
    coord_x, coord_y, coord_k = 0, 0, 0
    k = 3
    # assume k is not greater than 10
    while k < 10:
        for i in range(n + 1 - k):
            for j in range(n + 1 - k):
                sum = 0
                for row in range(k):
                    for column in range(k):
                        sum += mapa[i + row][j + column]
                if sum > max_power:
                    max_power = sum
                    coord_x = i + 1
                    coord_y = j + 1
                    coord_k = k
        k += 1
    return coord_x, coord_y, coord_k

print(solution1(mapa, n))
print(solution2(mapa))
