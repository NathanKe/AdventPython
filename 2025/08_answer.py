from itertools import combinations

import math

def distance(a_tu, b_tu):
    return math.sqrt(abs(a_tu[0] - b_tu[0])**2 + abs(a_tu[1] - b_tu[1])**2 + abs(a_tu[2] - b_tu[2])**2)






junctions = list(map(lambda s: tuple(map(int, s.split(','))), open('08_input').read().splitlines()))


junction_pairs = list(combinations(junctions, 2))
junction_pairs.sort(key=lambda p: distance(*p))



circuits = []

for i in range(1000):
    cur_pair = junction_pairs[i]
    found = False
    for circ in circuits:
        if not found:
            left_in = cur_pair[0] in circ
            right_in = cur_pair[1] in circ
            if left_in and right_in:
                found = True
            elif left_in:
                circ.append(cur_pair[1])
                found = True
            elif right_in:
                circ.append(cur_pair[0])
                found = True
    if not found:
        circuits.append(list(cur_pair))


def redux(i_circs):
    while True:
        index_pairs = list(combinations(range(len(i_circs)), 2))
        new_circuits = i_circs[::]
        for ip in index_pairs:
            m_a = i_circs[ip[0]]
            m_b = i_circs[ip[1]]
            if set(m_a).intersection(set(m_b)):
                new_circuits = []
                left_alone = list(set(range(len(i_circs))).difference({ip[0], ip[1]}))
                mmm = list(set(m_a).union(set(m_b)))
                new_circuits.append(mmm)
                for la in left_alone:
                    new_circuits.append(i_circs[la])
                break
        if i_circs == new_circuits:
            break
        else:
            i_circs = new_circuits[::]
    return i_circs



circuits = redux(circuits)


circ_lens = list(map(len, circuits))
circ_lens.sort(reverse=True)
print(circ_lens[0] * circ_lens[1] * circ_lens[2])


for jp in junction_pairs:
    cur_pair = jp
    found = False
    for circ in circuits:
        if not found:
            left_in = cur_pair[0] in circ
            right_in = cur_pair[1] in circ
            if left_in and right_in:
                found = True
            elif left_in:
                circ.append(cur_pair[1])
                found = True
            elif right_in:
                circ.append(cur_pair[0])
                found = True
    if not found:
        circuits.append(list(cur_pair))



