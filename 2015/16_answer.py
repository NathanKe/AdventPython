import re

aunts = open('16_input').read().splitlines()

criteria = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".splitlines()


def generic_filter(item, count, comp, aunt):
    rx_count = re.compile(item + r":\s(\d+)")
    if re.search(item, aunt) is None:
        return True
    else:
        mx = re.search(rx_count, aunt)
        return eval(count + comp + mx[1])


res = aunts.copy()
for criterion in criteria:
    m = re.match(r"(.+):\s(\d+)", criterion)
    res = list(filter(lambda aunt: generic_filter(m[1], m[2], '==', aunt), res))

print('Part 1: ', re.match(r"Sue\s(\d+):", res[0])[1])

res = aunts.copy()
for criterion in criteria:
    m = re.match(r"(.+):\s(\d+)", criterion)
    if m[1] == 'cats' or m[1] == 'trees':
        comp = '<'
    elif m[1] == 'pomeranians' or m[1] == 'goldfish':
        comp = '>'
    else:
        comp = '=='
    res = list(filter(lambda aunt: generic_filter(m[1], m[2], comp, aunt), res))

print('Part 2: ', re.match(r"Sue\s(\d+):", res[0])[1])
