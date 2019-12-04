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

movement_map = {
    "1": {
        "U": "1",
        "D": "3",
        "L": "1",
        "R": "1"
    },
    "2": {
        "U": "2",
        "D": "6",
        "L": "2",
        "R": "3"
    },
    "3": {
        "U": "1",
        "D": "7",
        "L": "2",
        "R": "4"
    },
    "4": {
        "U": "4",
        "D": "8",
        "L": "3",
        "R": "4"
    },
    "5": {
        "U": "5",
        "D": "5",
        "L": "5",
        "R": "6"
    },
    "6": {
        "U": "2",
        "D": "A",
        "L": "5",
        "R": "7"
    },
    "7": {
        "U": "3",
        "D": "B",
        "L": "6",
        "R": "8"
    },
    "8": {
        "U": "4",
        "D": "C",
        "L": "7",
        "R": "9"
    },
    "9": {
        "U": "9",
        "D": "9",
        "L": "8",
        "R": "9"
    },
    "A": {
        "U": "6",
        "D": "A",
        "L": "A",
        "R": "B"
    },
    "B": {
        "U": "7",
        "D": "D",
        "L": "A",
        "R": "C"
    },
    "C": {
        "U": "8",
        "D": "C",
        "L": "B",
        "R": "C"
    },
    "D": {
        "U": "B",
        "D": "D",
        "L": "D",
        "R": "D"
    }
}


def result_code(num, chain):
    for i in range(len(chain)):
        dr = chain[i]
        nxt = movement_map[num][dr]
        num = nxt
    return num


def calc_code_2(code_seq):
    out = ''
    cur = '5'
    for code in code_seq:
        cur = result_code(cur, list(code))
        out += cur
    return out


print('Part 2: ', calc_code_2(input_codes))
