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


def in_bounds_not_rocks(i_loc, i_m_r, i_m_c):
    potential_dirs = [1, -1, 1j, -1j]
    if i_loc.imag == 0:
        potential_dirs.remove(-1j)
    if i_loc.imag == i_m_r:
        potential_dirs.remove(1j)
    if i_loc.real == 0:
        potential_dirs.remove(-1)
    if i_loc.real == i_m_c:
        potential_dirs.remove(1)

    potential_neighbors = list(map(lambda d: i_loc + d, potential_dirs))
    actual_neighbors = []
    for pn in potential_neighbors:
        if rock_dict[pn] != '#':
            actual_neighbors.append(pn)
    return actual_neighbors


def simple_dijkstra(step_count, parity):
    garden_cost_map = {}
    for k, v in rock_dict.items():
        if v != '#':
            garden_cost_map[k] = float('inf')
    frontier = [(start_loc, 0)]
    garden_cost_map[start_loc] = 0
    while frontier:
        frontier.sort(key=lambda tu: tu[1], reverse=True)
        shortest_known_loc, shortest_known_steps = frontier.pop()
        check_neighbors = in_bounds_not_rocks(shortest_known_loc, max_row, max_col)
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
    if parity == 'even':
        return len([(k, v) for k, v in garden_cost_map.items() if v < float('inf') and v % 2 == 0])
    else:
        return len([(k, v) for k, v in garden_cost_map.items() if v < float('inf') and v % 2 == 1])


print(simple_dijkstra(64, 'even'))


def complex_dijkstra(step_count):
    # define full cost across entire map
    garden_cost_map = {}
    for k, v in rock_dict.items():
        if v != '#':
            garden_cost_map[k] = float('inf')
    frontier = [(start_loc, 0)]
    garden_cost_map[start_loc] = 0
    while frontier:
        frontier.sort(key=lambda tu: tu[1], reverse=True)
        shortest_known_loc, shortest_known_steps = frontier.pop()
        check_neighbors = [shortest_known_loc + d for d in [1, -1, 1j, -1j]]
        for ng in check_neighbors:
            if ng not in rock_dict.keys():
                pass
            elif rock_dict[ng] == '#':
                pass
            elif shortest_known_steps + 1 < garden_cost_map[ng]:
                garden_cost_map[ng] = shortest_known_steps + 1
                frontier.append((ng, shortest_known_steps + 1))

    print([(k, v) for k, v in garden_cost_map.items() if v % 2 == 0])
    even_parity = len([(k, v) for k, v in garden_cost_map.items() if v % 2 == 0])
    odd_parity = len([(k, v) for k, v in garden_cost_map.items() if v % 2 == 1])
    print('op', odd_parity)
    print('ep', even_parity)

    without_diamond_odd = len([(k, v) for k, v in garden_cost_map.items() if v % 2 != 0 and v > max_row / 2])
    without_diamond_even = len([(k, v) for k, v in garden_cost_map.items() if v % 2 == 0 and v > max_row / 2])
    print('do', without_diamond_odd)
    print('de', without_diamond_even)

    full_grid_steps = step_count // max_row

    # since total steps is even, our initial parity is odd
    # with 202300 'full grid steps' we cover (202300 + 1)^2 odd grids and (202300)^2 even grids

    # then we have to handle the 'cut-off' and 'extra' corners of our outer diamond

    # with 202300 'full grid steps' taken, our diamond is a 202300 wide square
    # since 202300 is even and we started odd, the outer ring is of odd squares
    # condensing the outer ring extras is equivalent to  202300 times a (square minus diamond).
    # that is, the outside bits of one square.  That count is the above 'without_diamond_odd'
    # onto the 'extra'.  Similarly that's (202300 - 1) times the 'without_diamond_odd'

    # even step count, starting square is of _odd_ parity
    e_o = step_count % 2
    if e_o == 0:
        answer = ((full_grid_steps + 1) ** 2) * even_parity + ((full_grid_steps) ** 2) * odd_parity \
                 - (full_grid_steps + 1) * without_diamond_even + (full_grid_steps) * without_diamond_odd
    else:
        answer = ((full_grid_steps + 1) ** 2) * odd_parity + ((full_grid_steps) ** 2) * even_parity \
                 - (full_grid_steps + 1) * without_diamond_odd + (full_grid_steps) * without_diamond_even
    return answer


# wrong: 617584090632396
#        617578031631769
#        617585628725916
#        617585575519239
#        617585575119082
#        608193763124774 (eooe)
# next:  608193716191058 (eoeo)

print(complex_dijkstra(26501365))

# FUCK THIS
