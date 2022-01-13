# https://www.devangthakkar.com/wordle_archive/

from collections import Counter
from collections import defaultdict
import numpy as np

data_word_list = open('word_list.txt').read().splitlines()

no_repeats_word_list = list(filter(lambda w: Counter(w).most_common()[0][1] == 1, data_word_list))


# 0 wrong, 1 right letter wrong place, 2 right letter in right place
def reduce_by_guess_result(guess, encoding, word_list):
    for i, (l, c) in enumerate(zip(guess, encoding)):
        if c == '2':
            word_list = list(filter(lambda word: word[i] == l, word_list))
        elif c == '1':
            word_list = list(filter(lambda word: word[i] != l and l in word, word_list))
        elif c == '0':
            word_list = list(filter(lambda word: l not in word, word_list))

    return word_list


def most_common_non_universal(word_list):
    alpha = [chr(x) for x in range(97, 122)]
    letter_hash = defaultdict(int)

    for word in word_list:
        for letter in alpha:
            if letter in word:
                letter_hash[letter] += 1

    non_universal_hash = dict(filter(lambda elem: elem[1] != len(word_list), letter_hash.items()))
    return sorted(non_universal_hash.items(), key=lambda x: x[1], reverse=True)


possible_results = [np.base_repr(y, base=3).zfill(5) for y in range(243)]


def most_reductive_word(word_list):
    smallest_largest_remaining_group = float('inf')
    best_word = 'xxxxx'

    for i, word in enumerate(word_list):
        largest_remaining_group = 0

        for res in possible_results:
            remainder_size = len(reduce_by_guess_result(word, res, word_list))
            if remainder_size > smallest_largest_remaining_group:
                largest_remaining_group = remainder_size
                break
            if remainder_size > largest_remaining_group:
                largest_remaining_group = remainder_size
        if largest_remaining_group < smallest_largest_remaining_group:
            smallest_largest_remaining_group = largest_remaining_group
            best_word = word
    return best_word


def best_avail_word(word_list):
    commonality_dict = dict(most_common_non_universal(word_list))
    max_score = 0
    cur_best_word = None
    for word in word_list:
        score = 0
        for letter in word:
            if letter in commonality_dict.keys():
                score += commonality_dict[letter]
        if score >= max_score:
            max_score = score
            cur_best_word = word

    return cur_best_word


game_list = data_word_list
print("First Guess 'serai' as established best first word")
guess = 'serai'
for i in range(6):
    result = input()
    game_list = reduce_by_guess_result(guess, result, game_list)
    guess = most_reductive_word(game_list)
    print(guess, len(game_list))
