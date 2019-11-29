import hashlib


def md5_first_n(instr, n):
    return hashlib.md5(instr.encode()).hexdigest()[0:n]


puzzleStr = 'iwrupvqb'

i = 0
while True:
    md5 = md5_first_n(puzzleStr + str(i), 5)
    if md5 == '00000':
        break
    else:
        i += 1

print('Part 1:', i)

while True:
    md5 = md5_first_n(puzzleStr + str(i), 6)
    if md5 == '000000':
        break
    else:
        i += 1

print('Part 2:', i)
