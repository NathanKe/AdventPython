import re

memory = open('03_input').read()


def exec_valid_mul(i_str):
    l, r = list(map(int, re.findall(r"\d+",i_str)))
    return l*r


q = re.findall(r"mul\(\d+,\d+\)", memory)

sum = 0
for qx in q:
    sum += exec_valid_mul(qx)

do_segs = re.split(r"do\(\)", memory)

do_heads = []
for ds in do_segs:
    ds_head = re.split(r"don\'t\(\)", ds)[0]
    do_heads.append(ds_head)


sumX = 0
for dh in do_heads:
    qh = re.findall(r"mul\(\d+,\d+\)", dh)
    for qhx in qh:
        sumX += exec_valid_mul(qhx)

print(sum)
print(sumX)