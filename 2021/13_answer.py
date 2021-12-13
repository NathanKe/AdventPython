input_data = open('13_input').read().splitlines()


class Paper:
    def __init__(self, data):
        self.dots = set()
        self.fold_instructions = []
        for line in input_data:
            if 'fold' in line:
                instr = line.split(' ')[-1]
                axis, val = instr.split('=')
                self.fold_instructions.append((axis, int(val)))
            elif line:
                x, y = map(int, line.split(','))
                self.dots.add((x, y))

    def execute_fold(self, instr):
        axis, val = instr
        n_dots = set()
        if axis == 'y':
            while self.dots:
                n_x, n_y = self.dots.pop()
                if n_y >= val:
                    n_y = 2 * val - n_y
                n_dots.add((n_x, n_y))
        if axis == 'x':
            while self.dots:
                n_x, n_y = self.dots.pop()
                if n_x >= val:
                    n_x = 2 * val - n_x
                n_dots.add((n_x, n_y))
        while n_dots:
            self.dots.add(n_dots.pop())

    def fold_all(self):
        first_fold = 0
        for i, instr in enumerate(self.fold_instructions):
            self.execute_fold(instr)
            if i == 0:
                first_fold = len(self.dots)
        return first_fold

    def pretty_print(self):
        max_x = max(map(lambda tu: tu[0], self.dots))
        max_y = max(map(lambda tu: tu[1], self.dots))

        out = "\n"
        for y in range(max_y + 1):
            row = ""
            for x in range(max_x + 1):
                ch = " "
                if (x, y) in self.dots:
                    ch = "█"
                row += ch
            row += "\n"
            out += row
        return out


paper = Paper(input_data)
print("Part 1: ", paper.fold_all())
print("Part 2: ", paper.pretty_print())
