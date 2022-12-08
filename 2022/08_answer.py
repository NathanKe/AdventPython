grid_lines = open('08_input').read().splitlines()

GRID_WIDTH = len(grid_lines[0])
GRID_HEIGHT = len(grid_lines)

forest_dict = {}

# real is row, imaginary is complex

for r in range(GRID_HEIGHT):
    for c in range(GRID_WIDTH):
        forest_dict[complex(r, c)] = int(grid_lines[r][c])


def cardinal_ranges(row, col):
    north = [complex(a, col) for a in range(0, row)]
    south = [complex(a, col) for a in range(row + 1, GRID_HEIGHT)]
    west = [complex(row, b) for b in range(0, col)]
    east = [complex(row, b) for b in range(col + 1, GRID_WIDTH)]
    return [north, south, east, west]


def can_be_seen_from_edge(row, col):
    cur_val = forest_dict[complex(row, col)]
    north, south, east, west = cardinal_ranges(row, col)
    vis_from_north = all([forest_dict[z] < cur_val for z in north])
    vis_from_south = all([forest_dict[z] < cur_val for z in south])
    vis_from_west = all([forest_dict[z] < cur_val for z in west])
    vis_from_east = all([forest_dict[z] < cur_val for z in east])
    return any([vis_from_north, vis_from_south, vis_from_east, vis_from_west])


# assumes list non empty
def sightline_builder(ordered_list, check_val):
    out_visibles = []
    while ordered_list:
        next_tree = ordered_list.pop()
        out_visibles.append(next_tree)
        if forest_dict[next_tree] >= check_val:
            break
    return out_visibles


def scenic_score(row, col):
    cur_val = forest_dict[complex(row, col)]
    north, south, east, west = cardinal_ranges(row, col)

    # we pop from these lists, so for south (up) and east (left) we reverse to work the other direction
    south.reverse()
    east.reverse()

    if len(north) == 0 or len(south) == 0 or len(east) == 0 or len(west) == 0:
        return 0

    north_visibles = sightline_builder(north, cur_val)
    south_visibles = sightline_builder(south, cur_val)
    east_visibles = sightline_builder(east, cur_val)
    west_visibles = sightline_builder(west, cur_val)

    return len(north_visibles) * len(south_visibles) * len(east_visibles) * len(west_visibles)


total_vis_count = 0
best_scenic_score = 0
for r in range(GRID_HEIGHT):
    for c in range(GRID_WIDTH):
        if can_be_seen_from_edge(r, c):
            total_vis_count += 1
        cur_scenic_score = scenic_score(r, c)
        if cur_scenic_score > best_scenic_score:
            best_scenic_score = cur_scenic_score

print("Part 1: ", total_vis_count)
print("Part 2: ", best_scenic_score)
