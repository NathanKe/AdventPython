import operator
import itertools

puzzle = [3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 30, 47, 64, 81, 98, 179, 260, 341, 422, 99999, 3, 9, 1001, 9, 5, 9, 4,
          9, 99, 3, 9, 1002, 9, 5, 9, 101, 4, 9, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9, 102, 3, 9, 9, 101, 2, 9, 9, 1002, 9,
          3, 9, 4, 9, 99, 3, 9, 1001, 9, 5, 9, 1002, 9, 3, 9, 1001, 9, 3, 9, 4, 9, 99, 3, 9, 1002, 9, 3, 9, 101, 2, 9,
          9, 102, 5, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3,
          9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9,
          1001, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 99, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9,
          102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9,
          1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002,
          9, 2, 9, 4, 9, 99, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 101, 1,
          9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1,
          9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 99, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1,
          9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4,
          9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9,
          99, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9,
          3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3,
          9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 99]


class IntCode:
    code = None
    indx = None
    outs = None
    inps = None
    inp_ind = None
    halt = None

    def __init__(self, inps, init_code):
        self.code = init_code[:]
        self.indx = 0
        self.outs = []
        self.inps = inps
        self.inp_ind = 0
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

    def run_code_to_halt(self):
        while not self.halt:
            self.run_instr()
        return self.outs[-1]

    def run_code_to_next_out_or_halt(self):
        #
        while self.code[self.indx] % 100 != 4 and self.code[self.indx] % 100 != 99:
            self.run_instr()
        self.run_instr()

    def get_next_out(self):
        self.run_code_to_next_out_or_halt()
        return self.outs[-1]

    def ex_combine(self, op):
        param1, param2, param3 = self.get_n_params(3)
        self.code[param3] = op(self.code[param1], self.code[param2])
        self.indx += 4

    def ex_put_input(self):
        param1, _, _ = self.get_n_params(1)
        self.code[param1] = self.inps[self.inp_ind]
        self.inp_ind += 1
        self.indx += 2

    def ex_write_out(self):
        param1, _, _ = self.get_n_params(1)
        # assert sum(self.outs) == 0
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


def code_runner(p_inputs, p_code):
    int_code = IntCode(p_inputs, p_code)
    return int_code.run_code_to_halt()


def amplifier_chain_single(p_phases, p_a_init, p_code):
    assert len(p_phases) == 5
    amp_a = code_runner([p_phases[0], p_a_init], p_code)
    amp_b = code_runner([p_phases[1], amp_a], p_code)
    amp_c = code_runner([p_phases[2], amp_b], p_code)
    amp_d = code_runner([p_phases[3], amp_c], p_code)
    amp_e = code_runner([p_phases[4], amp_d], p_code)
    return amp_e


def max_amplifier_chain_single(p_phase_opts, p_a_init, p_code):
    chains = itertools.permutations(p_phase_opts)
    return max(map(lambda chain: amplifier_chain_single(chain, p_a_init, p_code), chains))


def amplifier_chain_feedback(p_phases, p_a_init, p_code):
    amp_a = IntCode([p_phases[0], p_a_init], p_code)
    amp_b = IntCode([p_phases[1]], p_code)
    amp_c = IntCode([p_phases[2]], p_code)
    amp_d = IntCode([p_phases[3]], p_code)
    amp_e = IntCode([p_phases[4]], p_code)

    while not amp_e.halt:
        amp_b.inps.append(amp_a.get_next_out())
        amp_c.inps.append(amp_b.get_next_out())
        amp_d.inps.append(amp_c.get_next_out())
        amp_e.inps.append(amp_d.get_next_out())
        amp_a.inps.append(amp_e.get_next_out())

    return amp_e.outs[-1]


def max_amplifier_chain_feedback(p_phase_opts, p_a_init, p_code):
    chains = itertools.permutations(p_phase_opts)
    return max(map(lambda chain: amplifier_chain_feedback(chain, p_a_init, p_code), chains))


print('Part 1: ', max_amplifier_chain_single([0, 1, 2, 3, 4], 0, puzzle))
print('Part 2: ', max_amplifier_chain_feedback([5, 6, 7, 8, 9], 0, puzzle))
