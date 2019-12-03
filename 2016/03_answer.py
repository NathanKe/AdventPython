import re

lines = open('03_input').read().splitlines()
lines_split = list(map(lambda l: list(re.search(r"(\d+)\s+(\d+)\s+(\d+)", l).groups()), lines))
lines_ints = list(map(lambda li: list(map(int, li)), lines_split))
lines_sorted = list(map(sorted, lines_ints))

triangles = list(filter(lambda tr: tr[0] + tr[1] > tr[2], lines_sorted))

print('Part 1: ', len(triangles))

new_lines = []
for i in range(0, len(lines_ints), 3):
    a = lines_ints[i]
    b = lines_ints[i + 1]
    c = lines_ints[i + 2]
    new_lines.append([a[0], b[0], c[0]])
    new_lines.append([a[1], b[1], c[1]])
    new_lines.append([a[2], b[2], c[2]])

new_lines_sorted = lines_sorted = list(map(sorted, new_lines))
new_triangles = list(filter(lambda tr: tr[0] + tr[1] > tr[2], new_lines_sorted))
print('Part 1: ', len(new_triangles))
