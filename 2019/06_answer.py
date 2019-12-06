import re
import collections

puzzle = open('06_input').read().splitlines()


def children_of(p_planet):
    return list(map(lambda s: re.search(r"\)(.+)", s).group(1),
                    filter(lambda s: re.search(p_planet+r"\).+", s), puzzle)))


frontier = collections.deque([('COM', [])])
solved = {}

while len(frontier) > 0:
    cur_planet, cur_path = frontier.pop()
    for child in children_of(cur_planet):
        frontier.append((child, cur_path+[child]))
    solved[cur_planet] = cur_path

print('Part 1: ', sum(map(len, solved.values())))

you_path = solved['YOU']
santa_path = solved['SAN']
common_steps = list(set(you_path) & set(santa_path))

transfer_dist = (len(you_path) - len(common_steps) - 1) + (len(santa_path) - len(common_steps) - 1)

print('Part 2: ', transfer_dist)
