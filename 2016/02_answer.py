import re

input_codes = open('02_input').read().splitlines()


class Cursor:
    x_loc = None
    y_loc = None
    width = None
    height = None

    def __init__(self, x_st, y_st, wi, hi):
        self.x_loc = x_st
        self.y_loc = y_st
        self.width = wi
        self.height = hi

    def move_one(self, step):
        if step == 'U':
            self.y_loc = max(0, self.y_loc - 1)
        elif step == 'D':
            self.y_loc = min(self.height, self.y_loc + 1)
        if step == 'L':
            self.x_loc = max(0, self.x_loc - 1)
        elif step == 'R':
            self.x_loc = min(self.width, self.x_loc + 1)

    def move_seq(self, seq):
        for step in seq:
            self.move_one(step)
        return self.y_loc * (self.width + 1) + self.x_loc + 1


def calc_code(code_seq):
    c = Cursor(1, 1, 2, 2)
    out_code = ''
    for seq in code_seq:
        out_code += str(c.move_seq(seq))
    return out_code


print('Part 1: ', calc_code(input_codes))
