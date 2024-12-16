import math
from collections import defaultdict
from collections import deque

map_lines = open('16_input').read().splitlines()


map_dict = {}
start = None
end = None

for ri, rv in enumerate(map_lines):
    for ci, cv in enumerate(rv):
        loc = ri + 1j * ci
        map_dict[loc] = cv
        if cv == 'S':
            start = loc
        if cv == 'E':
            end = loc


cost_record = defaultdict(lambda: math.inf)


cost_record[(start, 1j)] = 0


def adjacencies(i_loc, i_dir, i_cost):
    out_adj = []
    if map_dict[i_loc + i_dir] != '#':
        fwd = i_loc + i_dir, i_dir, i_cost + 1
        out_adj.append(fwd)
    cw = i_loc, i_dir * 1j, i_cost + 1000
    ccw = i_loc, i_dir * -1j, i_cost + 1000
    out_adj.append(cw)
    out_adj.append(ccw)
    return out_adj


def value_fill():
    node_deque = deque([(start, 1j, 0)])

    while node_deque:
        cur_node = node_deque.popleft()
        cur_loc = cur_node[0]
        cur_dir = cur_node[1]
        cur_cst = cur_node[2]

        if cur_cst <= cost_record[(cur_loc, cur_dir)]:
            cost_record[(cur_loc, cur_dir)] = cur_cst
            cur_adj = adjacencies(*cur_node)
            for c_a in cur_adj:
                node_deque.append(c_a)


value_fill()
goal_min = min([cost_record[(end, d)] for d in [-1, 1, 1j, -1j]])
print(goal_min)


def value_fill_paths():
    path_deque = deque([([(start, 1j)], 0)])

    return_paths = []

    while path_deque:
        cur_path_obj = path_deque.popleft()
        cur_path = cur_path_obj[0]
        cur_cst = cur_path_obj[1]

        if cur_path[-1][0] == end and cur_cst == goal_min:
            return_paths.append(cur_path)

        if cur_cst <= cost_record[cur_path[-1]]:
            cost_record[cur_path[-1]] = cur_cst
            cur_adj = adjacencies(*cur_path[-1], cur_cst)
            for c_a in cur_adj:
                new_path = cur_path[::]
                new_path.append((c_a[0], c_a[1]))
                new_path_obj = (new_path, c_a[2])
                path_deque.append(new_path_obj)
    return return_paths


min_paths = value_fill_paths()

seats = len(set([tu[0] for min_p in min_paths for tu in min_p]))
print(seats)
