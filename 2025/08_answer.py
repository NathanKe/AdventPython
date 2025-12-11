from itertools import combinations

import math

def distance(a_tu, b_tu):
    return math.sqrt(abs(a_tu[0] - b_tu[0])**2 + abs(a_tu[1] - b_tu[1])**2 + abs(a_tu[2] - b_tu[2])**2)






junctions = list(map(lambda s: tuple(map(int, s.split(','))), open('08_input').read().splitlines()))


junction_pairs = list(combinations(junctions, 2))
junction_pairs.sort(key=lambda p: distance(*p))



circuits = []

for i in range(10):
    cur_pair = junction_pairs[i]
    print(cur_pair)
    print(circuits)
    found = False
    for circ in circuits:
        if not found:
            left_in = cur_pair[0] in circ
            right_in = cur_pair[1] in circ
            if left_in and right_in:
                print("both")
                found = True
            elif left_in:
                print("left")
                circ.append(cur_pair[1])
                found = True
            elif right_in:
                print("right")
                circ.append(cur_pair[0])
                found = True
    if not found:
        print("neither")
        circuits.append(list(cur_pair))
    print(circuits)
    print("-----------------")



circ_lens = list(map(len, circuits))
circ_lens.sort(reverse=True)
print(circ_lens[0] * circ_lens[1] * circ_lens[2])

