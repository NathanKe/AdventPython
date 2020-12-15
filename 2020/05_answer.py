from collections import Counter as co

seats = open('05_input').read().splitlines()


def recur_seat(avail, inst):
    if inst[0] == 'F' or inst[0] == 'L':
        avail = avail[:len(avail) // 2]
    else:
        avail = avail[len(avail) // 2:]

    if len(inst) == 1:
        return avail[0]
    else:
        return recur_seat(avail, inst[1:])


def seat_id(inst):
    return 8 * recur_seat(range(128), inst[:-3]) + recur_seat(range(8), inst[-3:])


print("Part 1: ", sorted(map(lambda x: seat_id(x), seats))[-1])

seat_dict = list(map(lambda s: {'r': recur_seat(range(128), s[:-3]),
                                'c': recur_seat(range(8), s[-3:]),
                                'i': seat_id(s)},
                     seats))

info = {}
for seat in seat_dict:
    if seat['r'] in info:
        info[seat['r']][0] += 1
        info[seat['r']][1].append(seat['c'])
    else:
        info[seat['r']] = [1, [seat['c']]]

my_info = list(filter(lambda elem: elem[1][0] == 7, info.items()))[0]

my_row = my_info[0]
my_col = list(filter(lambda x: x not in my_info[1][1], range(8)))[0]
print('Part 2: ', my_row * 8 + my_col)
