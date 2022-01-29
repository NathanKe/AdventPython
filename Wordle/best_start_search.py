# https://www.devangthakkar.com/wordle_archive/

from itertools import product
from collections import Counter

data_word_list = open('word_list.txt').read().splitlines()
answer_list = open('answer_list.txt').read().splitlines()
possible_results = open('possible_results.txt').read().splitlines()


def index_letter_code_filter(ind, let, code, dupe_letters, word):
    code2 = code == '2' and word[ind] == let
    code1 = code == '1' and word[ind] != let and let in word
    code0 = code == '0' and let not in word
    code0_dupe = code == '0' and let in dupe_letters and word[ind] != let
    return any([code2, code1, code0, code0_dupe])


def grand_filter(guess, encoding, dupe_letters, word):
    return all([index_letter_code_filter(i, l, c, dupe_letters, word) for i, (l, c) in enumerate(zip(guess, encoding))])


# 0 wrong, 1 right letter wrong place, 2 right letter in right place
def reduce_by_guess_result(guess, encoding, word_list):
    dupe_letters = []
    for i in range(5):
        sub_str = guess[:i] + guess[i + 1:]
        if guess[i] in sub_str:
            dupe_letters.append(guess[i])

    word_list = list(filter(lambda word: grand_filter(guess, encoding, dupe_letters, word), word_list))
    return word_list


def most_reductive_word(guessable_words, word_list, limit=15000):
    smallest_largest_remaining_group = len(word_list)
    best_word = 'xxxxx'

    for word in guessable_words:
        largest_remaining_group = 0

        for res in possible_results:
            remainder_size = len(reduce_by_guess_result(word, res, word_list))
            if remainder_size > smallest_largest_remaining_group or remainder_size >= limit:
                largest_remaining_group = remainder_size
                break
            if remainder_size > largest_remaining_group:
                largest_remaining_group = remainder_size
        if largest_remaining_group <= smallest_largest_remaining_group:
            smallest_largest_remaining_group = largest_remaining_group
            best_word = word
            if smallest_largest_remaining_group == 1:
                break
    return best_word, smallest_largest_remaining_group


def checker(guess, answer):
    result = ""
    for i in range(5):
        if guess[i] in guess[:i] + guess[i + 1:]:
            if guess[i] == answer[i]:
                result += "2"
            elif guess[i] in answer[i:]:
                result += "1"
            else:
                result += "0"
        else:
            if guess[i] == answer[i]:
                result += "2"
            elif guess[i] in answer:
                result += "1"
            else:
                result += "0"
    return result


def retrieve_guess(game_list):
    guess_from_poss, poss_redux = most_reductive_word(game_list, game_list)
    if poss_redux == 1:
        guess = guess_from_poss
    else:
        guess_from_rem, rem_redux = most_reductive_word([d for d in data_word_list if d not in game_list], game_list,
                                                        poss_redux)
        if poss_redux <= rem_redux:
            guess = guess_from_poss
        else:
            guess = guess_from_rem
    return guess


big_fucking_hash = {}


# big_fucking_hash = eval(open('big_fucking_hash_cache.txt').read().splitlines()[0])


def auto_play(answer, start_guess):
    steps = 1
    game_list = answer_list
    guess = start_guess

    game_chain = guess

    while True:
        result = checker(guess, answer)
        game_chain += result
        game_list = reduce_by_guess_result(guess, result, game_list)

        if result == "22222":
            big_fucking_hash[game_chain] = guess
            break

        if len(game_list) == 1:
            guess = game_list[0]
            big_fucking_hash[game_chain] = guess
        else:
            if game_chain in big_fucking_hash:
                guess = big_fucking_hash[game_chain]
            else:
                guess = retrieve_guess(game_list)
                big_fucking_hash[game_chain] = guess
        game_chain += guess
        steps += 1
        if steps > 6:
            break
    return steps


def start_word_outcome_step_total(start_word, limit=float('inf')):
    step_total = 0
    for answer_word in answer_list:
        print(f"---{answer_word}")
        current_steps = auto_play(answer_word, start_word)
        if current_steps > 6:
            step_total = float('inf')
            break
        step_total += current_steps
        if step_total > limit:
            step_total = float('inf')
            break
    return step_total


def find_best_start(search_set):
    best_word = 'xxxxx'
    best_step_count = float('inf')

    for start_word in search_set:
        print(start_word)
        total_steps_from_current_start_word = start_word_outcome_step_total(start_word, best_step_count)
        if total_steps_from_current_start_word < best_step_count:
            best_word = start_word
            best_step_count = total_steps_from_current_start_word
            print(f"New Best!: {best_word} with {best_step_count} steps")
        else:
            print(f"Failed: {start_word}")

    return best_word, best_step_count
