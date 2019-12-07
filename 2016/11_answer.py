import itertools
import collections
import copy

puzzle_state_1 = [
    ["EEE", "ThG", "ThM", "PlG", "StG"],
    ["PlM", "StM"],
    ["PrG", "PrM", "RuG", "RuM"],
    []
]

goal_state_1 = [
    ["EEE", "P1G", "PlM", "PrG", "PrM", "RuG", "RuM", "StG", "StM", "ThG", "ThM"],
    [],
    [],
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


def carry_up(p_state, p_carry, p_floor):
    out_state = copy.deepcopy(p_state)
    for item in p_carry:
        out_state[p_floor].remove(item)
        out_state[p_floor + 1].append(item)
    out_state[p_floor + 1].append('EEE')
    out_state[p_floor].remove('EEE')
    return out_state


def carry_down(p_state, p_carry, p_floor):
    out_state = copy.deepcopy(p_state)
    for item in p_carry:
        out_state[p_floor].remove(item)
        out_state[p_floor - 1].append(item)
    out_state[p_floor - 1].append('EEE')
    out_state[p_floor].remove('EEE')
    return out_state


def adjacent_states(p_state):
    result_states = []

    avail_dirs = []
    elev_floor = list(map(lambda fl: "EEE" in fl, p_state)).index(True)
    if elev_floor > 0:
        avail_dirs.append("DOWN")
    if elev_floor < len(p_state) - 1:
        avail_dirs.append("UP")

    poss_items = p_state[elev_floor][:]
    poss_items.remove('EEE')
    poss_carry = list(itertools.combinations(poss_items, 1)) + list(itertools.combinations(poss_items, 2))
    for poss_action in list(itertools.product(avail_dirs, poss_carry)):
        if poss_action[0] == 'UP':
            new_state = carry_up(p_state, poss_action[1], elev_floor)
            if is_safe_state(new_state):
                result_states.append(new_state)
        if poss_action[0] == 'DOWN':
            if len(p_state[elev_floor - 1]) != 0:
                new_state = carry_down(p_state, poss_action[1], elev_floor)
                if is_safe_state(new_state):
                    result_states.append(new_state)
    return result_states


frontier = collections.deque([(puzzle_state_1, [])])
solved = {}


def state_to_string(p_state):
    out = ""
    for i in range(len(p_state)):
        fl = "Floor %d:" % (i + 1)
        items = ""
        for item in sorted(p_state[i]):
            items += item
            items += ","
        fl += items
        out += fl + "\n"
    out += "########\n"
    return out


goal_string = state_to_string(goal_state_1)

i = 0
while len(frontier) > 0 and i < 10000:
    cur_state, cur_path = frontier.pop()
    for adj in adjacent_states(cur_state):
        if state_to_string(adj) not in solved.keys():
            frontier.append((adj, cur_path + [adj]))
    cur_string = state_to_string(cur_state)
    solved[cur_string] = cur_path
    if cur_string == goal_string:
        print('GOAL!')
        break
    i += 1
