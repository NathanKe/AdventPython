import re
from collections import deque
from numpy import base_repr

test_eqs = open('07_input').read().splitlines()


def parse_possible_two_op(i_eq):
    target_str, *operands = re.split(r"\D+", i_eq)

    target = int(target_str)

    operator_count = len(operands) - 1

    operator_possbility_range = 2**(operator_count)

    for op_test in range(operator_possbility_range):

        bin_format = '{0:0'+str(operator_count)+'b}'

        operand_bitmask = bin_format.format(op_test)
        assert (len(operand_bitmask) + 1 == len(operands))
        operand_bitmask = operand_bitmask.replace('0', '+')
        operand_bitmask = operand_bitmask.replace('1', '*')

        stack = deque([val for pair in zip(operands, operand_bitmask) for val in pair])
        stack.append(operands[-1])

        value = int(stack.popleft())

        while value <= target and len(stack) >= 2:
            eval_str = str(value) + stack.popleft() + stack.popleft()
            value = eval(eval_str)

        if value == target:
            return target

    return False


def parse_possible_three_op(i_eq):
    target_str, *operands = re.split(r"\D+", i_eq)

    target = int(target_str)

    operator_count = len(operands) - 1

    operator_possbility_range = 3**(operator_count)

    for op_test in range(operator_possbility_range):

        ternary = base_repr(op_test, base=3)
        operand_bitmask = '0' * (operator_count - len(ternary)) + ternary

        operand_bitmask = operand_bitmask.replace('0', '+')
        operand_bitmask = operand_bitmask.replace('1', '*')
        operand_bitmask = operand_bitmask.replace('2', '|')

        stack = deque([val for pair in zip(operands, operand_bitmask) for val in pair])
        stack.append(operands[-1])

        value = int(stack.popleft())

        while value <= target and len(stack) >= 2:
            c_op = stack.popleft()
            c_nm = stack.popleft()
            if c_op == "|":
                value = int(str(value) + str(c_nm))
            else:
                eval_str = str(value) + c_op + c_nm
                value = eval(eval_str)

        if value == target:
            return target

    return False


two_op_parse_res = [(ix, parse_possible_two_op(teq)) for (ix, teq) in enumerate(test_eqs)]

re_test_at_three_ixs = [tu[0] for tu in two_op_parse_res if not tu[1]]

p1 = sum([tu[1] for tu in two_op_parse_res if tu[1]])


print(p1)

p2 = p1 + sum([parse_possible_three_op(test_eqs[ix]) for ix in re_test_at_three_ixs])

print(p2)



# print(sum([parse_possible_two_op(teq) for teq in test_eqs]))
# print(sum([parse_possible_three_op(teq) for teq in test_eqs]))