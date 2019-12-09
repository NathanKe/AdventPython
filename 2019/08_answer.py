import collections

puzzle = open('08_input').read()

width = 25
height = 6

layers = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(int)))

min_zero_count = width * height
best = None
for l_num in range(len(puzzle) // width // height):
    sub_layer = puzzle[l_num * width * height:(l_num + 1) * width * height]
    for r_num in range(height):
        sub_row = sub_layer[r_num * width:(r_num + 1) * width]
        for c_num in range(width):
            layers[l_num][r_num][c_num] = int(sub_row[c_num])
    c_layer_flat = [layers[l_num][r][c] for r in range(height) for c in range(width)]
    c_zc = collections.Counter(c_layer_flat)[0]
    if c_zc < min_zero_count:
        min_zero_count = c_zc
        best = c_layer_flat[:]

coll = collections.Counter(best)
p1 = coll[1] * coll[2]
print('Part 1: ', p1)

pix_stacks = collections.defaultdict(lambda: collections.defaultdict(collections.deque))
for l_num in range(len(puzzle) // width // height):
    for r_num in range(height):
        for c_num in range(width):
            pix_stacks[r_num][c_num].appendleft(layers[l_num][r_num][c_num])

p2 = ""
for r_num in range(height):
    out_row = ""
    for c_num in range(width):
        c_stack = pix_stacks[r_num][c_num]
        while c_stack[-1] == 2:
            c_stack.pop()
        out_row += [" ", "X"][c_stack.pop()]
    out_row += "\n"
    p2 += out_row

print(p2)
