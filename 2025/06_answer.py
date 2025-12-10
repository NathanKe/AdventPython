import re

lines = open('06_input').read().splitlines()


splits = list(map(lambda l: re.split(r"\s+", str.strip(l)), lines))


checksum = 0
for c_i in range(len(splits[0])):
    prob = []
    for s_i in range(len(splits) - 1):
        prob.append(splits[s_i][c_i])
    eq = splits[-1][c_i].join(prob)
    checksum += eval(eq)

print(checksum)

