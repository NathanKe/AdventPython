import re


def str26_to_int10(s):
    rev = s[::-1]
    exp = 0
    str_sum = 0
    for ch in rev:
        str_sum += 26**exp * (ord(ch) - 97)
        exp += 1
    return str_sum


def int10_to_str26(i):
    ret_str = ""
    while True:
        m = i % 26
        d = i // 26
        ret_str += chr(m + 97)
        if d == 0:
            break
        else:
            i = d
    return ret_str[::-1]


def step_pswd(pswd):
    pswd_int = str26_to_int10(pswd)
    pswd_int += 1
    return int10_to_str26(pswd_int)


ascend_strs = []
for i in range(24):
    ascend_strs.append(chr(i+97)+chr(i+98)+chr(i+99))

ascend_regex = re.compile('|'.join(ascend_strs))


def good_pswd(pswd):
    if re.search(r"i|o|l", pswd):
        return False
    elif not re.search(r"(.)\1.*(.)\2", pswd):
        return False
    elif not re.search(ascend_regex, pswd):
        return False
    else:
        return True


pswd = step_pswd("hxbxwxba")

while not good_pswd(pswd):
    pswd = step_pswd(pswd)

print('Part 1: ', pswd)

pswd = step_pswd(pswd)

while not good_pswd(pswd):
    pswd = step_pswd(pswd)

print('Part 2: ', pswd)
