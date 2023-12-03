schematic_lines = open('03_input').read().split('\n')

number_locations = []
symbol_adjacent = set()
gear_locations = []


def in_bounds_neighbors(r, c, ROW_MAX, COL_MAX):
    i_b_n = set()
    if c > 0:
        i_b_n.add((r, c - 1))
    if c < COL_MAX:
        i_b_n.add((r, c + 1))

    if r > 0:
        i_b_n.add((r - 1, c))
        if col_num > 0:
            i_b_n.add((r - 1, c - 1))
        if col_num < COL_MAX:
            i_b_n.add((r - 1, c + 1))
    if r < ROW_MAX:
        i_b_n.add((r + 1, c))
        if c > 0:
            i_b_n.add((r + 1, c - 1))
        if c < COL_MAX:
            i_b_n.add((r + 1, c + 1))

    return i_b_n


for row_num, row_val in enumerate(schematic_lines):
    actively_building = False
    number_builder = []
    location_builder = []
    for col_num, col_val in enumerate(row_val):
        if actively_building:
            if col_val in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                number_builder.append(col_val)
                location_builder.append((row_num, col_num))
            else:
                number_locations.append((int(''.join(number_builder)), location_builder))
                actively_building = False
                number_builder = []
                location_builder = []
        else:
            if col_val in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                actively_building = True
                number_builder.append(col_val)
                location_builder.append((row_num, col_num))

        if col_val not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
            neighbors = in_bounds_neighbors(row_num, col_num, len(schematic_lines), len(row_val))
            for n in neighbors:
                symbol_adjacent.add(n)

        if col_val == '*':
            gear_locations.append((row_num, col_num))

    if actively_building:
        number_locations.append((int(''.join(number_builder)), location_builder))

part_sum = 0
for number_loc in number_locations:
    if set(number_loc[1]).intersection(symbol_adjacent):
        part_sum += number_loc[0]

print(part_sum)

ratio_sum = 0
for gear_index, gear_location in enumerate(gear_locations):
    gear_neighbors = in_bounds_neighbors(*gear_location, len(schematic_lines), len(schematic_lines[0]))
    numbers_next_to_gear = set()
    for number_loc in number_locations:
        if set(number_loc[1]).intersection(gear_neighbors):
            numbers_next_to_gear.add(number_loc[0])
    numbers_next_to_gear_list = list(numbers_next_to_gear)
    if len(numbers_next_to_gear_list) == 2:
        ratio_sum += numbers_next_to_gear_list[0] * numbers_next_to_gear_list[1]

print(ratio_sum)
