from collections import deque
from collections import defaultdict
grid_lines = open('12_input').read().splitlines()


grid = {}
paths = deque()

MAX_ROW = len(grid_lines) - 1
MAX_COL = len(grid_lines[0]) - 1

end_loc = None


for row_ix, row_val in enumerate(grid_lines):
    for col_ix, col_val in enumerate(list(row_val)):
        if col_val == 'S':
            grid[complex(row_ix, col_ix)] = chr(ord('a') - 1)
            #paths.append([complex(row_ix, col_ix)])
        elif col_val == 'E':
            end_loc = complex(row_ix, col_ix)
            grid[end_loc] = chr(ord('z') + 1)
        else:
            grid[complex(row_ix, col_ix)] = col_val


def expand_path(in_path):
    head = in_path[-1]
    head_val = ord(grid[head])
    north = head - 1
    south = head + 1
    east = head + 1j
    west = head - 1j

    return_paths = []

    if north.real >= 0 and north not in in_path and can_step_up_lookup[north] and ord(grid[north]) - 1 <= head_val:
        in_path_copy = in_path.copy()
        in_path_copy.append(north)
        return_paths.append(in_path_copy)
        
    if south.real <= MAX_ROW and south not in in_path and can_step_up_lookup[south] and ord(grid[south]) - 1 <= head_val:
        in_path_copy = in_path.copy()
        in_path_copy.append(south)
        return_paths.append(in_path_copy)
    
    if east.imag <= MAX_COL and east not in in_path and can_step_up_lookup[east] and ord(grid[east]) - 1 <= head_val:
        in_path_copy = in_path.copy()
        in_path_copy.append(east)
        return_paths.append(in_path_copy)
    
    if west.imag >= 0 and west not in in_path and can_step_up_lookup[west] and ord(grid[west]) - 1 <= head_val:
        in_path_copy = in_path.copy()
        in_path_copy.append(west)
        return_paths.append(in_path_copy)

    return return_paths


can_step_up_lookup = defaultdict(lambda: False)
can_step_up_lookup[end_loc] = True


def can_step_up(in_point):
    cur_val = grid[in_point]
    new_cluster = {in_point}
    start_cluster = set()
    while start_cluster != new_cluster:
        start_cluster = new_cluster.copy()
        for pt in start_cluster:
            if can_step_up_lookup[pt]:
                can_step_up_lookup[in_point] = True
                return True
            north = pt - 1
            south = pt + 1
            east = pt + 1j
            west = pt - 1j

            if north.real >= 0:
                if ord(grid[north]) - 1 == ord(cur_val):
                    can_step_up_lookup[in_point] = True
                    return True
                elif ord(grid[north]) == ord(cur_val):
                    new_cluster.add(north)
                else:
                    # too high or lower
                    pass
            if south.real <= MAX_ROW:
                if ord(grid[south]) - 1 == ord(cur_val):
                    can_step_up_lookup[in_point] = True
                    return True
                elif ord(grid[south]) == ord(cur_val):
                    new_cluster.add(south)
                else:
                    # too high or lower
                    pass
            if east.imag <= MAX_COL:
                if ord(grid[east]) - 1 == ord(cur_val):
                    can_step_up_lookup[in_point] = True
                    return True
                elif ord(grid[east]) == ord(cur_val):
                    new_cluster.add(east)
                else:
                    # too high or lower
                    pass
            if west.imag >= 0:
                if ord(grid[west]) - 1 == ord(cur_val):
                    can_step_up_lookup[in_point] = True
                    return True
                elif ord(grid[west]) == ord(cur_val):
                    new_cluster.add(west)
                else:
                    # too high or lower
                    pass
    return False


for r in range(MAX_ROW + 1):
    for c in range(MAX_COL + 1):
        can_step_up(complex(r, c))


min_dist_lookup = defaultdict(lambda: MAX_COL * MAX_ROW * 10000)

paths.append([24+109j])
while paths:
    active_path = paths.pop()
    active_head = active_path[-1]
    print(grid[active_head], abs(active_head - end_loc))
    if len(active_path) <= min_dist_lookup[active_head]:
        min_dist_lookup[active_head] = len(active_path)
        if grid[active_head] == chr(ord('z') + 1):
            print("Part 1: ", len(active_path) - 1)
            break
        else:
            expansion = expand_path(active_path)
            for ex in expansion:
                paths.appendleft(ex)

print("Done!")
