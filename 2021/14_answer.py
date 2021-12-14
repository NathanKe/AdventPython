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


def init_deque(in_str):
    out_deque = deque()
    for i in range(len(in_str)):
        out_deque.append(in_str[i])
    return out_deque


def expand(polymer):
    p_dq = deque(polymer)
    new_dq = deque()
    p_1 = p_dq.popleft()
    while p_dq:
        p_2 = p_dq.popleft()
        new_dq.append(p_1)
        new_dq.append(rule_hash[p_1 + p_2])
        p_1 = p_2
    new_dq.append(p_2)
    return ''.join(new_dq)


def count_recur(polymer, exp_count):
    if exp_count > 1:
        if len(polymer) >= 2:
            polymer = expand(polymer)
    p_len = len(polymer)
    if p_len == 2:
        if polymer in rule_hash.keys():
            return Counter(list(polymer)) + Counter(list(rule_hash[polymer]))
        else:
            return Counter(list(polymer))
    elif p_len == 1:
        return Counter(list(polymer))
    else:
        left = polymer[:p_len//2]
        right = polymer[p_len//2:]
        middle = rule_hash[polymer[p_len//2]+polymer[p_len//2 + 1]]
        l_c = Counter(count_recur(left, exp_count - 1))
        r_c = Counter(count_recur(right, exp_count - 1))
        m_c = Counter(middle)
        return l_c + r_c + m_c


def most_minus_least(ct):
    c_ord = ct.most_common()
    most = c_ord[0][1]
    least = c_ord[-1][1]
    return most - least


print("Part 1: ", most_minus_least(count_recur(template, 10)))


