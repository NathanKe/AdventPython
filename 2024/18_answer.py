import math
import re
from collections import deque
from collections import defaultdict

text_fall = open('18_input').read().splitlines()


def min_path_after(i_falls):
    fall_list = deque(map(lambda ff: list(map(int, re.findall(r"\d+", ff))), text_fall))

    WIDTH = 71
    HEIGHT = 71
    BYTE_FALL_COUNT = i_falls

    # z x y
    byte_cube = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: '.')))
    min_cost_cube = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: math.inf)))
    min_cost_cube[0][0][0] = 0

    for fi, fv in enumerate(fall_list):
        if fi < BYTE_FALL_COUNT:
            byte_cube[0][fv[0]][fv[1]] = '#'

    head = (0, 0, 0)
    goal = (0, WIDTH - 1, HEIGHT - 1)

    paths = deque([[head]])
    finished = []

    while paths:
        cur = paths.popleft()
        north = (cur[-1][0], cur[-1][1], cur[-1][2] - 1)
        south = (cur[-1][0], cur[-1][1], cur[-1][2] + 1)
        east = (cur[-1][0], cur[-1][1] + 1, cur[-1][2])
        west = (cur[-1][0], cur[-1][1] - 1, cur[-1][2])

        neighbors = [ng for ng in [north, south, east, west] if 0 <= ng[1] < WIDTH and 0 <= ng[2] < HEIGHT
                     and byte_cube[ng[0]][ng[1]][ng[2]] == '.'
                     and ng not in cur]

        for ng in neighbors:
            new_path = cur[::]
            new_path.append(ng)

            if len(new_path) - 1 < min_cost_cube[ng[0]][ng[1]][ng[2]]:
                min_cost_cube[ng[0]][ng[1]][ng[2]] = len(new_path) - 1
                if ng == goal:
                    finished.append(new_path)
                else:
                    paths.append(new_path)

    return min_cost_cube[goal[0]][goal[1]][goal[2]]



print(min_path_after(1024))

for i in range(1024, len(text_fall)):
    res = min_path_after(i)
    if res > 71*71:
        print(text_fall[i-1])
        break
