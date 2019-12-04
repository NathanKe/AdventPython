import re

puzzle = '168630-718098'


def get_run_lens(s):
    run_lens = []
    stack = []
    cur_char = None
    for i in range(len(s)):
        if s[i] != cur_char:
            run_lens.append(len(stack))
            stack = [s[i]]
            cur_char = s[i]
        else:
            stack.append(s[i])
            if i == 5:
                run_lens.append(len(stack))
    return run_lens


def two_adjacent(s):
    return max(get_run_lens(s)) >= 2


def disjoint_two_run(s):
    return 2 in get_run_lens(s)


def non_decreasing(s):
    return sorted(s) == list(s)


def valid_1(s):
    return two_adjacent(s) and non_decreasing(s)


start, stop = map(int, puzzle.split('-'))

p1 = list(filter(valid_1, [str(i) for i in range(start, stop)]))
print('Part 1: ', len(p1))

p2 = list(filter(disjoint_two_run, p1))
print('Part 1: ', len(p2))
