import hashlib

base_id = 'cxdnnyjw'

def md5_first_n(to_hash, n):
    return hashlib.md5(to_hash.encode()).hexdigest()[0:n]


def next_interesting(door_id, n):
    while True:
        to_hash = door_id + str(n)
        first_seven = md5_first_n(to_hash, 7)
        n += 1
        if first_seven[0:5] == '00000':
            return n, first_seven[5], first_seven[6]


num = 0
cur_char = None
res_pass = ''
for i in range(8):
    num, cur_char, _ = next_interesting(base_id, num)
    res_pass += cur_char

print('Part 1: ', res_pass)

num = 0
cur_char = None
res_pass = 'xxxxxxxx'
while 'x' in res_pass:
    num, ind, cur_char = next_interesting(base_id, num)
    if ind in ['0', '1', '2', '3', '4', '5', '6', '7']:
        int_ind = int(ind)
        if res_pass[int_ind] == 'x':
            res_pass = res_pass[:int_ind] + cur_char + res_pass[(int_ind + 1):]


print('Part 1', res_pass)
