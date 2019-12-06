import re
import itertools

puzzle_state_1 = [
    ["EEE", "ThG", "ThM", "PlG", "StG"],
    ["PlM", "StM"],
    ["PrG", "PrM", "RuG", "RuM"],
    []
]


def is_safe_floor(p_floor):
    micro_chips = []
    generators = []
    for item in p_floor:
        if item[-1] == 'G':
            generators.append(item[0:2])
        elif item[-1] == 'M':
            micro_chips.append(item[0:2])
    for gen in generators:
        if gen in micro_chips:
            micro_chips.remove(gen)
            generators.remove(gen)
    if len(generators) > len(micro_chips) > 0:
        return False
    else:
        return True


def is_safe_state(p_state):
    for floor in p_state:
        if not is_safe_floor(floor):
            return False
    return True


def carry_up(p_state, p_carry):
    # return new state
    ...


def carry_down(p_state, p_carry):
    # return new state
    ...


def adjacent_states(p_state):
    result_states = []

    avail_dirs = []
    elev_floor = list(map(lambda fl: "EEE" in fl, p_state)).index(True)
    if elev_floor > 0:
        avail_dirs.append("DOWN")
    if elev_floor < len(p_state):
        avail_dirs.append("UP")

    poss_items = p_state[elev_floor]
    poss_items.remove('EEE')
    poss_carry = list(itertools.combinations(poss_items, 1)) + list(itertools.combinations(poss_items, 2))
    for poss_action in list(itertools.product(avail_dirs, poss_carry)):
        if poss_action[0] == 'UP':
            new_state = carry_up()
            if is_safe_state(new_state):
                result_states.append(new_state)
        if poss_action[0] == 'DOWN':
            new_state = carry_down()
            if is_safe_state(new_state):
                result_states.append(new_state)
    return result_states
