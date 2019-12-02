input_code = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 13, 1, 19, 1, 19, 10, 23, 1, 23, 6, 27, 1, 6, 27, 31,
              1, 13,
              31, 35, 1, 13, 35, 39, 1, 39, 13, 43, 2, 43, 9, 47, 2, 6, 47, 51, 1, 51, 9, 55, 1, 55, 9, 59, 1, 59, 6,
              63, 1,
              9, 63, 67, 2, 67, 10, 71, 2, 71, 13, 75, 1, 10, 75, 79, 2, 10, 79, 83, 1, 83, 6, 87, 2, 87, 10, 91, 1, 91,
              6,
              95, 1, 95, 13, 99, 1, 99, 13, 103, 2, 103, 9, 107, 2, 107, 10, 111, 1, 5, 111, 115, 2, 115, 9, 119, 1, 5,
              119,
              123, 1, 123, 9, 127, 1, 127, 2, 131, 1, 5, 131, 0, 99, 2, 0, 14, 0]


def ex_one(i, code):
    code[code[i + 3]] = code[code[i + 1]] + code[code[i + 2]]
    i += 4
    return i, code


def ex_two(i, code):
    code[code[i + 3]] = code[code[i + 1]] * code[code[i + 2]]
    i += 4
    return i, code


def set_noun_verb(code, noun, verb):
    code[1] = noun
    code[2] = verb
    return code


def run_code(param_code, noun, verb):
    ind = 0
    code = param_code[:]
    code = set_noun_verb(code, noun, verb)
    while True:
        if code[ind] == 1:
            ind, code = ex_one(ind, code)
        if code[ind] == 2:
            ind, code = ex_two(ind, code)
        if code[ind] == 99:
            break
    return code[0]


p1_noun = 12
p1_verb = 2
p1 = run_code(input_code, p1_noun, p1_verb)

print('Part 1: ', p1)

p2 = None
for i_noun in range(100):
    for i_verb in range(100):
        res = run_code(input_code, i_noun, i_verb)
        if res == 19690720:
            p2 = 100 * i_noun + i_verb
            break

print('Part 2: ', p2)
