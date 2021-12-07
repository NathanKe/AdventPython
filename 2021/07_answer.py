crabs = list(map(int, open('07_input').read().splitlines()[0].split(',')))

lin = lambda fixed_crab: sum(map(lambda crab: abs(crab - fixed_crab), crabs))
tri = lambda fixed_crab: sum(map(lambda crab: abs(crab - fixed_crab)*(abs(crab - fixed_crab)+1)//2, crabs))

print("Part 1: ", min(map(lin, crabs)))
print("Part 2: ", min(map(tri, crabs)))
