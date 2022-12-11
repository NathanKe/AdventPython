from collections import deque

input_text = open('11_input').read()


class Monkey:
    def __init__(self, in_text):
        self.inspection_count = 0
        id_line, start_line, op_line, test_line, true_line, false_line = in_text.split("\n")
        self.id = int(id_line[-2:-1])
        self.start_items = deque(map(int, start_line.split(": ")[1].split(", ")))
        self.op_instr = op_line.split(" = ")[1]
        self.test_mod = int(test_line.split(" ")[-1])
        self.true_target = int(true_line.split(" ")[-1])
        self.false_target = int(false_line.split(" ")[-1])

    def apply_operation(self, old):
        self.inspection_count += 1
        return eval(self.op_instr)

    def single_monkey_round(self):
        true_throws = deque()
        false_throws = deque()
        while self.start_items:
            cur_item = self.start_items.popleft()
            op_applied = self.apply_operation(cur_item)
            worry_reduce = op_applied // 3
            test_res = worry_reduce % self.test_mod == 0
            if test_res:
                true_throws.appendleft(worry_reduce)
            else:
                false_throws.appendleft(worry_reduce)
        return {self.true_target: true_throws, self.false_target: false_throws}

    def single_monkey_round_part2(self, in_mega_mod):
        true_throws = deque()
        false_throws = deque()
        while self.start_items:
            cur_item = self.start_items.popleft()
            op_applied = self.apply_operation(cur_item)
            worry_reduce = op_applied
            test_res = worry_reduce % self.test_mod == 0
            mega_mod_applied = worry_reduce % in_mega_mod
            if test_res:
                true_throws.appendleft(mega_mod_applied)
            else:
                false_throws.appendleft(mega_mod_applied)
        return {self.true_target: true_throws, self.false_target: false_throws}


class Barrel:
    def __init__(self, in_text):
        self.monkeys = {}
        self.mega_mod = 1
        for ix, m_text in enumerate(in_text.split("\n\n")):
            self.monkeys[ix] = Monkey(m_text)
            self.mega_mod *= self.monkeys[ix].test_mod

    def troop_round(self):
        for k, cur_monkey in self.monkeys.items():
            throw_res = cur_monkey.single_monkey_round()
            for tf, thr in throw_res.items():
                while thr:
                    self.monkeys[tf].start_items.append(thr.pop())

    def troop_round_part2(self):
        for k, cur_monkey in self.monkeys.items():
            throw_res = cur_monkey.single_monkey_round_part2(self.mega_mod)
            for tf, thr in throw_res.items():
                while thr:
                    self.monkeys[tf].start_items.append(thr.pop())

    def monkey_business(self):
        inspection_counts = [m.inspection_count for m in self.monkeys.values()]
        inspection_counts.sort(reverse=True)
        return inspection_counts[0] * inspection_counts[1]


problem_barrel = Barrel(input_text)
for i in range(20):
    problem_barrel.troop_round()
print(problem_barrel.monkey_business())

problem_barrel2 = Barrel(input_text)
for i in range(10000):
    problem_barrel2.troop_round_part2()
print(problem_barrel2.monkey_business())
