import functools
from collections import Counter as co

hand_data = open('07_input').read().splitlines()

point_map = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

hands = [(list(map(lambda li: point_map[li], list(h.split(" ")[0]))), int(h.split(" ")[1])) for h in hand_data]


def pad_zeros(in_list, pad_length):
    if len(in_list) >= pad_length:
        return in_list
    else:
        in_list.append(0)
        return pad_zeros(in_list, pad_length)


def hand_comparator(hand_tuple_a, hand_tuple_b):
    hand_a = hand_tuple_a[0]
    hand_b = hand_tuple_b[0]
    cnt_a = co(hand_a)
    cnt_b = co(hand_b)
    counts_a = pad_zeros(list(cnt_a.values()), 5)
    counts_b = pad_zeros(list(cnt_b.values()), 5)
    counts_a.sort(reverse=True)
    counts_b.sort(reverse=True)


    if counts_a < counts_b:
        return -1
    elif counts_a > counts_b:
        return 1
    else:
        if hand_a < hand_b:
            return -1
        elif hand_a > hand_b:
            return 1
        else:
            return 0


hands.sort(key=functools.cmp_to_key(hand_comparator))

winnings = sum([(h[0]+1) * h[1][1] for h in enumerate(hands)])

print(winnings)


