import re
from collections import defaultdict

with open('santa2018.txt') as file:
    data=list(file)

def distance(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])

nanobots = [tuple(map(int, list(re.findall(r'-?\d+', ln)))) for ln in data]

strongest_rad = max(r for (x,y,z,r) in nanobots)
strongest = [b for b in nanobots if b[3]==strongest_rad][0]

print(sum(1 for a in nanobots if distance(a, strongest) <= strongest_rad))

# dist = defaultdict(int)
# for i in nanobots:
#     a = sum(i[0:3])
#     a_min = a-i[3]
#     a_max = a+i[3]+1
#     print(a_min,a_max)
#     for j in range(a_min,a_max):
#         dist[j] +=1
#
# print(max(dist, key=dist.get))


