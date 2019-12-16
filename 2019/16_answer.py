import itertools
import collections

base_pattern = [0, 1, 0, -1]

puzzle = '59773590431003134109950482159532121838468306525505797662142691007448458436452137403459145576019785048254045936039878799638020917071079423147956648674703093863380284510436919245876322537671069460175238260758289779677758607156502756182541996384745654215348868695112673842866530637231316836104267038919188053623233285108493296024499405360652846822183647135517387211423427763892624558122564570237850906637522848547869679849388371816829143878671984148501319022974535527907573180852415741458991594556636064737179148159474282696777168978591036582175134257547127308402793359981996717609700381320355038224906967574434985293948149977643171410237960413164669930'


def pattern(n):
    out = collections.deque([])
    for elem in base_pattern:
        for i in range(n):
            out.append(elem)
    out.rotate(-1)
    return list(out)


def new_signal_place(in_sig, in_place):
    pat = itertools.cycle(pattern(in_place))
    z = list(zip(in_sig, pat))
    sumprod = sum([a * b for a, b in z])
    return abs(sumprod) % 10


def new_signal(in_sig):
    out = []
    for i in range(1, len(in_sig)+1):
        out.append(new_signal_place(in_sig, i))
    return out


def nth_signal_int(in_sig, n):
    for i in range(n):
        in_sig = new_signal(in_sig)
    return in_sig


def nth_signal_string(in_sig_str, n):
    sig_int = list(map(int, list(in_sig_str)))
    return nth_signal_int(sig_int, n)


def first_8_nth_signal_string(in_sig_str, n):
    return ''.join(map(str, nth_signal_string(in_sig_str, n)[0:8]))


def offset_8th_nth_signal_string(in_sig_str, n):
    offset = int(in_sig_str[0:7])
    return ''.join(map(str, nth_signal_string(in_sig_str, n)[offset:offset+8]))


#print('Part 1: ', first_8_nth_signal_string(puzzle, 100))

puzzle_2 = puzzle * 1000
