import collections


def init_grid(filename):
    out_grid = collections.defaultdict(lambda: collections.defaultdict(lambda: '.'))
    raw_data = open(filename).read().splitlines()
    for row_num in range(len(raw_data)):
        for col_num in range(len(raw_data[row_num])):
            out_grid[row_num][col_num] = raw_data[row_num][col_num]
    return out_grid


def stringify(in_grid):
    out = ""
    for row_num in range(len(in_grid)):
        r = ""
        for col_num in range(len(in_grid[row_num])):
            r += in_grid[row_num][col_num]
        r += "\n"
        out += r
    return out


def neighbor_count(row_num, col_num, grid, char):
    n_c = 0
    for i in range(row_num - 1, row_num + 2):
        for j in range(col_num - 1, col_num + 2):
            if 0 <= i < len(grid) and 0 <= j < len(grid[row_num]) and grid[i][j] == char:
                n_c += 1
    return n_c


def step_grid_p1(in_grid):
    out_grid = collections.defaultdict(lambda: collections.defaultdict(str))
    change = False
    for row_num in range(len(in_grid)):
        for col_num in range(len(in_grid[0])):
            if in_grid[row_num][col_num] == 'L' and neighbor_count(row_num, col_num, in_grid, '#') == 0:
                out_grid[row_num][col_num] = '#'
                change = True
            elif in_grid[row_num][col_num] == '#' and neighbor_count(row_num, col_num, in_grid, '#') >= 5:
                out_grid[row_num][col_num] = 'L'
                change = True
            else:
                out_grid[row_num][col_num] = in_grid[row_num][col_num]
    return out_grid, change


def occupied_count_at_stable_p1():
    change = True
    grid = init_grid('11_input')
    while change:
        new_grid, change = step_grid_p1(grid)
        grid = new_grid
    return collections.Counter(stringify(grid))['#']


print('Part 1: ', occupied_count_at_stable_p1())


def ray(pos_r, pos_c, off_r, off_c, in_grid):
    cur_r = pos_r + off_r
    cur_c = pos_c + off_c
    ray_list = collections.deque([])
    while 0 <= cur_r < len(in_grid) and 0 <= cur_c < len(in_grid[cur_r]):
        cur_s = in_grid[cur_r][cur_c]
        ray_list.appendleft(cur_s)
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
    change = False
    out_grid = collections.defaultdict(lambda: collections.defaultdict(str))
    for row_num in range(len(in_grid)):
        for col_num in range(len(in_grid[0])):
            if in_grid[row_num][col_num] == 'L' and ray_occupied_count(row_num, col_num, in_grid) == 0:
                out_grid[row_num][col_num] = '#'
                change = True
            elif in_grid[row_num][col_num] == '#' and ray_occupied_count(row_num, col_num, in_grid) >= 5:  # 5 or more
                out_grid[row_num][col_num] = 'L'
                change = True
            else:
                out_grid[row_num][col_num] = in_grid[row_num][col_num]
    return out_grid, change


def occupied_count_at_stable_p2():
    change = True
    grid = init_grid('11_input')
    while change:
        new_grid, change = step_grid_p2(grid)
        grid = new_grid
    return collections.Counter(stringify(grid))['#']


print('Part 2: ', occupied_count_at_stable_p2())
