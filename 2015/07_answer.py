import re

wires = open('07_input').read().splitlines()

wires = list(map(lambda s: s.replace("NOT", "~"), wires))
wires = list(map(lambda s: s.replace("OR", "|"), wires))
wires = list(map(lambda s: s.replace("AND", "&"), wires))
wires = list(map(lambda s: s.replace("LSHIFT", "<<"), wires))
wires = list(map(lambda s: s.replace("RSHIFT", ">>"), wires))

results = {}


def eval_numeric_lefts(wire_list, value_dict):
    remaining_wires = []
    for wire in wire_list:
        m = re.match(r"(.+)\s->\s(.+)", wire)
        lhs, rhs = m[1], m[2]
        if not re.search('[a-z]', lhs):
            val = str(eval(lhs))
            key = rhs
            value_dict[key] = val
        else:
            remaining_wires.append(wire)
    return remaining_wires, value_dict


def substitute_known_number(wire_list, value_dict):
    new_wire_list = []
    for wire in wire_list:
        for key, val in value_dict.items():
            wire = re.sub(r"\b" + key + r"\b", val, wire)
        new_wire_list.append(wire)

    return new_wire_list, value_dict


def step(wire_list, value_dict):
    wire_list, value_dict = eval_numeric_lefts(wire_list, value_dict)
    wire_list, value_dict = substitute_known_number(wire_list, value_dict)
    return wire_list, value_dict


while len(wires) > 0:
    wires, results = step(wires, results)

p1 = results['a']
print('Part 1:', p1)

# reset wires
wires = open('07_input').read().splitlines()
wires = list(map(lambda s: s.replace("NOT", "~"), wires))
wires = list(map(lambda s: s.replace("OR", "|"), wires))
wires = list(map(lambda s: s.replace("AND", "&"), wires))
wires = list(map(lambda s: s.replace("LSHIFT", "<<"), wires))
wires = list(map(lambda s: s.replace("RSHIFT", ">>"), wires))
wires = list(map(lambda s: s.replace("RSHIFT", ">>"), wires))

results = {}

wires = list(map(lambda s: re.sub(r"(.+)(\s->\sb$)", p1 + r"\2", s), wires))

while len(wires) > 0:
    wires, results = step(wires, results)

p2 = results['a']
print('Part 2:', p2)
