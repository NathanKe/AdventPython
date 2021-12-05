import re

raw_data = open('19_input').read()

rule_lines, message_lines = map(lambda x: x.splitlines(), raw_data.split('\n\n'))

rule_tuples = [tuple(map(lambda x: x.replace("\"", ""), r.split(': '))) for r in rule_lines]

simple_tuples = []
for rt in rule_tuples:
    if not re.match(r"\d", rt[1]):
        simple_tuples.append(rt)


def simplify(in_tuple_list, in_simple_tuples):
    out_tuple_list = []
    for tu in in_tuple_list:
        ctv = tu[1]
        for st in in_simple_tuples:
            ctv = re.sub()
        if re.match(r"\d", ctv):
            out_tuple_list.append((tu[0], ctv))
        else:
            in_simple_tuples.append((tu[0], ctv))
    return out_tuple_list, in_simple_tuples
