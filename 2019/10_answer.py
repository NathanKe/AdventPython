import collections
import math
import teninput


def generate_dict(ast_string):
    ast_lines = ast_string.splitlines()
    out_dict = collections.defaultdict(lambda: collections.defaultdict(int))
    for row in range(len(ast_lines)):
        for col in range(len(ast_lines[row])):
            if ast_lines[row][col] == '#':
                out_dict[row][col] = 1
            else:
                out_dict[row][col] = 0
    return out_dict


def classify_point(p_x, p_y):
    c_gcd = math.gcd(p_x, p_y)
    if c_gcd:
        p_x //= c_gcd
        p_y //= c_gcd
    return p_x, p_y


def vis_asteroids_from_point(p_grid, s_x, s_y):
    class_dict = collections.defaultdict(collections.deque)
    for y in p_grid.keys():
        for x in p_grid[y].keys():
            cl_x, cl_y = classify_point(x - s_x, y - s_y)
            if (cl_x or cl_y) and p_grid[y][x]:
                class_dict[(cl_x, cl_y)].append((x + s_x, y + s_y))
    return class_dict


def max_vis_asteroid(p_grid):
    c_max = {}
    for y in p_grid.keys():
        for x in p_grid[y].keys():
            if p_grid[y][x]:
                c_vis = vis_asteroids_from_point(p_grid, x, y)
                if len(c_vis) > len(c_max):
                    c_max = c_vis.copy()
    return c_max


best_station = max_vis_asteroid(generate_dict(teninput.puzzle))
print('Part 1: ', len(best_station))


def convert_to_degrees_clockwise_from_north(p_station):
    out = []
    for k in p_station.keys():
        deg = (-1 * math.atan2(k[0], k[1]) * 180 / math.pi + 90 + 360) % 360
        out.append((deg, p_station[k]))
    out.sort()
    return out


target_deque = collections.deque(convert_to_degrees_clockwise_from_north(best_station))
eliminated = []

while len(eliminated) < 200:
    c_angle, c_ast_deque = target_deque.popleft()
    print(c_angle, c_ast_deque)
    eliminated.append(c_ast_deque.popleft())
    if len(c_ast_deque) > 0:
        print(c_angle, c_ast_deque)
        target_deque.append((c_angle, c_ast_deque))

print('Part 2: ', eliminated[-1][0]*100 + eliminated[-1][1])


