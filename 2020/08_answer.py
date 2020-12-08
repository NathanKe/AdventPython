raw_data = open('08_input').read().splitlines()


def reset_program():
    program_info = {}
    for instr_num in range(len(raw_data)):
        instr_type, val_str = raw_data[instr_num].split(' ')
        val_num = int(val_str)
        program_info[instr_num] = {
            'instr_type': instr_type,
            'val_num': val_num,
            'visit_count': 0
        }
    return program_info


def step_program(cur_program, cur_instr_num, cur_accum_val, cur_state, is_infinite):
    if cur_instr_num == len(cur_program):
        cur_state = False
        is_infinite = False
    elif cur_program[cur_instr_num]['visit_count'] == 1:
        cur_state = False
        is_infinite = True
    else:
        cur_program[cur_instr_num]['visit_count'] += 1
        cur_instr_type = cur_program[cur_instr_num]['instr_type']
        if cur_instr_type == 'acc':
            cur_accum_val += cur_program[cur_instr_num]['val_num']
            cur_instr_num += 1
        elif cur_instr_type == 'jmp':
            cur_instr_num += cur_program[cur_instr_num]['val_num']
        elif cur_instr_type == 'nop':
            cur_instr_num += 1

    return cur_program, cur_instr_num, cur_accum_val, cur_state, is_infinite


def program_visit_max(program_state):
    return max(map(lambda x: x['visit_count'], program_state.values()))


def run_program(program_state):
    acc = 0
    inst = 0
    active = True
    inf = False
    acc_history = []
    while active:
        program_state, inst, acc, active, inf = step_program(program_state, inst, acc, active, inf)
        acc_history.append(acc)
    return acc_history[-1], inf


def flip_instruction(inst_row, cur_program):
    if cur_program[inst_row]['instr_type'] == 'nop':
        cur_program[inst_row]['instr_type'] = 'jmp'
    elif cur_program[inst_row]['instr_type'] == 'jmp':
        cur_program[inst_row]['instr_type'] = 'nop'

    return cur_program


def possible_programs():
    return list(map(lambda i: flip_instruction(i, reset_program()), range(len(raw_data))))


print('Part 1: ', run_program(reset_program())[0])

print('Part 2: ', list(filter(lambda res: not res[1], (map(lambda pr: run_program(pr), possible_programs()))))[0][0])


