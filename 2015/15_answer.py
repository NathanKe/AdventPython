import re
import itertools
import functools

text = """Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8"""

text_lines = text.splitlines()


def parse(s):
    m = re.search(r"^.*\s(-?\d+).*\s(-?\d+).*\s(-?\d+).*\s(-?\d+).*\s(-?\d+)$", s)
    return [int(m[1]), int(m[2]), int(m[3]), int(m[4]), int(m[5])]


cookies = list(map(parse, text_lines))

grs = [i for i in range(0, 101)]

combos = filter(lambda tu: sum(tu) == 100, itertools.product(grs, repeat=4))


def ingr_score(ing, cmb):
    ingr_coeff = list(map(lambda li: li[ing], cookies))
    ingr_raw = sum(map(lambda tu: tu[0] * tu[1], zip(ingr_coeff, cmb)))
    if ingr_raw <= 0:
        return 0
    else:
        return ingr_raw


def combo_score(cmb):
    ingr_scores = [ingr_score(i, cmb) for i in range(0, 4)]
    return ingr_scores[0] * ingr_scores[1] * ingr_scores[2] * ingr_scores[3]


p1 = max(map(combo_score, combos))

print('Part 1: ', p1)


def five_hundred_calories(cmb):
    return ingr_score(4, cmb) == 500


p2 = max(map(combo_score, filter(five_hundred_calories, combos)))

print('Part 2: ', p2)
