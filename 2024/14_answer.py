import re

robot_lines = open('14_input').read().splitlines()

WIDTH = 11
HEIGHT = 7

robots = [list(map(int, re.findall(r"-?\d+", r_l))) for r_l in robot_lines]


def walk_robot(i_robot, i_steps):
    new_x = (i_robot[0] + i_steps * i_robot[2]) % WIDTH
    new_y = (i_robot[1] + i_steps * i_robot[3]) % HEIGHT
    return [new_x, new_y, i_robot[2], i_robot[3]]
