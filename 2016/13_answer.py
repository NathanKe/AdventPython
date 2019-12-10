import collections
import itertools

puzzle = 1350

walls = []
halls = []
solved = {}


def is_wall(p_x, p_y, favorite):
    if (p_x, p_y) in walls:
        return True
    elif (p_x, p_y) in halls:
        return False
    else:
        dec_num = p_x * p_x + 3 * p_x + 2 * p_x * p_y + p_y + p_y * p_y + favorite
        bin_num = bin(dec_num)
        one_count = sum(map(int, bin_num[2:]))
        if one_count % 2 != 0:
            walls.append((p_x, p_y))
            # solved[(p_x, p_y)] = 8888
            return True
        else:
            halls.append((p_x, p_y))
            return False


def valid_hall(node, favorite):
    return node[0] >= 0 and node[1] >= 0 and not is_wall(*node, favorite)


def adj_halls(p_x, p_y, favorite):
    up = (p_x, p_y + 1)
    down = (p_x, p_y - 1)
    left = (p_x - 1, p_y)
    right = (p_x + 1, p_y)

    ret_adj = []

    if valid_hall(up, favorite):
        ret_adj.append(up)
    if valid_hall(down, favorite):
        ret_adj.append(down)
    if valid_hall(left, favorite):
        ret_adj.append(left)
    if valid_hall(right, favorite):
        ret_adj.append(right)

    return ret_adj


def fill_grid_from_one_one(favorite, goal):
    print('-----------------------')
    frontier = collections.deque([((1, 1), [])])
    while len(frontier) > 0:
        print(frontier)
        cur_loc, cur_path = frontier.pop()
        solved[cur_loc] = len(cur_path)
        if cur_loc == goal:
            break
        if len(cur_path) > 10000:
            solved[cur_loc] = 9999
            break
        new_adj = adj_halls(*cur_loc, favorite)
        for adj in new_adj:
            if adj not in solved:
                frontier.appendleft((adj, cur_path[:] + [cur_loc]))


# fill_grid_from_one_one(puzzle, (31, 39))
# print(solved[(31, 39)])

# p2 - memoize solved dict outside of min_dist calc
# stop recalculating every node for every search
solved = {}
walls = []
halls = []
grid_points = list(itertools.product(range(60), range(60)))
grid_points.sort(key=sum)
for point in grid_points:
    if not is_wall(*point, puzzle) and point not in solved.keys():
        fill_grid_from_one_one(puzzle, point)
