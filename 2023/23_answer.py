text_lines = open('23_input').read().splitlines()

trail_info = {}
start_loc = None
end_loc = None
for r_n, r_v in enumerate(text_lines):
    for c_n, c_v in enumerate(r_v):
        loc = r_n + 1j * c_n
        trail_info[loc] = c_v
        if r_n == 0 and c_v == '.':
            start_loc = loc
        if r_n == len(text_lines) - 1 and c_v == '.':
            end_loc = loc

max_row = max([cm.real for cm in trail_info.keys()])
min_row = min([cm.real for cm in trail_info.keys()])
max_col = max([cm.imag for cm in trail_info.keys()])
min_col = min([cm.imag for cm in trail_info.keys()])

directions = [1, -1, 1j, -1j]

slope_force_map = {
    '>': 1j,
    '<': -1j,
    'v': 1,
    '^': -1
}

trail_info[start_loc - 1] = '#'
trail_info[end_loc + 1] = '#'


def cmp_manhattan(i_s, i_d):
    return abs(i_s.real - i_d.real) + abs(i_s.imag - i_d.imag)


def long_a_star():
    incomplete_paths = [[start_loc]]
    dead_end_paths = []
    complete_paths = []

    longest_known_cost = {}
    longest_guess_total_cost = {}
    walkable_points = 0
    for k, v in trail_info.items():
        if v != '#':
            walkable_points += 1
            longest_guess_total_cost[k] = -1
            longest_known_cost[k] = -1

    while incomplete_paths:
        # incomplete_paths.sort(key=lambda pt: (len(pt), cmp_manhattan(pt[-1], end_loc)))
        active_path = incomplete_paths.pop()
        active_head = active_path[-1]

        if active_head == end_loc:
            complete_paths.append(active_path)
        else:
            # cur_cost_to_head = len(active_path)
            # # cur_guess_total = walkable_points - cur_cost_to_head - cmp_manhattan(active_head, end_loc)
            # if cur_cost_to_head > longest_known_cost[active_head]:
            #     longest_known_cost[active_head] = cur_cost_to_head
            #     # longest_guess_total_cost[active_head] = cur_guess_total
            new_paths = []
            for d in directions:
                if trail_info[active_head + d] != '#':
                    if active_head + d not in active_path:
                        new_path = active_path[::]
                        new_path.append(active_head + d)
                        new_paths.append(new_path)
            if len(new_paths) == 0:
                dead_end_paths.append(active_path)
            else:
                for np in new_paths:
                    cur_trail_type = trail_info[np[-1]]
                    if cur_trail_type in slope_force_map.keys():
                        if np[-1] + slope_force_map[cur_trail_type] in np:
                            dead_end_paths.append(np)
                        else:
                            np.append(np[-1] + slope_force_map[cur_trail_type])
                            incomplete_paths.append(np)
                    else:
                        incomplete_paths.append(np)

    return max(map(lambda p: len(p) - 1, complete_paths))


# part 1
print(long_a_star())


def bfs(i_start, i_end, i_excl):
    # allow start and end to be in exclude, but we discount that possibility later
    # this lets us pass the whole junction list into the function, instead of pre-removing start and end
    paths = [[i_start]]
    while paths:
        cur_path = paths.pop()
        if cur_path[-1] == i_end:
            return cur_path
        else:
            new_heads = []
            for d in directions:
                potential_new_head = cur_path[-1] + d
                if trail_info[potential_new_head] == '#':
                    pass
                elif potential_new_head in cur_path:
                    pass
                elif potential_new_head != i_end and potential_new_head in i_excl:
                    pass
                else:
                    new_heads.append(potential_new_head)
        for nh in new_heads:
            np = cur_path[::]
            np.append(nh)
            paths.append(np)
    return "Not Found"


