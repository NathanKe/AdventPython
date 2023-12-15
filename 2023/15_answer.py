from collections import deque

text = open('15_input').read()

box_dict = {}
for i in range(256):
    box_dict[i] = deque()


def hash_val(i_dq):
    val = 0
    while i_dq:
        cur = i_dq.popleft()
        val += ord(cur)
        val *= 17
        val %= 256
    return val


def proc_dash(i_str):
    label = i_str.split("-")[0]
    i_box = hash_val(deque(label))
    new_lenses = deque()
    old_lenses = box_dict[i_box]
    while old_lenses:
        cur_lens = old_lenses.popleft()
        if cur_lens[0] == label:
            pass
        else:
            new_lenses.append(cur_lens)
    box_dict[i_box] = new_lenses


def proc_eq(i_str):
    label, focal_str = i_str.split("=")
    i_box = hash_val(deque(label))
    focal = int(focal_str)
    label_in_box = False
    for ix, lens in enumerate(box_dict[i_box]):
        if lens[0] == label:
            box_dict[i_box][ix] = (label, focal)
            label_in_box = True
            break
    if not label_in_box:
        box_dict[i_box].append((label, focal))


def proc(i_str):
    if "-" in i_str:
        proc_dash(i_str)
    else:
        proc_eq(i_str)


def box_power(box_num):
    box_sum = 0
    box_num_plus_one = box_num + 1
    for ix, v in enumerate(box_dict[box_num]):
        box_sum += box_num_plus_one * (ix + 1) * (v[1])
    return box_sum


def total_focal():
    total_sum = 0
    for i in box_dict.keys():
        if len(box_dict[i]) > 0:
            total_sum += box_power(i)
    return total_sum


step_deques = map(deque, text.split(","))
print(sum(map(hash_val, step_deques)))


instr_strs = text.split(",")
for instr in instr_strs:
    proc(instr)
print(total_focal())
