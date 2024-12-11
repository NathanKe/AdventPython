from collections import defaultdict


# problem_deque = deque([125, 17])
problem_stones = [70949, 6183, 4, 3825336, 613971, 0, 15, 182]


stone_blink_lookup = defaultdict(lambda: defaultdict(lambda: -1))


def parse_stone(i_st_bl_tu):
    i_st_n = i_st_bl_tu[0]
    i_bl = i_st_bl_tu[1]

    if stone_blink_lookup[i_st_n][i_bl] >= 0:
        return stone_blink_lookup[i_st_n][i_bl]

    if i_bl == 0:
        stone_blink_lookup[i_st_n][i_bl] = 1
        return 1

    st_str = str(i_st_n)
    st_str_len = len(st_str)

    if i_st_n == 0:
        recur_res = parse_stone((1, i_bl - 1))
        stone_blink_lookup[1][i_bl - 1] = recur_res
        return recur_res
    elif st_str_len % 2 == 0:
        half_ix = st_str_len//2
        left = int(st_str[:half_ix])
        right = int(st_str[half_ix:])
        left_recur_res = parse_stone((left, i_bl - 1))
        right_recur_res = parse_stone((right, i_bl - 1))
        stone_blink_lookup[left][i_bl - 1] = left_recur_res
        stone_blink_lookup[right][i_bl - 1] = right_recur_res
        stone_blink_lookup[i_st_n][i_bl] = left_recur_res + right_recur_res
        return left_recur_res + right_recur_res
    else:
        twtwfo_recur_res = parse_stone((i_st_n * 2024, i_bl - 1))
        stone_blink_lookup[i_st_n * 2024][i_bl - 1] = twtwfo_recur_res
        return twtwfo_recur_res


def stone_expand(i_ct):
    stone_count = 0
    for st in problem_stones:
        stone_count += parse_stone((st, i_ct))
    return stone_count


print(stone_expand(25))
print(stone_expand(75))
