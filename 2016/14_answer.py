import re
import hashlib

puzzle = 'cuanljph'

pre_hashed = {}
pre_hashed_stretch = {}


def md5_hash(s):
    return hashlib.md5(s.encode()).hexdigest()


def md5_hash_stretch(s):
    for i in range(2017):
        s = hashlib.md5(s.encode()).hexdigest()
    return s


def check_next_thousand(p_i, p_ch, p_puz):
    found = False
    for j in range(p_i + 1, p_i + 1001):
        if j not in pre_hashed.keys():
            cur_hash = md5_hash(p_puz + str(j))
            pre_hashed[j] = cur_hash
        cur_hash = pre_hashed[j]
        match_five = re.search(r"((" + p_ch + r")\2\2\2\2)", cur_hash)
        if match_five:
            found = True
            break
    return found


def check_next_thousand_stretch(p_i, p_ch, p_puz):
    found = False
    for j in range(p_i + 1, p_i + 1001):
        if j not in pre_hashed_stretch.keys():
            cur_hash = md5_hash_stretch(p_puz + str(j))
            pre_hashed_stretch[j] = cur_hash
        cur_hash = pre_hashed_stretch[j]
        match_five = re.search(r"((" + p_ch + r")\2\2\2\2)", cur_hash)
        if match_five:
            found = True
            break
    return found


def sixty_fourth_key(p_puz):
    pad_keys = []
    i = 0
    while len(pad_keys) < 64:
        c_h = md5_hash(p_puz + str(i))
        pre_hashed[i] = c_h
        match_three = re.search(r"((.)\2\2)", c_h)
        if match_three:
            if check_next_thousand(i, match_three.groups()[1], p_puz):
                pad_keys.append(i)
        i += 1
    return pad_keys[-1]


def sixty_fourth_key_stretch(p_puz):
    pad_keys = []
    i = 0
    while len(pad_keys) < 64:
        c_h = md5_hash_stretch(p_puz + str(i))
        pre_hashed_stretch[i] = c_h
        match_three = re.search(r"((.)\2\2)", c_h)
        if match_three:
            if check_next_thousand_stretch(i, match_three.groups()[1], p_puz):
                pad_keys.append(i)
        i += 1
    return pad_keys[-1]


print('Part 1: ', sixty_fourth_key(puzzle))
print('Part 2: ', sixty_fourth_key_stretch(puzzle))
