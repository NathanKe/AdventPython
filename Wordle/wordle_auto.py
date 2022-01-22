# https://www.devangthakkar.com/wordle_archive/

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


def retrieve_guess(game_list):
    guess_from_poss, poss_redux = most_reductive_word(game_list, game_list)
    if poss_redux == 1:
        guess = guess_from_poss
    else:
        guess_from_all, all_redux = most_reductive_word(data_word_list, game_list, poss_redux)
        if poss_redux <= all_redux:
            guess = guess_from_poss
        else:
            guess = guess_from_all
    return guess


big_fucking_hash = {}


def auto_play(answer, verbose=False):
    verbose_print(verbose, f"{answer} -----")
    steps = 1
    game_list = answer_list
    guess = 'arise'

    game_chain = guess

    while True:
        result = checker(guess, answer)
        game_chain += result
        verbose_print(verbose, f"{guess} : {result}")
        game_list = reduce_by_guess_result(guess, result, game_list)

        if result == "22222":
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
        # if steps == 1 and result in arise_hash:
        #     guess = arise_hash[result]
        # elif steps == 1 and result not in arise_hash:
        #     guess = retrieve_guess(game_list)
        #     arise_hash[result] = guess
        # else:
        #     guess = retrieve_guess(game_list)

        steps += 1
        if steps > 6:
            verbose_print(verbose, "Failure!")
            break
    return steps
