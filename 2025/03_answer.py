import itertools

banks = open('03_input').read().splitlines()


def short_max_joltage(num_str):
    return max(map(lambda x: int(''.join(x)), itertools.combinations(num_str, 2)))


print(sum(map(short_max_joltage, banks)))


def max_joltage(num_str, bat_cnt):
    if bat_cnt == 1:
        return max(map(int, num_str))
    head_tu = enumerate(num_str[:len(num_str) - bat_cnt + 1])
    max_head_i, max_head_v = max(head_tu, key=lambda tu: int(tu[1]))


    tail = num_str[max_head_i+1:]

    return int(max_head_v + str(max_joltage(tail, bat_cnt-1)))

print(sum(map(lambda b: max_joltage(b, 12), banks)))

