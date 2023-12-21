from collections import defaultdict

map_lines = open('21_input').read().splitlines()

start_loc = None
rock_dict = {}
for r_n, r_v in enumerate(map_lines):
    for c_n, c_v in enumerate(r_v):
        loc = r_n + 1j * c_n
        rock_dict[loc] = c_v
        if c_v == 'S':
            start_loc = loc

max_row = max(map(lambda cm: cm.real, rock_dict.keys()))
max_col = max(map(lambda cm: cm.imag, rock_dict.keys()))

garden_cost_map = {}
for k, v in rock_dict.items():
    if v != '#':
        garden_cost_map[k] = float('inf')


def in_bounds_not_rocks(i_loc):
    potential_dirs = [1, -1, 1j, -1j]
    if i_loc.imag == 0:
        potential_dirs.remove(-1j)
    if i_loc.imag == max_col:
        potential_dirs.remove(1j)
    if i_loc.real == 0:
        potential_dirs.remove(-1)
    if i_loc.real == max_row:
        potential_dirs.remove(1)

    potential_neighbors = list(map(lambda d: i_loc + d, potential_dirs))
    actual_neighbors = []
    for pn in potential_neighbors:
        if rock_dict[pn] != '#':
            actual_neighbors.append(pn)
    return actual_neighbors


frontier = [(start_loc, 0)]
garden_cost_map[start_loc] = 0


def simple_dijkstra(step_count):
    while frontier:
        frontier.sort(key=lambda tu: tu[1], reverse=True)
        shortest_known_loc, shortest_known_steps = frontier.pop()
        check_neighbors = in_bounds_not_rocks(shortest_known_loc)
        for ng in check_neighbors:
            redux_row = ng.real % max_row
            redux_col = ng.imag % max_col
            redux_val = redux_row + 1j * redux_col
            if shortest_known_steps + 1 > step_count:
                pass
            elif rock_dict[redux_val] == '#':
                pass
            elif shortest_known_steps + 1 < garden_cost_map[ng]:
                garden_cost_map[ng] = shortest_known_steps + 1
                frontier.append((ng, shortest_known_steps + 1))
    return len([(k, v) for k, v in garden_cost_map.items() if v < float('inf') and (step_count - v) % 2 == 0])


print(simple_dijkstra(64))
