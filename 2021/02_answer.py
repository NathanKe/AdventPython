instructions = open('02_input').read().splitlines()


class Submarine:
    def __init__(self):
        self.x = 0
        self.d = 0

    def parse_instruction(self, instr):
        instr_type, val_str = instr.split(" ")
        val = int(val_str)
        if instr_type == "forward":
            self.x += val
        elif instr_type == "down":
            self.d += val
        elif instr_type == "up":
            self.d -= val

    def depth_times_horiz(self):
        return self.d * self.x


sub = Submarine()
for cur_instr in instructions:
    sub.parse_instruction(cur_instr)

print("Part 1: ", sub.depth_times_horiz())


class Submarine2:
    def __init__(self):
        self.x = 0
        self.d = 0
        self.a = 0

    def parse_instruction(self, instr):
        instr_type, val_str = instr.split(" ")
        val = int(val_str)
        if instr_type == "forward":
            self.x += val
            self.d += val * self.a
        elif instr_type == "down":
            self.a += val
        elif instr_type == "up":
            self.a -= val

    def depth_times_horiz(self):
        return self.d * self.x


sub2 = Submarine2()
for cur_instr in instructions:
    sub2.parse_instruction(cur_instr)

print("Part 1: ", sub2.depth_times_horiz())
