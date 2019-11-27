import re

p1 = 0
p2 = 0

words = open('05_input').readlines()


def has_three_vowels(check_word):
    if len(re.findall('[aeiou]', check_word)) < 3:
        return False
    else:
        return True


def has_double_letter(check_word):
    if re.search(r"(\w)\1", check_word):
        return True
    else:
        return False


def has_disallowed_string(check_word):
    if re.search('(ab|cd|pq|xy)', check_word):
        return True
    else:
        return False


def has_pair_twice(check_word):
    if re.search(r"(\w{2})\w*\1", check_word):
        return True
    else:
        return False


def has_repeat_with_one_inbetween(check_word):
    if re.search(r"(\w)\w\1", check_word):
        return True
    else:
        return False


def is_nice(check_word):
    if has_three_vowels(check_word) and has_double_letter(check_word) and not has_disallowed_string(check_word):
        return True
    else:
        return False


def is_nice_2(check_word):
    if has_pair_twice(check_word) and has_repeat_with_one_inbetween(check_word):
        return True
    else:
        return False


for word in words:
    if is_nice(word):
        p1 += 1
    if is_nice_2(word):
        p2 += 1

print('Part 1:', p1)
print('Part 2:', p2)
