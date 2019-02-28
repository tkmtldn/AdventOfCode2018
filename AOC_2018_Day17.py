#Not finished
clay = []
water = []
spring = (500, 0)
x_min = 500
x_max = 500
y_max = 0
with open('santa2018.txt', 'r') as sp:
    for i in sp.readlines():
        i = i.strip().split(', ')
        pos_a_item, pos_a_line = i[0].split('=')
        pos_b = i[1].split('=')
        pos_b_item = pos_b[0]
        pos_b_start, pos_b_finish = pos_b[1].split('..')
        if pos_b_item == 'x':
            if int(pos_a_line) > y_max:
                y_max = int(pos_a_line)
            if int(pos_b_start) < x_min:
                x_min = int(pos_b_start)
            if int(pos_b_finish) > x_max:
                x_max = int(pos_b_finish)
            for i in range(int(pos_b_finish)-int(pos_b_start)+1):
                clay.append((int(pos_b_start)+i, int(pos_a_line)))
        else:
            if int(pos_a_line) > x_max:
                x_max = int(pos_a_line)
            if int(pos_b_finish) > y_max:
                y_max = int(pos_b_finish)
            for i in range(int(pos_b_finish)-int(pos_b_start)+1):
                clay.append((int(pos_a_line), int(pos_b_start)+i))
print(len(clay))
print(x_min, x_max, y_max)