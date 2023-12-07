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


def highest_most_common_non_joker(i_hand):
    non_joker = [card for card in i_hand if card != 11]
    hand_counter = co(non_joker)
    most_common_count = hand_counter.most_common()[0][1]
    equally_most_common = [tu for tu in hand_counter.items() if tu[1] == most_common_count]
    highest_most_common = sorted([tu[0] for tu in equally_most_common])[-1]
    return highest_most_common


def best_use_of_joker(i_hand):
    if i_hand == [11, 11, 11, 11, 11]:
        return [14, 14, 14, 14, 14]
    else:
        target = highest_most_common_non_joker(i_hand)
        new_hand = []
        for card in i_hand:
            if card == 11:
                new_hand.append(target)
            else:
                new_hand.append(card)
    return new_hand


def low_val_joker(i_hand):
    new_hand = []
    for card in i_hand:
        if card == 11:
            new_hand.append(0)
        else:
            new_hand.append(card)
    return new_hand


def hand_comparator_2(hand_tuple_a, hand_tuple_b):
    hand_a = hand_tuple_a[0]
    hand_b = hand_tuple_b[0]
    joker_a = best_use_of_joker(hand_a)
    joker_b = best_use_of_joker(hand_b)
    cnt_a = co(joker_a)
    cnt_b = co(joker_b)
    counts_a = pad_zeros(list(cnt_a.values()), 5)
    counts_b = pad_zeros(list(cnt_b.values()), 5)
    counts_a.sort(reverse=True)
    counts_b.sort(reverse=True)

    if counts_a < counts_b:
        return -1
    elif counts_a > counts_b:
        return 1
    else:
        low_joker_a = low_val_joker(hand_a)
        low_joker_b = low_val_joker(hand_b)

        if low_joker_a < low_joker_b:
            return -1
        elif low_joker_a > low_joker_b:
            return 1
        else:
            return 0


hands.sort(key=functools.cmp_to_key(hand_comparator_2))

winnings2 = sum([(h[0]+1) * h[1][1] for h in enumerate(hands)])

print(winnings2)
