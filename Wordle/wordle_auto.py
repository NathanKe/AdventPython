# https://www.devangthakkar.com/wordle_archive/

from collections import Counter

data_word_list = open('word_list.txt').read().splitlines()
answer_list = open('answer_list.txt').read().splitlines()
possible_results = open('possible_results.txt').read().splitlines()


def grand_filter(ind, let, code, dupe_letters, word):
    code2 = code == 2 and word[ind] == let
    code1 = code == 1 and word[ind] != let and let in word
    code0 = code == 0 and let not in word
    code0_dupe = code == 0 and let in dupe_letters and word[ind] != let
    return code2 or code1 or code0 or code0_dupe


# 0 wrong, 1 right letter wrong place, 2 right letter in right place
def reduce_by_guess_result(guess, encoding, word_list):
    dupe_letters = []
    for i in range(5):
        sub_str = guess[:i] + guess[i + 1:]
        if guess[i] in sub_str:
            dupe_letters.append(guess[i])

    for i, (l, c) in enumerate(zip(guess, encoding)):
        if c == '2':
            word_list = list(filter(lambda word: word[i] == l, word_list))
        elif c == '1':
            word_list = list(filter(lambda word: word[i] != l and l in word, word_list))
        elif c == '0':
            if l in dupe_letters:
                word_list = list(filter(lambda word: word[i] != l, word_list))
            elif l not in dupe_letters:
                word_list = list(filter(lambda word: l not in word, word_list))

    return word_list


def most_reductive_word(guessable_words, word_list):
    smallest_largest_remaining_group = float('inf')
    best_word = 'xxxxx'

    for i, word in enumerate(guessable_words):
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
            if smallest_largest_remaining_group == 1:
                break
    return best_word, smallest_largest_remaining_group


def verbose_print(verbose, to_print):
    if verbose:
        print(to_print)


def checker(guess, answer):
    dupe_letters = []
    for i in range(5):
        sub_str = guess[:i]+guess[i+1:]
        if guess[i] in sub_str:
            dupe_letters.append(guess[i])

    result = ""
    for i in range(5):
        if guess[i] in dupe_letters:
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


arise_hash = {}


def auto_play(answer, verbose=False):
    verbose_print(verbose, f"{answer} -----")
    steps = 1
    game_list = answer_list
    guess = 'arise'
    while True:
        result = checker(guess, answer)
        verbose_print(verbose, f"{guess} : {result}")
        if steps == 1 and result in arise_hash:
            game_list = arise_hash[result]
        elif steps == 1 and result not in arise_hash:
            game_list = reduce_by_guess_result(guess, result, game_list)
            arise_hash[result] = game_list
        else:
            game_list = reduce_by_guess_result(guess, result, game_list)

        if result == "22222":
            break

        if len(game_list) == 1:
            guess = game_list[0]
        else:
            guess_from_poss, poss_redux = most_reductive_word(game_list, game_list)
            if poss_redux == 1:
                guess = guess_from_poss
            else:
                guess_from_all, all_redux = most_reductive_word(data_word_list, game_list)

                if poss_redux <= all_redux:
                    guess = guess_from_poss
                else:
                    guess = guess_from_all
        steps += 1
        if steps > 6:
            verbose_print(verbose, "Failure!")
            break
    return steps


# To-Do: