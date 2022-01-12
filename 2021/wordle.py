from collections import Counter
from collections import defaultdict

data_word_list = open('word_list.txt').read().splitlines()


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
    alpha = [chr(x) for x in range(65, 91)]
    letter_hash = defaultdict(int)

    for word in word_list:
        for letter in alpha:
            if letter in word:
                letter_hash[letter] += 1

    non_universal_hash = dict(filter(lambda elem: elem[1] != len(word_list), letter_hash.items()))

    return sorted(non_universal_hash.items(), key=lambda x: x[1], reverse=True)


def best_word(word_list):
    commonality_dict = dict(most_common_non_universal(word_list))
    max_score = 0
    cur_best_word = None
    for word in word_list:
        score = 0
        for letter in word:
            if letter in commonality_dict.keys():
                score += commonality_dict[letter]
        print(word, score)
        if score >= max_score:
            max_score = score
            cur_best_word = word

    return cur_best_word

