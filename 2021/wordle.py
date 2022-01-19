# https://www.devangthakkar.com/wordle_archive/

from collections import Counter
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


possible_results = open('possible_results.txt').read().splitlines()


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


def largest_remaining_group(word, word_list, limiter = float('inf')):
    largest_rem_size = 0
    for res in possible_results:
        rem_size = len(reduce_by_guess_result(word, res, word_list))
        if rem_size > limiter:
            return limiter
        elif rem_size > largest_rem_size:
            largest_rem_size = rem_size
    return rem_size


def depth_2_largest_group(word_1, word_2, word_list, limiter=float('inf')):
    best_res = float('inf')
    for res_1 in possible_results:
        redux_1_list = reduce_by_guess_result(word_1, res_1, word_list)
        cur_res = largest_remaining_group(word_2, redux_1_list, best_res)
        if cur_res < best_res:
            best_res = cur_res
    return best_res


def starting_pair(word_list):
    smallest_largest = float('inf')
    best = ('xxxxx', 'yyyyy')
    for word_1 in word_list:
        for res_1 in possible_results:
            redux_1_list = reduce_by_guess_result(word_1, res_1, word_list)
            for word_2 in word_list:
                w2_fails = False
                if all([w1 not in word_2 for w1 in word_1]):
                    print(word_1, word_2, best, smallest_largest)
                    depth_2_largest = 0
                    for res_2 in possible_results:
                        redux_2_list = reduce_by_guess_result(word_2, res_2, redux_1_list)
                        cur_rem_len = len(redux_2_list)
                        if cur_rem_len > smallest_largest:
                            w2_fails = True
                            break
                        elif cur_rem_len > depth_2_largest:
                            depth_2_largest = cur_rem_len
                    if depth_2_largest < smallest_largest:
                        smallest_largest = depth_2_largest
                        best = (word_1, word_2)
                if w2_fails:
                    break



def play():
    game_list = data_word_list
    print("First Guess 'serai' as established best first word")
    guess = 'serai'
    for i in range(6):
        result = input()
        game_list = reduce_by_guess_result(guess, result, game_list)
        guess = most_reductive_word(game_list)
        rem_len = len(game_list)
        info = f"Remaining words: {rem_len}, please guess: {guess}"
        if rem_len < 15:
            info = f"Remaining words: {game_list}"
        print(info)
        if rem_len < 6 - i:
            break


def free_play():
    game_list = data_word_list
    print("Guess:")
    guess = input()
    while True:
        print("Result:")
        result = input()
        game_list = reduce_by_guess_result(guess, result, game_list)
        guess = most_reductive_word(game_list)
        rem_len = len(game_list)
        info = f"Remaining words: {rem_len}, please guess: {guess}"
        if rem_len < 5:
            print(f"Remaining words: {game_list}")
            break
        print(info)

#play()
