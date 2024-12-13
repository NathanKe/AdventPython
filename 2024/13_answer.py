from z3 import *
import re
machine_texts = open('13_input').read()


patt = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"


machine_nums = [list(map(int, sub_list)) for sub_list in re.findall(patt, machine_texts)]


def z3ifier(i_nums, max_steps):
    a_x, a_y, b_x, b_y, p_x, p_y = i_nums

    a_step, b_step = Ints('a_step b_step')

    s = Solver()
    s.add(a_step <= max_steps)
    s.add(b_step <= max_steps)
    s.add(a_step * a_x + b_step * b_x == p_x)
    s.add(a_step * a_y + b_step * b_y == p_y)

    if s.check() == sat:
        model = s.model()

        return [model[val].as_long() for val in model]
    else:
        return False


token_sum = 0
for mch in machine_nums:
    z3res = z3ifier(mch, 100)
    if z3res:
        token_sum += 3 * z3res[1] + z3res[0]

print(token_sum)

token_sum = 0
for mch in machine_nums:
    mch[-1] += 10000000000000
    mch[-2] += 10000000000000
    z3res = z3ifier(mch, 1000000000000000)
    if z3res:
        token_sum += 3 * z3res[1] + z3res[0]

print(token_sum)