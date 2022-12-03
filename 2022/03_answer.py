rucks = open('03_input').read().splitlines()

priority_hash = {}
for lower_case_index in range(97, 123):
    priority_hash[chr(lower_case_index)] = lower_case_index - 96

for upper_case_index in range(65, 91):
    priority_hash[chr(upper_case_index)] = upper_case_index - 38

common_prop_sum = 0
for ruck in rucks:
    ruck_list = list(ruck)
    left_ruck_list = ruck_list[:len(ruck_list) // 2]
    right_ruck_list = ruck_list[len(ruck_list) // 2:]
    common = set(left_ruck_list) & set(right_ruck_list)
    for c in common:
        common_prop_sum += priority_hash[c]

print("Part 1: ", common_prop_sum)

groups_of_three = [rucks[i: i + 3] for i in range(0, len(rucks), 3)]
badge_sum = 0
for group in groups_of_three:
    common = set(group[0]) & set(group[1]) & set(group[2])
    for c in common:
        badge_sum += priority_hash[c]

print("Part 2: ", badge_sum)
