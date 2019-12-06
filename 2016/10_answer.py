import re
import collections

lines = open('10_input').read().splitlines()
all_lines = '|'.join(lines)

frontier = collections.deque([(208, 3, 19)])
solved = []
outs = []
orphans = []

direct_inputs = {}
for line in lines:
    m = re.match(r"value (\d+) goes to bot (\d+)", line)
    if m:
        v, b = m.groups()
        direct_inputs[int(b)] = int(v)


def get_outs(p_bot):
    low_type, low_num, high_type, high_num = \
        re.search(r"bot " + str(p_bot) + r" gives low to (output|bot) (\d+) and high to (output|bot) (\d+)",
                  all_lines).groups()
    if low_type == "output":
        low_num = 99000 + int(low_num)
    if high_type == "output":
        high_num = 99000 + int(high_num)
    return int(low_num), int(high_num)


while len(frontier) > 0:
    print(frontier)
    bot, v1, v2 = frontier.pop()
    assert v1 and v2
    low_val, high_val = sorted([v1, v2])
    low_out, high_out = get_outs(bot)
    if low_out < 90000:
        if low_out in direct_inputs.keys():
            frontier.appendleft((low_out, low_val, direct_inputs[low_out]))
        else:
            in_solved_low = list(filter(lambda tu: low_out == tu[1], solved))
            in_solved_high = list(filter(lambda tu: low_out == tu[3], solved))
            if len(in_solved_low) == 1:
                frontier.appendleft((low_out, low_val, in_solved_low[0][2]))
            elif len(in_solved_high) == 1:
                frontier.appendleft((low_out, low_val, in_solved_high[0][4]))
    else:
        outs.append((low_out, low_val))
    if high_out < 90000:
        if high_out in direct_inputs.keys():
            frontier.appendleft((high_out, high_val, direct_inputs[high_out]))
        else:
            in_solved_low = list(filter(lambda tu: high_out == tu[1], solved))
            in_solved_high = list(filter(lambda tu: high_out == tu[3], solved))
            if len(in_solved_low) == 1:
                frontier.appendleft((high_out, high_val, in_solved_low[0][2]))
            elif len(in_solved_high) == 1:
                frontier.appendleft((high_out, high_val, in_solved_high[0][4]))
    else:
        outs.append((high_out, high_out))
    print(bot, low_out, low_val, high_out, high_val)
    solved.append((bot, low_out, low_val, high_out, high_val))
