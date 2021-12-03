from collections import Counter

diag_report = open('03_input').read().splitlines()

rep_lists = list(map(list, diag_report))
pos_lists = [*zip(*rep_lists)]


def most_common(a):
    co = Counter(a)
    return co.most_common(1)[0][0]


def least_common(a):
    co = Counter(a)
    return co.most_common()[-1][0][0]


gamma_str = ''.join(list(map(most_common, pos_lists)))
epsilon_str = ''.join(list(map(least_common, pos_lists)))


print("Part 1: ", int(gamma_str, 2) * int(epsilon_str, 2))


def most_common_1_tie_break(a):
    co = Counter(a)
    x, y = co.most_common(2)
    if x[1] == y[1]:
        return '1'
    else:
        return x[0]


def least_common_0_tie_break(a):
    co = Counter(a)
    x = co.most_common()[-1]
    y = co.most_common()[-2]
    if x[1] == y[1]:
        return '0'
    else:
        return x[0]


ox_index = 0
rep_for_ox = rep_lists.copy()
while len(rep_for_ox) > 1:
    most_common_at_cur_pos = most_common_1_tie_break(map(lambda x: x[ox_index], rep_for_ox))
    rep_for_ox = list(filter(lambda x: x[ox_index] == most_common_at_cur_pos, rep_for_ox))
    ox_index += 1

co_index = 0
rep_for_co = rep_lists.copy()
while len(rep_for_co) > 1:
    least_common_at_cur_pos = least_common_0_tie_break(map(lambda x: x[co_index], rep_for_co))
    rep_for_co = list(filter(lambda x: x[co_index] == least_common_at_cur_pos, rep_for_co))
    co_index += 1


ox_rate = int(''.join(rep_for_ox[0]), 2)
co_rate = int(''.join(rep_for_co[0]), 2)

print("Part 2: ", ox_rate * co_rate)
