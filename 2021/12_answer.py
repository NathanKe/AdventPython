from collections import Counter
from itertools import chain

edges = open('12_input').read().splitlines()

edge_hash = {}
big_caves = set()
small_caves = set()

for edge in edges:
    a, b = edge.split('-')
    if a in edge_hash.keys():
        edge_hash[a].add(b)
    else:
        edge_hash[a] = {b}
    if b in edge_hash.keys():
        edge_hash[b].add(a)
    else:
        edge_hash[b] = {a}
    if a.isupper():
        big_caves.add(a)
    else:
        small_caves.add(a)
    if b.isupper():
        big_caves.add(b)
    else:
        small_caves.add(b)


def path_count_by_allowed_double_small_cave(double_cave):
    completed_paths = []
    paths_under_construction = [['start']]
    while paths_under_construction:
        cur_path = paths_under_construction.pop()
        assert (cur_path[-1] != 'end')
        frontier = edge_hash[cur_path[-1]]
        for frontier_elem in frontier:
            if frontier_elem == 'end':
                new_path = [i for i in cur_path]
                new_path.append(frontier_elem)
                completed_paths.append(new_path)
            elif frontier_elem == double_cave:
                double_cave_count = Counter(cur_path)[double_cave]
                if double_cave_count < 2:
                    new_path = [i for i in cur_path]
                    new_path.append(frontier_elem)
                    paths_under_construction.append(new_path)
            elif frontier_elem not in small_caves or frontier_elem not in cur_path:
                new_path = [i for i in cur_path]
                new_path.append(frontier_elem)
                paths_under_construction.append(new_path)
    return completed_paths


print("Part 1: ", len(path_count_by_allowed_double_small_cave(None)))

small_non_start_end = small_caves.difference({'start', 'end'})
small_non_start_end.add(None)
including_dupes = chain(*map(path_count_by_allowed_double_small_cave, small_non_start_end))
stringified = map(lambda p: ''.join(p), including_dupes)
uniqueified = set(stringified)
print("Part 2: ", len(uniqueified))
