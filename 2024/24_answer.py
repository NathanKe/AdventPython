import re
from collections import deque

init_vals, instructions = map(lambda lines: lines.splitlines(), open('24_input').read().split('\n\n'))

state_dict = {}

for iv in init_vals:
    reg_name, reg_val = iv.split(': ')
    state_dict[reg_name] = int(reg_val)

instruction_deque = deque(instructions)

while instruction_deque:
    instr = instruction_deque.popleft()
    lf, op, rg, out = (re.match(r"(.+)\s(OR|XOR|AND)\s(.+)\s\->\s(.+)", instr)).groups()
    if lf in state_dict.keys() and rg in state_dict.keys():
        if op == 'XOR':
            state_dict[out] = state_dict[lf] ^ state_dict[rg]
        elif op == "OR":
            state_dict[out] = state_dict[lf] | state_dict[rg]
        elif op == "AND":
            state_dict[out] = state_dict[lf] & state_dict[rg]
    else:
        instruction_deque.append(instr)

print(int((''.join(map(lambda tu: str(tu[1]),
                       sorted([(k, v) for k, v in state_dict.items() if k[0] == 'z'], key=lambda tu: tu[0],
                              reverse=True)))), 2))
