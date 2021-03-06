import operator

puzzle_code = [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1101, 37, 34, 224, 101, -71, 224, 224, 4, 224, 1002,
               223, 8, 223, 101, 6, 224, 224, 1, 224, 223, 223, 1002, 113, 50, 224, 1001, 224, -2550, 224, 4, 224, 1002,
               223, 8, 223, 101, 2, 224, 224, 1, 223, 224, 223, 1101, 13, 50, 225, 102, 7, 187, 224, 1001, 224, -224,
               224, 4, 224, 1002, 223, 8, 223, 1001, 224, 5, 224, 1, 224, 223, 223, 1101, 79, 72, 225, 1101, 42, 42,
               225, 1102, 46, 76, 224, 101, -3496, 224, 224, 4, 224, 102, 8, 223, 223, 101, 5, 224, 224, 1, 223, 224,
               223, 1102, 51, 90, 225, 1101, 11, 91, 225, 1001, 118, 49, 224, 1001, 224, -140, 224, 4, 224, 102, 8, 223,
               223, 101, 5, 224, 224, 1, 224, 223, 223, 2, 191, 87, 224, 1001, 224, -1218, 224, 4, 224, 1002, 223, 8,
               223, 101, 4, 224, 224, 1, 224, 223, 223, 1, 217, 83, 224, 1001, 224, -124, 224, 4, 224, 1002, 223, 8,
               223, 101, 5, 224, 224, 1, 223, 224, 223, 1101, 32, 77, 225, 1101, 29, 80, 225, 101, 93, 58, 224, 1001,
               224, -143, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 4, 224, 1, 223, 224, 223, 1101, 45, 69, 225, 4, 223,
               99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227, 247, 1105, 1, 99999, 1005,
               227, 99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999,
               1006, 227, 274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1,
               0, 1105, 1, 99999, 1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1,
               99999, 7, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 329, 101, 1, 223, 223, 108, 677, 226, 224, 102, 2,
               223, 223, 1005, 224, 344, 1001, 223, 1, 223, 1108, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 359, 1001,
               223, 1, 223, 8, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 374, 1001, 223, 1, 223, 107, 226, 226, 224,
               102, 2, 223, 223, 1006, 224, 389, 101, 1, 223, 223, 1108, 677, 226, 224, 1002, 223, 2, 223, 1005, 224,
               404, 1001, 223, 1, 223, 108, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 419, 101, 1, 223, 223, 7, 226,
               677, 224, 1002, 223, 2, 223, 1006, 224, 434, 1001, 223, 1, 223, 107, 226, 677, 224, 102, 2, 223, 223,
               1005, 224, 449, 101, 1, 223, 223, 1108, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 464, 101, 1, 223,
               223, 7, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 479, 101, 1, 223, 223, 1007, 677, 677, 224, 1002,
               223, 2, 223, 1005, 224, 494, 101, 1, 223, 223, 1008, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 509,
               1001, 223, 1, 223, 107, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 524, 1001, 223, 1, 223, 8, 226, 226,
               224, 1002, 223, 2, 223, 1005, 224, 539, 1001, 223, 1, 223, 1007, 677, 226, 224, 102, 2, 223, 223, 1006,
               224, 554, 1001, 223, 1, 223, 1007, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 569, 1001, 223, 1, 223,
               8, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 584, 101, 1, 223, 223, 108, 226, 226, 224, 1002, 223, 2,
               223, 1006, 224, 599, 101, 1, 223, 223, 1107, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 614, 1001, 223,
               1, 223, 1107, 226, 677, 224, 102, 2, 223, 223, 1006, 224, 629, 1001, 223, 1, 223, 1008, 226, 677, 224,
               102, 2, 223, 223, 1005, 224, 644, 101, 1, 223, 223, 1107, 226, 226, 224, 102, 2, 223, 223, 1006, 224,
               659, 1001, 223, 1, 223, 1008, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 674, 1001, 223, 1, 223, 4, 223,
               99, 226]


class IntCode:
    code = None
    indx = None
    outs = None
    inp = None
    halt = None

    def __init__(self, inp, init_code):
        self.code = init_code[:]
        self.indx = 0
        self.outs = []
        self.inp = inp
        self.halt = False

    def run_instr(self):
        cmd = self.code[self.indx] % 100
        if cmd == 1:
            self.ex_combine(operator.add)
        elif cmd == 2:
            self.ex_combine(operator.mul)
        elif cmd == 3:
            self.ex_put_input()
        elif cmd == 4:
            self.ex_write_out()
        elif cmd == 5:
            self.ex_jump_if(operator.truth)
        elif cmd == 6:
            self.ex_jump_if(operator.not_)
        elif cmd == 7:
            self.ex_compare(operator.lt)
        elif cmd == 8:
            self.ex_compare(operator.eq)
        elif cmd == 99:
            self.ex_halt()

    def get_nth_param(self, n):
        mode = (self.code[self.indx] // 10 ** (1 + n)) % 10
        param = [self.code[self.indx + n], self.indx + n][mode]
        return param

    def get_n_params(self, n):
        assert 1 <= n <= 3
        param1 = self.get_nth_param(1)

        if n == 2 or n == 3:
            param2 = self.get_nth_param(2)
        else:
            param2 = None
        if n == 3:
            param3 = self.get_nth_param(3)
        else:
            param3 = None

        return param1, param2, param3

    def run_code(self):
        while not self.halt:
            self.run_instr()
        return self.outs[-1]

    def ex_combine(self, op):
        param1, param2, param3 = self.get_n_params(3)
        self.code[param3] = op(self.code[param1], self.code[param2])
        self.indx += 4

    def ex_put_input(self):
        param1, _, _ = self.get_n_params(1)
        self.code[param1] = self.inp
        self.indx += 2

    def ex_write_out(self):
        param1, _, _ = self.get_n_params(1)
        assert sum(self.outs) == 0
        self.outs.append(self.code[param1])
        self.indx += 2

    def ex_jump_if(self, op):
        param1, param2, _ = self.get_n_params(2)
        if op(self.code[param1]):
            self.indx = self.code[param2]
        else:
            self.indx += 3

    def ex_compare(self, op):
        param1, param2, param3 = self.get_n_params(3)
        self.code[param3] = int(op(self.code[param1], self.code[param2]))
        self.indx += 4

    def ex_halt(self):
        self.halt = True


print('Part 1: ', IntCode(1, puzzle_code).run_code())
print('Part 2: ', IntCode(5, puzzle_code).run_code())
