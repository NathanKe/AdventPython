from collections import deque

input_text = open('11_input').read()


def instr_eval(old, instr):
    return eval(instr)


class Barrel:
    def __init__(self, in_text):
        self.inspection_counts = []
        self.instr_strings = []
        self.true_false_destinations = []
        self.mod_checks = []
        self.mega_mod = 1
        self.state = deque()
        for ix, m_text in enumerate(in_text.split("\n\n")):
            self.inspection_counts.append(0)
            id_line, start_line, op_line, test_line, true_line, false_line = m_text.split("\n")
            start_items = deque(map(int, start_line.split(": ")[1].split(", ")))
            self.state.extend([(ix, itm) for itm in start_items])
            self.instr_strings.append(op_line.split(" = ")[1])
            self.mod_checks.append(int(test_line.split(" ")[-1]))
            self.mega_mod *= int(test_line.split(" ")[-1])
            self.true_false_destinations.append((int(true_line.split(" ")[-1]), int(false_line.split(" ")[-1])))

        self.monkey_count = len(self.inspection_counts)
        self.item_count = len(self.state)

    def part_1_round(self):
        for monkey_index in range(self.monkey_count):
            for item_index in range(self.item_count):
                owner, cur_val = self.state.popleft()
                if owner == monkey_index:
                    self.inspection_counts[monkey_index] += 1
                    new_val = instr_eval(cur_val, self.instr_strings[monkey_index])
                    worry_reduce = new_val // 3
                    if worry_reduce % self.mod_checks[monkey_index] == 0:
                        self.state.append((self.true_false_destinations[monkey_index][0], worry_reduce))
                    else:
                        self.state.append((self.true_false_destinations[monkey_index][1], worry_reduce))
                else:
                    self.state.append((owner, cur_val))

    def part_2_round(self):
        for monkey_index in range(self.monkey_count):
            for item_index in range(self.item_count):
                owner, cur_val = self.state.popleft()
                if owner == monkey_index:
                    self.inspection_counts[monkey_index] += 1
                    new_val = instr_eval(cur_val, self.instr_strings[monkey_index])
                    worry_reduce = new_val % self.mega_mod
                    if worry_reduce % self.mod_checks[monkey_index] == 0:
                        self.state.append((self.true_false_destinations[monkey_index][0], worry_reduce))
                    else:
                        self.state.append((self.true_false_destinations[monkey_index][1], worry_reduce))
                else:
                    self.state.append((owner, cur_val))

    def monkey_business(self):
        top_two = sorted(self.inspection_counts, reverse=True)[0:2]
        return top_two[0] * top_two[1]


barrel_p1 = Barrel(input_text)
for i in range(20):
    barrel_p1.part_1_round()
print(barrel_p1.monkey_business())

barrel_p2 = Barrel(input_text)
for i in range(10000):
    barrel_p2.part_2_round()
print(barrel_p2.monkey_business())
