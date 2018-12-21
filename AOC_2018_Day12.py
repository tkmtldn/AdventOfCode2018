st = '##.##..#.#....#.##...###.##.#.#..###.#....##.###.#..###...#.##.#...#.#####.###.##..#######.####..#'
s = '''.##.. => #
#...# => .
####. => #
##..# => #
..##. => .
.###. => .
..#.# => .
##### => .
##.#. => #
...## => #
.#.#. => .
##.## => #
#.##. => .
#.... => .
#..## => .
..#.. => #
.#..# => #
.#.## => #
...#. => .
.#... => #
###.# => #
#..#. => #
.#### => #
#.### => #
.##.# => #
#.#.. => .
###.. => #
..... => .
##... => .
....# => .
#.#.# => #
..### => #
'''
lines = s.splitlines()
next = {}
for i in range(len(lines)):
    a = lines[i].split()[0]
    b = lines[i].split()[2]
    next[a] = b

def sum_plants(ans):
    ans = ans[2:]
    sum = 0
    for x in range(len(ans)):
        if ans[x] == '#':
            sum += x
    return sum


generations_number = 1000
s = '..' + st + '..........'
diffs = []
curr_sum = 0
prev_sum = sum_plants(st)
for t in range(generations_number):
    ans = '..'
    for i in range(2, len(s)):
        ans += next.get(s[i-2:i+3], '.')
    s = ans + '.'
    curr_sum = sum_plants(ans)
    if t == 20-1:
        print('Answer 1:', curr_sum)
    diff = curr_sum - prev_sum
    diffs.append(diff)
    if (len(diffs) > 100): diffs.pop(0)
    prev_sum = curr_sum

delta = sum(diffs) // len(diffs)

total = (50000000000 - generations_number) * delta + sum_plants(ans)

print("Answer 2: " + str(total))


