map_lines, move_lines = map(lambda ll: ll.splitlines(), open('15_input').read().split("\n\n"))

map_dict = {}
start = None
for ri, rv in enumerate(map_lines):
    for ci, cv in enumerate(rv):
        map_dict[ri + 1j * ci] = cv
        if cv == '@':
            start = ri + 1j * ci


all_moves = "".join(move_lines)


move_char_dict = {
    '^': -1,
    'v': 1,
    '<': -1j,
    '>': 1j
}


cursor = start


def parse_move(i_move_char):
    global cursor
    global map_dict
    move_dir = move_char_dict[i_move_char]
    peek = cursor + move_dir
    if map_dict[peek] == '.':
        map_dict[peek] = '@'
        map_dict[cursor] = '.'

        cursor = peek
    elif map_dict[cursor + move_dir] == '#':
        pass
    else:
        scan_stack = []
        scan_res = False
        while not scan_res:
            if map_dict[peek] == 'O':
                scan_stack.append(peek)
                peek += move_dir
            elif map_dict[peek] == '#':
                scan_res = "WALL"
            else:
                scan_res = "SPACE"
        if scan_res == "WALL":
            pass
        else:
            for block in scan_stack:
                map_dict[block + move_dir] = 'O'
            map_dict[cursor + move_dir] = '@'
            map_dict[cursor] = '.'
            cursor = cursor + move_dir


def map_print():
    global map_dict
    for ri in range(len(map_lines)):
        out_row = ""
        for ci in range(len(map_lines[0])):
            out_row += map_dict[ri + 1j * ci]
        print(out_row)


for move in list(all_moves):
    parse_move(move)


def coord_sum():
    global map_dict
    out_sum = 0
    for k, v in map_dict.items():
        if v == 'O':
            out_sum += 100 * k.real + k.imag
    return int(out_sum)

print(coord_sum())
