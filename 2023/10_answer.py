import math

map_text = open('10_input').read().splitlines()

start_loc = 0
map_dict = {}
# real rows, imag columns
for r_n, row in enumerate(map_text):
    for c_n, c_v in enumerate(row):
        loc = r_n * (1 + 0j) + c_n * (0 + 1j)
        map_dict[loc] = c_v
        if c_v == "S":
            start_loc = loc

MAX_ROW = max(map(lambda v: v.real, map_dict.keys()))
MAX_COL = max(map(lambda v: v.imag, map_dict.keys()))

frontier = []
if start_loc.real > 0 and map_dict[start_loc - 1] in ['|', '7', 'F']:
    frontier.append((start_loc - 1, -1))
if start_loc.real < MAX_ROW and map_dict[start_loc + 1] in ['|', 'L', 'J']:
    frontier.append((start_loc + 1, 1))
if start_loc.imag > 0 and map_dict[start_loc - 1j] in ['-', 'F', 'L']:
    frontier.append((start_loc - 1j, -1j))
if start_loc.imag < MAX_COL and map_dict[start_loc + 1j] in ['-', '7', 'J']:
    frontier.append((start_loc + 1j, +1j))

# into to out of direction map
# from to
direction_map = {
    '|': {1: 1,
          -1: -1},
    '-': {-1j: -1j,
          1j: 1j},
    'L': {-1j: -1,
          1: 1j},
    'J': {1j: -1,
          1: -1j},
    '7': {1j: 1,
          -1: -1j},
    'F': {-1j: 1,
          -1: 1j}
}

path0 = frontier[0]
path1 = frontier[1]
steps = 1

loop_set = {start_loc, path0[0], path1[0]}

while path0[0] != path1[0]:
    next_dir_0 = direction_map[map_dict[path0[0]]][path0[1]]
    next_dir_1 = direction_map[map_dict[path1[0]]][path1[1]]

    path0 = (path0[0] + next_dir_0, next_dir_0)
    path1 = (path1[0] + next_dir_1, next_dir_1)
    steps += 1
    loop_set.add(path0[0])
    loop_set.add(path1[0])

print(steps)

# set of whole grid
# subtract set of loop
# pick element of remaining set
# expand its reachable neighbors
# if connected to map edge, add whole neighbor set to "OUTSIDE CONNECTED", subtract from remaining set
# else add whole neighbor set to "STUCK IN LOOP", subtract from remaining set
# OUTSIDE + INSIDE + LOOP _should_ equal size of grid
# answer is size of INSIDE


# temp pre-compute true value of start_loc
map_dict[start_loc] = '|'

big_dict = {}
loop_list = list(loop_set)
for loop_loc in loop_set:
    loop_item = map_dict[loop_loc]
    loop_loc_real_3x = loop_loc.real * 3
    loop_loc_imag_3x = loop_loc.imag * 3
    if loop_item == 'F':
        # ...
        # .##
        # .#.
        big_dict[(loop_loc_real_3x + 0) + (loop_loc_imag_3x + 0) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 0) + (loop_loc_imag_3x + 1) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 0) + (loop_loc_imag_3x + 2) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 1) + (loop_loc_imag_3x + 0) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 1) + (loop_loc_imag_3x + 1) * 1j] = '#'
        big_dict[(loop_loc_real_3x + 1) + (loop_loc_imag_3x + 2) * 1j] = '#'
        big_dict[(loop_loc_real_3x + 2) + (loop_loc_imag_3x + 0) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 2) + (loop_loc_imag_3x + 1) * 1j] = '#'
        big_dict[(loop_loc_real_3x + 2) + (loop_loc_imag_3x + 2) * 1j] = ' '
    elif loop_item == 'J':
        # .#.
        # ##.
        # ...
        big_dict[(loop_loc_real_3x + 0) + (loop_loc_imag_3x + 0) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 0) + (loop_loc_imag_3x + 1) * 1j] = '#'
        big_dict[(loop_loc_real_3x + 0) + (loop_loc_imag_3x + 2) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 1) + (loop_loc_imag_3x + 0) * 1j] = '#'
        big_dict[(loop_loc_real_3x + 1) + (loop_loc_imag_3x + 1) * 1j] = '#'
        big_dict[(loop_loc_real_3x + 1) + (loop_loc_imag_3x + 2) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 2) + (loop_loc_imag_3x + 0) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 2) + (loop_loc_imag_3x + 1) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 2) + (loop_loc_imag_3x + 2) * 1j] = ' '
    elif loop_item == 'L':
        # .#.
        # .##
        # ...
        big_dict[(loop_loc_real_3x + 0) + (loop_loc_imag_3x + 0) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 0) + (loop_loc_imag_3x + 1) * 1j] = '#'
        big_dict[(loop_loc_real_3x + 0) + (loop_loc_imag_3x + 2) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 1) + (loop_loc_imag_3x + 0) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 1) + (loop_loc_imag_3x + 1) * 1j] = '#'
        big_dict[(loop_loc_real_3x + 1) + (loop_loc_imag_3x + 2) * 1j] = '#'
        big_dict[(loop_loc_real_3x + 2) + (loop_loc_imag_3x + 0) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 2) + (loop_loc_imag_3x + 1) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 2) + (loop_loc_imag_3x + 2) * 1j] = ' '
    elif loop_item == '7':
        # ...
        # ##.
        # .#.
        big_dict[(loop_loc_real_3x + 0) + (loop_loc_imag_3x + 0) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 0) + (loop_loc_imag_3x + 1) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 0) + (loop_loc_imag_3x + 2) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 1) + (loop_loc_imag_3x + 0) * 1j] = '#'
        big_dict[(loop_loc_real_3x + 1) + (loop_loc_imag_3x + 1) * 1j] = '#'
        big_dict[(loop_loc_real_3x + 1) + (loop_loc_imag_3x + 2) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 2) + (loop_loc_imag_3x + 0) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 2) + (loop_loc_imag_3x + 1) * 1j] = '#'
        big_dict[(loop_loc_real_3x + 2) + (loop_loc_imag_3x + 2) * 1j] = ' '
    elif loop_item == '|':
        # .#.
        # .#.
        # .#.
        big_dict[(loop_loc_real_3x + 0) + (loop_loc_imag_3x + 0) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 0) + (loop_loc_imag_3x + 1) * 1j] = '#'
        big_dict[(loop_loc_real_3x + 0) + (loop_loc_imag_3x + 2) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 1) + (loop_loc_imag_3x + 0) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 1) + (loop_loc_imag_3x + 1) * 1j] = '#'
        big_dict[(loop_loc_real_3x + 1) + (loop_loc_imag_3x + 2) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 2) + (loop_loc_imag_3x + 0) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 2) + (loop_loc_imag_3x + 1) * 1j] = '#'
        big_dict[(loop_loc_real_3x + 2) + (loop_loc_imag_3x + 2) * 1j] = ' '
    elif loop_item == '-':
        # .#.
        # .#.
        # .#.
        big_dict[(loop_loc_real_3x + 0) + (loop_loc_imag_3x + 0) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 0) + (loop_loc_imag_3x + 1) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 0) + (loop_loc_imag_3x + 2) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 1) + (loop_loc_imag_3x + 0) * 1j] = '#'
        big_dict[(loop_loc_real_3x + 1) + (loop_loc_imag_3x + 1) * 1j] = '#'
        big_dict[(loop_loc_real_3x + 1) + (loop_loc_imag_3x + 2) * 1j] = '#'
        big_dict[(loop_loc_real_3x + 2) + (loop_loc_imag_3x + 0) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 2) + (loop_loc_imag_3x + 1) * 1j] = ' '
        big_dict[(loop_loc_real_3x + 2) + (loop_loc_imag_3x + 2) * 1j] = ' '


