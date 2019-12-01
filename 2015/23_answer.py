import re

instr_set = """jio a, +16
inc a
inc a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
tpl a
inc a
jmp +23
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
inc a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7""".splitlines()


def exec_instr_at_index(i, reg_a, reg_b):
    cur_instr = instr_set[i]
    if cur_instr[0:3] == "hlf":
        if cur_instr[-1] == "a":
            reg_a //= 2
        else:
            reg_b //= 2
        i += 1
    elif cur_instr[0:3] == "tpl":
        if cur_instr[-1] == "a":
            reg_a *= 3
        else:
            reg_b *= 3
        i += 1
    elif cur_instr[0:3] == "inc":
        if cur_instr[-1] == "a":
            reg_a += 1
        else:
            reg_b += 1
        i += 1
    elif cur_instr[0:3] == "jmp":
        m = re.search(r"([+\-])(\d+)$", cur_instr)
        if m[1] == "-":
            i -= int(m[2])
        else:
            i += int(m[2])
    elif cur_instr[0:3] == "jie":
        check_reg = cur_instr[4]
        if check_reg == 'a':
            if reg_a % 2 == 0:
                m = re.search(r"([+\-])(\d+)$", cur_instr)
                if m[1] == "-":
                    i -= int(m[2])
                else:
                    i += int(m[2])
            else:
                i += 1
        else:
            if reg_b % 2 == 0:
                m = re.search(r"([+\-])(\d+)$", cur_instr)
                if m[1] == "-":
                    i -= int(m[2])
                else:
                    i += int(m[2])
            else:
                i += 1
    elif cur_instr[0:3] == "jio":
        check_reg = cur_instr[4]
        if check_reg == 'a':
            if reg_a == 1:
                m = re.search(r"([+\-])(\d+)$", cur_instr)
                if m[1] == "-":
                    i -= int(m[2])
                else:
                    i += int(m[2])
            else:
                i += 1
        else:
            if reg_b == 1:
                m = re.search(r"([+\-])(\d+)$", cur_instr)
                if m[1] == "-":
                    i -= int(m[2])
                else:
                    i += int(m[2])
            else:
                i += 1
    return i, reg_a, reg_b


i, a, b = 0, 0, 0
while True:
    try:
        i, a, b = exec_instr_at_index(i, a, b)
    except:
        print('Part 1: ', b)
        break
    else:
        continue

i, a, b = 0, 1, 0
while True:
    try:
        i, a, b = exec_instr_at_index(i, a, b)
    except:
        print('Part 2: ', b)
        break
    else:
        continue
