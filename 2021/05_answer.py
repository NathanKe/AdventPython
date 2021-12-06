from collections import Counter

data = open('05_input').read().splitlines()

horiz_endpoint_set = []
verti_endpoint_set = []
diaga_endpoint_set = []
for line in data:
    left, right = line.split(' -> ')
    lx, ly = map(int, left.split(','))
    rx, ry = map(int, right.split(','))
    if lx == rx:
        verti_endpoint_set.append(((lx, ly), (rx, ry)))
    elif ly == ry:
        horiz_endpoint_set.append(((lx, ly), (rx, ry)))
    else:
        diaga_endpoint_set.append(((lx, ly), (rx, ry)))

covered_points = []
for h_end in horiz_endpoint_set:
    y = h_end[0][1]
    low_x, high_x = sorted([h_end[0][0], h_end[1][0]])
    for x in range(low_x, high_x + 1):
        covered_points.append((x, y))
for v_end in verti_endpoint_set:
    x = v_end[0][0]
    low_y, high_y = sorted([v_end[0][1], v_end[1][1]])
    for y in range(low_y, high_y + 1):
        covered_points.append((x, y))

point_counter = Counter(covered_points)
commonality_counter = Counter(point_counter.values())
overlap_count = 0
for k, v in commonality_counter.items():
    if k != 1:
        overlap_count += v

print("Part 1: ", overlap_count)

for d_end in diaga_endpoint_set:
    if d_end[0][0] < d_end[1][0]:
        left = d_end[0]
        right = d_end[1]
    else:
        left = d_end[1]
        right = d_end[0]
    if left[1] < right[1]:
        y_incr = 1
    else:
        y_incr = -1
    y = left[1]
    for x in range(left[0], right[0] + 1):
        covered_points.append((x, y))
        y += y_incr

point_counter = Counter(covered_points)
commonality_counter = Counter(point_counter.values())
overlap_count = 0
for k, v in commonality_counter.items():
    if k != 1:
        overlap_count += v

print("Part 2: ", overlap_count)
