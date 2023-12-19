import re
from collections import deque

rule_lines, part_lines = open('19_input').read().split('\n\n')


class Part:
    def __init__(self, i_x, i_m, i_a, i_s):
        self.x = i_x
        self.m = i_m
        self.a = i_a
        self.s = i_s
        self.result = "Unknown"

    def process(self):
        proc_res = rule_proc('in', self)
        self.result = proc_res

    def rate_sum(self):
        return self.x + self.m + self.a + self.s


rule_text = rule_lines.splitlines()
part_text = part_lines.splitlines()

rule_map = {}
for rule_str in rule_text:
    rule_lab, rule_val = rule_str[:-1].split('{')
    rule_map[rule_lab] = rule_val

part_set = []
for part_line in part_text:
    xx, mm, aa, ss = map(int, re.findall(r"\d+", part_line))
    p_o = Part(xx, mm, aa, ss)
    part_set.append(p_o)


def rule_proc(rule_label, part_obj):
    rule_components = deque(rule_map[rule_label].split(','))
    while rule_components:
        active_component = rule_components.popleft()
        if ':' in active_component:
            active_condition, active_result = active_component.split(':')
            x = part_obj.x
            m = part_obj.m
            a = part_obj.a
            s = part_obj.s
            if eval(active_condition):
                if active_result == 'A':
                    return 'Accepted'
                elif active_result == 'R':
                    return 'Rejected'
                else:
                    return rule_proc(active_result, part_obj)
        else:
            if active_component == 'A':
                return 'Accepted'
            elif active_component == 'R':
                return 'Rejected'
            else:
                return rule_proc(active_component, part_obj)


accept_sum = 0
for p in part_set:
    p.process()
    if p.result == 'Accepted':
        accept_sum += p.rate_sum()

print(accept_sum)

xr = list(range(1, 4001))
mr = list(range(1, 4001))
ar = list(range(1, 4001))
sr = list(range(1, 4001))


def split_range(i_r, i_s_v, i_cmp):
    r_start = i_r[0]
    r_end = i_r[-1]

    r_pass = None
    r_fail = None

    # split is in the middle of the range, handle fairly normally
    if r_start <= i_s_v <= r_end:
        if i_cmp == '<':
            r_pass = list(range(r_start, i_s_v))
            r_fail = list(range(i_s_v, r_end + 1))
        if i_cmp == '>':
            r_pass = list(range(i_s_v + 1, r_end + 1))
            r_fail = list(range(r_start, i_s_v + 1))
    # split is right and call is greater, nothing passes
    elif i_s_v >= r_end and i_cmp == '>':
        r_pass = []
        r_fail = i_r
    # split is left and call is less, nothing passes
    elif i_s_v <= r_start and i_cmp == '<':
        r_pass = []
        r_fail = i_r
    # split is left and call is greater, everything passes
    elif i_s_v <= r_start and i_cmp == '>':
        r_pass = i_r
        r_fail = []
    # split is right and call is less, everything passes
    elif i_s_v >= r_end and i_cmp == '<':
        r_pass = i_r
        r_fail = []
    else:
        print('fucky edge case')

    assert len(r_pass) + len(r_fail) == len(i_r)
    return r_pass, r_fail


def new_ranges(target, split_val, comparison, i_xr, i_mr, i_ar, i_sr):
    if target == 'x':
        r_pass, r_fail = split_range(i_xr, split_val, comparison)
        return (r_pass, i_mr, i_ar, i_sr), (r_fail, i_mr, i_ar, i_sr)
    elif target == 'm':
        r_pass, r_fail = split_range(i_mr, split_val, comparison)
        return (i_xr, r_pass, i_ar, i_sr), (i_xr, r_fail, i_ar, i_sr)
    elif target == 'a':
        r_pass, r_fail = split_range(i_ar, split_val, comparison)
        return (i_xr, i_mr, r_pass, i_sr), (i_xr, i_mr, r_fail, i_sr)
    elif target == 's':
        r_pass, r_fail = split_range(i_sr, split_val, comparison)
        return (i_xr, i_mr, i_ar, r_pass), (i_xr, i_mr, i_ar, r_fail)
    else:
        return 'something fucky'


full_range = [list(range(1, 4001)), list(range(1, 4001)), list(range(1, 4001)), list(range(1, 4001))]


def range_proc(rule_label, i_xr, i_mr, i_ar, i_sr):
    accept_count = 0
    reject_count = 0
    rule_components = deque(rule_map[rule_label].split(','))
    while rule_components:
        component = rule_components.popleft()
        if ':' in component:
            condition, result = component.split(':')
            attrib, compar = condition[:2]
            val = int(condition[2:])
            pass_ranges, fail_ranges = new_ranges(attrib, val, compar, i_xr, i_mr, i_ar, i_sr)
            if result == 'A':
                accept_count += len(pass_ranges[0]) * len(pass_ranges[1]) * len(pass_ranges[2]) * len(pass_ranges[3])
            elif result == 'R':
                reject_count += len(pass_ranges[0]) * len(pass_ranges[1]) * len(pass_ranges[2]) * len(pass_ranges[3])
            else:
                sub_acc, sub_rej = range_proc(result, *pass_ranges)
                accept_count += sub_acc
                reject_count += sub_rej
            i_xr, i_mr, i_ar, i_sr = fail_ranges
        else:
            if component == 'A':
                accept_count += len(i_xr) * len(i_mr) * len(i_ar) * len(i_sr)
            elif component == 'R':
                reject_count += len(i_xr) * len(i_mr) * len(i_ar) * len(i_sr)
            else:
                sub_acc, sub_rej = range_proc(component, i_xr, i_mr, i_ar, i_sr)
                accept_count += sub_acc
                reject_count += sub_rej
    return accept_count, reject_count


print(range_proc('in', *full_range)[0])
