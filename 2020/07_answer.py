import re

rules_text = raw_data = open('07_input').read().splitlines()

rules_text = [re.sub(r"bag(,|\.)", r"bags\1", rule) for rule in rules_text]


rules_dict = {}
for rule in rules_text:
    container, containees = rule.split(' contain ')
    if containees == "no other bags.":
        containees = []
    else:
        containees = containees[:-1].split(", ")

    containee_dict = {}
    for containee in containees:
        qty = containee[0]
        bag = containee[2:]
        containee_dict[bag] = int(qty)

    rules_dict[container] = containee_dict


def bags_that_contain(search_bag):
    return [b for b in rules_dict.keys() if search_bag in rules_dict[b].keys()]


search = ['shiny gold bags']
contains_shiny_gold = []
while search:
    check = search.pop()
    containers = bags_that_contain(check)
    contains_shiny_gold.extend(containers)
    for c in containers:
        search.append(c)

print('Part 1: ', len(set(contains_shiny_gold)))


def child_count(parent, cur_sum):
    direct_children = rules_dict[parent].items()
    print(parent, direct_children)
    for child in direct_children:
        cur_sum += child[1]
        cur_sum += child[1] * child_count(child[0], 0)
    return cur_sum


print('Part 2: ', child_count('shiny gold bags', 1))







