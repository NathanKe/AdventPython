import math
import collections

rxs = open('14_input').read().splitlines()


def rx_elems(p_chem):
    for rx in rxs:
        lhs, rhs = rx.split(' => ')
        out_qty, out_chem = rhs.split(' ')
        out_qty = int(out_qty)
        if out_chem == p_chem:
            sub_elems_str = lhs.split(', ')
            sub_elems_tu = list(map(lambda s: (int(s.split(' ')[0]), s.split(' ')[1]), sub_elems_str))
            return out_qty, sub_elems_tu


def ore_cost(p_qty, p_chem, surp_dict):
    if surp_dict is None:
        surp_dict = collections.defaultdict(int)
    if p_chem == 'ORE':
        return p_qty
    if surp_dict[p_chem] >= p_qty:
        surp_dict[p_chem] -= p_qty
        return 0
    p_qty -= surp_dict[p_chem]
    surp_dict[p_chem] = 0
    ore = 0
    rx_out_qty, rx_components = rx_elems(p_chem)
    iter_count = math.ceil(p_qty / rx_out_qty)
    surplus = iter_count * rx_out_qty - p_qty
    surp_dict[p_chem] += surplus
    for rx_comp in rx_components:
        ore += ore_cost(iter_count * rx_comp[0], rx_comp[1], surp_dict)
    return ore


def ore_fuel_cost(fuel_qty):
    return ore_cost(fuel_qty, 'FUEL', None)


print('Part 1: ', ore_fuel_cost(1))

one_trillion = 1000000000000

too_few_fuel_units = 1
too_many_fuel_units = ore_fuel_cost(one_trillion)

while True:
    mid_guess = (too_few_fuel_units + too_many_fuel_units) // 2
    guess_cost = ore_fuel_cost(mid_guess)
    guess_cost_plus_one = ore_fuel_cost(mid_guess + 1)
    if guess_cost > one_trillion:
        too_many_fuel_units = mid_guess
    elif ore_fuel_cost(mid_guess + 1) > one_trillion:
        print('Part 2: ', mid_guess)
        break
    else:
        too_few_fuel_units = mid_guess + 1
