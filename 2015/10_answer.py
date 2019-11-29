import itertools

sx = "3113322113"


def look_say_expand(string):
    grs = []
    for _, g in itertools.groupby(string):
        grs.append(''.join(g))
    ret = ""
    for g in grs:
        ret += str(len(g))
        ret += g[0]
    return ret


for i in range(40):
    sx = look_say_expand(sx)

print('Part 1: ', len(sx))

for i in range(10):
    sx = look_say_expand(sx)

print('Part 2: ', len(sx))
