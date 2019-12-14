import math
import collections
import re

rx_text = open('14_input').read().splitlines()


def rx_qty_type(s):
    q, t = s.split(' ')
    return int(q), t


def rx_digest(p_qty, p_chem, p_text):
    for rx in p_text:
        lhs, rhs = rx.split(' => ')
        c_qty, c_chem = rhs.split(' ')
        c_qty = int(c_qty)
        if c_chem == p_chem:
            return math.ceil(p_qty / c_qty) * list(map(rx_qty_type, lhs.split(', ')))


def collapse(p_chem_list):
    ch_dict = collections.defaultdict(int)
    for ch in p_chem_list:
        ch_dict[ch[1]] += ch[0]
    out_list = []
    for i in ch_dict.items():
        out_list.append((i[1], i[0]))
    return collections.deque(out_list)


def base_info(p_text):
    ch_list = []
    for rx in p_text:
        if re.search('ORE', rx):
            lhs, rhs = rx.split(' => ')
            out_qty, chem = rhs.split(' ')
            ore_qty = lhs.split(' ')[0]
            ch_list.append((int(ore_qty), int(out_qty), chem))
    return ch_list


def base_names(p_text):
    b_i = base_info(p_text)
    return list(map(lambda tu: tu[2], b_i))


def rx_expand(p_qty, p_chem, p_text):
    bases = base_names(p_text)
    print(bases)
    dq = collections.deque(rx_digest(p_qty, p_chem, p_text))
    while len(dq) > 0:
        dq = collapse(dq)
        print(dq)
        if dq[-1][1] not in bases:
            new_expandee = dq.pop()
            new_digest = rx_digest(*new_expandee, p_text)
            for tu in new_digest:
                dq.append(tu)
        else:
            dq.rotate(1)
