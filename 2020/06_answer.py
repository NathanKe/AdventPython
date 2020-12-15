from collections import Counter

raw_data = open('06_input').read()

group_answers = list(map(lambda x: x.split('\n'), raw_data.split('\n\n')))

print("Part 1: ", sum(map(lambda gr: len(Counter(''.join(gr))), group_answers)))

unanimous_count = 0
for group in group_answers:
    ans_dict = {}
    for person in group:
        for question in person:
            if question not in ans_dict:
                ans_dict[question] = 1
            else:
                ans_dict[question] += 1

    group_unanimous_count = len([q for q in ans_dict if ans_dict[q] == len(group)])
    unanimous_count += group_unanimous_count

print('Part 2: ', unanimous_count)
