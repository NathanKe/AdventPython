raw = open('17_input').read()

on_set = set()
off_set = set([(i, j, k, l)
               for i in range(-13, 13) for j in range(-13, 13) for k in range(-13, 13) for l in range(-13, 13)])

for row in enumerate(raw.splitlines()):
    yy = row[0]
    for col in enumerate(row[1]):
        xx = col[0]
        if col[1] == '#':
            on_set.add((xx, yy, 0, 0))
        else:
            off_set.add((xx, yy, 0, 0))


def neighbor_set(point):
    neighbors = set()
    for cx in range(point[0] - 1, point[0] + 2):
        for cy in range(point[1] - 1, point[1] + 2):
            for cz in range(point[2] - 1, point[2] + 2):
                for cw in range(point[3] - 1, point[3] + 2):
                    if cx != point[0] or cy != point[1] or cz != point[2] or cw != point[3]:
                        neighbors.add((cx, cy, cz, cw))
    return neighbors


def active_neighbor_count(point, in_on_set):
    return len(neighbor_set(point) & in_on_set)


def iterate_state(in_on, in_off):
    out_on = set()
    out_off = set()
    for on_point in in_on:
        if 2 <= active_neighbor_count(on_point, in_on) <= 3:
            out_on.add(on_point)
        else:
            out_off.add(on_point)
    for off_point in in_off:
        if active_neighbor_count(off_point, in_on) == 3:
            out_on.add(off_point)
        else:
            out_off.add(off_point)
    return out_on, out_off


def n_iterations(iter_count, on, off):
    for _ in range(iter_count):
        on, off = iterate_state(on, off)
    return on, off


print('Part 1: ', len(n_iterations(6, on_set, off_set)[0]))