BIG_MAX_COL = int(max(map(lambda c: c.imag, big_dict.keys())))
BIG_MAX_ROW = int(max(map(lambda c: c.real, big_dict.keys())))
BIG_MIN_ROW = int(min(map(lambda c: c.real, big_dict.keys())))
BIG_MIN_COL = int(min(map(lambda c: c.imag, big_dict.keys())))

for r in range(BIG_MIN_ROW, BIG_MAX_ROW + 1):
    for c in range(BIG_MIN_COL, BIG_MAX_COL + 1):
        if r+c*1j not in big_dict.keys():
            big_dict[r+c*1j] = ' '


grid_set = set(big_dict.keys())


def pretty_print():
    out = ""
    for r in range(BIG_MIN_ROW, BIG_MAX_ROW):
        for c in range(BIG_MIN_COL, BIG_MAX_COL):
            out += big_dict[r + c * 1j]
        out += "\n"
    return out


def in_bounds_non_block_neighbors(i_loc, s_ngb):
    test_ngb = [i_loc + 1,
                i_loc - 1,
                i_loc + 1j,
                i_loc - 1j,
                i_loc + 1 + 1j,
                i_loc + 1 - 1j,
                i_loc - 1 + 1j,
                i_loc - 1 - 1j]
    in_bound_ngb = [i for i in test_ngb if
                    BIG_MIN_ROW <= i.real <= BIG_MAX_ROW and BIG_MIN_COL <= i.imag <= BIG_MAX_COL]
    non_block_ngb = [i for i in in_bound_ngb if big_dict[i] != '#']
    new_ngb = [i for i in non_block_ngb if i not in s_ngb]
    return set(new_ngb)


search_set = set([k for k, v in big_dict.items() if v != '#'])


def bfs(i_loc):
    frontier = {i_loc}
    neighbor_set = {i_loc}
    outside = False
    while frontier:
        expandee = frontier.pop()
        ibn = in_bounds_non_block_neighbors(expandee, neighbor_set)
        neighbor_set.update(ibn)
        frontier.update(ibn)
        # print('----', len(neighbor_set), len(frontier))
        if outside:
            pass
        else:
            if expandee.real in [BIG_MIN_ROW, BIG_MAX_ROW]:
                outside = True
            if expandee.imag in [BIG_MIN_COL, BIG_MAX_COL]:
                outside = True
    return neighbor_set, outside


outside_set = set()
inside_set = set()
while search_set:
    search_item = search_set.pop()
    bfs_g, bfs_t = bfs(search_item)
    if bfs_t:
        outside_set.update(bfs_g)
    else:
        inside_set.update(bfs_g)
    search_set.difference_update(bfs_g)

quasi_integer_inside_list = [x for x in list(inside_set) if x.real % 3 == 1 and x.imag % 3 == 1]
print(len(quasi_integer_inside_list))
