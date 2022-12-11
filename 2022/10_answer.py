instruction_set = open('10_input').read().splitlines()


class System:
    def __init__(self):
        self.active_cycle_number = 1
        self.regX = 1
        # set a dummy value for index 0.  there is no 'zeroth' cycle, so skip that
        self.signalStrengths = [0]
        self.crt = ""

    def signal_strength_sum(self, in_index_list):
        return sum([self.signalStrengths[x] for x in in_index_list])

    def add_to_crt(self):
        sprite = [self.regX - 1, self.regX, self.regX + 1]
        if (self.active_cycle_number - 1) % 40 in sprite:
            self.crt += "█"
        else:
            self.crt += " "

    def update_signal_strengths(self):
        self.signalStrengths.append(self.active_cycle_number * self.regX)
        self.add_to_crt()
        self.active_cycle_number += 1

    def parse(self, in_instr):
        if in_instr == "noop":
            self.update_signal_strengths()
        else:
            reg_change = int(in_instr.split(" ")[1])
            self.update_signal_strengths()
            self.update_signal_strengths()
            self.regX += reg_change


problem_system = System()
for instr in instruction_set:
    problem_system.parse(instr)

index_list = [20, 60, 100, 140, 180, 220]
print("Part 1: ", problem_system.signal_strength_sum(index_list))

out_str = ""
for ix in index_list:
    line = problem_system.crt[ix - 20:ix + 20]
    out_str += line
    out_str += "\n"

print(out_str)
