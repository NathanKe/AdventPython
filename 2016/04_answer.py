import re
import collections
import functools

input_rooms = open('04_input').read().splitlines()

rooms_parse = list(map(lambda s: re.search(r"(\D+)(\d+)\[(.+)\]", s).groups(), input_rooms))


def five_most_common(s):
    no_dash = re.sub(r"-", "", s)
    counter = collections.Counter(no_dash)
    letter_count_tuple = list(zip(counter.keys(), counter.values()))
    letter_count_tuple.sort(key=lambda tu: tu[0], reverse=False)
    letter_count_tuple.sort(key=lambda tu: tu[1], reverse=True)
    first_five = list(map(lambda tu: tu[0], letter_count_tuple))[:5]
    first_five_str = ''.join(first_five)
    return first_five_str


def check_sum_checks(room_tuple):
    return five_most_common(room_tuple[0]) == room_tuple[2]


real_rooms = list(filter(check_sum_checks, rooms_parse))

print('Part 1: ', sum(list(map(lambda tu: int(tu[1]), real_rooms))))


def shift_letter(letter, shift):
    if letter == '-':
        return '-'
    else:
        return chr((ord(letter) - 97 + shift) % 26 + 97)


def shift_string(string, shift):
    ret = ""
    for c in string:
        ret += shift_letter(c, shift)
    return ret


npo = *filter(lambda tu: re.search(r"(north|pole|obj)", tu[0]),
              map(lambda tu: (shift_string(tu[0], int(tu[1])), tu[1]),
                  real_rooms)),

if len(npo) == 1:
    print('Part 2: ', npo[0][1])
else:
    print('Multiple Candidates')
