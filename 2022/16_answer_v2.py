import re
from collections import defaultdict
from collections import deque
from itertools import combinations

data_lines = open('16_input').read().splitlines()

edges = []
non_zero_valve_list = []
valve_flow_map = {}
adjacency_map = {}
initial_valve_state = ""

print("Parsing Data...")
for line in data_lines:
    regex_parse = re.match(r"Valve (\w{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)$", line)
    cur_valve = regex_parse.group(1)
    cur_flow = int(regex_parse.group(2))
    if cur_flow > 0:
        non_zero_valve_list.append(cur_valve)
    cur_connections = regex_parse.group(3).split(", ")
    valve_flow_map[cur_valve] = cur_flow
    initial_valve_state += cur_valve
    for conn in cur_connections:
        if cur_valve in adjacency_map.keys():
            adjacency_map[cur_valve].add(conn)
        else:
            adjacency_map[cur_valve] = {conn}
        edges.append((cur_valve, conn))


def bfs(start, end):
    if start == end:
        return 0
    paths = deque([[start]])
    while paths:
        path = paths.pop()
        next_steps = adjacency_map[path[-1]]
        if next_steps:
            if end in next_steps:
                path.append(end)
                return path
            else:
                for step in next_steps:
                    if step not in path:
                        n_p = path[:]
                        n_p.append(step)
                        paths.appendleft(n_p)
    return "No Solution"


print("Generating Distance Lookup...")
distance_lookup = {}
for xa in adjacency_map.keys():
    for xb in adjacency_map.keys():
        if xa != xb and (xa == 'AA' or xb == 'AA') or (
                xa != xb and valve_flow_map[xa] != 0 and valve_flow_map[xb] != 0):
            distance_lookup[(xa, xb)] = len(bfs(xa, xb)) - 1
            distance_lookup[(xb, xa)] = len(bfs(xb, xa)) - 1

# def deserialize(valve_list):
#     return "|".join(valve_list)
#
#
# def key_gen(open_valves, steps_remaining, location):
#     return deserialize(open_valves) + str(steps_remaining) + location
#
#
# memoized_lookup = defaultdict(lambda: float('inf'))
#

# def best_flow(open_valves, steps_remaining, location):
#     one_more_tick_of_currently_open_valves = sum([valve_flow_map[v] for v in open_valves])
#
#     cur_key = key_gen(open_valves, steps_remaining, location)
#
#     # pre cached, return it
#     if memoized_lookup[cur_key] < float('inf'):
#         return memoized_lookup[cur_key]
#     # out of time, no more flow
#     if steps_remaining == 0:
#         memoized_lookup[cur_key] = 0
#         return 0
#     # one more step, one more flow tick
#     elif steps_remaining == 1:
#         memoized_lookup[cur_key] = one_more_tick_of_currently_open_valves
#         return one_more_tick_of_currently_open_valves
#     # everything open, let it run
#     elif len(open_valves) == len(non_zero_valve_list):
#         memoized_lookup[cur_key] = steps_remaining * one_more_tick_of_currently_open_valves
#         return memoized_lookup[cur_key]
#     # options exist!
#     else:
#         options = []
#
#         # first option is to do nothin
#         do_nothing_tuple = (open_valves, steps_remaining - 1, location)
#         do_nothing_key = key_gen(*do_nothing_tuple)
#         if memoized_lookup[do_nothing_key] < float('inf'):
#             options.append(one_more_tick_of_currently_open_valves + memoized_lookup[do_nothing_key])
#         else:
#             sub_res = best_flow(*do_nothing_tuple)
#             memoized_lookup[do_nothing_key] = sub_res
#             options.append(one_more_tick_of_currently_open_valves + sub_res)
#
#         # next option is to open current valve
#         if location not in open_valves and location:
#             new_open_valves = open_valves[:]
#             new_open_valves.append(location)
#             open_current_valve_tuple = (new_open_valves, steps_remaining - 1, location)
#             open_current_valve_key = key_gen(*open_current_valve_tuple)
#             if memoized_lookup[open_current_valve_key] < float('inf'):
#                 options.append(one_more_tick_of_currently_open_valves + memoized_lookup[open_current_valve_key])
#             else:
#                 sub_res = best_flow(*open_current_valve_tuple)
#                 memoized_lookup[open_current_valve_key] = sub_res
#                 options.append(one_more_tick_of_currently_open_valves + sub_res)
#
#         # next option is to go to another valve
#         for n_z_v in non_zero_valve_list:
#             if n_z_v != location and n_z_v not in open_valves:
#                 dist = distance_lookup[(location, n_z_v)]
#                 if dist <= steps_remaining:
#                     go_to_another_valve_tuple = (open_valves, steps_remaining - dist, n_z_v)
#                     go_to_another_valve_key = key_gen(*go_to_another_valve_tuple)
#                     if memoized_lookup[go_to_another_valve_key] < float('inf'):
#                         options.append(
#                             one_more_tick_of_currently_open_valves * dist + memoized_lookup[go_to_another_valve_key])
#                     else:
#                         sub_res = best_flow(*go_to_another_valve_tuple)
#                         memoized_lookup[go_to_another_valve_key] = sub_res
#                         options.append(one_more_tick_of_currently_open_valves * dist + sub_res)
#
#         return max(options)
#
#
# print("Calculating Best Flow...")
# print("Part 1: ", best_flow([], 30, 'AA'))

