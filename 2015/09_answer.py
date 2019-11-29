import re
import itertools
import collections

lines = open('09_input').read().splitlines()

locs = list(set(list(map(lambda s: re.sub(r"(\S+)(\s.+)", r"\1", s), lines))))
locs.append(lines[-1].split()[2])

loc_perm = list(itertools.permutations(locs))
half_len = len(loc_perm) // 2
half_sorted_perm = sorted(loc_perm)[:half_len]

cur_min = 1000000
cur_max = 0

for path in half_sorted_perm:
    steps = [(path[i], path[i + 1]) for i in range(0, len(path) - 1)]
    dist = 0
    for step in steps:
        has_left = list(filter(lambda s: re.search(step[0], s), lines))
        has_right = list(filter(lambda s: re.search(step[1], s), has_left))
        has_both = has_right[0]

        step_dist = int(re.search(r"\d+", has_both)[0])

        dist += step_dist
    if dist < cur_min:
        cur_min = dist
    if dist > cur_max:
        cur_max = dist

print('Part 1: ', cur_min)
print('Part 2: ', cur_max)
