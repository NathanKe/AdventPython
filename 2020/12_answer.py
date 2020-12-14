import cmath
import math


class Ship:
    dir_list = ['N', 'E', 'S', 'W']

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.dir_index = 1

    def parse_instruction(self, code, val):
        if code == 'N':
            self.pos_y += val
        elif code == 'S':
            self.pos_y -= val
        elif code == 'E':
            self.pos_x += val
        elif code == 'W':
            self.pos_x -= val
        elif code == 'R':
            dir_index_offset = val // 90
            self.dir_index = (self.dir_index + dir_index_offset) % 4
        elif code == 'L':
            dir_index_offset = val // 90
            self.dir_index = (self.dir_index - dir_index_offset) % 4
        elif code == 'F':
            self.parse_instruction(self.dir_list[self.dir_index], val)

    def parse_instruction_string(self, in_instr):
        code = in_instr[0]
        val = int(in_instr[1:])
        self.parse_instruction(code, val)


instr_set = open('12_input').read().splitlines()

ship = Ship()
for instr in instr_set:
    ship.parse_instruction_string(instr)

print('Part 1', abs(ship.pos_x) + abs(ship.pos_y))


class Ship2:
    dir_list = ['N', 'E', 'S', 'W']

    def __init__(self):
        self.ship_pos = 0 + 0j
        self.wayp_pos = 10 + 1j

    def parse_instruction(self, code, val):
        if code == 'E':
            self.wayp_pos += val
        elif code == 'W':
            self.wayp_pos -= val
        elif code == 'N':
            self.wayp_pos += val * 1j
        elif code == 'S':
            self.wayp_pos -= val * 1j
        elif code == 'R':
            self.wayp_pos *= cmath.exp(-1j * math.radians(val))
        elif code == 'L':
            self.wayp_pos *= cmath.exp(1j * math.radians(val))
        elif code == 'F':
            self.ship_pos += val * self.wayp_pos

    def parse_instruction_string(self, in_instr):
        code = in_instr[0]
        val = int(in_instr[1:])
        self.parse_instruction(code, val)


ship2 = Ship2()
for instr in instr_set:
    ship2.parse_instruction_string(instr)

print('Part 2', round(abs(ship2.ship_pos.real) + abs(ship2.ship_pos.imag)))
