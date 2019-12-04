import re
import collections


class Screen:
    width = None
    height = None
    lights = None

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.lights = collections.defaultdict(lambda: collections.defaultdict(bool))

    def on_rectangle(self, w, h):
        for x in range(w):
            for y in range(h):
                self.lights[x][y] = True

    def rotate_col(self, col, shift):
        cur_col = collections.deque([self.lights[col][i] for i in range(self.height)])
        cur_col.rotate(shift)
        for i in range(self.height):
            self.lights[col][i] = cur_col[i]

    def rotate_row(self, row, shift):
        cur_row = collections.deque([self.lights[i][row] for i in range(self.width)])
        cur_row.rotate(shift)
        for i in range(self.width):
            self.lights[i][row] = cur_row[i]

    def parse_instr(self, instr):
        if 'rect' in instr:
            w, h = re.search(r"(\d+)x(\d+)", instr).groups()
            self.on_rectangle(int(w), int(h))
        elif 'row' in instr:
            row, shift = re.search(r"y=(\d+)\sby\s(\d+)", instr).groups()
            self.rotate_row(int(row), int(shift))
        elif 'column' in instr:
            col, shift = re.search(r"x=(\d+)\sby\s(\d+)", instr).groups()
            self.rotate_col(int(col), int(shift))

    def parse_instr_set(self, instr_set):
        for instr in instr_set:
            self.parse_instr(instr)

    def count_on(self):
        ct = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.lights[x][y]:
                    ct += 1
        return ct

    def out_string(self):
        out = '\n'
        for y in range(self.height):
            line = ''
            for x in range(self.width):
                if self.lights[x][y]:
                    line += 'X'
                else:
                    line += ' '
            line += '\n'
            out += line
        return out


puzzle_instr = open('08_input').read().splitlines()

scr = Screen(50, 6)
scr.parse_instr_set(puzzle_instr)
print('Part 1: ', scr.count_on())
print('Part 2:', scr.out_string())


