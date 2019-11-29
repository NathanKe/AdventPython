import re
import json

raw_str = open('12_input').read().splitlines()[0]

p1 = sum(map(int, re.findall(r"-?\d+", raw_str)))

print('Part 1: ', p1)

j_d = json.loads(raw_str)


def sum_non_red(js):
    if type(js) == int:
        return js
    elif type(js) == list:
        return sum([sum_non_red(j) for j in js])
    elif type(js) == str:
        return 0
    elif 'red' in js.values():
        return 0
    else:
        return sum_non_red(list(js.values()))


print('Part 2: ', sum_non_red(j_d))
