from collections import deque

test = [1, 2, -3, 3, -2, 0, 4]


# (orig index, value, current index)

def index_listing(in_list):
    lists = []
    for i in range(len(in_list)):
        lists.append([i, in_list[i], i])
    return lists


def shift_redux(list_len, orig_index, val, current_index):
    # in bounds, it's fine:
    if 0 <= current_index + val < list_len:
        return val
    # goes out of bounds left
    elif current_index + val < 0:
        right_equiv = val % (list_len - 1)
        return shift_redux(list_len, orig_index, right_equiv, current_index)
    elif current_index + val >= list_len:
        left_equiv = val % (-1 * (list_len - 1))
        return shift_redux(list_len, orig_index, left_equiv, current_index)


# ABSOLUTE SPAGHETTI

def mix(in_lists):
    in_lists.sort()
    length = len(in_lists)
    for i in range(length):
        left = deque(in_lists[:i])
        right = deque(in_lists[i + 1:])
        shift = shift_redux(length, *in_lists[i])
        print(in_lists)
        if shift == 0:
            pass
        elif shift < 0:
            new_right = deque()
            new_left = deque()
            while right:
                r = right.popleft()
                if r[2] + 1 >= length:
                    new_left.append(r)
                else:
                    r[2] += 1
                    new_right.append(r)
            for ii in range(len(new_right)):
                left[i][2] += 1
            left = new_left + left
            for ii in range(in_lists[i][1]):
                l_pop = left.pop()
                l_pop[2] += 1
                right.appendleft(l_pop)
            in_lists[i][2] -= shift
            in_lists = list(left) + [in_lists[i][2]] + list(new_right)
        elif shift > 0:
            new_right = deque()
            new_left = deque()
            for ii in range(in_lists[i][1]):
                r_pop = right.popleft()
                r_pop[2] -= 1
                left.append(r_pop)
            while right:
                r = right.popleft()
                if r[2] + 1 >= length:
                    new_left.append(r)
                else:
                    r[2] += 1
                    new_right.append(r)
            for ii in range(len(new_right)):
                left[i][2] += 1
            in_lists[i][2] += shift
            in_lists = list(left) + [in_lists[i]] + list(right)
    print(in_lists)
    return in_lists
