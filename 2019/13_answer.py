import collections
import operator


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


class GameState:
    def __init__(self, p_inps, p_code):
        self.code = IntCode(p_inps, p_code)
        self.board = collections.defaultdict(lambda: collections.defaultdict(int))
        self.score = 0

    def paddle_col(self):
        for c in self.board[21].keys():
            if self.board[21][c] == 3:
                return c
        return None

    def parse_next_three_outputs(self):
        col = self.code.get_next_out()
        row = self.code.get_next_out()
        out = self.code.get_next_out()
        if col == -1 and row == 0:
            self.score = out
        else:
            if out == 4:
                cur_paddle_col = self.paddle_col()
                if cur_paddle_col is not None and cur_paddle_col < col:
                    self.code.inps.append(1)
                elif cur_paddle_col is not None and cur_paddle_col > col:
                    self.code.inps.append(-1)
                else:
                    self.code.inps.append(0)
            self.board[row][col] = out

    def play_to_exit(self):
        while not self.code.halt:
            self.parse_next_three_outputs()

    def block_count(self):
        b_c = 0
        for r in self.board.keys():
            for c in self.board[r].keys():
                if self.board[r][c] == 2:
                    b_c += 1
        return b_c


puzzle = list(map(int, open('13_input').read().split(',')))

game = GameState([], puzzle)
game.play_to_exit()
print('Part 1: ', game.block_count())

puzzle_2 = puzzle.copy()
puzzle_2[0] = 2
game_2 = GameState([], puzzle_2)
game_2.play_to_exit()
print('Part 2: ', game_2.score)
