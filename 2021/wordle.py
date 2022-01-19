# https://www.devangthakkar.com/wordle_archive/

from collections import Counter

data_word_list = open('word_list.txt').read().splitlines()
possible_results = open('possible_results.txt').read().splitlines()


# 0 wrong, 1 right letter wrong place, 2 right letter in right place
def reduce_by_guess_result(guess, encoding, word_list):
    dupe_letters = []
    for i in range(5):
        sub_str = guess[:i]+guess[i+1:]
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


def get_largest_remaining_group(word, word_list):
    largest_remaining_group = 0
    for res in possible_results:
        remainder_size = len(reduce_by_guess_result(word, res, word_list))
        if remainder_size > largest_remaining_group:
            largest_remaining_group = remainder_size
    return largest_remaining_group


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


def play():
    game_list = data_word_list
    print("First Guess 'serai' precomputed as best first word")
    guess = 'serai'
    for i in range(6):
        result = input()
        game_list = reduce_by_guess_result(guess, result, game_list)
        guess = most_reductive_word(game_list)
        rem_len = len(game_list)
        info = f"Remaining words: {rem_len}, please guess: {guess}"
        if 2 <= rem_len < 15:
            info = f"Remaining words: {game_list}, please guess: {guess}"
        elif rem_len == 1:
            info = f"Solution is: {guess}"
        print(info)


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
