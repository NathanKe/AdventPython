import itertools
from itertools import product
from collections import Counter
from collections import defaultdict

data_word_list = open('word_list.txt').read().splitlines()
answer_list = open('answer_list.txt').read().splitlines()
possible_results = open('possible_results.txt').read().splitlines()

alphabet = [chr(x) for x in range(97, 123)]

let_loc_dict = defaultdict(lambda: defaultdict(int))
for alpha in alphabet:
    for i in range(0, 5):
        let_loc_dict[alpha][i] = 0

for ans in answer_list:
    for index, char in enumerate(ans):
        let_loc_dict[char][index] += 1


def score(word):
    out_score = 0
    for index, char in enumerate(word):
        out_score += let_loc_dict[char][index]
    return out_score


def find_best(word_list):
    out_max = 0
    best_word = ''
    for word in word_list:
        sc = score(word)
        if sc > out_max:
            out_max = sc
            best_word = word
    return best_word, out_max


def reduce(word_list, word):
    return [w for w in word_list if all(w[i] != word[i] for i in range(0, 5))]


def get_guess_order():
    working_list = data_word_list
    while working_list:
        cur_best, cur_best_score = find_best(working_list)
        print(cur_best, cur_best_score, len(working_list))
        working_list = reduce(working_list, cur_best)
    print(working_list)
