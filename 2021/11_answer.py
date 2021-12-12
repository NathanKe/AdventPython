input_grid = list(map(lambda r: list(map(int, list(r))), open('11_input').read().splitlines()))


class Octopi:
    def __init__(self, in_grid):
        self.grid = in_grid
        self.flash_count = 0

    def in_bounds_neighbors(self, row, col):
        if row == 0:
            if col == 0:
                return {(row + 1, col), (row, col + 1), (row + 1, col + 1)}
            elif col == len(self.grid[row]) - 1:
                return {(row + 1, col), (row, col - 1), (row + 1, col - 1)}
            else:
                return {(row + 1, col), (row, col - 1), (row, col + 1), (row + 1, col + 1), (row + 1, col - 1)}
        elif row == len(self.grid) - 1:
            if col == 0:
                return {(row - 1, col), (row, col + 1), (row - 1, col + 1)}
            elif col == len(self.grid[row]) - 1:
                return {(row - 1, col), (row, col - 1), (row - 1, col - 1)}
            else:
                return {(row - 1, col), (row, col - 1), (row, col + 1), (row - 1, col + 1), (row - 1, col - 1)}
        else:
            if col == 0:
                return {(row - 1, col), (row + 1, col), (row, col + 1), (row + 1, col + 1), (row - 1, col + 1)}
            elif col == len(self.grid[row]) - 1:
                return {(row - 1, col), (row + 1, col), (row, col - 1), (row + 1, col - 1), (row - 1, col - 1)}
            else:
                return {(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1), (row + 1, col + 1),
                        (row + 1, col - 1), (row - 1, col + 1), (row - 1, col - 1)}

    def flash_grid(self):
        flashing = set()
        flashed = set()

        for r_i, r_v in enumerate(self.grid):
            for c_i, c_v in enumerate(r_v):
                self.grid[r_i][c_i] += 1
                if self.grid[r_i][c_i] > 9:
                    flashing.add((r_i, c_i))

        while flashing:
            cur_oct = flashing.pop()
            self.grid[cur_oct[0]][cur_oct[1]] = 0
            flashed.add(cur_oct)
            un_flashed_neighbors = self.in_bounds_neighbors(*cur_oct).difference(flashed)
            for neighbor in un_flashed_neighbors:
                self.grid[neighbor[0]][neighbor[1]] += 1
                if self.grid[neighbor[0]][neighbor[1]] > 9:
                    flashing.add(neighbor)
        self.flash_count += len(flashed)
        return len(flashed)


ooo = Octopi(input_grid)
i = 0
while True:
    f_c = ooo.flash_grid()
    if f_c == 100:
        print("Part 2: ", i + 1)
        break
    elif i == 99:
        print("Part 1: ", ooo.flash_count)
    i += 1
