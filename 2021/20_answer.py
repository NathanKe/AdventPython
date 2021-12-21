from collections import defaultdict


class Image:
    def __init__(self, input_file):
        alg_string, _, *input_rows = open(input_file).read().splitlines()

        self.min_dim = 0
        self.max_dim = 100

        self.alg_list = []
        for ch in alg_string:
            if ch == '#':
                self.alg_list.append(1)
            else:
                self.alg_list.append(0)

        self.enhance_count = 0

        self.image = defaultdict(lambda: defaultdict(lambda: 0))
        for r, row in enumerate(input_rows):
            for c, col in enumerate(row):
                if col == "#":
                    col = 1
                else:
                    col = 0
                self.image[r][c] = col

    def surround_index(self, r, c):
        index = 0
        index += pow(2, 8) * self.image[r - 1][c - 1]
        index += pow(2, 7) * self.image[r - 1][c]
        index += pow(2, 6) * self.image[r - 1][c + 1]
        index += pow(2, 5) * self.image[r][c - 1]
        index += pow(2, 4) * self.image[r][c]
        index += pow(2, 3) * self.image[r][c + 1]
        index += pow(2, 2) * self.image[r + 1][c - 1]
        index += pow(2, 1) * self.image[r + 1][c]
        index += pow(2, 0) * self.image[r + 1][c + 1]
        return index

    def enhance(self):
        if self.enhance_count % 2 == 0:
            new_image = defaultdict(lambda: defaultdict(lambda: 1))
            for r in range(self.min_dim - 1, self.max_dim + 1):
                for c in range(self.min_dim - 1, self.max_dim + 1):
                    new_val = self.alg_list[self.surround_index(r, c)]

                    new_image[r][c] = new_val
            self.image = new_image
        else:
            new_image = defaultdict(lambda: defaultdict(lambda: 0))
            for r in range(self.min_dim - 1, self.max_dim + 1):
                for c in range(self.min_dim - 1, self.max_dim + 1):
                    new_val = self.alg_list[self.surround_index(r, c)]

                    new_image[r][c] = new_val
            self.image = new_image

        self.enhance_count += 1
        self.min_dim -= 1
        self.max_dim += 1

    def light_count(self):
        out_count = 0
        for r in range(self.min_dim - 1, self.max_dim + 1):
            for c in range(self.min_dim - 1, self.max_dim + 1):
                if self.image[r][c] == 1:
                    out_count += 1
        return out_count


p1_image = Image('20_input')
p1_image.enhance()
p1_image.enhance()
print("Part 1: ", p1_image.light_count())
for i in range(48):
    p1_image.enhance()
print("Part 1: ", p1_image.light_count())
