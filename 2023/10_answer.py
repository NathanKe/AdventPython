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
map_dict[start_loc] = 'F'

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

for r in range(BIG_MIN_ROW - 1, BIG_MAX_ROW + 1):
    for c in range(BIG_MIN_COL - 1, BIG_MAX_COL +1):
        if r+c*1j not in big_dict.keys():
            big_dict[r+c*1j] = ' '


grid_set = set(big_dict.keys())
search_set = grid_set.difference(loop_set)
outside_set = set()
inside_set = set()


def in_bounds_un_blocked_neighbors(i_loc, mn_row, mx_row, mn_col, mx_col):
    i_r = i_loc.real
    i_c = i_loc.imag

    out_set = []

    if i_r > mn_row:
        out_set.append(i_r - 1 + i_c*1j)
        if i_c > mn_col:
            out_set.append(i_r - 1 + (i_c - 1)*1j)
        if i_c < mx_col:
            out_set.append(i_r - 1 + (i_c + 1) * 1j)
    if i_r < mx_row:
        out_set.append(i_r + 1 + i_c*1j)
        if i_c > mn_col:
            out_set.append(i_r + 1 + (i_c - 1)*1j)
        if i_c < mx_col:
            out_set.append(i_r + 1 + (i_c + 1) * 1j)
    if i_c > mn_col:
        out_set.append(i_r + (i_c - 1) * 1j)
    if i_c < mx_col:
        out_set.append(i_r + (i_c + 1) * 1j)

    return set([a for a in out_set if big_dict[a] != '#'])


def bfs(i_loc):
    outside = False
    neighbor_group = set()
    frontier = {i_loc}
    while frontier:
        expandee = frontier.pop()
        if expandee.real == BIG_MIN_ROW or expandee.imag == BIG_MIN_ROW or expandee.real == BIG_MAX_ROW or expandee.imag == BIG_MAX_COL:
            outside = True
        neighbor_group.add(expandee)
        expansion = in_bounds_un_blocked_neighbors(expandee, BIG_MIN_ROW, BIG_MAX_ROW, BIG_MIN_COL, BIG_MAX_COL)

        frontier.update(expansion)
    return neighbor_group, outside




