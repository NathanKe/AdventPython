import collections

start_nums = [8, 13, 1, 0, 18, 9]

number_history = collections.defaultdict(lambda: [])
for i in range(len(start_nums)):
    number_history[start_nums[i]].append(i+1)


turn_count = len(start_nums) + 1
previous_number = start_nums[-1]

while turn_count <= 30000000:
    if len(number_history[previous_number]) == 1:
        number_history[0].append(turn_count)
        previous_number = 0
    else:
        say = number_history[previous_number][-1] - number_history[previous_number][-2]
        number_history[say].append(turn_count)
        previous_number = say
    if turn_count == 2020:
        print('Part 1: ', previous_number)
    turn_count += 1

print('Part 2: ', previous_number)
