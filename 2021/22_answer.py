from collections import defaultdict
import re

reactor = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: False)))

steps = open('22_input').read().splitlines()

for step in steps:
    instr = step.split(' ')[0]
    low_x, high_x, low_y, high_y, low_z, high_z = map(int, re.findall(r"-?\d+", step))
    low_x = max(low_x, -50)
    low_y = max(low_y, -50)
    low_z = max(low_z, -50)
    high_x = min(high_x, 50)
    high_y = min(high_y, 50)
    high_z = min(high_z, 50)

    for x in range(low_x, high_x + 1):
        for y in range(low_y, high_y + 1):
            for z in range(low_z, high_z + 1):
                if instr == 'on':
                    reactor[x][y][z] = True
                else:
                    reactor[x][y][z] = False

cube_count = 0
for x in range(-50, 51):
    for y in range(-50, 51):
        for z in range(-50, 51):
            if reactor[x][y][z]:
                cube_count += 1

print("Part 1: ", cube_count)
