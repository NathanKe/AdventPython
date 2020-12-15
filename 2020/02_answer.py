import re
import collections as c

pswds = open('02_input').read().splitlines()


def good_pswd_1(in_line):
    m = re.match(r"(\d+)\-(\d+)\s(\w):\s(.+)", in_line)
    min_val = int(m.group(1))
    max_val = int(m.group(2))
    letter = m.group(3)
    pswd = m.group(4)

    letter_count = c.Counter(pswd)

    return min_val <= letter_count[letter] <= max_val


def good_pswd_2(in_line):
    m = re.match(r"(\d+)\-(\d+)\s(\w):\s(.+)", in_line)
    left_val = int(m.group(1))
    right_val = int(m.group(2))
    letter = m.group(3)
    pswd = m.group(4)

    return (pswd[left_val - 1] == letter) ^ (pswd[right_val - 1] == letter)


print("Part 1: ", len(list(filter(lambda p: good_pswd_1(p), pswds))))
print("Part 2: ", len(list(filter(lambda p: good_pswd_2(p), pswds))))
