import re
import math
from itertools import combinations


class HailParticle:
    def __init__(self, x_start, y_start, z_start, x_vel, y_vel, z_vel):
        self.x_start = x_start
        self.y_start = y_start
        self.z_start = z_start
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.z_vel = z_vel

    def print_val(self):
        out_str = ""
        out_str += str(self.x_start) + ","
        out_str += str(self.y_start) + ","
        out_str += str(self.z_start)
        out_str += ":"
        out_str += str(self.x_vel) + ","
        out_str += str(self.y_vel) + ","
        out_str += str(self.z_vel)
        return out_str


stone_lines = open('24_input').read().splitlines()
hail_objs = []
for line in stone_lines:
    nums = map(int, re.findall(r"-?\d+", line))
    cur_obj = HailParticle(*nums)
    hail_objs.append(cur_obj)

hail_pairs = list(combinations(hail_objs, 2))

p1_min_x = 200000000000000
p1_min_y = 200000000000000
p1_max_x = 400000000000000
p1_max_y = 400000000000000
