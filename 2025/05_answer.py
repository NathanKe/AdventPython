from collections import defaultdict

i_lines = open('05_input').read().splitlines()

range_strs = []
ingr_strs = []

for line in i_lines:
    if '-' in line:
        range_strs.append(line)
    elif line != "":
        ingr_strs.append(line)



id_dict = defaultdict(lambda: "S")


range_tuples = list(map(lambda s: list(map(int, s.split("-"))), range_strs))


def is_fresh(ingr):
    found_fresh = False
    range_ix = 0
    while not found_fresh:
        if range_ix >= len(range_tuples):
            return False
        elif range_tuples[range_ix][0] <= ingr <= range_tuples[range_ix][1]:
            return True
        else:
            range_ix += 1


print(len([ig for ig in ingr_strs if is_fresh(int(ig))]))



range_tuples.sort(key=lambda tu: tu[1])
fresh_count = 0

while len(range_tuples)>=2:
    high = range_tuples.pop()
    check = range_tuples.pop()

    if high[0] <= check[1] <= high[1]:
        range_tuples.append((min(check[0], high[0]), high[1]))
    else:
        range_tuples.append(check)
        fresh_count += high[1] - high[0] + 1

fresh_count += range_tuples[0][1] - range_tuples[0][0] + 1

print(fresh_count)


