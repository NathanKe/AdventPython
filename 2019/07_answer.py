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
