st = (int(x) for x in [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2])

stack = []
stack_rsl = []
result = 0
new_node = True

while 1:
    if new_node == True:
        child, metadata = next(st), next(st)
        if child == 0:
            new_node = False
            stack.append((0, metadata))
        else:
            print("a", child)
            stack.append((child-1, metadata))
    else:
        if len(stack) == 0:
            break
        child, metadata = stack.pop()
        if child == 0:
            rsl = []
            for x in range(metadata):
                a =  next(st)
                result += a
                rsl.append(a)
            stack_rsl.append(rsl)
            print(rsl)
            new_node = False
        else:
            print(child)
            stack.append((child-1, metadata))
            new_node = True

print(result)
print(stack_rsl)