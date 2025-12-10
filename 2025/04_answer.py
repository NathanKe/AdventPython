from collections import defaultdict

grid = defaultdict(lambda: '#')


grid_rows = open('04_input').read().splitlines()

MAX_ROW = len(grid_rows)
MAX_COL = len(grid_rows[0])


def pretty_print(i_grid):
    out_str = ""
    for r_x in range(MAX_ROW):
        row_str = ""
        for c_x in range(MAX_COL):
            row_str += i_grid[r_x + 1j*c_x]
        row_str += "\n"
        out_str += row_str
    print(out_str)

for r_i, r_v in enumerate(grid_rows):
    for c_i, c_v in enumerate(r_v):
        grid[r_i+1j*c_i] = c_v


def neighbors(i_loc):
    return [i_loc - 1,
            i_loc + 1,
            i_loc - 1j,
            i_loc + 1j,
            i_loc + 1 + 1j,
            i_loc + 1 - 1j,
            i_loc - 1 + 1j,
            i_loc - 1 - 1j]

def paper_count(i_loc):
    return len([a for a in neighbors(i_loc) if grid[a] == '@'])


def access_count(grid):
    acc_cnt = 0
    for r_x in range(MAX_ROW):
        for c_x in range(MAX_COL):
            cur_loc_x = r_x + 1j * c_x
            if grid[cur_loc_x] == "@":
                if paper_count(cur_loc_x) <= 3:
                    acc_cnt += 1
    return acc_cnt


remove_count = 0

removeable = True
while removeable:
    removeable = False
    for r_i in range(MAX_ROW):
        for c_i in range(MAX_COL):
            cur_loc = r_i + 1j * c_i
            if grid[cur_loc] == "@":
                if paper_count(cur_loc) <= 3:
                    removeable = True
                    remove_count += 1
                    grid[cur_loc] = '.'

print(remove_count)
