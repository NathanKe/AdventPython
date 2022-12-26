import re

lines = open('21_input').read().splitlines()


class MonkeyNode:
    def __init__(self, in_str):
        if re.search(r"\d", in_str):
            name, num = in_str.split(": ")
            self.name = name
            self.value = num
        else:
            name, left, op, right = re.match(r"^(.+):\s(.+)\s(.)\s(.+)$", in_str).groups()
            self.name = name
            self.left = left
            self.op = op
            self.right = right
            self.value = None


def compute(monkey):
    cur_monkey = monkey_dict[monkey]
    if cur_monkey.value:
        return cur_monkey.value
    else:
        left_res = compute(cur_monkey.left)
        right_res = compute(cur_monkey.right)
        ev_str = left_res + cur_monkey.op + right_res
        return str(eval(ev_str))


monkey_dict = {}
for line in lines:
    name, info = line.split(": ")
    monkey_dict[name] = MonkeyNode(line)

print(compute('root'))

parent = None
child = 'humn'
trail = [child]
while parent != 'root':
    parent = [x.split(": ")[0] for x in lines if child in x.split(": ")[1]][0]
    child = parent
    trail.append(child)
print("Done!")

monkey_dict['humn'].value = 'humn'


def compute2(monkey):
    cur_monkey = monkey_dict[monkey]
    if cur_monkey.value:
        return cur_monkey.value
    else:
        left_res = compute2(cur_monkey.left)
        right_res = compute2(cur_monkey.right)
        ev_str = left_res + cur_monkey.op + right_res
        return "(" + ev_str + ")"


root_lf = compute2(monkey_dict['root'].left)
root_rg = compute2(monkey_dict['root'].right)
