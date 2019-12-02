import re

in_path = ["L1", "L5", "R1", "R3", "L4", "L5", "R5", "R1", "L2", "L2", "L3", "R4", "L2", "R3", "R1", "L2", "R5", "R3",
           "L4", "R4", "L3", "R3", "R3", "L2", "R1", "L3", "R2", "L1", "R4", "L2", "R4", "L4", "R5", "L3", "R1", "R1",
           "L1", "L3", "L2", "R1", "R3", "R2", "L1", "R4", "L4", "R2", "L189", "L4", "R5", "R3", "L1", "R47", "R4",
           "R1", "R3", "L3", "L3", "L2", "R70", "L1", "R4", "R185", "R5", "L4", "L5", "R4", "L1", "L4", "R5", "L3",
           "R2", "R3", "L5", "L3", "R5", "L1", "R5", "L4", "R1", "R2", "L2", "L5", "L2", "R4", "L3", "R5", "R1", "L5",
           "L4", "L3", "R4", "L3", "L4", "L1", "L5", "L5", "R5", "L5", "L2", "L1", "L2", "L4", "L1", "L2", "R3", "R1",
           "R1", "L2", "L5", "R2", "L3", "L5", "L4", "L2", "L1", "L2", "R3", "L1", "L4", "R3", "R3", "L2", "R5", "L1",
           "L3", "L3", "L3", "L5", "R5", "R1", "R2", "L3", "L2", "R4", "R1", "R1", "R3", "R4", "R3", "L3", "R3", "L5",
           "R2", "L2", "R4", "R5", "L4", "L3", "L1", "L5", "L1", "R1", "R2", "L1", "R3", "R4", "R5", "R2", "R3", "L2",
           "L1", "L5"]


class Walker:
    dir_ind = None
    x_loc = None
    y_loc = None
    dir_list = ['N', 'E', 'S', 'W']
    visited = None

    def __init__(self, init_dir_ind, init_x, init_y):
        self.dir_ind = init_dir_ind
        self.x_loc = init_x
        self.y_loc = init_y
        self.visited = [(0, 0)]

    def take_step(self, step):
        m = re.search(r"([LR])(\d+)", step)
        turn = m[1]
        step_len = int(m[2])

        if turn == 'R':
            self.dir_ind = (self.dir_ind + 1) % 4
        elif turn == 'L':
            self.dir_ind = (self.dir_ind - 1) % 4

        cur_dir = self.dir_list[self.dir_ind]
        if cur_dir == 'N':
            for i in range(1, step_len + 1):
                self.visited.append((self.x_loc, self.y_loc + i))
        elif cur_dir == 'E':
            for i in range(1, step_len + 1):
                self.visited.append((self.x_loc + i, self.y_loc))
        elif cur_dir == 'S':
            for i in range(1, step_len + 1):
                self.visited.append((self.x_loc, self.y_loc - i))
        elif cur_dir == 'W':
            for i in range(1, step_len + 1):
                self.visited.append((self.x_loc - i, self.y_loc))
        self.x_loc, self.y_loc = self.visited[-1]

    def take_path(self, path):
        for step in path:
            self.take_step(step)

    def dist_from_zero(self):
        return self.x_loc + self.y_loc


w = Walker(0, 0, 0)
w.take_path(in_path)
print('Part 1: ', w.dist_from_zero())

first_visit_twice = None
for i in range(1, len(w.visited)):
    if w.visited[i] in w.visited[0:i - 1]:
        first_visit_twice = w.visited[i]
        break

print('Part 2: ', first_visit_twice[0] + first_visit_twice[1])
