import re

text = """Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
Rudolph can fly 3 km/s for 15 seconds, but then must rest for 28 seconds.
Donner can fly 19 km/s for 9 seconds, but then must rest for 164 seconds.
Blitzen can fly 19 km/s for 9 seconds, but then must rest for 158 seconds.
Comet can fly 13 km/s for 7 seconds, but then must rest for 82 seconds.
Cupid can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Dancer can fly 3 km/s for 16 seconds, but then must rest for 37 seconds.
Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds."""

text_lines = text.splitlines()


def full_cycles(s, time):
    m = re.match(r"(.+?)\s.+?(\d+).+?(\d+).+?(\d+)\sseconds\.", s)
    name, speed, endu, rest = m[1], int(m[2]), int(m[3]), int(m[4])

    cnt = time // (endu + rest)
    rem = time - cnt * (endu + rest)

    return name, speed * endu * cnt + speed * min(endu, rem), time


print('Part 1: ', max(list(map(lambda t: t[1], map(lambda s: full_cycles(s, 2503), text_lines)))))

all_steps = []
for i in range(1, 2504):
    for horse in text_lines:
        all_steps.append(full_cycles(horse, i))


def winning_at_time(time):
    state_at_time = list(filter(lambda tu: tu[2] == time, all_steps))
    max_at_time = max(list(map(lambda tu: tu[1], state_at_time)))
    in_lead_at_time = list(map(lambda tu: tu[0], list(filter(lambda tu: tu[1] == max_at_time, state_at_time))))
    return in_lead_at_time


winner_list = []
for i in range(1, 2504):
    for winner in winning_at_time(i):
        winner_list.append(winner)

max_wins = 0
for horse in list(set(winner_list)):
    cnt = winner_list.count(horse)
    if cnt > max_wins:
        max_wins = cnt

print('Part 2: ', max_wins)
