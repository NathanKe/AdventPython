from collections import defaultdict
from collections import deque

map_lines = open('12_input').read().splitlines()


map_dict = {}

for ri, rv in enumerate(map_lines):
    for ci, cv in enumerate(rv):
        map_dict[ri + 1j * ci] = cv


def region_expand(i_region, i_checked):
    cur_type = map_dict[i_region[0]]
    out_region = i_region[::]
    for loc in i_region:
        if loc not in i_checked:
            i_checked.append(loc)
            north = loc - 1
            south = loc + 1
            east = loc + 1j
            west = loc - 1j

            loc_front = [new_loc for new_loc in [north, south, east, west]
                         if new_loc not in out_region
                         and new_loc in map_dict.keys()
                         and map_dict[new_loc] == cur_type]
            out_region.extend(loc_front)
    if all([o_r in i_checked for o_r in out_region]):
        return out_region
    else:
        return region_expand(out_region, i_checked)


def fence_count(i_region):
    out_fence_count = 0
    for loc in i_region:
        north = loc - 1
        south = loc + 1
        east = loc + 1j
        west = loc - 1j
        for neighbor in [north, south, east, west]:
            if neighbor not in i_region:
                out_fence_count += 1
    return out_fence_count


full_regions = []
key_set = set(map_dict.keys())

while key_set:
    cur_key = list(key_set)[0]
    new_region = region_expand([cur_key], [])

    full_regions.append(new_region)
    key_set.difference_update(set(new_region))


print(sum(map(lambda li: len(li) * fence_count(li), full_regions)))


def directional_fences(i_region):
    reg_type = map_dict[i_region[0]]
    dir_fences = []
    for loc in i_region:
        north = loc - 1
        south = loc + 1
        east = loc + 1j
        west = loc - 1j
        if north not in i_region and (north not in map_dict.keys() or map_dict[north] != reg_type):
            dir_fences.append((loc, -1))
        if south not in i_region and (south not in map_dict.keys() or map_dict[south] != reg_type):
            dir_fences.append((loc, 1))
        if east not in i_region and (east not in map_dict.keys() or map_dict[east] != reg_type):
            dir_fences.append((loc, 1j))
        if west not in i_region and (west not in map_dict.keys() or map_dict[west] != reg_type):
            dir_fences.append((loc, -1j))
    return dir_fences





