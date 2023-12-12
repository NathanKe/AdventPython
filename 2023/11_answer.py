from itertools import combinations

galaxy_text = open('11_input').read().splitlines()


def transpose_text(text_rows):
    result_matrix = [['#'] * len(text_rows) for i in range(len(text_rows[0]))]
    for r_i, r_v in enumerate(text_rows):
        for c_i, c_v in enumerate(r_v):
            result_matrix[c_i][r_i] = c_v

    return list(map(lambda row: ''.join(row), result_matrix))


def galaxy_locations(text_rows):
    galaxy_set = set()
    for r_i, r_v in enumerate(text_rows):
        for c_i, c_v in enumerate(r_v):
            if c_v == '#':
                galaxy_set.add(r_i + 1j * c_i)
    return galaxy_set


blank_rows = []
for r_i, row in enumerate(galaxy_text):
    if row == '.' * len(row):
        blank_rows.append(r_i)

blank_cols = []
for r_i, row in enumerate(transpose_text(galaxy_text)):
    if row == '.' * len(row):
        blank_cols.append(r_i)


def complex_manhattan_distance(start, finish):
    return abs(start.real - finish.real) + abs(start.imag - finish.imag)


def blank_row_count_btw(start, finish):
    bl_cnt = 0
    lower, higher = map(int, sorted([start.real, finish.real]))
    for r in range(lower, higher):
        if r in blank_rows:
            bl_cnt += 1
    return bl_cnt


def blank_col_count_btw(start, finish):
    bl_cnt = 0
    lower, higher = map(int, sorted([start.imag, finish.imag]))
    for r in range(lower, higher):
        if r in blank_cols:
            bl_cnt += 1
    return bl_cnt


def distance_with_expansion(start, finish, expansion_count):
    row_portion = blank_row_count_btw(start, finish) * expansion_count
    col_portion = blank_col_count_btw(start, finish) * expansion_count
    raw = complex_manhattan_distance(start, finish)
    return raw + row_portion + col_portion


galaxy_pairs = list(combinations(galaxy_locations(galaxy_text), 2))

print(int(sum(map(lambda tu: distance_with_expansion(tu[0], tu[1], 1), galaxy_pairs))))
print(int(sum(map(lambda tu: distance_with_expansion(tu[0], tu[1], 999999), galaxy_pairs))))
