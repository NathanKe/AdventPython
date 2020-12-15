import collections

instrs = open('14_input').read().splitlines()


def zip_tuple_redux(tu):
    if tu[0] == 'X':
        return str(tu[1])
    else:
        return str(tu[0])


def apply_mask(in_mask, in_val_dec):
    in_val_bin = format(in_val_dec, '036b')

    return int(''.join(map(lambda tu: zip_tuple_redux(tu), zip(in_mask, in_val_bin))), 2)


def part1():
    registers = collections.defaultdict(int)
    cur_mask = None

    for instr in instrs:
        instr_type, instr_val = instr.split(' = ')

        if instr_type == 'mask':
            cur_mask = instr_val
        else:
            cur_reg = int(instr_type[4:-1])
            registers[cur_reg] = apply_mask(cur_mask, int(instr_val))
    return sum(registers.values())


print('Part 1: ', part1())


def zip_tuple_redux_2(tu):
    if tu[0] == '0':
        return tu[1]
    elif tu[0] == '1':
        return '1'
    elif tu[0] == 'X':
        return 'X'


def expand_mask(in_mask):
    mask_set = collections.deque([in_mask])

    no_x_count = 0
    while no_x_count < len(mask_set):
        cur_mask = mask_set.popleft()
        x_ind = cur_mask.find('X')
        if x_ind != -1:
            mask_zero = cur_mask[:x_ind] + '0' + cur_mask[(x_ind+1):]
            mask_one = cur_mask[:x_ind] + '1' + cur_mask[(x_ind+1):]
            mask_set.append(mask_zero)
            mask_set.append(mask_one)
        else:
            no_x_count += 1
            mask_set.append(cur_mask)

    return list(mask_set)


def expand_addresses(in_mask, in_addr_dec):
    in_addr_bin = format(in_addr_dec, '036b')
    base_application = ''.join(map(lambda tu: zip_tuple_redux_2(tu), zip(in_mask, in_addr_bin)))
    addr_set = map(lambda x: int(x, 2), expand_mask(base_application))
    return list(addr_set)


def part2():
    registers = collections.defaultdict(int)
    cur_mask = None

    for instr in instrs:
        instr_type, instr_val = instr.split(' = ')

        if instr_type == 'mask':
            cur_mask = instr_val
        else:
            base_addr = int(instr_type[4:-1])
            addrs = expand_addresses(cur_mask, base_addr)
            for addr in addrs:
                registers[addr] = int(instr_val)
    return sum(registers.values())


print('Part 1: ', part2())
