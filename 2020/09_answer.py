import itertools

data = list(map(int, open('09_input').readlines()))


def valid(index):
    return data[index] in set(map(sum,
                                  filter(lambda tu: tu[0] != tu[1],
                                         itertools.product(data[index - 25:index], data[index - 25: index]))))


first_invalid = 0
for i in range(25, len(data)):
    if not valid(i):
        first_invalid = data[i]
        print('Part 1: ', first_invalid)
        break


def sequence_search(start_index, search_for):
    cur_offset = 1
    cur_sum = data[start_index]
    while cur_sum < search_for:
        cur_sum += data[start_index + cur_offset]
        cur_offset += 1
    if cur_sum == search_for:
        sequence = data[start_index: start_index + cur_offset]
        sorted_sequence = sorted(sequence)
        return sorted_sequence[0] + sorted_sequence[-1]
    else:
        return 0


for i in range(len(data)):
    check = sequence_search(i, first_invalid)
    if check:
        print('Part 2: ', check)
        break
