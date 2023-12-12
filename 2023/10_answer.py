import math

map_text = open('10_input').read().splitlines()

start_loc = 0
map_dict = {}
# real rows, imag columns
for r_n, row in enumerate(map_text):
    for c_n, c_v in enumerate(row):
        loc = r_n * (1 + 0j) + c_n * (0 + 1j)
        map_dict[loc] = c_v
        map_dict[loc + 0.5] = '.'
        map_dict[loc + 0.5j] = '.'
        map_dict[loc + 0.5 + 0.5j] = '.'
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
grid_set = set(map_dict.keys())
search_set = grid_set.difference(loop_set)
outside_set = set()
inside_set = set()


def in_bounds_neighbors(i_loc, ROW_MAX, COL_MAX):
    i_b_n = set()
    r = i_loc.real
    c = i_loc.imag
    if c > 0:
        i_b_n.add((r, c - 0.5))
    if c < COL_MAX:
        i_b_n.add((r, c + 0.5))

    if r > 0:
        i_b_n.add((r - 0.5, c))
        if c > 0:
            i_b_n.add((r - 0.5, c - 0.5))
        if c < COL_MAX:
            i_b_n.add((r - 0.5, c + 0.5))
    if r < ROW_MAX:
        i_b_n.add((r + 0.5, c))
        if c > 0:
            i_b_n.add((r + 0.5, c - 0.5))
        if c < COL_MAX:
            i_b_n.add((r + 0.5, c + 0.5))

    return set([a for a in map(lambda tu: complex(*tu), i_b_n) if map_dict[a] != 'X'])


def pretty_print(frontier):
    out_str = ""
    for r_v in range(math.floor(MAX_ROW) + 1):
        for c_v in range(math.floor(MAX_COL) + 1):
            m_v = map_dict[r_v + c_v * 1j]
            if r_v + c_v * 1j in frontier:
                m_v = 'X'
            if m_v == '.':
                m_v = ' '
            out_str += m_v
        out_str += "\n"
    return out_str


# temp pre calculate
map_dict[start_loc] = 'F'

verts = ['|', 'F', 'J', '7', 'L']
horzs = ['-', 'F', 'J', '7', 'L']

for key, value in map_dict.items():
    if key not in loop_set:
        map_dict[key] = '.'

    # block corner passage?
    if key.imag % 1 != 0 and key.real % 1 != 0:
        map_dict[key] = "X"

    # between rows
    if key.imag % 1 == 0 and key.real % 1 != 0:
        if key.real >= MAX_ROW:
            # padding on outside
            pass
        else:
            top = map_dict[key - 0.5]
            bottom = map_dict[key + 0.5]
            # blockages
            if top == '|' and bottom in verts:
                map_dict[key] = 'X'
            if bottom == '|' and top in verts:
                map_dict[key] = 'X'
            if top == 'F' and bottom == 'L':
                map_dict[key] = 'X'
            if top == 'F' and bottom == 'J':
                map_dict[key] = 'X'
            if top == '7' and bottom == 'J':
                map_dict[key] = 'X'
            if top == '7' and bottom == 'L':
                map_dict[key] = 'X'
    # between cols
    elif key.imag % 1 != 0 and key.real % 1 == 0:
        if key.imag >= MAX_COL:
            # padding on outside
            pass
        else:
            left = map_dict[key - 0.5j]
            right = map_dict[key + 0.5j]
            # blockages
            if left == '-' and right in horzs:
                map_dict[key] = 'X'
            if right == '-' and left in horzs:
                map_dict[key] = 'X'
            if left == 'F' and right == '7':
                map_dict[key] = 'X'
            if left == 'F' and right == 'J':
                map_dict[key] = 'X'
            if left == 'L' and right == 'J':
                map_dict[key] = 'X'
            if left == 'L' and right == 'F':
                map_dict[key] = 'X'


def bfs(i_loc):
    print("======================================")
    outside = False
    neighbor_group = set()
    frontier = {i_loc}
    while frontier:
        expandee = frontier.pop()
        print(pretty_print(frontier))
        if expandee.real == 0 or expandee.imag == 0 or expandee.real == MAX_ROW or expandee.imag == MAX_COL:
            outside = True
        neighbor_group.add(expandee)
        expansion = in_bounds_neighbors(expandee, MAX_ROW, MAX_COL)
        expansion.difference_update(loop_set)
        expansion = [e for e in expansion if map_dict[e] != 'X']

        frontier.update(expansion)
        frontier.difference_update(neighbor_group)
    return neighbor_group, outside


while search_set:
    search_loc = search_set.pop()
    group, res = bfs(search_loc)
    if res:
        outside_set.update(group)
    else:
        inside_set.update(group)


def integer_points(i_set):
    return [a for a in i_set if a.real % 1 == 0 and a.imag % 1 == 0]


print(len(integer_points(inside_set)))
