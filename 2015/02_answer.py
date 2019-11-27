p1 = 0
p2 = 0

import numpy as np;

boxLines = open('02_input').readlines()

boxSorts = []
for boxLine in boxLines:
    boxSortArr = sorted([int(dim) for dim in boxLine.split('x')])
    boxSorts.append(boxSortArr)

for box in boxSorts:
    p1 += box[0] * box[1] * 3  # 3 for extra required slack beyond surface area
    p1 += box[0] * box[2] * 2
    p1 += box[1] * box[2] * 2
    p2 += box[0] * 2 + box[1] * 2
    p2 += np.prod(box)

print('Part 1:', p1)
print('Part 2:', p2)
