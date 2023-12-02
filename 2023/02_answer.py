import re

game_lines = open('02_input').read().split('\n')


def game_tuple(in_round_str):
    r = re.search(r"(\d+)\sred", in_round_str)
    g = re.search(r"(\d+)\sgreen", in_round_str)
    b = re.search(r"(\d+)\sblue", in_round_str)

    if r:
        red = int(r.group(1))
    else:
        red = 0

    if g:
        green = int(g.group(1))
    else:
        green = 0

    if b:
        blue = int(b.group(1))
    else:
        blue = 0

    return red, green, blue


id_sum = 0
criteria_tuple = (12, 13, 14)
games = []
for game_line in game_lines:
    game_id_str, rounds_str = re.split(":", game_line)
    game_id = int(re.search(r"(\d+)", game_id_str).group())

    rounds_strs = re.split(";", rounds_str)
    round_tuples = list(map(lambda r_s: game_tuple(r_s), rounds_strs))

    games.append(round_tuples)

    possible = True
    for round_tuple in round_tuples:
        if not all([round_tuple[0] <= criteria_tuple[0], round_tuple[1] <= criteria_tuple[1],
                    round_tuple[2] <= criteria_tuple[2]]):
            possible = False
            break

    if possible:
        id_sum += game_id

print(id_sum)


def power(in_round_tuples):
    red_max = max([r_t[0] for r_t in in_round_tuples])
    green_max = max([r_t[1] for r_t in in_round_tuples])
    blue_max = max([r_t[2] for r_t in in_round_tuples])
    return red_max * green_max * blue_max


power_sum = 0
for game in games:
    power_sum += power(game)

print(power_sum)
