import re
from collections import Counter

lines = open('01_input').read().split('\n')

lefts = []
rights = []

for i in range(len(lines)-1):
    cl, cr = re.split(r"\s+",lines[i])
    lefts.append(int(cl))
    rights.append(int(cr))

lefts.sort()
rights.sort()


zipper = list(zip(lefts, rights))

diffSum = 0
for i in range(len(zipper)):
    diffSum += abs(zipper[i][0]-zipper[i][1])

print(diffSum)

lookup = Counter(rights)

simSum = 0
for left in lefts:
    simSum += left * lookup[left]

print(simSum)