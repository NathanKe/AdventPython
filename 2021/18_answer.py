import re
from math import floor, ceil
from collections import deque
import json

snail_nums = open('18_input').read().splitlines()


def snail_explode(sn):
    sn_r = deque(sn)
    sn_l = deque()
    depth = 0
    five_deep = False
    while sn_r and not five_deep:
        ch = sn_r.popleft()
        sn_l.append(ch)
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1

        if depth == 5:
            sn_r.appendleft(sn_l.pop())
            five_deep = True

    if five_deep:
        left = ''.join(sn_l)
        right = ''.join(sn_r)

        pair_to_explode = re.search(r'(\[\d+,\d+\])', right).groups()[0]
        pair_left, pair_right = pair_to_explode[1:-1].split(',')
        pair_left_int = int(pair_left)
        pair_right_int = int(pair_right)

        right = right[len(pair_to_explode):]

        left_reg_nums = re.findall(r'\d+', left)
        right_reg_nums = re.findall(r'\d+', right)

        if left_reg_nums:
            last_left = left_reg_nums[-1]
            new_last_left = int(last_left) + pair_left_int
            left_rev = left[::-1]
            rev_repl = left_rev.replace(last_left[::-1], str(new_last_left)[::-1], 1)
            left = rev_repl[::-1]
        if right_reg_nums:
            first_right = right_reg_nums[0]
            new_first_right = int(first_right) + pair_right_int
            right = right.replace(first_right, str(new_first_right), 1)

        sn = left + '0' + right
        return sn, True
    else:
        return sn, False


def snail_split(sn):
    reg_search_res = re.search(r'(\d{2,})', sn)

    if reg_search_res:
        first_num = reg_search_res.groups()[0]
        low_left = str(floor(int(first_num) / 2))
        high_right = str(ceil(int(first_num) / 2))
        new_pair = "[" + low_left + "," + high_right + "]"
        sn = sn.replace(first_num, new_pair, 1)
        return sn, True
    else:
        return sn, False


def snail_reduce(sn):
    sn, exploded = snail_explode(sn)
    if not exploded:
        sn, splitted = snail_split(sn)
        if not splitted:
            return sn
    return snail_reduce(sn)


def snail_add(a, b):
    return snail_reduce("[" + a + "," + b + "]")


def snail_listify(sn):
    return json.loads(sn)


def snail_magnitude(sn_li):
    if type(sn_li) == int:
        return sn_li
    else:
        return 3 * snail_magnitude(sn_li[0]) + 2 * snail_magnitude(sn_li[1])


def snail_homework(sn_nums):
    sn_sum = sn_nums[0]

    for sn_n in sn_nums[1:]:
        sn_sum = snail_add(sn_sum, sn_n)
    return snail_magnitude(snail_listify(sn_sum))


print("Part 1: ", snail_homework(snail_nums))

max_mag = 0
for x in snail_nums:
    for y in snail_nums:
        if x == y:
            continue
        xy_mag = snail_magnitude(snail_listify(snail_add(x, y)))
        if xy_mag > max_mag:
            max_mag = xy_mag

        yx_mag = snail_magnitude(snail_listify(snail_add(y, x)))
        if yx_mag > max_mag:
            max_mag = yx_mag

print("Part 2: ", max_mag)
