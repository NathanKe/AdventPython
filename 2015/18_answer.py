import collections

text = open('18_input').read().splitlines()
grid_lists = []
for line in text:
    grid_lists.append(list(map(int, line.replace(".", "0").replace('#', '1'))))


class point:
    def __init__(self, row, col, cur_state, next_state):
        self.row = row
        self.col = col
        self.cur_state = cur_state
        self.next_state = next_state

    def neighbor_on_count(self):
        prev_row = self.row - 1
        next_row = self.row + 1
        prev_col = self.col - 1
        next_col = self.col + 1

        # nw
        if prev_row >= 0 and prev_col >= 0:
            north_west = grid[prev_row][prev_col].cur_state
        else:
            north_west = 0
        # n
        if prev_row >= 0:
            north = grid[prev_row][self.col].cur_state
        else:
            north = 0
        # ne
        if prev_row >= 0 and next_col < len(grid_lists):
            north_east = grid[prev_row][next_col].cur_state
        else:
            north_east = 0
        # w
        if prev_col >= 0:
            west = grid[self.row][prev_col].cur_state
        else:
            west = 0
        # e
        if next_col < len(grid_lists):
            east = grid[self.row][next_col].cur_state
        else:
            east = 0
        # sw
        if next_row < len(grid_lists) and prev_col >= 0:
            south_west = grid[next_row][prev_col].cur_state
        else:
            south_west = 0
        # s
        if next_row < len(grid_lists):
            south = grid[next_row][self.col].cur_state
        else:
            south = 0
        # se
        if next_row < len(grid_lists) and next_col < len(grid_lists):
            south_east = grid[next_row][next_col].cur_state
        else:
            south_east = 0

        # print('north_west', north_west)
        # print('north', north)
        # print('north_east', north_east)
        # print('west', west)
        # print('east', east)
        # print('south_west', south_west)
        # print('south', south)
        # print('south_east', south_east)

        return north + north_east + north_west + east + west + south + south_east + south_west

    def calc_next_state(self):
        n_o_c = self.neighbor_on_count()
        if self.cur_state == 1:
            if n_o_c == 2 or n_o_c == 3:
                self.next_state = 1
            else:
                self.next_state = 0
        else:
            if n_o_c == 3:
                self.next_state = 1
            else:
                self.next_state = 0

    def update_state(self):
        self.cur_state = self.next_state

    def update_state_p2(self):
        if self.row == 0 and self.col == 0 \
                or self.row == 0 and self.col == len(grid_lists) - 1 \
                or self.row == len(grid_lists) - 1 and self.col == 0 \
                or self.row == len(grid_lists) - 1 and self.col == len(grid_lists) - 1:
            self.cur_state = 1
        else:
            self.cur_state = self.next_state


grid = collections.defaultdict(lambda: collections.defaultdict(point))

for i in range(len(grid_lists)):
    for j in range(len(grid_lists[0])):
        grid[i][j] = point(i, j, grid_lists[i][j], 0)


def step_grid():
    for i in range(len(grid_lists)):
        for j in range(len(grid_lists[0])):
            grid[i][j].calc_next_state()
    for i in range(len(grid_lists)):
        for j in range(len(grid_lists[0])):
            grid[i][j].update_state()


def print_grid():
    print('\n'.join(
        str([''.join(
            [str(grid[i][j].cur_state) for j in range(len(grid_lists))])])
        for i in range(len(grid_lists))))


for i in range(100):
    step_grid()

on_count = 0
for i in range(len(grid_lists)):
    for j in range(len(grid_lists[0])):
        on_count += grid[i][j].cur_state

print('Part 1: ', on_count)


def step_grid_2():
    for i in range(len(grid_lists)):
        for j in range(len(grid_lists[0])):
            grid[i][j].calc_next_state()
    for i in range(len(grid_lists)):
        for j in range(len(grid_lists[0])):
            grid[i][j].update_state_p2()


# reset grid
for i in range(len(grid_lists)):
    for j in range(len(grid_lists[0])):
        grid[i][j] = point(i, j, grid_lists[i][j], 0)

# re step
for i in range(100):
    step_grid_2()

# re count
on_count = 0
for i in range(len(grid_lists)):
    for j in range(len(grid_lists[0])):
        on_count += grid[i][j].cur_state

print('Part 2: ', on_count)
