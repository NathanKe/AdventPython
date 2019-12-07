class AsemBunny:
    def __init__(self, p_reg_init, p_code):
        self.reg = p_reg_init[:]
        self.ind = 0
        self.code = p_code[:]
        self.halt = False

    def halt_check(self):
        if self.ind >= len(self.code):
            self.halt = True

    def exec_intstr(self):
        cmd = self.code[self.ind]
        cmd_type = cmd.split(' ')[0]
        if cmd_type == 'cpy':
            self.exec_cpy(cmd)
        elif cmd_type == 'inc':
            self.exec_inc(cmd)
        elif cmd_type == 'dec':
            self.exec_dec(cmd)
        elif cmd_type == 'jnz':
            self.exec_jnz(cmd)
        self.halt_check()

    def exec_code(self):
        while not self.halt:
            self.exec_intstr()
        return self.reg

    def exec_cpy(self, cmd):
        val, dest = cmd.split(' ')[1:]
        if val in ['a', 'b', 'c', 'd']:
            val = self.reg[ord(val) - 97]
        self.reg[ord(dest) - 97] = int(val)
        self.ind += 1

    def exec_inc(self, cmd):
        self.reg[ord(cmd[-1]) - 97] += 1
        self.ind += 1

    def exec_dec(self, cmd):
        self.reg[ord(cmd[-1]) - 97] -= 1
        self.ind += 1

    def exec_jnz(self, cmd):
        val, jump_len = cmd.split(' ')[1:]
        if val in ['a', 'b', 'c', 'd']:
            val = self.reg[ord(val) - 97]
        if val != 0:
            self.ind += int(jump_len)
        else:
            self.ind += 1


t_1 = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a""".splitlines()

puzzle = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 19 c
cpy 11 d
inc a
dec d
jnz d -2
dec c
jnz c -5
""".splitlines()

print('Test 1: ', AsemBunny([0, 0, 0, 0], t_1).exec_code()[0])
print('Part 1: ', AsemBunny([0, 0, 0, 0], puzzle).exec_code()[0])
print('Part 2: ', AsemBunny([0, 0, 1, 0], puzzle).exec_code()[0])
