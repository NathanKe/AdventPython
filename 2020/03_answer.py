rows = open('03_input').read().splitlines()

cursorHalf = 0
cursor1 = 0
cursor3 = 0
cursor5 = 0
cursor7 = 0
tree_countHalf = 0
tree_count1 = 0
tree_count3 = 0
tree_count5 = 0
tree_count7 = 0

for row in rows:
    if cursorHalf % 1 == 0 and row[int(cursorHalf)] == '#':
        tree_countHalf += 1
    if row[cursor1] == '#':
        tree_count1 += 1
    if row[cursor3] == '#':
        tree_count3 += 1
    if row[cursor5] == '#':
        tree_count5 += 1
    if row[cursor7] == '#':
        tree_count7 += 1

    cursorHalf = (cursorHalf + 0.5) % len(row)
    cursor1 = (cursor1 + 1) % len(row)
    cursor3 = (cursor3 + 3) % len(row)
    cursor5 = (cursor5 + 5) % len(row)
    cursor7 = (cursor7 + 7) % len(row)


print("Part 1: ", tree_count3)
print("Part 2: ", tree_count1 * tree_count3 * tree_count5 * tree_count7 * tree_countHalf)


