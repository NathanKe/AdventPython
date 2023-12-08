import re
import math

right_left_text, elem_lines = open('08_input').read().split("\n\n")

right_left = list(right_left_text)


elem_dict = {}
for line in elem_lines.splitlines():
    match_info = re.search(r"(.+)\s=\s\((.+),\s(.+)\)", line)
    node, left, right = match_info.groups()
    elem_dict[node] = [left, right]


cur_node = "AAA"
step_count = 0
while cur_node != 'ZZZ':
    rl_ind = step_count % len(right_left)
    if right_left[rl_ind] == 'R':
        cur_node = elem_dict[cur_node][1]
    else:
        cur_node = elem_dict[cur_node][0]
    step_count += 1

print(step_count)


end_z_count = len([node for node in elem_dict.keys() if node[-1] == 'Z'])
end_a_list = [node for node in elem_dict.keys() if node[-1] == 'Z']

a_to_z_distances = []

for a_node in end_a_list:
    cur_node = a_node
    distance_map = {}
    step_count = 0
    while True:
        rl_ind = step_count % len(right_left)
        if right_left[rl_ind] == 'R':
            cur_node = elem_dict[cur_node][1]
        else:
            cur_node = elem_dict[cur_node][0]
        step_count += 1
        ind_node = str(rl_ind) + ":" + cur_node
        if ind_node not in distance_map.keys():
            distance_map[ind_node] = step_count
        else:
            break
    for item in distance_map.items():
        if item[0][-1] == 'Z':
            a_to_z_distances.append((a_node, item[1]))


result = math.lcm(*[tu[1] for tu in a_to_z_distances])
print(result)
