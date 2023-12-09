import re

lines = open('09_input').read().splitlines()

histories = []
for line in lines:
    histories.append(list(map(int, re.findall(r"-?\d+", line))))


def diff_list(i_list):
    return [i_list[i + 1] - i_list[i] for i in range(len(i_list) - 1)]


def diff_chain(i_list):
    chain = [i_list]
    while True:
        diff = diff_list(i_list)
        chain.append(diff)
        if diff.count(0) == len(diff):
            break
        i_list = diff[::]
    return chain


def bubble_up(i_list):
    chain = diff_chain(i_list)
    ends = [li[-1] for li in chain]
    return sum(ends)


extrapolate_sum = sum(map(lambda li: bubble_up(li), histories))
print(extrapolate_sum)

rev_extrapolate_sum = sum(map(lambda li: bubble_up(li[::-1]), histories))
print(rev_extrapolate_sum)
