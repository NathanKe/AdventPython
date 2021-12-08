data = open('08_input').read().splitlines()

outputs = map(lambda x: x.split(' '), map(lambda x: x.split(" | ")[1], data))

oneFourSevenEightCount = sum(map(lambda y: len(list(filter(lambda x: len(x) in [2, 3, 4, 7], y))), outputs))

print("Part 1: ", oneFourSevenEightCount)


def ident_three(one, two_three_five):
    for digit in two_three_five:
        if one.intersection(digit) == one:
            return digit


def ident_zero(three, one, zero_six_nine):
    top_middle_bottom = three.difference(one)
    for digit in zero_six_nine:
        if top_middle_bottom.intersection(digit) != top_middle_bottom:
            return digit


def ident_nine(three, zero_six_nine):
    for digit in zero_six_nine:
        if three.intersection(digit) == three:
            return digit


def ident_six(six, zero, zero_six_nine):
    for digit in zero_six_nine:
        if digit != six and digit != zero:
            return sorted(digit)


def ident_five(six, two_three_five):
    for digit in two_three_five:
        if digit.intersection(six) == digit:
            return digit


def ident_two(three, five, two_three_five):
    for digit in two_three_five:
        if digit != three and digit != five:
            return sorted(digit)


def decode(data_line):
    signal, output = map(lambda x: x.split(' '), data_line.split(" | "))

    len_sorted_signal = list(map(lambda x: set(list(x)), sorted(signal, key=len)))
    sig_one = len_sorted_signal[0]
    sig_seven = len_sorted_signal[1]
    sig_four = len_sorted_signal[2]
    sig_eight = len_sorted_signal[9]

    sig_two_three_five = len_sorted_signal[3:6]
    sig_zero_six_nine = len_sorted_signal[6:9]

    sig_three = ident_three(sig_one, sig_two_three_five)

    sig_zero = ident_zero(sig_three, sig_one, sig_zero_six_nine)
    sig_nine = ident_nine(sig_three, sig_zero_six_nine)
    sig_six = ident_six(sig_nine, sig_zero, sig_zero_six_nine)

    sig_five = ident_five(sig_six, sig_two_three_five)
    sig_two = ident_two(sig_three, sig_five, sig_two_three_five)

    hashable_zero = ''.join(sorted(list(sig_zero)))
    hashable_one = ''.join(sorted(list(sig_one)))
    hashable_two = ''.join(sorted(list(sig_two)))
    hashable_three = ''.join(sorted(list(sig_three)))
    hashable_four = ''.join(sorted(list(sig_four)))
    hashable_five = ''.join(sorted(list(sig_five)))
    hashable_six = ''.join(sorted(list(sig_six)))
    hashable_seven = ''.join(sorted(list(sig_seven)))
    hashable_eight = ''.join(sorted(list(sig_eight)))
    hashable_nine = ''.join(sorted(list(sig_nine)))

    sig_hash = {
        hashable_zero: 0,
        hashable_one: 1,
        hashable_two: 2,
        hashable_three: 3,
        hashable_four: 4,
        hashable_five: 5,
        hashable_six: 6,
        hashable_seven: 7,
        hashable_eight: 8,
        hashable_nine: 9
    }

    alphabetical_outputs = list(map(lambda x: ''.join(sorted(x)), output))

    return sum(map(lambda x: sig_hash[x[0]]*x[1], zip(alphabetical_outputs, [1000, 100, 10, 1])))


print("Part 2: ", sum(map(decode, data)))
