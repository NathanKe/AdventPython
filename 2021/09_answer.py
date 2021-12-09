heightmap = open('09_input').read().splitlines()


def in_bounds_neighbors(row, col):
    if row == 0:
        if col == 0:
            return {(row + 1, col), (row, col + 1)}
        elif col == len(heightmap[row]) - 1:
            return {(row + 1, col), (row, col - 1)}
        else:
            return {(row + 1, col), (row, col - 1), (row, col + 1)}
    elif row == len(heightmap) - 1:
        if col == 0:
            return {(row - 1, col), (row, col + 1)}
        elif col == len(heightmap[row]) - 1:
            return {(row - 1, col), (row, col - 1)}
        else:
            return {(row - 1, col), (row, col - 1), (row, col + 1)}
    else:
        if col == 0:
            return {(row - 1, col), (row + 1, col), (row, col + 1)}
        elif col == len(heightmap[row]) - 1:
            return {(row - 1, col), (row + 1, col), (row, col - 1)}
        else:
            return {(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)}


low_points = []
for row_i, row_val in enumerate(heightmap):
    for col_i, cur_val in enumerate(row_val):
        i_b_n = in_bounds_neighbors(row_i, col_i)
        neighbor_vals = map(lambda p: int(heightmap[p[0]][p[1]]), i_b_n)
        min_neighbor = min(neighbor_vals)
        if int(cur_val) < min_neighbor:
            low_points.append((row_i, col_i))


print("Part 1: ", sum(map(lambda p: int(heightmap[p[0]][p[1]]) + 1, low_points)))


def expand_basin(basin):
    out_basin = list(basin)
    for b_point in basin:
        frontier = in_bounds_neighbors(*b_point).difference(basin)
        for f_point in frontier:
            if int(heightmap[b_point[0]][b_point[1]]) < int(heightmap[f_point[0]][f_point[1]]) < 9:
                out_basin.append(f_point)
    if set(out_basin) == basin:
        return False
    else:
        return set(out_basin)


def basin_size(low_point):
    basin = {low_point}
    cur_size = 1
    while basin:
        cur_size = len(basin)
        basin = expand_basin(basin)
    return cur_size


low_point_sizes = sorted(list(map(basin_size, low_points)), reverse=True)
big_three_prod = low_point_sizes[0] * low_point_sizes[1] * low_point_sizes[2]

print("Part 2: ", big_three_prod)
