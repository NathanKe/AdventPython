brick_lines = open('22_input').read().splitlines()

brick_xyz_n_dict = {}
settled = []
unsettled = []
for bn, bt in enumerate(brick_lines):
    lf, rg = bt.split('~')
    lx, ly, lz = map(int, lf.split(','))
    rx, ry, rz = map(int, rg.split(','))
    low_x = min(lx, rx)
    high_x = max(lx, rx)
    low_y = min(ly, ry)
    high_y = max(ly, ry)
    low_z = min(lz, rz)
    high_z = max(lz, rz)
    b_lab = bn
    for ix in range(low_x, high_x + 1):
        for iy in range(low_y, high_y + 1):
            for iz in range(low_z, high_z + 1):
                brick_xyz_n_dict[(ix, iy, iz)] = b_lab
    unsettled.append(b_lab)

while unsettled:
    print('uns', len(unsettled))
    z_sort = sorted(brick_xyz_n_dict.items(), key=lambda tu: tu[0][2])
    lowest_unsettled_z_label = [(loc, lab) for loc, lab in z_sort if lab in unsettled][0][1]
    lowest_unsettled_brick_pieces = [loc for loc, lab in brick_xyz_n_dict.items() if lab == lowest_unsettled_z_label]

    # vert brick case
    if len(lowest_unsettled_brick_pieces) > 1 and \
            lowest_unsettled_brick_pieces[0][2] != lowest_unsettled_brick_pieces[1][2]:
        vert_z_vals = [z for x, y, z in lowest_unsettled_brick_pieces]
        min_z = min(vert_z_vals)
        x_y_of_low_z = [(x, y) for x, y, z in lowest_unsettled_brick_pieces if z == min_z][0]
        high_z_val_at_that_loc = [loc[2] for (loc, lab) in brick_xyz_n_dict.items() if lab in settled
                                  and (loc[0], loc[1]) == x_y_of_low_z]
        high_z_val_at_that_loc.append(0)
        fall_dist = min_z - max(high_z_val_at_that_loc) - 1
    # horz brick case
    else:
        lowest_unsettled_x_y = [(x, y) for x, y, z in lowest_unsettled_brick_pieces]
        brick_vals_under = [0] + [loc[2] for loc, lab in brick_xyz_n_dict.items() if
                                  (loc[0], loc[1]) in lowest_unsettled_x_y and lab in settled]
        highest_occupied_under = max(brick_vals_under)
        fall_dist = lowest_unsettled_brick_pieces[0][2] - highest_occupied_under - 1
    for bp in lowest_unsettled_brick_pieces:
        assert bp in brick_xyz_n_dict.keys()
        brick_xyz_n_dict.pop(bp)
        new_piece = (bp[0], bp[1], bp[2] - fall_dist)
        brick_xyz_n_dict[new_piece] = lowest_unsettled_z_label
    unsettled.remove(lowest_unsettled_z_label)
    settled.append(lowest_unsettled_z_label)


def supporting_count(b_lab):
    pieces = [loc for loc, lab in brick_xyz_n_dict.items() if lab == b_lab]
    labels_below = set()
    if len(pieces) > 1 and pieces[0][2] != pieces[1][2]:
        vert_z_vals = [z for x, y, z in pieces]
        min_z = min(vert_z_vals)
        below = pieces[0][0], pieces[0][1], min_z - 1
        assert min_z == 1 or below in brick_xyz_n_dict.keys()
        if below in brick_xyz_n_dict.keys():
            labels_below.add(brick_xyz_n_dict[below])
    else:
        for p in pieces:
            below = (p[0], p[1], p[2] - 1)
            if below in brick_xyz_n_dict.keys():
                labels_below.add(brick_xyz_n_dict[below])
    return len(labels_below)


def disintegratable(b_lab):
    pieces = [loc for loc, lab in brick_xyz_n_dict.items() if lab == b_lab]

    labels_above = set()

    # vert case
    if len(pieces) > 1 and pieces[0][2] != pieces[1][2]:
        vert_z_vals = [z for x, y, z in pieces]
        max_z = max(vert_z_vals)
        above = pieces[0][0], pieces[0][1], max_z + 1
        if above in brick_xyz_n_dict.keys():
            labels_above.add(brick_xyz_n_dict[above])
    else:
        for p in pieces:
            above = (p[0], p[1], p[2] + 1)
            if above in brick_xyz_n_dict.keys():
                labels_above.add(brick_xyz_n_dict[above])

    supp_counts = list(map(lambda lab: supporting_count(lab), labels_above))
    return all(map(lambda sc: sc > 1, supp_counts))


print(len([x for x in map(lambda l: disintegratable(l), settled) if x]))

supp_map = {}
for b_l in settled:
    b_data = [loc for loc, lab in brick_xyz_n_dict.items() if lab == b_l]
    belows = set()
    for bb in b_data:
        beneath = (bb[0], bb[1], bb[2] - 1)
        if beneath in brick_xyz_n_dict.keys():
            label_below = brick_xyz_n_dict[beneath]
            if label_below != b_l:
                belows.add(brick_xyz_n_dict[beneath])
    supp_map[b_l] = list(belows)


def fall_count(i_b_l):
    print(i_b_l)
    fall_front = [i_b_l]
    fallen = set()
    while fall_front:
        current_fallee = fall_front.pop()
        fallen.add(current_fallee)
        new_fallees = [k for k, v in supp_map.items() if len(v) > 0 and all([x in fallen for x in v])]
        for nf in new_fallees:
            if nf not in fallen:
                fall_front.append(nf)
    return len(fallen) - 1


print(sum(map(lambda bx: fall_count(bx), settled)))
