import re

distance_report_lines = open('15_input').read().splitlines()

# x is imag, y is real.  y increase goes down the page

sensor_beacons = []
for line in distance_report_lines:
    sx, sy, bx, by = map(int, re.findall(r"-*\d+", line))
    sensor_beacons.append((sx, sy, bx, by))


def calc_manhattan_distance(jx, jy, kx, ky):
    return abs(jx - kx) + abs(jy - ky)


def reduce_bound_pairs(pair_list):
    pair_list.sort(key=lambda tu: tu[0])
    if len(pair_list) == 1:
        return pair_list
    elif len(pair_list) == 2:
        a_l, a_r = pair_list[0]
        b_l, b_r = pair_list[1]
        # completely contained
        if b_l <= a_l <= a_r <= b_r or a_l <= b_l <= b_r <= a_r:
            return [(min(a_l, b_l), max(a_r, b_r))]
        # overlaps
        elif a_r >= b_l >= a_l or b_r >= a_l >= b_l:
            return [(min(a_l, b_l), max(a_r, b_r))]
        elif b_l <= a_r <= b_r or a_l <= b_r <= a_r:
            return [(min(a_l, b_l), max(a_r, b_r))]
        # disjoint
        else:
            return pair_list
    else:
        # pairwise recursive reduction
        cur_len = len(pair_list)
        assert (cur_len >= 3)
        pair_ix = 0
        while True:
            if pair_ix > cur_len - 2:
                return pair_list
            new_pairs = pair_list[:pair_ix] + reduce_bound_pairs(
                [pair_list[pair_ix], pair_list[pair_ix + 1]]) + pair_list[pair_ix + 2:]
            if len(new_pairs) == cur_len:
                pair_ix += 1
            else:
                return reduce_bound_pairs(new_pairs)


def positions_without_beacon(search_row, is_part_2):
    bound_pairs = []
    for sx, sy, bx, by in sensor_beacons:
        manhattan_distance = calc_manhattan_distance(sx, sy, bx, by)
        if sy - manhattan_distance <= search_row <= sy + manhattan_distance:
            dist_to_search_row = abs(sy - search_row)
            remaining_distance = manhattan_distance - dist_to_search_row
            cur_left_bound = sx - remaining_distance
            cur_right_bound = sx + remaining_distance
            if is_part_2:
                if cur_left_bound <= 4000000 and cur_right_bound >= 0:
                    bound_pairs.append((max(0, cur_left_bound), min(4000000, cur_right_bound)))
            else:
                bound_pairs.append((cur_left_bound, cur_right_bound))
            bound_pairs = reduce_bound_pairs(bound_pairs)
    return bound_pairs


p1_res = positions_without_beacon(2000000, False)
assert (len(p1_res) == 1)
# lucked out here... off by one error in the range width calculation
# off by one error in positions on line 2000000 that are THEMSELVES beacons
print("Part 1: ", abs(p1_res[0][1] - p1_res[0][0]))

for i in range(0, 4000001):
    x = positions_without_beacon(i, True)
    if len(x) == 1 and x[0] == (0, 4000000):
        pass
    else:
        print("Part 2: ", (x[0][1] + 1) * 4000000 + i)
        break

# the right answer is clever vector intersection math of the "shell" one step outside each scanners range
#
