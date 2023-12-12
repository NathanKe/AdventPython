import re

lines = open('12_input').read().splitlines()


def poss_by_count(i_line):
    s, n = i_line.split(" ")

    num_lst = list(map(int, re.findall(r"\d+", n)))
    pnd_lst = list(map(len, re.findall(r"#+", s)))
    if num_lst == pnd_lst:
        return True
    else:
        return False


def left_possible(i_str, i_nums):
    candidate_left = i_str.split("?")[0]
    candidate_nums = list(map(len, re.findall(r"#+", candidate_left)[:-1]))
    left_match = True
    for i in range(min(len(candidate_nums), len(i_nums))):
        if candidate_nums[i] != i_nums[i]:
            left_match = False
    return left_match


def max_possible(i_str, i_max):
    pnd_run_max = max([0] + list(map(len, re.findall(r"#+", i_str))))
    return pnd_run_max <= i_max


def arrangement_count(i_line):
    i_str, i_nums_txt = i_line.split(" ")
    i_nums = list(map(int, i_nums_txt.split(",")))

    max_run = max(i_nums)

    candidates = [i_str]
    possibilities = set()
    while candidates:
        active_candidate = candidates.pop()
        if '?' not in active_candidate:
            if poss_by_count(active_candidate + " " + i_nums_txt):
                possibilities.add(active_candidate + " " + i_nums_txt)
        else:
            left, right = re.split(r"\?", active_candidate, 1)
            dot_opt = left + "." + right
            pnd_opt = left + "#" + right
            if '?' not in dot_opt:
                candidates.append(dot_opt)
            elif max_possible(dot_opt, max_run) and left_possible(dot_opt, i_nums):
                candidates.append(dot_opt)

            if '?' not in pnd_opt:
                candidates.append(pnd_opt)
            elif max_possible(pnd_opt, max_run) and left_possible(pnd_opt, i_nums):
                candidates.append(pnd_opt)
    return len(possibilities)


print(sum(map(lambda x: arrangement_count(x), lines)))

unfold = []
for line in lines:
    ii_str, ii_num_txt = line.split(" ")
    xx_str = '?'.join([ii_str] * 5)
    xx_num_txt = ','.join(ii_num_txt.split(',') * 5)
    unfold.append(xx_str + " " + xx_num_txt)


# print(sum(map(lambda x: arrangement_count(x), unfold)))


def reduce_left(i_str, i_nums):
    if '.' not in i_str:
        return i_str, i_nums
    if len(i_nums) == 0:
        return i_str, i_nums

    splits = i_str.split(".", 1)
    left_most = splits[0]
    remainder = splits[1]
    if '?' in left_most:
        return i_str, i_nums
    else:
        if left_most.count('#') == i_nums[0]:
            return remainder, i_nums[1:]
        else:
            return i_str, i_nums


def reduce_right(i_str, i_nums):
    r_str = i_str[::-1]
    r_nums = i_nums[::-1]
    x_str, x_nums = reduce_left(r_str, r_nums)
    v_str = x_str[::-1]
    v_nums = x_nums[::-1]
    return v_str, v_nums


def trim_outside_dots(i_line):
    o_line = re.sub(r"^\.+", "", i_line)
    o_line = re.sub(r"\.+$", "", o_line)
    return o_line


def reduce_pre_trimmed(i_str, i_nums):
    rx_left = reduce_left(i_str, i_nums)
    rx_right = reduce_right(*rx_left)
    full_rx = trim_outside_dots(rx_right[0]) + " " + ','.join(map(str, rx_right[1]))
    return full_rx


def reduce_untrimmed(i_line):
    i_str, i_num_txt = i_line.split(" ")
    i_str = trim_outside_dots(i_str)
    i_nums = list(map(int, re.findall(r"\d+", i_num_txt)))
    return reduce_pre_trimmed(i_str, i_nums)


arrange_hash = {}


def purely_correct(i_line):
    assert "?" not in i_line
    i_str, i_num_txt = i_line.split(" ")
    i_nums = list(map(int, re.findall(r"\d+", i_num_txt)))
    pnd_cnt = list(map(len, re.findall(r"#+", i_str)))
    res = pnd_cnt == i_nums
    print("PURE", i_str, i_nums, res)
    return


def left_fail(i_line):
    i_str, i_num_txt = i_line.split(" ")
    i_nums = [0] + list(map(int, re.findall(r"\d+", i_num_txt)))

    candidate_left = i_str.split("?")[0]
    candidate_nums = list(map(len, re.findall(r"#+", candidate_left)[:-1]))
    left_match = True
    for i in range(min(len(candidate_nums), len(i_nums))):
        if candidate_nums[i] != i_nums[i]:
            left_match = False
            break
    print('LEFT', i_str, i_num_txt, left_match)
    return not left_match


def max_fail(i_line):
    i_str, i_num_txt = i_line.split(" ")
    i_nums = [0] + list(map(int, re.findall(r"\d+", i_num_txt)))
    pnd_cnt = [0] + list(map(len, re.findall(r"#+", i_str)))
    res = max(pnd_cnt) > max(i_nums)
    print('MAX', i_str, pnd_cnt, i_num_txt, res)
    return res


def arrangement_count_2(i_line):
    r_line = reduce_untrimmed(i_line)
    if r_line in arrange_hash.keys():
        return arrange_hash[r_line]
    else:
        if "?" not in r_line:
            if purely_correct(r_line):
                arrange_hash[r_line] = 1
                return 1
            else:
                arrange_hash[r_line] = 0
                return 0
        elif left_fail(i_line):
            arrange_hash[r_line] = 0
            return 0
        elif max_fail(i_line):
            arrange_hash[r_line] = 0
            return 0
        else:
            left, right = re.split(r"\?", r_line, 1)
            dot_opt = left + "." + right
            pnd_opt = left + "#" + right
            split_possibilites = arrangement_count_2(dot_opt) + arrangement_count_2(pnd_opt)
            arrange_hash[r_line] = split_possibilites
            arrange_hash[i_line] = split_possibilites
            return split_possibilites


# print(sum(map(lambda l: arrangement_count_2(l), unfold)))
