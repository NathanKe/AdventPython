import math
import re
from itertools import product
from collections import defaultdict

robot_lines = open('14_input').read().splitlines()

WIDTH = 101
HEIGHT = 103

robots = [list(map(int, re.findall(r"-?\d+", r_l))) for r_l in robot_lines]


def walk_robot(i_robot, i_steps):
    new_x = (i_robot[0] + i_steps * i_robot[2]) % WIDTH
    new_y = (i_robot[1] + i_steps * i_robot[3]) % HEIGHT
    return [new_x, new_y, i_robot[2], i_robot[3]]


def quadrator(i_w, i_h):
    left_width = list(range(0, i_w // 2))
    right_width = list(range(i_w // 2 + 1, i_w))
    top_height = list(range(0, i_h // 2))
    bot_height = list(range(i_h // 2 + 1, i_h))

    q1 = list(product(left_width, top_height))
    q2 = list(product(left_width, bot_height))
    q3 = list(product(right_width, top_height))
    q4 = list(product(right_width, bot_height))

    return q1, q2, q3, q4


walked_robots = [walk_robot(r, 100) for r in robots]

quad1, quad2, quad3, quad4 = quadrator(WIDTH, HEIGHT)


def entropy(i_robots):
    q1_r = [r for r in i_robots if (r[0], r[1]) in quad1]
    q2_r = [r for r in i_robots if (r[0], r[1]) in quad2]
    q3_r = [r for r in i_robots if (r[0], r[1]) in quad3]
    q4_r = [r for r in i_robots if (r[0], r[1]) in quad4]

    return len(q1_r) * len(q2_r) * len(q3_r) * len(q4_r)


print(entropy(walked_robots))


def robot_printer(i_robots):
    robot_places = set([(r[0], r[1]) for r in i_robots])
    for row in range(HEIGHT):
        out_row = ""
        for col in range(WIDTH):
            if (row, col) in robot_places:
                out_row += "#"
            else:
                out_row += " "
        print(out_row)


def tree_poss_printer(i_robots):
    min_entropy = math.inf
    for i in range(WIDTH * HEIGHT):
        i_robots = [walk_robot(r, 1) for r in i_robots]
        cur_entropy = entropy(i_robots)
        if i % 100 == 0:
            print(i)
        if cur_entropy < min_entropy:
            print(i + 1)
            robot_printer(i_robots)
            min_entropy = cur_entropy


tree_poss_printer(robots)
