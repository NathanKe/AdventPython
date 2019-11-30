import re
import itertools
import collections

raw = open('13_input').read().splitlines()


def extract(s):
    m = re.match(r"(.+)\swould\s(gain|lose)\s(\d+)\shappiness\sunits\sby\ssitting\snext\sto\s(.+)\.", s)
    if m[2] == "gain":
        n = 1 * int(m[3])
    else:
        n = -1 * int(m[3])
    return m[1], m[4], n


lookup = collections.defaultdict(lambda: collections.defaultdict(int))

for line in list(map(extract, raw)):
    lookup[line[0]][line[1]] = line[2]


def prep_perms(dict):
    base_perm = map(list, itertools.permutations(list(dict.keys())))

    looped_perm = []
    for perm in base_perm:
        perm.append(perm[0])
        looped_perm.append(perm)

    return looped_perm[0:len(looped_perm) // 2]


looped_perm_half = prep_perms(lookup)


def happy_sum_dir(l):
    s = 0
    for i in range(0, len(l) - 1):
        s += lookup[l[i]][l[i + 1]]
    return s


def happy_sum(l):
    s = 0
    s += happy_sum_dir(l)
    s += happy_sum_dir(l[::-1])
    return s


p1 = max(list(map(happy_sum, looped_perm_half)))

print('Part 1: ', p1)

for k in lookup.copy().keys():
    lookup['Me'][k] = 0

p2_looped_perm_half = prep_perms(lookup)

p2 = max(list(map(happy_sum, p2_looped_perm_half)))

print('Part 2: ', p2)
