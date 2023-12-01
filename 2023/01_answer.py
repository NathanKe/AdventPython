lines = open('01_input').read().split('\n')

import re

calib_sum = 0

for line in lines:
    foundNumbers = re.findall(r"\d", line)
    line_calib = int(foundNumbers[0] + foundNumbers[-1])
    calib_sum += line_calib

print(calib_sum)

spell_dict = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}


def traverser(in_line, reverse=False):
    if reverse:
        in_line = in_line[::-1]

    buffered_line = in_line + "---------"

    for ind in range(0, len(in_line)):
        ch1 = buffered_line[ind:ind+1]
        ch3 = buffered_line[ind:ind+3]
        ch4 = buffered_line[ind:ind+4]
        ch5 = buffered_line[ind:ind+5]

        if reverse:
            ch3 = ch3[::-1]
            ch4 = ch4[::-1]
            ch5 = ch5[::-1]

        if re.match(r"\d", ch1):
            return ch1
        elif ch3 in spell_dict.keys():
            return spell_dict[ch3]
        elif ch4 in spell_dict.keys():
            return spell_dict[ch4]
        elif ch5 in spell_dict.keys():
            return spell_dict[ch5]


calib_sum = 0
for line in lines:
    fwd = traverser(line)
    bck = traverser(line, reverse=True)
    calib_sum += int(fwd + bck)

print(calib_sum)