def bfs_to_first_junction(i_start, i_junctions):
    # allow start and end to be in exclude, but we discount that possibility later
    # this lets us pass the whole junction list into the function, instead of pre-removing start and end
    paths = [[i_start]]
    while paths:
        cur_path = paths.pop()
        if cur_path[-1] in i_junctions:
            return cur_path
        else:
            new_heads = []
            for d in directions:
                potential_new_head = cur_path[-1] + d
                if trail_info[potential_new_head] == '#':
                    pass
                elif potential_new_head in cur_path:
                    pass
                else:
                    new_heads.append(potential_new_head)
        for nh in new_heads:
            np = cur_path[::]
            np.append(nh)
            paths.append(np)
    return "Not Found"


junctions = []
for k, v in trail_info.items():
    if v != '#':
        branch_count = list(map(lambda pt: trail_info[pt] != '#', [k + d for d in directions])).count(True)
        if branch_count > 2:
            junctions.append(k)

path_weights = {}
for j1 in junctions:
    for j2 in junctions:
        if j1 != j2:
            c_bfs = bfs(j1, j2, junctions)
            if c_bfs != 'Not Found':
                path_weights[(j1, j2)] = len(bfs(j1, j2, junctions)) - 1

start_to_first_junction = bfs_to_first_junction(start_loc, junctions)
end_to_last_junction = bfs_to_first_junction(end_loc, junctions)

path_weights[(start_loc, start_to_first_junction[-1])] = len(start_to_first_junction) - 1
path_weights[(end_loc, end_to_last_junction[-1])] = len(end_to_last_junction) - 1
path_weights[(start_to_first_junction[-1], start_loc)] = len(start_to_first_junction) - 1
path_weights[(end_to_last_junction[-1], end_loc)] = len(end_to_last_junction) - 1


def path_total_weight(i_path):
    if len(i_path) < 2:
        return 0
    else:
        out_weight = 0
        for i in range(len(i_path) - 1):
            out_weight += path_weights[(i_path[i], i_path[i + 1])]
        return out_weight


# assuming that each sub path is in path_weights twice, once forwards and once backwards
trail_total_weight = sum([v for v in path_weights.values()]) / 2

neighbor_hash = {}
for k, v in path_weights.items():
    lk, rk = k
    if lk not in neighbor_hash.keys():
        neighbor_hash[lk] = [rk]
    else:
        neighbor_hash[lk].append(rk)


def pathy_long_a_star(i_start, i_end):
    incomplete_paths = [[i_start]]
    dead_end_paths = []
    complete_paths = []

    best_found = -1

    # longest_known_cost = {}
    # longest_guess_total_cost = {}
    # for j in junctions:
    #     longest_guess_total_cost[j] = -1
    #     longest_known_cost[j] = -1
    # longest_known_cost[i_start] = -1
    # longest_known_cost[i_end] = -1
    # longest_guess_total_cost[i_start] = -1
    # longest_guess_total_cost[i_end] = -1

    while incomplete_paths:
        # incomplete_paths.sort(key=lambda pt: path_total_weight(pt))
        active_path = incomplete_paths.pop()
        active_head = active_path[-1]

        if active_head == i_end:
            x_tot = path_total_weight(active_path)
            if x_tot > best_found:
                best_found = x_tot
                print(x_tot)
                complete_paths.append(active_path)
        else:
            # cur_cost_to_head = path_total_weight(active_path)
            # cur_guess_total = trail_total_weight - cur_cost_to_head
            # if cur_cost_to_head > longest_known_cost[active_head]:
            #     longest_known_cost[active_head] = cur_cost_to_head
            #     longest_guess_total_cost[active_head] = cur_guess_total
            # neighbors = [k[1] for k, v in path_weights.items() if k[0] == active_head and k[1] not in active_path]
            neighbors = neighbor_hash[active_head]
            if len(neighbors) == 0:
                dead_end_paths.append(active_path)
            for ng in neighbors:
                if ng not in active_path:
                    new_path = active_path[::]
                    new_path.append(ng)
                    incomplete_paths.append(new_path)

    return complete_paths


print(max(map(lambda p: path_total_weight(p), pathy_long_a_star(start_loc, end_loc))))