# labor_divisons = []
# for human_valve_count in range(len(non_zero_valve_list) + 1):
#     human_sets_of_cur_count = combinations(non_zero_valve_list, human_valve_count)
#     for human_set in human_sets_of_cur_count:
#         elephant_set = [v for v in non_zero_valve_list if v not in human_set]
#         labor_divisons.append((list(human_set), elephant_set))


flow_res_memo = {}
extra_flow_memo = {}


def flow_result(path_taken, steps_rem):
    cur_key = "".join(path_taken) + str(steps_rem)

    if cur_key in flow_res_memo.keys():
        return flow_res_memo[cur_key]
    else:
        path_taken = deque(path_taken)
        flow = 0
        cur_pt = path_taken.popleft()
        while path_taken:
            next_pt = path_taken.popleft()
            steps_rem -= (distance_lookup[(cur_pt, next_pt)] + 1)
            flow += valve_flow_map[next_pt] * steps_rem
            cur_pt = next_pt

        flow_res_memo[cur_key] = flow
        return flow


def theoretical_extra_flow(path_taken, steps_rem):
    cur_key = "".join(path_taken) + str(steps_rem)
    if cur_key in extra_flow_memo.keys():
        return extra_flow_memo[cur_key]
    else:
        closed_valves = set(non_zero_valve_list).difference(set(path_taken))
        extra = sum([valve_flow_map[v] for v in closed_valves]) * steps_rem
        extra_flow_memo[cur_key] = extra
        return extra


def paths_of_max_length(max_len):
    complete_paths = []
    in_progress_paths = deque([['AA', nz] for nz in non_zero_valve_list])

    while in_progress_paths:
        path = in_progress_paths.pop()
        path_cost = sum([distance_lookup[(path[i], path[i + 1])] for i in range(len(path) - 1)])
        if path_cost <= max_len:
            # all valves visited
            if len(path) == len(non_zero_valve_list) + 1:
                complete_paths.append(path)
            for ns in non_zero_valve_list:
                if ns not in path:
                    path_x = path[:]
                    path_x.append(ns)
                    in_progress_paths.append(path_x)
        # path is too long
        else:
            path.pop()
            complete_paths.append(path)

    return complete_paths


print("iterating known short for human")
human_max = 0
best_human_path = None
twentySix = paths_of_max_length(26)
# for human_path in len_26_paths:
#     cur_flow = flow_result(human_path, 26)
#     if cur_flow > human_max:
#         human_max = cur_flow
#         best_human_path = human_path
#
# best_human_set_without_aa = set(best_human_path[1:])
#
# print("iterating disjoint elephant paths")
# best_overall = 0
# best_elephant_path = None
# for elephant_path in len_26_paths:
#     if best_human_set_without_aa.isdisjoint(set(elephant_path[1:])):
#         cur_flow = flow_result(elephant_path, 26)
#         if cur_flow + human_max > best_overall:
#             best_overall = cur_flow + human_max
#
# print("Part 2: ", best_overall)
#
#
# print("Done!")
