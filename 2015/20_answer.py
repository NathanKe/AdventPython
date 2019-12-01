import itertools
import math

target = 36000000


def divisors(n):
    divs = []
    for i in range(1, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.append(i)
            if n // i != i:
                divs.append(n // i)
    return divs


def present_count_1(dvs):
    return sum(map(lambda d: d * 10, dvs))


def present_count_2(house, dvs):
    return sum(map(lambda d: d * 11, filter(lambda di: house // di <= 50, dvs)))


p1, p2 = 0, 0
for h in itertools.count(800000):
    dvs = divisors(h)
    if p1 == 0 and present_count_1(dvs) >= target:
        p1 = h
    if p2 == 0 and present_count_2(h, dvs) >= target:
        p2 = h
    if p1 != 0 and p2 != 0:
        break
    if h % 10000 == 0:
        print(h)

print('Part 1: ', p1)
print('Part 2: ', p2)
