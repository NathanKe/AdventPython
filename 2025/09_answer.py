from itertools import combinations


coords = list(map(lambda s: list(map(int, s.split(','))), open('09_input').read().splitlines()))


coordpairs = list(combinations(coords, 2))


def rect_size(co_a, co_b):
    return (abs(co_a[0] - co_b[0]) + 1) * (abs(co_a[1] - co_b[1]) + 1)


coordpairs.sort(key=lambda tu: rect_size(*tu), reverse=True)

print(rect_size(*coordpairs[0]))



