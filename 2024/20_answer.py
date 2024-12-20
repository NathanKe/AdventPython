import math
from collections import defaultdict
from collections import Counter

map_lines = open('20_input').read().splitlines()

map_dict = defaultdict(lambda: '#')
start = None
end = None
cheat_removals = []

for ri, rv in enumerate(map_lines):
    for ci, cv in enumerate(rv):
        cur_loc = ri + 1j * ci
        map_dict[cur_loc] = cv
        if cv == "S":
            start = cur_loc
        if cv == "E":
            end = cur_loc

main_path = [k for k, v in map_dict.items() if v == '.' or v == 'S']

for n in main_path:
    for direction in [1, -1, 1j, -1j]:
        if map_dict[n + direction] == '#' and map_dict[n + direction + direction] in ('.', 'E'):
            cheat_removals.append((n, n + direction, n + direction + direction))

low_cost_dict = defaultdict(lambda: math.inf)
frontier = [start]
low_cost_dict[start] = 0
while frontier:
    cur_expandee = frontier.pop()
    cur_cost = low_cost_dict[cur_expandee]
    for i_dir in [1, -1, 1j, -1j]:
        cur_ng = cur_expandee + i_dir
        if map_dict[cur_ng] != '#':
            if cur_cost + 1 < low_cost_dict[cur_ng]:
                low_cost_dict[cur_ng] = cur_cost + 1
                frontier.append(cur_ng)

cheat_savings = [low_cost_dict[c[2]] - low_cost_dict[c[0]] - 2 for c in cheat_removals]

print(len([cs for cs in cheat_savings if cs >= 100]))


def manhattan_teleports(i_loc, i_len):
    manhat_shell = set()
    for vert in range(i_len + 1):
        for horz in range(i_len + 1):
            if vert + horz == i_len:
                manhat_shell.add((i_loc, i_loc + vert + 1j * horz, i_len))
                manhat_shell.add((i_loc, i_loc - vert + 1j * horz, i_len))
                manhat_shell.add((i_loc, i_loc + vert - 1j * horz, i_len))
                manhat_shell.add((i_loc, i_loc - vert - 1j * horz, i_len))
    return list(manhat_shell)


max_cheat_len = 20

all_valid_manhat_cheats = []

for cheat_start in main_path:
    for cheat_len in range(2, max_cheat_len + 1):
        cur_manhat_teleports = manhattan_teleports(cheat_start, cheat_len)
        all_valid_manhat_cheats.extend([c_m_t for c_m_t in cur_manhat_teleports if map_dict[c_m_t[1]] in ['.', 'E']])

manhat_cheat_savings = [low_cost_dict[v_m_t[1]] - low_cost_dict[v_m_t[0]] - v_m_t[2]
                        for v_m_t in all_valid_manhat_cheats]

print(len([cs for cs in manhat_cheat_savings if cs >= 100]))
