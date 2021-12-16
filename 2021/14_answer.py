from collections import Counter
from collections import defaultdict
from collections import deque

data = open('14_input').read().splitlines()

template = data[0]
rules = data[2:]


rule_hash = defaultdict(str)
for rule in rules:
    lft, rgt = rule.split(' -> ')
    rule_hash[lft] = rgt


def pair_count(in_template, depth):
    c_a = Counter()
    for i in range(len(in_template) - 1):
        c_a[in_template[i] + in_template[i + 1]] += 1

    for i in range(depth):
        c_b = Counter()
        for p in c_a:
            res = rule_hash[p]
            c_b[p[0] + res] += c_a[p]
            c_b[res + p[1]] += c_a[p]
        c_a = c_b
    return c_a


def most_minus_least(in_template, depth):
    letter_counter = Counter()
    letter_counter[in_template[-1]] += 1
    pair_counter = pair_count(in_template, depth)

    for pair, count in pair_counter.items():
        letter_counter[pair[0]] += count

    ord_count = letter_counter.most_common()
    return ord_count[0][1] - ord_count[-1][1]


print("Part 1: ", most_minus_least(template, 10))
print("Part 2: ", most_minus_least(template, 40))
