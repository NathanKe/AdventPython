import functools
from collections import defaultdict

rule_lines, test_lines = map(lambda ll: ll.splitlines(), open('05_input').read().split('\n\n'))

afters_to_befores = defaultdict(lambda: [])

for rl in rule_lines:
    bef, aft = map(int, rl.split("|"))
    afters_to_befores[aft].append(bef)


def custom_comparator_less_than(a, b):
    if a == b:
        return 0
    elif a in afters_to_befores[b]:
        return -1
    else:
        return 1


pass_sum = 0
fixed_sum = 0
for tl in test_lines:
    tl_nums = list(map(int, tl.split(',')))
    sorted_tl = sorted(tl_nums, key=functools.cmp_to_key(custom_comparator_less_than))
    if sorted_tl == tl_nums:
        pass_sum += tl_nums[len(tl_nums)//2]
    else:
        fixed_sum += sorted_tl[len(sorted_tl)//2]

print(pass_sum)
print(fixed_sum)


