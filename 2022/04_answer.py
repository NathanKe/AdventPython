import re

assignment_pairs_strings = open('04_input').read().splitlines();


def assignment_string_to_data(assignment_string):
    low_left, high_left, low_right, high_right = map(int, re.split(',|-', assignment_string))
    left_set = set(range(low_left, high_left + 1))
    right_set = set(range(low_right, high_right + 1))
    return left_set, right_set


fully_contain_count = 0
overlap_count = 0
for assignment_pair in assignment_pairs_strings:
    left, right = assignment_string_to_data(assignment_pair)
    # check non-empty set intersection
    if any(left & right):
        overlap_count += 1
        # check if either is subset of the other
        if left <= right or right <= left:
            fully_contain_count += 1

print("Part 1: ", fully_contain_count)
print("Part 2: ", overlap_count)
