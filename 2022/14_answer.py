from collections import defaultdict


wall_text_lines = open('14_input').read().splitlines()
# complex number format:  real is row, column is imaginary
# but real increasing actually descends _down_ the cave


class Cavern:

    def __init__(self, text_rep, is_part_2):
        self.cavern = defaultdict(lambda: " ")
        self.full_of_sand = False
        self.resting_sand_count = 0
        for line in text_rep:
            points_text = line.split(" -> ")
            for pt_ix in range(len(points_text) - 1):
                ax, ay = map(int, points_text[pt_ix].split(","))
                bx, by = map(int, points_text[pt_ix + 1].split(","))
                for x in range(min(ax, bx), max(ax, bx) + 1):
                    for y in range(min(ay, by), max(ay, by) + 1):
                        self.cavern[complex(y, x)] = "#"

        self.bottom_most_rock = max(map(lambda z: int(z.real), self.cavern.keys()))

        if is_part_2:
            extreme_left = 500 - self.bottom_most_rock - 10
            extreme_right = 500 + self.bottom_most_rock + 10
            for i in range(extreme_left, extreme_right):
                self.cavern[complex(self.bottom_most_rock + 2, i)] = "#"
            self.bottom_most_rock += 2

    def cave_print(self):
        outstr = ""
        min_real = 0
        max_real = max(map(lambda z: int(z.real), self.cavern.keys()))
        min_imag = min(map(lambda z: int(z.imag), self.cavern.keys()))
        max_imag = max(map(lambda z: int(z.imag), self.cavern.keys()))
        for r in range(min_real, max_real+1):
            outstr += str(r).zfill(5)
            for c in range(min_imag, max_imag+1):
                outstr += self.cavern[complex(r, c)]
            outstr += "\n"
        return outstr

    def sand_unit_fall(self):
        sand_loc = 500j
        at_rest = False
        while not at_rest and not self.full_of_sand:
            if self.cavern[sand_loc + 1] == " ":
                sand_loc = sand_loc + 1
            elif self.cavern[sand_loc + 1 - 1j] == " ":
                sand_loc = sand_loc + 1 - 1j
            elif self.cavern[sand_loc + 1 + 1j] == " ":
                sand_loc = sand_loc + 1 + 1j
            else:
                at_rest = True

            if sand_loc.real > self.bottom_most_rock:
                self.full_of_sand = True

        # filled up to starting point - for part 2 mainly
        # need to count this the last sand unit that entered at 500j into the list
        if sand_loc == 500j:
            self.full_of_sand = True
            self.cavern[sand_loc] = "o"
            self.resting_sand_count += 1

        if not self.full_of_sand:
            self.cavern[sand_loc] = "o"
            self.resting_sand_count += 1

    def fill_with_sand(self):
        while not self.full_of_sand:
            self.sand_unit_fall()


xc = Cavern(wall_text_lines, False)
xc.fill_with_sand()
print("Part 1: ", xc.resting_sand_count)


yc = Cavern(wall_text_lines, True)
yc.fill_with_sand()
print("Part 1: ", yc.resting_sand_count)
