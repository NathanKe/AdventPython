import re
import itertools

to_check = open('07_input').read().splitlines()


def has_abba(s):
    search = re.search(r"((.)(.)\3\2)", s)
    if search:
        groups = search.groups()
        if groups[1] != groups[2]:
            return True
        else:
            return False
    else:
        return False


def map_abba_over_list(ss):
    return list(map(has_abba, ss))


def abba_in_brackets(ss):
    x = [v for v in ss[1::2]]
    return True in x


def abba_out_brackets(ss):
    y = [v for v in ss[0::2]]
    return True in y


def passes_abba_check(chck):
    abba_map = map_abba_over_list(re.split(r"[\[\]]", chck))
    found_out = abba_out_brackets(abba_map)
    found_in = abba_in_brackets(abba_map)
    res = found_out and not found_in
    return res


print('Part 1: ', len(list(filter(passes_abba_check, to_check))))


def distinct_aba_string(s):
    return list(set(filter(lambda x: x[0] != x[1], map(lambda tu: tu[0], re.findall(r"(?=((.).\2))", s)))))


def distinct_aba_string_list(li):
    all_res = []
    for item in li:
        cur_res = distinct_aba_string(item)
        for aba in cur_res:
            all_res.append(aba)
    return list(set(all_res))


def aba_out(s):
    split = re.split(r"[\[\]]", s)
    outs = split[0::2]
    return distinct_aba_string_list(outs)


def aba_in(s):
    split = re.split(r"[\[\]]", s)
    ins = split[1::2]
    return distinct_aba_string_list(ins)


def aba_out_and_bab_in(s):
    outs = aba_out(s)
    ins = aba_in(s)

    outs_rev = [a[1] + a[0] + a[1] for a in outs]

    for rev in outs_rev:
        if rev in ins:
            return True
    return False


print('Part 2: ', len(list(filter(aba_out_and_bab_in, to_check))))
