from collections import deque
import re

board_stuff, instructions = open('22_input').read().split("\n\n")

board_raw_lines = board_stuff.splitlines()

board_height = len(board_raw_lines)
board_width = max([len(x) for x in board_raw_lines])

board_lines = []
for b_l in board_raw_lines:
    board_lines.append(b_l.ljust(board_width))

# real is row, imag is col
# indexed by 1

board_dict = {}
for r_i, b_l in enumerate(board_lines):
    for c_i, c_v in enumerate(b_l):
        board_dict[complex(r_i + 1, c_i + 1)] = c_v

start_imag = min([x[0].imag for x in board_dict.items() if x[1] != ' ' and x[0].real == 1])
start_real = 1

dir_increments = [-1, 1j, 1, -1j]


def board_wrap_next(direction_index, location):
    poss_next = location + dir_increments[direction_index]
    # trying to go up
    if direction_index == 0:
        if location.real > 1 and poss_next in board_dict.keys() and board_dict[poss_next] != ' ':
            return poss_next
        else:
            max_real_of_cur_column = max(
                [x[0].real for x in board_dict.items() if x[1] != ' ' and x[0].imag == location.imag])
            return complex(max_real_of_cur_column, location.imag)
    # trying to go right
    elif direction_index == 1:
        if location.imag < board_width and poss_next in board_dict.keys() and board_dict[poss_next] != ' ':
            return poss_next
        else:
            min_imag_of_cur_row = min(
                [x[0].imag for x in board_dict.items() if x[1] != ' ' and x[0].real == location.real])
            return complex(location.real, min_imag_of_cur_row)
    # trying to go down
    elif direction_index == 2:
        if location.real < board_height and poss_next in board_dict.keys() and board_dict[poss_next] != ' ':
            return poss_next
        else:
            min_real_of_cur_column = min(
                [x[0].real for x in board_dict.items() if x[1] != ' ' and x[0].imag == location.imag])
            return complex(min_real_of_cur_column, location.imag)
    # trying to go left
    elif direction_index == 3:
        if location.imag > 1 and poss_next in board_dict.keys() and board_dict[poss_next] != ' ':
            return poss_next
        else:
            max_imag_of_cur_row = max(
                [x[0].imag for x in board_dict.items() if x[1] != ' ' and x[0].real == location.real])
            return complex(location.real, max_imag_of_cur_row)


instruction_deque = deque(instructions)
count_stack = []

cur_dir_ix = 1
cur_loc = complex(start_real, start_imag)

instruction_deque.append("X")

while instruction_deque:
    x = instruction_deque.popleft()
    if re.match("\d", x):
        count_stack.append(x)
    else:
        count_val = int(''.join(count_stack))
        for step in range(count_val):
            next_loc = board_wrap_next(cur_dir_ix, cur_loc)
            if board_dict[next_loc] == '#':
                pass
            else:
                cur_loc = next_loc
        count_stack = []
        if x == 'L':
            cur_dir_ix = (cur_dir_ix - 1) % len(dir_increments)
        elif x == 'R':
            cur_dir_ix = (cur_dir_ix + 1) % len(dir_increments)
        elif x == 'X':
            # end of instruction character, done
            pass

print("Part 1: ", 1000 * cur_loc.real + 4 * cur_loc.imag + (cur_dir_ix - 1) % len(dir_increments))
