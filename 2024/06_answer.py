from collections import defaultdict
from collections import Counter

grid_lines = open('06_input').read().splitlines()

grid_data = defaultdict(lambda: '-')

start = None

for ri, rv in enumerate(grid_lines):
    for ci, cv in enumerate(rv):
        loc = ri + ci * 1j
        grid_data[loc] = cv
        if cv == '^':
            start = loc


def route_proc(i_start, i_dir):
    c_loc = i_start
    dir = i_dir
    i_visited = [(start, dir)]

    in_grid = True
    looped = False

    while in_grid and not looped:
        next_loc = c_loc + dir
        loc_peek = grid_data[next_loc]
        if loc_peek == '#':
            dir = dir * -1j
        else:
            c_loc = next_loc

        if (c_loc, dir) in i_visited:
            looped = True
        if grid_data[c_loc] == '-':
            in_grid = False

        i_visited.append((c_loc, dir))

    if looped:
        return "looped", i_visited
    if not in_grid:
        return "out of grid", i_visited


_, visit_tuples = route_proc(start, -1)

visited_spaces = set((map(lambda tu: tu[0], visit_tuples)))
print(len(visited_spaces) - 1)

loop_set = set()
for ix, vt in enumerate(visit_tuples):

    if grid_data[vt[0]] == '.' and vt[0] != start and vt[0] not in loop_set:
        grid_data[vt[0]] = '#'

        route_res, route_path = route_proc(start, -1)
        if route_res == "looped":
            loop_set.add(vt[0])
        grid_data[vt[0]] = '.'

print(len(loop_set))
