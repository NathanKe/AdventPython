nums = list(map(int, open('01_input').read().splitlines()))

print('Part 1: ', sum(map(lambda x: x // 3 - 2, nums)))


def redux_sum(n):
    s = 0
    while n > 6:
        n = n // 3 - 2
        s += n
    return s


print('Part 2: ', sum(map(redux_sum, nums)))
