strategy = open('02_input').read().splitlines()


part_1_hash = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

part_2_hash = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}


print("Part 1: ", sum(map(lambda cur_round:
                          part_1_hash[cur_round],
                          strategy)))

print("Part 2 ", sum(map(lambda cur_round:
                         part_2_hash[cur_round],
                         strategy)))
