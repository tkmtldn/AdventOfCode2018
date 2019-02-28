depth = 9465
target = (13, 704)

def part_1(depth, target):
    sum = 0
    geo_index = {}
    for x in range(target[0]+1):
        for y in range(target[1]+1):
            if (x , y) in [(0,0), target]:
                geo = 0
            elif y==0:
                geo = x*16807
            elif x==0:
                geo = y*48271
            else:
                geo = geo_index[(x-1,y)][1] * geo_index[(x,y-1)][1]
            ero = (geo + depth) % 20183
            sum += ero % 3
            geo_index[(x, y)] = (geo, ero)
    return sum

if __name__ == "__main__":
    print(part_1(depth, target))
