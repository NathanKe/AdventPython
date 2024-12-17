from collections import deque


class IntCode:
    pointer = None
    reg_a = None
    reg_b = None
    reg_c = None

    commands = []

    def __init__(self, i_reg_a, i_reg_b, i_reg_c, i_commands):
        self.reg_a, self.reg_b, self.reg_c = i_reg_a, i_reg_b, i_reg_c
        self.commands = i_commands
        self.pointer = 0

    def execute_one(self):
        instruction = self.commands[self.pointer]
        literal = self.commands[self.pointer + 1]

        combo_dict = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: self.reg_a,
            5: self.reg_b,
            6: self.reg_c,
            7: None
        }

        combo = combo_dict[literal]

        out_val = -1

        # ADV : a = a / 2 ** combo
        if instruction == 0:
            self.reg_a = self.reg_a // 2 ** combo
            self.pointer += 2
        # BXL : b = b XOR lit
        elif instruction == 1:
            self.reg_b = self.reg_b ^ literal
            self.pointer += 2
        # BST : b = combo % 8
        elif instruction == 2:
            self.reg_b = combo % 8
            self.pointer += 2
        # JNZ : if a=0 > Nothing | pointer = literal
        elif instruction == 3:
            if self.reg_a == 0:
                self.pointer += 2
            else:
                self.pointer = literal
        # BXC : b = b ^ c
        elif instruction == 4:
            self.reg_b = self.reg_b ^ self.reg_c
            self.pointer += 2
        # OUT : output = combo % 8
        elif instruction == 5:
            out_val = combo % 8
            self.pointer += 2
        # BDV : b = a / 2 ** combo
        elif instruction == 6:
            self.reg_b = self.reg_a // 2 ** combo
            self.pointer += 2
        # CDV : c = a / 2 ** combo
        elif instruction == 7:
            self.reg_c = self.reg_a // 2 ** combo
            self.pointer += 2
        else:
            pass

        return out_val

    def execute_all(self):
        out_list = []
        while self.pointer < len(self.commands):
            exec_res = self.execute_one()
            if exec_res >= 0:
                out_list.append(exec_res)
        return out_list

    def execute_all_break(self):
        out_list = []
        while self.pointer < len(self.commands):
            # print(self.reg_a, self.reg_b, self.reg_c, self.pointer)
            exec_res = self.execute_one()
            if exec_res >= 0:
                out_list.append(exec_res)
            cur_len = len(out_list)
            if self.commands[:cur_len] != out_list or cur_len > len(self.commands):
                out_list = "BREAK"
                break

        return out_list

    def circular_execute(self):
        try_a = 0
        found = False
        while not found:
            if try_a % 10000 == 0:
                print(try_a)

            self.reg_a = try_a
            self.reg_b = 0
            self.reg_c = 0
            self.pointer = 0
            exec_res = self.execute_all_break()
            # print(exec_res)
            if exec_res != "BREAK" and exec_res == self.commands:
                found = True
            else:
                try_a += 1
        return try_a


comp = IntCode(62769524, 0, 0, [2, 4, 1, 7, 7, 5, 0, 3, 4, 0, 1, 7, 5, 5, 3, 0])
print(comp.execute_all())

comp = IntCode(62769524, 0, 0, [2, 4, 1, 7, 7, 5, 0, 3, 4, 0, 1, 7, 5, 5, 3, 0])
print(comp.circular_execute())
# print(comp.circular_execute())


# 2, 4, b = a % 8
# 1, 7, b = b ^ 7
# 7, 5, c = a // 2**b
# 0, 3, a = a // 2**3
# 4, 0, b = b ^ c
# 1, 7, b = b & 7
# 5, 5, out = b % 8
# 3, 0] jump 0
