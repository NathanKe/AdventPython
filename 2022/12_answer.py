from collections import deque
from collections import defaultdict

grid_lines = open('12_input').read().splitlines()

grid = {}

NUM_ROWS = len(grid_lines)
NUM_COLS = len(grid_lines[0])

end_loc = None
start_loc = None

for row_ix, row_val in enumerate(grid_lines):
    for col_ix, col_val in enumerate(list(row_val)):
        if col_val == 'S':
            grid[complex(row_ix, col_ix)] = chr(ord('a'))
            start_loc = complex(row_ix, col_ix)
        elif col_val == 'E':
            end_loc = complex(row_ix, col_ix)
            grid[end_loc] = chr(ord('z'))
        else:
            grid[complex(row_ix, col_ix)] = col_val


def expand_frontier(in_frontier, in_steps_to_z_heights, in_min_distance_map):
    new_frontier = []
    while in_frontier:
        cur_node = in_frontier.pop()
        dist_to_cur = in_min_distance_map[cur_node]
        neighbors = [cur_node + x for x in [1, 1j, -1, -1j]]
        for neighbor in neighbors:
            if 0 <= neighbor.real < NUM_ROWS and 0 <= neighbor.imag < NUM_COLS:
                if ord(grid[neighbor]) == ord(grid[end_loc]):
                    in_steps_to_z_heights.append(dist_to_cur + 1)
                if ord(grid[neighbor]) - 1 <= ord(grid[cur_node]):
                    if neighbor not in in_min_distance_map.keys():
                        in_min_distance_map[neighbor] = dist_to_cur + 1
                        new_frontier.append(neighbor)
                    elif dist_to_cur + 1 < in_min_distance_map[neighbor]:
                        in_min_distance_map[neighbor] = dist_to_cur + 1
                        new_frontier.append(neighbor)
    return new_frontier, in_steps_to_z_heights, in_min_distance_map


def shortest_length_path_to_height_z(in_start_loc):
    frontier = [in_start_loc]
    steps_to_z_heights = [10000]
    min_distance_map = {in_start_loc: 0}
    while frontier:
        frontier, steps_to_z_heights, min_distance_map = expand_frontier(frontier, steps_to_z_heights, min_distance_map)
    return min(steps_to_z_heights)


print("Part 1:", shortest_length_path_to_height_z(start_loc))

best_a_start = 10000
for r in range(NUM_ROWS):
    for c in range(NUM_COLS):
        if grid[complex(r, c)] == 'a':
            cur_a_start = shortest_length_path_to_height_z(complex(r, c))
            if cur_a_start < best_a_start:
                best_a_start = cur_a_start
print("Part 2: ", best_a_start)
