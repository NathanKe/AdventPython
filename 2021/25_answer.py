from collections import defaultdict


class CucumberField:
    def __init__(self, field_data):
        self.width = len(field_data[0])
        self.height = len(field_data)
        self.field = [['.'] * self.width] * self.height

        for r, line in enumerate(field_data):
            for c, char in enumerate(line):
                self.field[r][c] = char

        self.step_count = 0
        self.finished = False

    def step_right(self):
        movable = []
        for r in range(self.height):
            for c in range(self.width):
                if self.field[r][c] == ">":
                    if self.field[r][(c + 1) % self.width] == ".":
                        movable.append((r, c))
        for m in movable:
            self.field[m[0]][m[1]] = "."
            self.field[m[0]][(m[1] + 1) % self.width] = ">"

        if movable:
            return True

    def step_down(self):
        movable = []
        for r in range(self.height):
            for c in range(self.width):
                if self.field[r][c] == "v":
                    if self.field[(r + 1) % self.width][c] == ".":
                        movable.append((r, c))
        for m in movable:
            self.field[m[0]][m[1]] = "."
            self.field[(m[0] + 1) % self.width][m[1]] = "v"

        if movable:
            return True

    def step(self):
        right_success = self.step_right()
        down_success = self.step_down()
        if right_success or down_success:
            self.step_count += 1
            return True
        else:
            return False

    def run(self):
        while not self.finished:
            print("-------------------------------------")
            self.pretty_print()
            stepped = self.step()
            self.finished = not stepped

        return self.step_count

    def pretty_print(self):
        out = ""
        for r in range(self.height):
            for c in range(self.width):
                out += self.field[r][c]
            out += "\n"
        print(out)


cuces = CucumberField(open('25_input').read().splitlines())
