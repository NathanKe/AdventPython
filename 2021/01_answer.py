depths = list(map(int, open('01_input').read().splitlines()))
print("starting")

increases = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        increases += 1

print("Part 1: ", increases)

redux = list(map(lambda x: depths[x]+depths[x+1]+depths[x+2], range(0, len(depths)-2)))
redux_increases = 0
for i in range(1, len(redux)):
    if redux[i] > redux[i-1]:
        redux_increases += 1

print("Part 2: ", redux_increases)
