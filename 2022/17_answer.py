from collections import deque

# real is height above floor (floor at real = 0)
# imag is distance from left wall (left wall at imag = 0, right wall at imag = 8


test_instr = deque(">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>")


class Rock:
    def __init__(self, block_type, in_chamber, in_instr, in_full_instr):
        self.min_height = 0
        self.chamber = in_chamber
        self.highest_at_rest = max([0] + [x.real + 1 for x in self.chamber])
        self.instr = in_instr
        self.reset_instr = in_full_instr
        self.state = "FALLING"
        if block_type == "HORIZ":
            self.blocks = [complex(self.highest_at_rest + 3, 3),
                           complex(self.highest_at_rest + 3, 4),
                           complex(self.highest_at_rest + 3, 5),
                           complex(self.highest_at_rest + 3, 6)]
        elif block_type == "PLUS":
            self.blocks = [complex(self.highest_at_rest + 4, 3),
                           complex(self.highest_at_rest + 4, 4),
                           complex(self.highest_at_rest + 4, 5),
                           complex(self.highest_at_rest + 3, 4),
                           complex(self.highest_at_rest + 5, 4)]
        elif block_type == "ELL":
            self.blocks = [complex(self.highest_at_rest + 3, 3),
                           complex(self.highest_at_rest + 3, 4),
                           complex(self.highest_at_rest + 3, 5),
                           complex(self.highest_at_rest + 4, 5),
                           complex(self.highest_at_rest + 5, 5)]
        elif block_type == "VERT":
            self.blocks = [complex(self.highest_at_rest + 3, 3),
                           complex(self.highest_at_rest + 4, 3),
                           complex(self.highest_at_rest + 5, 3),
                           complex(self.highest_at_rest + 6, 3)]
        elif block_type == "SQUARE":
            self.blocks = [complex(self.highest_at_rest + 3, 3),
                           complex(self.highest_at_rest + 3, 4),
                           complex(self.highest_at_rest + 4, 3),
                           complex(self.highest_at_rest + 4, 4)]
        # self.right = max([b.imag for b in self.blocks])
        # self.left = 2j
        # self.bottom = highest_at_rest + 3

    def gas_push(self, direction):
        if direction == ">":
            if any([(b + 1j).imag >= 8 or (b + 1j) in self.chamber for b in self.blocks]):
                pass
            else:
                for b_ix in range(len(self.blocks)):
                    self.blocks[b_ix] += 1j
        elif direction == "<":
            if any([(b - 1j).imag <= 0 or (b - 1j) in self.chamber for b in self.blocks]):
                pass
            else:
                for b_ix in range(len(self.blocks)):
                    self.blocks[b_ix] -= 1j
        else:
            pass
        return

    def fall(self):
        if any([(b - 1).real < self.min_height or (b - 1) in self.chamber for b in self.blocks]):
            self.state = "LOCKED"
        else:
            for b_ix in range(len(self.blocks)):
                self.blocks[b_ix] -= 1

    def step(self):
        assert (len(self.instr) >= 1)
        self.gas_push(self.instr.popleft())
        self.fall()

    def trim_chamber(self):
        for row in reversed(range(int(self.highest_at_rest) + 5)):
            row_blocks = [b for b in self.chamber if b.real == row]
            if len(row_blocks) == 7:
                self.min_height = row
                self.chamber = [b for b in self.chamber if b.real >= row]
                break

    def process(self):
        while self.state == "FALLING":
            if len(self.instr) == 0:
                self.instr = self.reset_instr.copy()
            self.step()
        self.chamber.extend(self.blocks)
        self.trim_chamber()
        return self.chamber, self.instr

    def pretty_print(self):
        outstr = ""
        for r in range(int(self.highest_at_rest) + 5):
            rowstr = "|"
            for c in range(1, 8):
                if complex(r, c) in self.chamber:
                    rowstr += "#"
                else:
                    rowstr += " "
            rowstr += "|"
            outstr = rowstr + "\n" + outstr
        outstr += "+-------+"
        return outstr


rock_rotation = ["HORIZ", "PLUS", "ELL", "VERT", "SQUARE"]

real_input = open("17_input").read()
real_instr = deque(real_input)
#
# completed_rock_count = 0
# instruction_remnant = real_instr.copy()
# chamber_part_1 = []
# while completed_rock_count < 2023:
#     cur_rock = Rock(rock_rotation[completed_rock_count % 5], chamber_part_1, instruction_remnant, real_instr.copy())
#     chamber_part_1, instruction_remnant = cur_rock.process()
#     completed_rock_count += 1
#
# print("Part 1: ", cur_rock.highest_at_rest)


# complete one pass of instruction set to get started.  Mark its height and rocks used
# complete a second pass of instruction set to find the cyclical height additive.
# --- Mark that. count how many rocks it takes
# each subsequent cycle adds (2nd cycle height - 1st cycle height) and uses above # rocks
# NUMBER_EASY_CYCLES = (1000000000000 - (1st cycle rock count)) // (2nd cycle rock count)
# REMNANT_ROCKS = 1000000000000 - 1st Cycle Rock Count - NUMBER_EASY_CYCLES * 2nd cycle rock count
# check extra height added by remnant rocks
# add 1st cycle height plus subsequent cycle heights plus extra height
#####  But does each "easy cycle" start with the same rock type?


# does the input magically not have leftover jets?


# Process one complete instruction set:
