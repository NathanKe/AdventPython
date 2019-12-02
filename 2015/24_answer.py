import functools
import itertools

in_weights = [1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47,
              53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]


def min_size_passenger_grouping(weight_list, groupings):
    size = 1
    while True:
        combos_length_size = list(filter(lambda li: sum(li) == sum(weight_list) // groupings,
                                         itertools.combinations(weight_list, size)))
        if len(combos_length_size) != 0:
            break
        else:
            size += 1
    return size


def splittable_in_groupings_less_one(weight_list, groupings_less_one):
    for size in range(1, len(weight_list) // groupings_less_one):
        while True:
            combos_length_size = list(filter(lambda li: sum(li) == sum(weight_list) // groupings_less_one,
                                             itertools.combinations(weight_list, size)))
            if len(combos_length_size) != 0:
                return True
            else:
                size += 1
    return False


def remainder_splittable_in_groupings_less_one(weights_list, min_size_combo, groupings_less_one):
    rem = [x for x in weights_list if x not in min_size_combo]
    return splittable_in_groupings_less_one(rem, groupings_less_one)


def min_entangle(weights_list, grouping_count):
    min_size = min_size_passenger_grouping(weights_list, grouping_count)
    poss_min_size_combos = list(filter(lambda li: sum(li) == sum(weights_list) // grouping_count,
                                       itertools.combinations(weights_list, min_size)))
    valid_min_size_combos = list(
        filter(lambda cmb: remainder_splittable_in_groupings_less_one(weights_list, cmb, grouping_count - 1),
               poss_min_size_combos))
    min_entanglement = min(map(lambda cmb: functools.reduce(lambda x, y: x * y, cmb), valid_min_size_combos))
    return min_entanglement


print('Part 1: ', min_entangle(in_weights, 3))
print('Part 2: ', min_entangle(in_weights, 4))
