manifold_rows = open('07_input').read().splitlines()

start_beam = [ix for (ix, iv) in enumerate(manifold_rows[0]) if iv == "S"][0]

beam_set = set([start_beam])

split_count = 0
for rx in range(len(manifold_rows) -1):
    child_beams = set()
    for b in beam_set:
        if manifold_rows[rx+1][b] == '^':
            child_beams.add(b - 1)
            child_beams.add(b + 1)
            split_count += 1
        else:
            child_beams.add(b)
    beam_set = child_beams


print(split_count)


def step_beam(i_b_c, i_b_r):
    if manifold_rows[i_b_r + 1][i_b_c] == '^':
        return [(i_b_c - 1, i_b_r + 1), (i_b_c + 1, i_b_r + 1)]
    else:
        return [(i_b_c, i_b_r + 1)]

countHash = {}

def sub_beam_count(i_b_c, i_b_r):
    if i_b_r == len(manifold_rows) - 1:
        return 1
    elif (i_b_c, i_b_r) in countHash.keys():
        return countHash[(i_b_c, i_b_r)]
    else:
        sub_res = sum(map(lambda tu: sub_beam_count(*tu), step_beam(i_b_c, i_b_r)))
        countHash[(i_b_c, i_b_r)] = sub_res
        return sub_res

print(sub_beam_count(start_beam, 0))
