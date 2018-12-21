with open("santa2018.txt", 'r') as santa:
    s = santa.read()
    d = [line.split(" ") for line in s.splitlines()]
    d = [(d[1], d[-3]) for d in d]

tasks = {}
for before, after in d:
    if before not in tasks:
        tasks[before] = []
    if after not in tasks:
        tasks[after] = []
    tasks[after].append(before)

tasks = sorted(tasks.items(), key=lambda x: x[0])

def problem1(d):
    final = []
    done = set()
    while len(done) != len(tasks):
        for key, value in tasks:
            if key not in done and all(t in done for t in value):
                done.add(key)
                final.append(key)
                break
    return "".join(final)

def problem2(d):
    base_time = 60 if len(d) != 7 else 0
    num_workers = 5 if len(d) != 7 else 2

    time_cur = 0
    current = {}
    done = set()
    while len(done) != len(tasks):
        for key, value in tasks:
            if key not in done and key not in current and all(t in done for t in value):
                current[key] = base_time + ord(key) - 64
                if len(current) == num_workers:
                    break
        next_step = min(current.values())
        time_cur += next_step
        for t in current:
            current[t] -= next_step
            if current[t] == 0:
                done.add(t)

        for t in done:
            if t in current:
                del current[t]

    return time_cur

print(problem1(d))
print(problem2(d))