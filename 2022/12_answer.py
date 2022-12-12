from collections import deque
from collections import defaultdict
grid_lines = open('12_input').read().splitlines()


grid = {}
paths = []

MAX_ROW = len(grid_lines) - 1
MAX_COL = len(grid_lines[0]) - 1

end_loc = None


for row_ix, row_val in enumerate(grid_lines):
    for col_ix, col_val in enumerate(list(row_val)):
        if col_val == 'S':
            grid[complex(row_ix, col_ix)] = chr(ord('a') - 1)
            paths.append([complex(row_ix, col_ix)])
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

    if north.real >= 0 and ord(grid[north]) - 1 <= head_val:
        in_path_copy = in_path.copy()
        in_path_copy.append(north)
        return_paths.append(in_path_copy)
        
    if south.real <= MAX_ROW and ord(grid[south]) - 1 <= head_val:
        in_path_copy = in_path.copy()
        in_path_copy.append(south)
        return_paths.append(in_path_copy)
    
    if east.imag <= MAX_COL and ord(grid[east]) - 1 <= head_val:
        in_path_copy = in_path.copy()
        in_path_copy.append(east)
        return_paths.append(in_path_copy)
    
    if west.imag >= 0 and ord(grid[west]) - 1 <= head_val:
        in_path_copy = in_path.copy()
        in_path_copy.append(west)
        return_paths.append(in_path_copy)

    return return_paths


min_dist_lookup = defaultdict(lambda: MAX_COL * MAX_ROW * 10000)

complete_paths = []

while paths:
    active_path = paths.pop()
    active_head = active_path[-1]
    print(len(paths), grid[active_head], active_head, abs(active_head - end_loc))
    if len(active_path) < min_dist_lookup[active_head]:
        min_dist_lookup[active_head] = len(active_path)
        if grid[active_head] == chr(ord('z') + 1):
            complete_paths.append(active_path)
        else:
            expansion = expand_path(active_path)
            for ex in expansion:
                paths.append(ex)
    paths.sort(key=lambda p: len(p), reverse=True)


print("Done!")
