from collections import defaultdict

init_secrets = list(map(int, open('22_input').read().splitlines()))


def nth_next_number(i_number, nth):
    for _ in range(nth):
        i_number = ((i_number << 6) ^ i_number) & 16777215
        i_number = ((i_number >> 5) ^ i_number) & 16777215
        i_number = ((i_number << 11) ^ i_number) & 16777215
    return i_number


print(sum(map(lambda initial: nth_next_number(initial, 2000), init_secrets)))


def price_change_sequence_dicts(i_number, seq_len):
    incoming_price = i_number % 10

    out_seq = []
    out_dict = defaultdict(lambda: 0)

    for ix in range(seq_len):
        i_number = ((i_number << 6) ^ i_number) & 16777215
        i_number = ((i_number >> 5) ^ i_number) & 16777215
        i_number = ((i_number << 11) ^ i_number) & 16777215
        cur_price = i_number % 10
        out_seq.append(cur_price - incoming_price)
        incoming_price = cur_price
        if ix >= 3:
            prev_seq = tuple(*[out_seq[ix - 3:ix + 1]])
            if prev_seq not in out_dict.keys():
                out_dict[prev_seq] = cur_price
    return out_dict


seq_sum_dict = defaultdict(lambda: 0)
for i_n in init_secrets:
    init_dict = price_change_sequence_dicts(i_n, 2000)
    for k, v in init_dict.items():
        seq_sum_dict[k] += v

print(sorted(list(seq_sum_dict.items()), key=lambda tu: tu[1])[-1][1])
