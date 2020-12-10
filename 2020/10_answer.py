from collections import Counter
import numpy

adapters = sorted(list(map(int, open('10_input').read().split())))

adapters.insert(0, 0)
adapters.append(adapters[-1]+3)


def diff_list(in_list):
    return [in_list[i+1]-in_list[i] for i in range(len(in_list)-1)]

adapt_diffs = diff_list(adapters)
diff_counter = Counter(adapt_diffs)

p1 = diff_counter[1] * diff_counter[3]

print('Part 1: ', p1)

segments = {}
cur_seg = 0
cur_cnt = 1
for diff in adapt_diffs:
    if diff == 1:
        cur_cnt += 1
    elif diff == 3:
        segments[cur_seg] = cur_cnt
        cur_cnt = 1
        cur_seg += 1

path_count_dict = {1: 1,
                   2: 1,
                   3: 2,
                   4: 4,
                   5: 7}


p2 = numpy.prod(list(map(lambda x: path_count_dict[x], segments.values())), dtype='int64')
print('Part 2: ', p2)
