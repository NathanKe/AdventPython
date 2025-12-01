import itertools

stuff = list(map(lambda lns: lns.splitlines(), open('25_input').read().split('\n\n')))

keys = []
locks = []
for st in stuff:
    if st[0] == '#####':
        locks.append(st)
    if st[-1] == '#####':
        keys.append(st)

combos = itertools.product(keys, locks)

fit_count = 0
for (k, l) in combos:
    fits = True
    for ri in range(7):
        for ci in range(5):
            if k[ri][ci] == '#' and l[ri][ci] == '#':
                fits = False
    if fits:
        fit_count += 1
