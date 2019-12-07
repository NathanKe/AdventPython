import collections

puzzle = 1350

walls = []
halls = []
solved = []


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
            return True
        else:
            halls.append((p_x, p_y))
            return False


def valid_hall(node, favorite):
    return node[0] >= 0 and node[1] >= 0 and node and not is_wall(*node, favorite)


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


def min_distance(favorite, s_x, s_y, g_x, g_y):
    frontier = collections.deque([((1, 1), [])])
    solved = []
    while len(frontier) > 0:
        cur_loc, cur_path = frontier.pop()
        solved.append(cur_loc)
        if cur_loc[0] == g_x and cur_loc[1] == g_y:
            print(cur_path)
            break
        if len(cur_path) >= 92:
            break
        new_adj = adj_halls(*cur_loc, favorite)
        for adj in new_adj:
            if adj not in solved:
                frontier.appendleft((adj, cur_path[:] + [cur_loc]))
    return len(cur_path)


print(min_distance(puzzle, 1, 1, 31, 39))

# p2 - memoize solved dict outside of min_dist calc
# stop recalculating every node for every search
lt_50 = []
for m_x in range(52):
    for m_y in range(52):
        if not is_wall(m_x, m_y, puzzle):
            min_d = min_distance(puzzle, 1, 1, m_x, m_y)
            print(m_x, m_y, min_d)
            if min_d <= 50:
                lt_50.append((m_x, m_y, min_d))

print(len(lt_50))
