import math
import re
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

    def boundary_times_x_y(self, x_min, x_max, y_min, y_max):
        t_x_left = (x_min - self.x_start) / self.x_vel
        t_x_right = (x_max - self.x_start) / self.x_vel
        t_y_left = (y_min - self.y_start) / self.y_vel
        t_y_right = (y_max - self.y_start) / self.y_vel

        t_x_start, t_x_end = sorted([t_x_left, t_x_right])
        t_y_start, t_y_end = sorted([t_y_left, t_y_right])

        t_x_start = max(0, t_x_start)
        t_y_start = max(0, t_y_start)

        if t_x_end < 0 or t_y_end < 0:
            return [0, 0]

        t_both_start = max(t_x_start, t_y_start)
        t_both_end = min(t_x_end, t_y_end)

        if t_both_end < t_both_start:
            return [0, 0]

        return math.ceil(t_both_start), math.floor(t_both_end)

    def boundary_points(self, t_start, t_end):
        x_begin = self.x_start + self.x_vel * t_start
        x_end = self.x_start + self.x_vel * t_end
        y_begin = self.y_start + self.y_vel * t_start
        y_end = self.y_start + self.y_vel * t_end

        return (x_begin, y_begin), (x_end, y_end)


# calculate time t that particle is at bounds of box - for x and y directions
# clamp that result by a minimum of t = 0 to get future time only

# for a pair of points, take both of their time ranges and consider only the 'overlap' time
# where they both are in the box
# that should give us 4 end points - start and finish within box for each particle
# assert(?) at least one of these points _should_ be on the box boundary
# assert(?) all points should be within the box

# perform an transformation standardization
# W.L.G. - translate A_Start to origin, translating all 3 others accordingly
#        - rotate A_End to X-axis (y=0, x>0), rotating the other 2 accordingly
#        - A is now coincident with X-axis.
#        - If B crosses A, then B_Start_Y and B_End_Y will have different signs

def rotate_point(x, y, theta):
    out_x = x * math.cos(theta) - y * math.sin(theta)
    out_y = y * math.cos(theta) + x * math.sin(theta)
    return out_x, out_y


def standardize(a_start, a_end, b_start, b_end):
    # translate
    a_start_x_diff = 0 - a_start[0]
    a_start_y_diff = 0 - a_start[1]

    tr_a_start_x = a_start[0] + a_start_x_diff
    tr_a_start_y = a_start[1] + a_start_y_diff
    tr_a_end_x = a_end[0] + a_start_x_diff
    tr_a_end_y = a_end[1] + a_start_y_diff
    tr_b_start_x = b_start[0] + a_start_x_diff
    tr_b_start_y = b_start[1] + a_start_y_diff
    tr_b_end_x = b_end[0] + a_start_x_diff
    tr_b_end_y = b_end[1] + a_start_y_diff

    # rotate

    tr_a_end_angle = math.atan2(tr_a_end_y, tr_a_end_x)
    rot_a_end_x, rot_a_end_y = rotate_point(tr_a_end_x, tr_a_end_y, - 1 * tr_a_end_angle)
    rot_b_start_x, rot_b_start_y = rotate_point(tr_b_start_x, tr_b_start_y, - 1 * tr_a_end_angle)
    rot_b_end_x, rot_b_end_y = rotate_point(tr_b_end_x, tr_b_end_y, - 1 * tr_a_end_angle)

    return (tr_a_start_x, tr_a_start_y), (rot_a_end_x, rot_a_end_y), \
           (rot_b_start_x, rot_b_start_y), (rot_b_end_x, rot_b_end_y)


def x_intercept_by_two_points(ax, ay, bx, by):
    if math.isclose(ax, bx):
        return bx
    else:
        slope = (by - ay) / (bx - ax)
        if math.isclose(slope, 0):
            return 'HORZ!'
        else:
            x_intercept = ax - ay / slope
            return x_intercept


def crosses_by_boundary_points(a_start, a_end, b_start, b_end):
    stand_res = standardize(a_start, a_end, b_start, b_end)
    b_line_x_int = x_intercept_by_two_points(stand_res[2][0], stand_res[2][1], stand_res[3][0], stand_res[3][1])

    if b_line_x_int == 'HORZ!':
        return False
    else:
        if stand_res[0][0] <= b_line_x_int <= stand_res[1][0] and (
                stand_res[2][0] <= b_line_x_int <= stand_res[3][0] or stand_res[3][0] <= b_line_x_int <= stand_res[2][
            0]):
            if math.copysign(1, stand_res[2][1]) != math.copysign(1, stand_res[3][1]):
                return True
            else:
                return False
        else:
            return False


def crosses(h_o_a, h_o_b, min_x, max_x, min_y, max_y):
    a_bound_times = h_o_a.boundary_times_x_y(min_x, max_x, min_y, max_y)
    b_bound_times = h_o_b.boundary_times_x_y(min_x, max_x, min_y, max_y)

    if math.isclose(a_bound_times[0], 0) and math.isclose(a_bound_times[1], 0):
        return False
    if math.isclose(b_bound_times[0], 0) and math.isclose(b_bound_times[1], 0):
        return False

    a_start, a_end = h_o_a.boundary_points(*a_bound_times)
    b_start, b_end = h_o_b.boundary_points(*b_bound_times)

    return crosses_by_boundary_points(a_start, a_end, b_start, b_end)


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

intersection_count = 0
for hp in hail_pairs:
    cross_res = crosses(hp[0], hp[1], p1_min_x, p1_max_x, p1_min_y, p1_max_y)
    if cross_res:
        intersection_count += 1

print(intersection_count)
