from collections import defaultdict

dig_instrs = open('18_input').read().splitlines()

d_map = {
    'R': 1j,
    'L': -1j,
    'U': -1,
    'D': 1
}

i_map = {
    '0': 1j,
    '2': -1j,
    '3': -1,
    '1': 1
}


def points_within(i_coords):
    assert len(i_coords) >= 3
    sum = 0
    for i in range(len(i_coords) - 1):
        x1 = i_coords[i].real
        y1 = i_coords[i].imag
        x2 = i_coords[i + 1].real
        y2 = i_coords[i + 1].imag
        sum += x1 * y2 - y1 * x2
    return abs(sum / 2)


def points_on_line(instr_tus):
    point_count = 0
    for instr_tu in instr_tus:
        c_dist = instr_tu[1]
        point_count += c_dist
    return point_count


def polygon_builder(instr_tus):
    polygon = [0]
    location = 0
    for instr_tu in instr_tus:
        c_dir = instr_tu[0]
        c_dist = instr_tu[1]
        location += c_dir * c_dist
        polygon.append(location)
    return polygon


def total_area_by_pick(instr_tus):
    within = points_within(polygon_builder(instr_tus))
    on_line = points_on_line(instr_tus)
    return int(within + on_line / 2 + 1)


tus_1 = []
tus_2 = []
for instr in dig_instrs:
    c_dr, c_ds, c_co = instr.split(' ')
    tus_1.append((d_map[c_dr], int(c_ds)))

    col_dist_hex = c_co[2:7]
    col_dir_val = c_co[7]
    tus_2.append((i_map[col_dir_val], int('0x' + col_dist_hex, 16)))

print(total_area_by_pick(tus_1))
print(total_area_by_pick(tus_2))
