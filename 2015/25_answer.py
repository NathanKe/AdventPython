import collections

sheet = collections.defaultdict(lambda: collections.defaultdict(int))


def next_cell(cur_row, cur_col):
    if cur_row == 1:
        return cur_col + 1, 1
    else:
        return cur_row - 1, cur_col + 1


def next_code(cur_code):
    return cur_code * 252533 % 33554393


code = 20151125
row = 1
col = 1
while sheet[2947][3029] == 0:
    sheet[row][col] = code
    code = next_code(code)
    row, col = next_cell(row, col)

print('Part 1: ', sheet[2947][3029])
