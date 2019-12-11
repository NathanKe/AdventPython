import operator
import collections


class IntCode:
    def __init__(self, inps, init_code):
        self.code = collections.defaultdict(int)
        for i in range(len(init_code)):
            self.code[i] = init_code[i]
        self.indx = 0
        self.outs = []
        self.inps = inps
        self.inp_ind = 0
        self.halt = False
        self.rel_base = 0

    def get_nth_param(self, n):
        mode = (self.code[self.indx] // 10 ** (1 + n)) % 10
        #              0 = position              1 = immediate  2 = relative
        base_params = [self.code[self.indx + n], self.indx + n, self.code[self.indx + n] + self.rel_base]
        param = base_params[mode]
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

    def run_instr(self):
        cmd = self.code[self.indx] % 100
        param1, param2, param3 = self.get_n_params(3)
        if cmd == 1:
            self.ex_combine(operator.add, param1, param2, param3)
        elif cmd == 2:
            self.ex_combine(operator.mul, param1, param2, param3)
        elif cmd == 3:
            self.ex_put_input(param1)
        elif cmd == 4:
            self.ex_write_out(param1)
        elif cmd == 5:
            self.ex_jump_if(operator.truth, param1, param2)
        elif cmd == 6:
            self.ex_jump_if(operator.not_, param1, param2)
        elif cmd == 7:
            self.ex_compare(operator.lt, param1, param2, param3)
        elif cmd == 8:
            self.ex_compare(operator.eq, param1, param2, param3)
        elif cmd == 9:
            self.ex_rel_base_adj(param1)
        elif cmd == 99:
            self.ex_halt()

    def run_code_to_halt(self):
        while not self.halt:
            self.run_instr()
        return self.outs[-1]

    def run_code_to_next_out_or_halt(self):
        while self.code[self.indx] % 100 != 4 and self.code[self.indx] % 100 != 99:
            self.run_instr()
        self.run_instr()

    def get_next_out(self):
        self.run_code_to_next_out_or_halt()
        return self.outs[-1]

    def ex_combine(self, op, param1, param2, param3):
        self.code[param3] = op(self.code[param1], self.code[param2])
        self.indx += 4

    def ex_put_input(self, param1):
        self.code[param1] = self.inps[self.inp_ind]
        self.inp_ind += 1
        self.indx += 2

    def ex_write_out(self, param1):
        self.outs.append(self.code[param1])
        self.indx += 2

    def ex_jump_if(self, op, param1, param2):
        if op(self.code[param1]):
            self.indx = self.code[param2]
        else:
            self.indx += 3

    def ex_compare(self, op, param1, param2, param3):
        self.code[param3] = int(op(self.code[param1], self.code[param2]))
        self.indx += 4

    def ex_rel_base_adj(self, param1):
        self.rel_base += self.code[param1]
        self.indx += 2

    def ex_halt(self):
        self.halt = True


puzzle = [3,8,1005,8,330,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,29,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1001,8,0,51,1006,0,78,2,107,9,10,1006,0,87,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,82,2,1103,5,10,1,101,8,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,112,1006,0,23,1006,0,20,1,2,11,10,1,1007,12,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,148,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,170,2,101,12,10,2,5,7,10,1,102,10,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,205,1,1004,10,10,2,6,13,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1001,8,0,235,2,102,4,10,1006,0,16,1006,0,84,1006,0,96,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,269,1006,0,49,2,1003,6,10,2,1104,14,10,1006,0,66,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,305,2,1,11,10,101,1,9,9,1007,9,1020,10,1005,10,15,99,109,652,104,0,104,1,21102,838479487744,1,1,21102,1,347,0,1106,0,451,21101,666567967640,0,1,21101,358,0,0,1106,0,451,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,28994219048,0,1,21102,405,1,0,1105,1,451,21102,3375459559,1,1,21101,0,416,0,1106,0,451,3,10,104,0,104,0,3,10,104,0,104,0,21102,838433665892,1,1,21102,1,439,0,1106,0,451,21102,988669698816,1,1,21102,450,1,0,1105,1,451,99,109,2,21201,-1,0,1,21102,1,40,2,21101,482,0,3,21102,472,1,0,1105,1,515,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,477,478,493,4,0,1001,477,1,477,108,4,477,10,1006,10,509,1101,0,0,477,109,-2,2105,1,0,0,109,4,1201,-1,0,514,1207,-3,0,10,1006,10,532,21101,0,0,-3,22102,1,-3,1,21201,-2,0,2,21102,1,1,3,21101,551,0,0,1106,0,556,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,579,2207,-4,-2,10,1006,10,579,21201,-4,0,-4,1105,1,647,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21101,0,598,0,1106,0,556,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,617,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,639,22102,1,-1,1,21101,0,639,0,106,0,514,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]


def paint_runner(start_color, code_to_run):
    paint_board = collections.defaultdict(int)
    painted = collections.defaultdict(int)
    robo_pos = 0 + 0j
    paint_board[robo_pos] = start_color
    robo_dir = 1j
    robo_code = IntCode([], code_to_run)

    while not robo_code.halt:
        robo_code.inps.append(paint_board[robo_pos])
        color = robo_code.get_next_out()
        if robo_code.halt:
            break
        painted[robo_pos] += 1
        if color:
            paint_board[robo_pos] = 1
        else:
            paint_board[robo_pos] = 0
        dir_change = [1j, -1j][robo_code.get_next_out()]
        robo_dir = robo_dir * dir_change
        robo_pos = robo_pos + robo_dir

    return painted, paint_board


p1_painted, _ = paint_runner(0, puzzle)
print('Part 1', len(p1_painted.keys()))

_, p2_board = paint_runner(1, puzzle)

out_str = ""
for row in range(10):
    line = ""
    for col in range(50):
        # negate for positive y is up in complex plane, but rows decrement upwards
        cpx = col - 1j * row
        line += [' ', '#'][p2_board[cpx]]
    line += "\n"
    out_str += line

print(out_str)
