school = list(map(int, (open('06_input').read().splitlines()[0]).split(',')))
six_hash = {}
eight_hash = {}


def descent_count(time_to_spawn, days_remaining):
    if days_remaining <= time_to_spawn:
        return 1
    else:
        x = days_remaining - time_to_spawn - 1
        if x in six_hash.keys():
            a = six_hash[x]
        else:
            a = descent_count(6, x)
            six_hash[x] = a
        if x in eight_hash.keys():
            b = eight_hash[x]
        else:
            b = descent_count(8, x)
            eight_hash[x] = b
        return a+b


print("Part 1: ", sum(map(lambda fish: descent_count(fish, 80), school)))
print("Part 2: ", sum(map(lambda fish: descent_count(fish, 256), school)))
