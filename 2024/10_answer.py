from collections import defaultdict
from collections import deque

grid_lines = open('10_input').read().splitlines()

grid_dict = defaultdict(lambda: -1)

for ri, rv in enumerate(grid_lines):
    for ci, cv in enumerate(rv):
        grid_dict[ri + 1j * ci] = cv


def path_expand(i_path):
    head = i_path[-1]
    head_height = int(grid_dict[head])
    frontier = [head + d for d in [1, -1, 1j, -1j] if grid_dict[head+d] != '.' and int(grid_dict[head+d]) - 1 == head_height]
    out_paths = []
    for f in frontier:
        np = i_path[::]
        np.append(f)
        out_paths.append(np)
    return out_paths


path_deque = deque([[k] for k, v in grid_dict.items() if v == "0"])


completed_paths = []

while path_deque:
    c_path = path_deque.popleft()
    if grid_dict[c_path[-1]] == "9":
        completed_paths.append(c_path)
    else:
        exp_paths = path_expand(c_path)
        if len(exp_paths) == 0:
            pass # dead end, no expansion, drop from to-do queue
        else:
            for ep in exp_paths:
                path_deque.append(ep)


print(len(set([(p[0], p[-1]) for p in completed_paths])))


print(len(completed_paths))
