# going to hash by head, direction, completed straight count steps
# going to expand paths willy-nilly, and prune impossible one

import heapq

text_lines = open('17_input').read().splitlines()

directions = [1, -1, 1j, -1j]

heat_loss_map = {}
for r_n, r_v in enumerate(text_lines):
    for c_n, c_v in enumerate(r_v):
        cur_loc = r_n + 1j * c_n
        heat_loss_map[cur_loc] = int(c_v)


def heat_accrual(i_path):
    assert i_path[0] == 0 + 0j
    out_heat = 0
    for node in i_path[1:]:
        out_heat += heat_loss_map[node]
    return out_heat


def diff_runs(i_path):
    diff_run_arr = []
    diffs = [i_path[i + 1] - i_path[i] for i in range(len(i_path[:-1]))]

    left = diffs[0]
    cur_count = 1
    for d_n, d_v in enumerate(diffs[1:]):
        if d_v == left:
            cur_count += 1
        else:
            diff_run_arr.append(cur_count)
            cur_count = 1
        left = d_v
    diff_run_arr.append(cur_count)

    return diff_run_arr


def cmp_manhattan(i_s, i_d):
    return abs(i_s.real - i_d.real) + abs(i_s.imag - i_d.imag)


def path_is_valid(i_path, MAX_ROW, MAX_COL, min_run, max_run):
    i_head = i_path[-1]
    # boundary check
    if i_head.real < 0:
        return False
    if i_head.real > MAX_ROW:
        return False
    if i_head.imag < 0:
        return False
    if i_head.imag > MAX_COL:
        return False
    # double back check
    if len(i_path) >= 3:
        if i_path[-1] == i_path[-3]:
            return False
    # straight check
    # defined by max_run
    tail_css = completed_straight_steps(i_path)
    if 0 <= tail_css <= max_run:
        pass
    else:
        return False

    i_d_r = diff_runs(i_path)
    if len(i_d_r) >= 2:
        if not all([min_run <= a <= max_run for a in i_d_r[:-1]]):
            return False

    return True


def completed_straight_steps(i_path):
    if len(i_path) == 2:
        return 1
    diffs = [i_path[i] - i_path[i - 1] for i in range(1, len(i_path))]
    same_diff_count = 1
    cur_diff_index = -1
    while -1 * cur_diff_index < len(diffs):
        if diffs[cur_diff_index] == diffs[cur_diff_index - 1]:
            same_diff_count += 1
            cur_diff_index -= 1
        else:
            break
    return same_diff_count


def path_to_key(i_path):
    i_head = i_path[-1]
    i_dir = i_path[-1] - i_path[-2]
    i_css = completed_straight_steps(i_path)
    return i_head, i_dir, i_css


class PathObj:
    def __init__(self, path, destination):
        self.path = path
        self.head, self.dir, self.css = path_to_key(path)
        self.destination = destination
        self.heat = heat_accrual(self.path)
        self.rem_dist = cmp_manhattan(self.head, self.destination)
        self.heur = self.heat + self.rem_dist

    def __lt__(self, other):
        return self.heur < other.heur

    def __eq__(self, other):
        return self.head == other.head and self.dir == other.dir and self.css == other.css


def a_star(min_run, max_run):
    best_guess_total_cost_loc_leaving_map = {}
    best_known_cost_so_far_loc_leaving_map = {}
    for r_n, r_v in enumerate(text_lines):
        for c_n, c_v in enumerate(r_v):
            cur_loc = r_n + 1j * c_n
            for d in directions:
                for sc in range(max_run + 1):
                    best_guess_total_cost_loc_leaving_map[(cur_loc, d, sc)] = float('inf')
                    best_known_cost_so_far_loc_leaving_map[(cur_loc, d, sc)] = float('inf')

    MAX_ROW = max(map(lambda cm: cm.real, heat_loss_map.keys()))
    MAX_COL = max(map(lambda cm: cm.imag, heat_loss_map.keys()))

    destination = MAX_ROW + 1j * MAX_COL

    start_down = [i for i in range(min_run + 1)]
    start_right = [i * 1j for i in range(min_run + 1)]

    best_known_cost_so_far_loc_leaving_map[(1, 1, 1)] = 0
    best_known_cost_so_far_loc_leaving_map[(1, 1j, 1)] = 0
    best_known_cost_so_far_loc_leaving_map[(1j, 1, 1)] = 0
    best_known_cost_so_far_loc_leaving_map[(1j, 1j, 1)] = 0

    open_set = [PathObj(start_down, destination), PathObj(start_right, destination)]
    best_finish = float('inf')
    best_path = None

    while open_set:
        active = heapq.heappop(open_set)
        print(len(open_set), active.head)
        if active.path[-1] == destination:
            if min_run <= completed_straight_steps(active.path) <= max_run:
                if active.heat < best_finish:
                    best_finish = active.heat
                    best_path = active.path

        for n_d in directions:
            new_path = active.path[::] + [active.path[-1] + n_d]
            if path_is_valid(new_path, MAX_ROW, MAX_COL, min_run, max_run):
                new_head, new_dir, new_css = path_to_key(new_path)
                new_obj = PathObj(new_path, destination)
                tentative_known_so_far = new_obj.heat
                rem_dist = new_obj.rem_dist
                if tentative_known_so_far + rem_dist > best_finish:
                    pass
                elif tentative_known_so_far < best_known_cost_so_far_loc_leaving_map[(new_head, new_dir, new_css)]:
                    best_known_cost_so_far_loc_leaving_map[(new_head, new_dir, new_css)] = tentative_known_so_far
                    best_guess_total_cost_loc_leaving_map[
                        (new_head, new_dir, new_css)] = tentative_known_so_far + rem_dist
                    new_obj = PathObj(new_path, destination)
                    heapq.heappush(open_set, new_obj)

    return best_finish, best_path
