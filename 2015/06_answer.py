import collections
import re

instructions = open('06_input').readlines()

p1 = 0
p2 = 0

gridp1 = collections.defaultdict(lambda: collections.defaultdict(int))
gridp2 = collections.defaultdict(lambda: collections.defaultdict(int))
for x in range(0, 1000):
    for y in range(0, 1000):
        gridp1[x][y] = 0
        gridp2[x][y] = 0

for instr in instructions:
    m = re.match(r"(turn on|turn off|toggle)\s(\d{1,3}),(\d{1,3})\sthrough\s(\d{1,3}),(\d{1,3})", instr)
    opt, leftX, bottomY, rightX, topY = m[1], int(m[2]), int(m[3]), int(m[4]), int(m[5])
    for x in range(leftX, rightX + 1):
        for y in range(bottomY, topY + 1):
            if opt == "turn on":
                gridp1[x][y] = 1
                gridp2[x][y] += 1
            elif opt == "turn off":
                gridp1[x][y] = 0
                if gridp2[x][y] != 0:
                    gridp2[x][y] -= 1
            elif opt == "toggle":
                gridp1[x][y] = +(not gridp1[x][y])
                gridp2[x][y] += 2

for x in range(0, 1000):
    for y in range(0, 1000):
        p1 += gridp1[x][y]
        p2 += gridp2[x][y]

print('Part 1:', p1)
print('Part 2:', p2)
