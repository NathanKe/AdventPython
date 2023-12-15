from collections import deque

rock_text = open('14_input').read().splitlines()
rock_text_1 = open('14_input').read().splitlines()


def shuffle_left(i_str):
    queue = deque(i_str)
    out = []
    dots = []
    ohs = []
    while queue:
        cur = queue.popleft()
        if cur == '#':
            out += ohs
            out += dots
            ohs = []
            dots = []
            out.append(cur)
        elif cur == 'O':
            ohs.append(cur)
        else:
            dots.append(cur)
    out += ohs
    out += dots
    res = ''.join(out)
    assert len(i_str) == len(res)
    return res


def shuffle_right(i_str):
    queue = deque(i_str)
    out = deque()
    dots = []
    ohs = []
    while queue:
        cur = queue.pop()
        if cur == '#':
            [out.appendleft(o) for o in ohs]
            [out.appendleft(d) for d in dots]
            ohs = []
            dots = []
            out.appendleft(cur)
        elif cur == 'O':
            ohs.append(cur)
        else:
            dots.append(cur)
    [out.appendleft(o) for o in ohs]
    [out.appendleft(d) for d in dots]
    res = ''.join(out)
    assert len(i_str) == len(res)
    return res


def shuffle_arr(i_arr, direction):
    o_arr = []
    for row in i_arr:
        if direction == "LEFT":
            o_arr.append(shuffle_left(row))
        else:
            o_arr.append(shuffle_right(row))
    return o_arr


def rotate_ccw(i_arr):
    return list(map(lambda tu: ''.join(tu), list(zip(*i_arr))[::-1]))


def rotate_clock(i_arr):
    return list(map(lambda tu: ''.join(tu), list(zip(*i_arr[::-1]))))


# assume starting North, return in North orientation.
def cycle(i_arr):
    i_arr = rotate_ccw(i_arr)
    i_arr = shuffle_arr(i_arr, "LEFT")
    i_arr = rotate_ccw(i_arr)
    i_arr = shuffle_arr(i_arr, "RIGHT")
    i_arr = rotate_ccw(i_arr)
    i_arr = shuffle_arr(i_arr, "LEFT")
    i_arr = rotate_ccw(i_arr)
    i_arr = shuffle_arr(i_arr, "RIGHT")
    return i_arr


def load_calc(i_arr):
    load = 0
    height = len(i_arr)
    width = len(i_arr[0])
    for row_n in range(height):
        for col_n in range(width):
            if i_arr[row_n][col_n] == 'O':
                load += height - row_n
    return load


print(load_calc(rotate_clock(shuffle_arr(rotate_ccw(rock_text_1), "LEFT"))))

# kind of assuming a few things here:
# once you get somewhere a second time, you'll always repeat the cycle of that same length
#
# general process:
# shuffle and keep track of steps taken to reach each state
# when duplicate state found, cycle length is difference of current steps to get there and initial steps to get there
# lop off by mod a huge chunk of the space
# process the tail end of things
# (shuffles to establish pattern) (shuffles with pattern) (shuffles to close out all steps)
cycle_dict = {}
steps_to_go = 1000000000
steps_completed = 0
cycle_found = False
while steps_to_go > 0:
    rock_text = cycle(rock_text)
    steps_to_go -= 1
    steps_completed += 1
    rock_text_rep = repr(rock_text)
    if cycle_found:
        pass
    else:
        if rock_text_rep in cycle_dict.keys():
            cycle_length = steps_completed - cycle_dict[rock_text_rep]
            steps_to_go = steps_to_go % cycle_length
        else:
            cycle_dict[rock_text_rep] = steps_completed

print(load_calc(rock_text))
