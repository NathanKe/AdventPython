import itertools

containers = list(map(int, """33
14
18
20
45
35
16
35
1
13
18
13
50
44
48
6
24
41
30
42""".splitlines()))

p1 = len(list(filter(lambda tu: sum(tu) == 150, itertools.chain(
    *[list(itertools.combinations(containers, i)) for i in range(1, len(containers) + 1)]))))
print('Part 1: ', p1)

min_container_count = min(map(len, list(filter(lambda tu: sum(tu) == 150, itertools.chain(
    *[list(itertools.combinations(containers, i)) for i in range(1, len(containers) + 1)])))))
p2 = len(list(filter(lambda tu: sum(tu) == 150, list(itertools.combinations(containers, min_container_count)))))
print('Part 2: ', p2)
