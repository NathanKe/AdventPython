import re
import collections

puzzle = open('09_input').read()


def expand_1(comp_str):
    comp_deque = collections.deque(comp_str)
    result = ""
    while len(comp_deque) > 0:
        cur_char = comp_deque.popleft()
        if cur_char == "(":
            paren = ""
            while cur_char != ")":
                cur_char = comp_deque.popleft()
                paren += cur_char
            ln, ct = map(int, re.match(r"(\d+)x(\d+)\)", paren).groups())
            capt = ""
            for i in range(ln):
                capt += comp_deque.popleft()
            repetitions = capt * ct
            result += repetitions
        else:
            result += cur_char
    return result


def expand_2(comp_str):
    comp_deque = collections.deque(comp_str)
    exp_len = 0
    while len(comp_deque) > 0:
        cur_char = comp_deque.popleft()
        if cur_char == "(":
            paren = ""
            while cur_char != ")":
                cur_char = comp_deque.popleft()
                paren += cur_char
            ln, ct = map(int, re.match(r"(\d+)x(\d+)\)", paren).groups())
            capt = ""
            for i in range(ln):
                capt += comp_deque.popleft()
            capt_len = len(capt)
            if "(" in capt:
                capt_len = expand_2(capt)
            exp_len += capt_len * ct
        else:
            exp_len += 1
    return exp_len


print('Part 1: ', len(expand_1(puzzle)))
print('Part 2: ', expand_2(puzzle))
