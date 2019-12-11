import collections
import math
import teninput


def generate_dict(ast_string):
    ast_lines = ast_string.splitlines()
    out_dict = collections.defaultdict(lambda: collections.defaultdict(int))
    for row in range(len(ast_lines)):
        for col in range(len(ast_lines[row])):
            if ast_lines[row][col] == '#':
                out_dict[col][row] = 1
            else:
                out_dict[col][row] = 0
    return out_dict


def classify_point(p_x, p_y):
    c_gcd = math.gcd(p_x, p_y)
    if c_gcd:
        p_x //= c_gcd
        p_y //= c_gcd
    return p_x, p_y


def vis_asteroids_from_point(p_grid, s_x, s_y):
    class_dict = collections.defaultdict(collections.deque)
    for x in p_grid.keys():
        for y in p_grid[x].keys():
            cl_x, cl_y = classify_point(x - s_x, y - s_y)
            if (cl_x or cl_y) and p_grid[x][y]:
                class_dict[(cl_x, cl_y)].append((x, y))
    return class_dict


def max_vis_asteroid(p_grid):
    c_max = {}
    for x in p_grid.keys():
        for y in p_grid[x].keys():
            if p_grid[x][y]:
                c_vis = vis_asteroids_from_point(p_grid, x, y)
                if len(c_vis) > len(c_max):
                    c_max = c_vis
    return c_max


best_station = max_vis_asteroid(generate_dict(teninput.puzzle))
print('Part 1: ', len(best_station))


def convert_to_degrees_clockwise_from_north(p_station):
    out = []
    for k in p_station.keys():
        # k[1] is y, k[0] is x
        # negate y to account for up positive on Cartesian, up is descending in grid
        # negate atan2 to run CW
        # 180/pi to get degrees
        # add 90 to move to 0 = Y Axis
        # add 360 to constrain as positive
        # mod 360 to constrain [0, 360]
        deg = (-1 * math.atan2(-1 * k[1], k[0]) * 180 / math.pi + 90 + 360) % 360
        out.append((deg, k, p_station[k]))
    out.sort()
    return out


target_deque = collections.deque(convert_to_degrees_clockwise_from_north(best_station))
eliminated = []

while len(eliminated) < 200:
    c_angle, c_loc, c_ast_deque = target_deque.popleft()
    eliminated.append(c_ast_deque.pop())
    if len(c_ast_deque) > 0:
        target_deque.append((c_angle, c_loc, c_ast_deque))

print('Part 2: ', eliminated[-1][0] * 100 + eliminated[-1][1])
