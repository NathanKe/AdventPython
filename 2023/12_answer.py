import re

lines = open('12_input').read().splitlines()


# what a mess
# at its heart, this is recursion + memoization
# but good lord, what a cluster
# reduction logic to try to get to previously solved steps
# lots of quasi manual pruning rules to short cut dead end branchings
# probably losing lots of speed on function call overhead, but only way I could stay sane

def string_and_num_list(i_line):
    i_str, i_num_txt = i_line.split(" ")
    i_nums = list(map(int, re.findall(r"\d+", i_num_txt)))
    return i_str, i_nums


# reduction functions - left, right, both
def reduce_left(i_str, i_nums):
    if "_" not in i_str:
        return i_str, i_nums
    if len(i_nums) == 0:
        return i_str, i_nums

    splits = i_str.split("_", 1)
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
    o_line = re.sub(r"^_+", "", i_line)
    o_line = re.sub(r"_+$", "", o_line)
    return o_line


def reduce_pre_trimmed(i_str, i_nums):
    rx_left = reduce_left(i_str, i_nums)
    rx_right = reduce_right(*rx_left)
    full_rx = trim_outside_dots(rx_right[0]) + " " + ','.join(map(str, rx_right[1]))
    return full_rx


def reduce_untrimmed(i_line):
    while True:
        i_str, i_nums = string_and_num_list(i_line)
        redux_one = reduce_pre_trimmed(i_str, i_nums)
        if redux_one == i_line:
            return redux_one
        else:
            i_line = redux_one


def valid_final_arrangement(i_line):
    if "?" in i_line:
        return False
    i_str, i_nums = string_and_num_list(i_line)
    pound_runs = re.findall(r"#+", i_str)
    pound_lens = list(map(len, pound_runs))
    if pound_lens == i_nums:
        return True
    else:
        return False


def dead_end_by_max_error(i_line):
    i_str, i_nums = string_and_num_list(i_line)
    pound_runs = re.findall(r"#+", i_str)
    longest_pound_run = max([0] + list(map(len, pound_runs)))
    biggest_allowed_pound_run = max([0] + i_nums)
    if longest_pound_run > biggest_allowed_pound_run:
        return True
    return False


def dead_end_by_too_many_pounds(i_line):
    i_str, i_nums = string_and_num_list(i_line)
    pound_count = i_str.count('#')
    if pound_count > sum(i_nums):
        return True
    return False


def dead_end_by_length_mismatch(i_line):
    i_str, i_nums = string_and_num_list(i_line)
    non_dot_char_count = len(i_str) - i_str.count("_")
    if non_dot_char_count < sum(i_nums):
        return True
    else:
        return False


def dead_end_by_packing(i_line):
    i_str, i_nums = string_and_num_list(i_line)
    if len(i_str) < sum(i_nums) + len(i_nums) - 1:
        return True
    return False


def dead_end_by_sequence_error(i_line):
    i_str, i_nums = string_and_num_list(i_line)
    first_pound_to_question_match_info = re.search(r"#*\?", i_str)
    if not first_pound_to_question_match_info:
        left_sub = i_str
    else:
        left_sub = i_str[:first_pound_to_question_match_info.start()]
    pound_runs = re.findall(r"#+", left_sub)
    pound_lens = list(map(len, pound_runs))
    sequence_fail = False
    for i in range(min(len(pound_lens), len(i_nums))):
        if i_nums[i] != pound_lens[i]:
            sequence_fail = True
            break

    return sequence_fail


def dead_end_arrangement(i_line):
    return dead_end_by_length_mismatch(i_line) or dead_end_by_max_error(i_line) or dead_end_by_sequence_error(i_line)


arrange_hash = {}


def only_one_way_to_do_nothing(i_line):
    i_str, i_nums = string_and_num_list(i_line)
    if '#' not in i_str and not i_nums:
        return True
    else:
        return False


def arrangement_count(i_line, recur):
    # if it exists, we're done
    if i_line in arrange_hash.keys():
        return arrange_hash[i_line]

    # reduce it - peeling off 'solved' front and back
    r_line = reduce_untrimmed(i_line)
    # if we've been here before, we're done
    if r_line in arrange_hash.keys():
        return arrange_hash[r_line]

    # bunch of leftover question marks and spaces, no digits left.
    # There's only one way to do nothing
    if only_one_way_to_do_nothing(r_line):
        arrange_hash[r_line] = 1
        return 1

    # if we have more numbers at the end of our string, it can't be done
    r_str, r_nums = string_and_num_list(r_line)
    if r_nums and not r_str:
        arrange_hash[r_line] = 0
        return 0

        # if we're done, check if it is valid
    if valid_final_arrangement(r_line):
        arrange_hash[r_line] = 1
        return 1

    # apply packing rule, string needs to be long enough for the configuration
    if dead_end_by_packing(r_line):
        arrange_hash[r_line] = 0
        return 0

    # apply too many pounds rule, can't have more pounds than requested numbers
    if dead_end_by_too_many_pounds(r_line):
        arrange_hash[r_line] = 0
        return 0

    # apply length mismatch rule, need enough raw character length for the request
    if dead_end_by_length_mismatch(r_line):
        arrange_hash[r_line] = 0
        return 0

    # apply sequence error rule, if the 'solved' sequence up to the first ? doesn't match the goal, prune it!
    if dead_end_by_sequence_error(r_line):
        arrange_hash[r_line] = 0
        return 0

    # apply the max pound rule, if we have a string of pounds longer than the longest requested, prune it!
    if dead_end_by_max_error(r_line):
        arrange_hash[r_line] = 0
        return 0

    # we're neither dead nor finished.  Time to branch!
    # assert "?" in r_line
    left, right = re.split(r"\?", r_line, 1)
    dot_opt = left + "_" + right
    pnd_opt = left + "#" + right
    split_possibilites = arrangement_count(dot_opt, recur + "-") + arrangement_count(pnd_opt, recur + "-")
    arrange_hash[r_line] = split_possibilites
    arrange_hash[i_line] = split_possibilites
    return split_possibilites


print(sum(map(lambda l: arrangement_count(l, "-"), lines)))


def unfold(i_line):
    i_str, i_nums = string_and_num_list(i_line)
    x_str = '?'.join([i_str] * 5)
    x_num_txt = ','.join(map(str, i_nums * 5))
    return x_str + " " + x_num_txt


print(sum(map(lambda l: arrangement_count(unfold(l), "-"), lines)))
