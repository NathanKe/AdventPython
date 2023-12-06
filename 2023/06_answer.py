import re
import math

time_line, dist_line = open('06_input').read().splitlines()

times = list(map(int, re.findall(r"\d+", time_line)))
distances = list(map(int, re.findall(r"\d+", dist_line)))

race_tuples = list(zip(times, distances))


def win_count(i_time, i_dist):
    left_zero = (-i_time + (i_time ** 2 - 4 * i_dist) ** 0.5) / -2
    right_zero = (-i_time - (i_time ** 2 - 4 * i_dist) ** 0.5) / -2
    return math.ceil(right_zero) - math.floor(left_zero) - 1


prod = 1
for race in race_tuples:
    prod *= win_count(*race)

print(prod)


big_time = int(''.join(re.findall(r"\d", time_line)))
big_dist = int(''.join(re.findall(r"\d", dist_line)))

print(win_count(big_time, big_dist))



