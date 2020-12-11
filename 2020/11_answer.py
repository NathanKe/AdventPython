import collections

def init_grid(filename):
    out_grid = collections.defaultdict(lambda: collections.defaultdict(lambda: '.'))
    raw_data = open(filename).read().splitlines()
    for row_num in range(len(raw_data)):
        for col_num in range(len(raw_data[row_num])):
            out_grid[row_num][col_num] = raw_data[row_num][col_num]
    return out_grid


def pretty_print(grid_dict):
    out_str = ""
    for row_num in range(len(grid_dict)):
        row_str = ""
        for col_num in range(len(grid_dict[row_num])):
            row_str += grid_dict[row_num][col_num]
        row_str += "\n"
        out_str += row_str
    return out_str


def neighbor_count(row_num, col_num, grid, char):
    n_c = 0
    for i in range(row_num - 1, row_num + 2):
        for j in range(col_num - 1, col_num + 2):
            if 0 <= i < len(grid) and 0 <= j < len(grid[row_num]) and grid[i][j] == char:
                n_c += 1
    return n_c


def step_grid_p1(in_grid):
    out_grid = collections.defaultdict(lambda: collections.defaultdict(str))
    for row_num in range(len(in_grid)):
        for col_num in range(len(in_grid[0])):
            if in_grid[row_num][col_num] == 'L' and neighbor_count(row_num, col_num, in_grid, '#') == 0:
                out_grid[row_num][col_num] = '#'
            elif in_grid[row_num][col_num] == '#' and neighbor_count(row_num, col_num, in_grid, '#') >= 5:  # 4 or more, plus 1 for the seat itself
                out_grid[row_num][col_num] = 'L'
            else:
                out_grid[row_num][col_num] = in_grid[row_num][col_num]
    return out_grid


def occupied_count_at_stable_p1():
    dupe = False
    grid = init_grid('11_input')
    steps = 0
    while not dupe:
        new_grid = step_grid_p1(grid)
        steps += 1
        if pretty_print(grid) == pretty_print(new_grid):
            dupe = True
        grid = new_grid
    return collections.Counter(pretty_print(grid))['#']


print('Part 1: ', occupied_count_at_stable_p1())


def ray(pos_r, pos_c, off_r, off_c, in_grid):
    cur_r = pos_r + off_r
    cur_c = pos_c + off_c
    ray_list = []
    while 0 <= cur_r < len(in_grid) and 0 <= cur_c < len(in_grid[cur_r]):
        cur_s = in_grid[cur_r][cur_c]
        ray_list.append(cur_s)
        cur_r += off_r
        cur_c += off_c
    return ray_list


def first_vis_seat(pos_r, pos_c, off_r, off_c, in_grid):
    cur_ray = ray(pos_r, pos_c, off_r, off_c, in_grid)
    while cur_ray:
        cur_itm = cur_ray.pop()
        if cur_itm != '.':
            return cur_itm
    return '.'


directions = [
    (0, -1),
    (0, 1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]


def ray_occupied_count(pos_r, pos_c, in_grid):
    first_vis_all_dir = [first_vis_seat(pos_r, pos_c, *d, in_grid) for d in directions]
    return collections.Counter(first_vis_all_dir)['#']


def step_grid_p2(in_grid):
    out_grid = collections.defaultdict(lambda: collections.defaultdict(str))
    for row_num in range(len(in_grid)):
        for col_num in range(len(in_grid[0])):
            if in_grid[row_num][col_num] == 'L' and ray_occupied_count(row_num, col_num, in_grid) == 0:
                out_grid[row_num][col_num] = '#'
            elif in_grid[row_num][col_num] == '#' and ray_occupied_count(row_num, col_num, in_grid) >= 6:  # 5 or more
                out_grid[row_num][col_num] = 'L'
            else:
                out_grid[row_num][col_num] = in_grid[row_num][col_num]
    return out_grid


def occupied_count_at_stable_p2():
    dupe = False
    grid = init_grid('11_input')
    steps = 0
    while not dupe:
        new_grid = step_grid_p2(grid)
        steps += 1
        if pretty_print(grid) == pretty_print(new_grid):
            dupe = True
        grid = new_grid
        print(pretty_print(grid))
    return collections.Counter(pretty_print(grid))['#']


print('Part 2: ', occupied_count_at_stable_p2())

