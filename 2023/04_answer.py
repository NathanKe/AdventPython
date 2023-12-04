import re

card_lines = open('04_input').read().split('\n')

card_data = []
for card_line in card_lines:
    prefix, nums = re.split(r":", card_line)
    card_number = int(re.search(r"(\d+)", prefix).group(1))
    winning_text, assigned_text = re.split(r"\|", nums)
    winning_numbers = list(map(int, re.findall(r"\d+", winning_text)))
    assigned_numbers = list(map(int, re.findall(r"\d+", assigned_text)))
    card_data.append([card_number, 1, winning_numbers, assigned_numbers])


point_sum = 0

for card in card_data:
    cur_ordinal = card[0]
    win_count = len(set(card[2]).intersection(card[3]))
    point_sum += int(2 ** (win_count - 1))
    for j in range(card[1]):
        for i in range(win_count):
            # 1-indexed card numbers and adding to subsequent items in the list cancel out 2 off-by-ones
            card_data[cur_ordinal + i][1] += 1


print(point_sum)
print(sum(map(lambda c: c[1], card_data)))
