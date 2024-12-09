import math
from collections import defaultdict
from collections import Counter
from itertools import combinations

grid_lines = open('08_input').read().splitlines()

MAX_ROW = len(grid_lines)
MAX_COL = len(grid_lines[0])

grid_dict = defaultdict(lambda: '-')

for ri, rv in enumerate(grid_lines):
    for ci, cv in enumerate(rv):
        if cv != '.':
            grid_dict[ri + ci*1j] = cv


uniq_frequencies = list(set(grid_dict.values()))


def manhat_distance(i_p1, i_p2):
    return abs(i_p1.real - i_p2.real) + abs(i_p1.imag - i_p2.imag)
    # return math.sqrt((i_p1.real - i_p2.real)**2 + (i_p1.imag - i_p2.imag)**2)

def manhat_vector(i_p1, i_p2):
    return (i_p2.real - i_p1.real) + 1j * (i_p2.imag - i_p1.imag)


antinodeSet = set()

for ri in range(MAX_ROW):
    for ci in range(MAX_COL):
        cur_loc = ri + 1j * ci
        for fq in uniq_frequencies:
            if cur_loc not in antinodeSet:
                targets = [k for k, v in grid_dict.items() if v == fq]
                for tg in targets:
                    distance = manhat_vector(cur_loc, tg)
                    assert(cur_loc + distance in targets)
                    if (abs(distance.real) > 0 or abs(distance.imag) > 0) and cur_loc + distance + distance in targets:
                        antinodeSet.add(cur_loc)
                        break

print(len(antinodeSet))

antinodeSet2 = set()

for ri in range(MAX_ROW):
    for ci in range(MAX_COL):
        cur_loc = ri + 1j * ci
        for fq in uniq_frequencies:
            if cur_loc not in antinodeSet2:
                targets = [k for k, v in grid_dict.items() if v == fq]
                for tg in targets:
                    distance = manhat_vector(cur_loc, tg)
                    if abs(distance.real) > 0 or abs(distance.imag) > 0:
                        gcd = math.gcd(int(distance.real), int(distance.imag))
                        redux_distance = distance.real / gcd + 1j * distance.imag / gcd
                        big_sweeping_line = [cur_loc + i * redux_distance for i in range(-1 * MAX_ROW, MAX_ROW)]
                        intersection = set(big_sweeping_line).intersection(set(targets))
                        if len(intersection) >= 2:
                            antinodeSet2.add(cur_loc)
                            break
                    elif len(targets) >= 2:
                        antinodeSet2.add(cur_loc)
                        break

print(len(antinodeSet2))
