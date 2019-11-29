import re

lines = open('08_input').read().splitlines()

total_len = sum(map(len, lines))

compress_len = sum(map(len, list(map(eval, lines))))


def encode(str):
    result = ''
    for ch in str:
        if ch == '"':
            result += '\\\"'
        elif ch == '\\':
            result += '\\\\'
        else:
            result += ch
    return '"' + result + '"'


expand_len = sum(map(len, list(map(encode, lines))))

print('Part 1:', total_len - compress_len)
print('Part 2:', expand_len - total_len)
