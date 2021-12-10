from collections import deque

data = open('10_input').read().splitlines()

opens = ['!', '(', '[', '{', '<']
closes = ['!', ')', ']', '}', '>']

points_1 = {
    '!': 0,
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
points_2 = {
    '!': 0,
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}


illegal_chars_vals = []
completion_sequences_vals = []


def first_illegal_char(in_line):
    dq = deque()
    for char in in_line:
        if char in opens:
            dq.append(char)
        elif char in closes:
            prev_open = dq.pop()
            if closes.index(char) != opens.index(prev_open):
                return char
    return '!'


def closing_sequence_val(in_line):
    dq = deque()
    for char in in_line:
        if char in opens:
            dq.append(char)
        if char in closes and closes.index(char) == opens.index(dq[-1]):
            dq.pop()
    score = 0
    while dq:
        char = dq.pop()
        score *= 5
        score += points_2[char]
    return score


for line in data:
    f_i_c = first_illegal_char(line)
    if f_i_c == '!':
        completion_sequences_vals.append(closing_sequence_val(line))
    else:
        illegal_chars_vals.append(points_1[f_i_c])

print("Part 1: ", sum(illegal_chars_vals))
print("Part 2: ", sorted(completion_sequences_vals)[len(completion_sequences_vals)//2])
