import functools

avail_text, _, *targets = open('19_input').read().splitlines()

avail = avail_text.split(', ')


@functools.lru_cache()
def towel_is_possible(i_head, i_tail):
    if i_head == "":
        if i_tail in avail:
            return True
        else:
            sub_tails = [(i_tail[:i], i_tail[i:]) for i in range(1, len(i_tail))]
            return any(map(lambda tu: towel_is_possible(tu[0], tu[1]), sub_tails))
    else:
        if i_head in avail:
            return towel_is_possible("", i_tail)


print(sum(list(map(lambda tg: towel_is_possible("", tg), targets))))


@functools.lru_cache()
def towel_poss_count(i_head, i_tail):
    if not towel_is_possible(i_head, i_tail):
        return 0
    elif i_head == "":
        sub_tails = [(i_tail[:i], i_tail[i:]) for i in range(1, len(i_tail))]
        sub_posses = sum(map(lambda tu: towel_poss_count(tu[0], tu[1]), sub_tails))
        if i_tail in avail:
            return 1 + sub_posses
        else:
            return sub_posses
    else:
        if i_head in avail:
            return towel_poss_count("", i_tail)
        else:
            return 0


print(sum(list(map(lambda tg: towel_poss_count("", tg), targets))))
