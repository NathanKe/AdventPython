import re
from collections import deque

lines = open('06_input').read().splitlines()


splits = list(map(lambda l: re.split(r"\s+", l[:-1].strip()), lines))


checksum = 0
probs = []
for c_i in range(len(splits[0])):
    prob = []
    for s_i in range(len(splits) - 1):
        prob.append(splits[s_i][c_i])
    probs.append(prob)
    eq = splits[-1][c_i].join(prob)
    checksum += eval(eq)

print(checksum)






chargrid = list(map(list, lines))

#Cover Down
for zx in range(len(lines)):
    for rx in range(len(lines) - 2):
        for cx in range(len(chargrid[0])):
            if chargrid[rx+1][cx] == ' ':
                chargrid[rx+1][cx] = chargrid[rx][cx]
                chargrid[rx][cx] = ' '


INOP = False
OPTY = None
CKSM = 0
operands = []
for ix, iv in enumerate(chargrid[-1]):
    if iv == "*" or iv == "+":
        INOP = True
        OPTY = iv
    elif all(map(lambda c: c == ' ', [chargrid[a][ix] for a in range(-2, -1*(len(chargrid) + 1), -1)])):
        INOP = False
        CKSM += eval(OPTY.join(map(str, operands)))
        operands = []


    if INOP:
        cur_op = 0
        for jx in range(-2, -1*(len(chargrid) + 1), -1):
            exp = jx * -1 - 2
            cur_char = chargrid[jx][ix]
            if cur_char != ' ':
                cur_op += int(cur_char) * 10**exp
        operands.append(cur_op)

print(CKSM)
