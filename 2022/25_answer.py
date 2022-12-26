from collections import deque

num_list = open('25_input').read().splitlines()


def snafu_to_dec(snafu):
    sn_dq = deque(snafu)
    multiplicand = 1
    val_arr = []
    while sn_dq:
        x = sn_dq.pop()
        y = None
        if x == '=':
            y = -2
        elif x == '-':
            y = -1
        else:
            y = int(x)
        val_arr.append(multiplicand * y)
        multiplicand *= 5
    return sum(val_arr)


def dec_to_snafu(dec):
    snaf_digs = deque()
    while dec:
        cur_mod = dec % 5
        if cur_mod == 4:
            dec += 1
            snaf_digs.appendleft('-')
        elif cur_mod == 3:
            dec += 2
            snaf_digs.appendleft('=')
        else:
            dec -= cur_mod
            snaf_digs.appendleft(str(cur_mod))
        dec //= 5
    return ''.join(snaf_digs)


# print(dec_to_snafu(str(sum(map(lambda x: snafu_to_dec(x), num_list)))))


dec_sum = sum(map(lambda n: snafu_to_dec(n), num_list))
snaf_sum = dec_to_snafu(dec_sum)

print("Part 1: ", snaf_sum)
