import re

distance_report_lines = open('15_input').read().splitlines()

# x is imag, y is real.  y increase goes down the page

sensor_beacons = []
for line in distance_report_lines:
    sx, sy, bx, by = map(int, re.findall(r"-*\d+", line))
    sensor_beacons.append((sx, sy, bx, by))


SEARCH_ROW = 10


def calc_manhattan_distance(jx, jy, kx, ky):
    return abs(jx - kx) + abs(jy - ky)


cant_be_beacon = set()
for sx, sy, bx, by in sensor_beacons:

    manhattan_distance = calc_manhattan_distance(sx, sy, bx, by)

    if SEARCH_ROW in range(sy - manhattan_distance, sy + manhattan_distance + 1):
        dist_to_search_row = abs(sy - SEARCH_ROW)
        remaining_distance = manhattan_distance - dist_to_search_row
        cant_be_beacon.add(sx)
        for offset in range(remaining_distance + 1):
            cant_be_beacon.add(sx + offset)
            cant_be_beacon.add(sx - offset)


for sx, sy, bx, by in sensor_beacons:
    if by == SEARCH_ROW:
        if bx in cant_be_beacon:
            cant_be_beacon.remove(bx)

print("Part 1: ", len(cant_be_beacon))


# compute distance map
# for each cell in search area
# ---- for each beacon
# --------- if in range
# -------------- break
# ----------


sensor_distance_map = {}
for sx, sy, bx, by in sensor_beacons:
    sensor_distance_map[(sx, sy)] = calc_manhattan_distance(sx, sy, bx, by)


def in_range_of_a_beacon(qx, qy):
    for sx, sy, bx, by in sensor_beacons:
        dist_to_beacon = calc_manhattan_distance(qx, qy, bx, by)
        if dist_to_beacon <= sensor_distance_map[(sx, sy)]:
            return True
    return False


def set_builder(sx, sy, bx, by):
    vis_set = []
    m_d = calc_manhattan_distance(sx, sy, bx, by)
    for vert_steps_taken in range(m_d + 1):
        for steps_remain in range(m_d - vert_steps_taken + 1):
            vis_set.append((sx - steps_remain, sy - vert_steps_taken))
            vis_set.append((sx + steps_remain, sy - vert_steps_taken))
            vis_set.append((sx - steps_remain, sy + vert_steps_taken))
            vis_set.append((sx + steps_remain, sy + vert_steps_taken))
    return vis_set


def one_outside_of_range(sx, sy, bx, by):
    m_d = calc_manhattan_distance(sx, sy, bx, by)

    shell = []
    for i in range(0, m_d + 1):
        shell.append((sx + i + 1, sy + m_d - i))
        shell.append((sx + i + 1, sy - m_d + i))
        shell.append((sx - i + 1, sy + m_d - i))
        shell.append((sx - i + 1, sy - m_d + i))

    return shell

# mega_set = set().union(*[set_builder(*sb) for sb in sensor_beacons])
print("Done!")



# current thought:  calculate 'shells' of each sensor - those spaces exactly one unit out of range
# iterate over those, stopping when you find one that is out of range of
# shell size is square of (range + 1)


# pair-wise intersect "shells"?

# work more with range limits, not sets/arrays of actual ranges
