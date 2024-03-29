# https://www.devangthakkar.com/wordle_archive/

from collections import Counter

data_word_list = open('word_list.txt').read().splitlines()
answer_list = open('answer_list.txt').read().splitlines()
possible_results = open('possible_results.txt').read().splitlines()


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


def print_feedback(guess, game_list):
    rem_len = len(game_list)
    if rem_len >= 15:
        info = f"Remaining words: {rem_len}, please guess: {guess}"
        print(info)
    if 2 <= rem_len < 15:
        info = f"Remaining words: {game_list}, please guess: {guess}"
        print(info)
    elif rem_len == 1:
        info = f"Solution is: {guess}"
        print(info)
        return True
    return False


# Guesses allowed from all valid words
# Guesses pulled from remaining possibilities
def standard_play():
    game_list = data_word_list
    print("First Guess 'arise' precomputed as best first word")
    guess = 'arise'
    for i in range(6):
        print("Result:")
        result = input()
        game_list = reduce_by_guess_result(guess, result, game_list)
        guess, _ = most_reductive_word(game_list, game_list)
        end_early = print_feedback(guess, game_list)
        if end_early:
            break


# Guesses only pulled from valid answer set
# Guesses pulled from remaining possibilities
def allowed_answers_only_play():
    game_list = answer_list
    print("First Guess 'arise' precomputed as best first word")
    guess = 'arise'
    for i in range(6):
        print("Result:")
        result = input()
        game_list = reduce_by_guess_result(guess, result, game_list)
        guess, _ = most_reductive_word(game_list, game_list)
        end_early = print_feedback(guess, game_list)
        if end_early:
            break


# First guess not pre-computed
# Guesses pulled from all valid words
# Guesses pulled from remaining possibilities
def open_first_guess_play():
    game_list = data_word_list
    print("Guess:")
    guess = input()
    while True:
        print("Result:")
        result = input()
        game_list = reduce_by_guess_result(guess, result, game_list)
        guess, _ = most_reductive_word(game_list, game_list)
        end_early = print_feedback(guess, game_list)
        if end_early:
            break


# Answers set to available answer set
# checks results from both all words and possible answer words
# if there is a tie in reduction strength, guesses the possible answer word
#   in order to maximize luck
def slow_advanced_play():
    game_list = answer_list
    print("First Guess 'arise' precomputed as best first word")
    guess = 'arise'
    for i in range(6):
        print("Result:")
        result = input()
        game_list = reduce_by_guess_result(guess, result, game_list)
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
        end_early = print_feedback(guess, game_list)
        if end_early:
            break


# Player free to guess at all stages
# only feedback is length of remaining possible words
def free_play():
    game_list = data_word_list
    while True:
        print("Guess:")
        guess = input()
        print("Result:")
        result = input()
        if result == "22222":
            break
        game_list = reduce_by_guess_result(guess, result, game_list)
        rem_len = len(game_list)
        if rem_len >= 15:
            info = f"Remaining words: {rem_len}"
            print(info)
        if rem_len < 15:
            info = f"Remaining words: {game_list}"
            print(info)


def four_search():
    x = ''.join(answer_list)
    q = [i[0] for i in Counter(x).most_common(20)]
    count = 0
    for a in answer_list:
        if all([l in q for l in a]):
            for b in answer_list:
                if all([l not in a for l in b]) and all([l in q for l in b]):
                    for c in answer_list:
                        if all([l not in a+b for l in c]) and all([l in q for l in c]):
                            for d in answer_list:
                                if all([l in a+b+c+d for l in q]):
                                    print(a,b,c,d)
                                    count += 1
                                    if count >= 10:
                                        return
