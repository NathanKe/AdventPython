import re
from collections import deque

line_info = open('20_input').read().splitlines()

flip_state_map = {}
orig_dest_map = {}
orig_type_map = {}
conj_mods = []
for line in line_info:
    match_info = re.search(r"([%|&])?(.+)\s->\s(.+)", line)
    c_type, c_lab, c_dst_text = match_info.groups()
    c_dst_lst = c_dst_text.split(", ")

    orig_dest_map[c_lab] = c_dst_lst
    orig_type_map[c_lab] = c_type

    if c_type == '%':
        flip_state_map[c_lab] = 'off'
    if c_type == '&':
        conj_mods.append(c_lab)

conj_mem_map = {}
for cj_m in conj_mods:
    conj_mem_map[cj_m] = {}
    for line in line_info:
        match_info = re.search(r"([%|&])?(.+)\s->\s(.+)", line)
        c_type, c_lab, c_dst_text = match_info.groups()
        c_dst_lst = c_dst_text.split(", ")
        if cj_m in c_dst_lst:
            conj_mem_map[cj_m][c_lab] = 'low'


def handle(i_src, i_lvl, i_dst):
    o_lvl = None
    if i_src == 'button':
        assert i_dst == 'broadcaster'
        o_lvl = i_lvl
    elif i_dst not in orig_dest_map.keys():
        return []
    else:
        i_type = orig_type_map[i_dst]
        if i_type == '%':
            if i_lvl == 'high':
                return []
            else:
                i_flip_state = flip_state_map[i_dst]
                if i_flip_state == 'off':
                    flip_state_map[i_dst] = 'on'
                    o_lvl = 'high'
                else:
                    flip_state_map[i_dst] = 'off'
                    o_lvl = 'low'
        elif i_type == '&':
            conj_mem_map[i_dst][i_src] = i_lvl
            relevant_history = conj_mem_map[i_dst]
            all_inputs_high = all(map(lambda v: v == 'high', [v for v in relevant_history.values()]))
            if all_inputs_high:
                o_lvl = 'low'
            else:
                o_lvl = 'high'
        else:
            o_lvl = 'XXXXXX'
    follow_on_calls = []
    for f in orig_dest_map[i_dst]:
        follow_on_calls.append((i_dst, o_lvl, f))
    return follow_on_calls


high_count = 0
low_count = 0
for i in range(1000):
    calls_to_make = deque([('button', 'low', 'broadcaster')])
    while calls_to_make:
        cur_call = calls_to_make.popleft()
        if cur_call[1] == 'low':
            low_count += 1
        else:
            high_count += 1
        new_calls = handle(*cur_call)
        for nc in new_calls:
            calls_to_make.append(nc)

print(high_count * low_count)
