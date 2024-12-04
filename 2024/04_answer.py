from collections import defaultdict

grid_lines = open('04_input').read().split('\n')

grid_dict = defaultdict(lambda: "-")

for ri, rv in enumerate(grid_lines):
    for ci, cv in enumerate(rv):
        grid_dict[ri + ci * 1j] = cv

MAXROW = len(grid_lines)
MAXCOL = len(grid_lines[0])

xmas_count = 0
ecksmas_count = 0

for ri in range(MAXROW):
    for ci in range(MAXCOL):
        north = [grid_dict[(ri - 0) + (ci + 0) * 1j],
                 grid_dict[(ri - 1) + (ci + 0) * 1j],
                 grid_dict[(ri - 2) + (ci + 0) * 1j],
                 grid_dict[(ri - 3) + (ci + 0) * 1j]]
        north_east = [grid_dict[(ri - 0) + (ci + 0) * 1j],
                      grid_dict[(ri - 1) + (ci + 1) * 1j],
                      grid_dict[(ri - 2) + (ci + 2) * 1j],
                      grid_dict[(ri - 3) + (ci + 3) * 1j]]
        east = [grid_dict[(ri - 0) + (ci + 0) * 1j],
                grid_dict[(ri - 0) + (ci + 1) * 1j],
                grid_dict[(ri - 0) + (ci + 2) * 1j],
                grid_dict[(ri - 0) + (ci + 3) * 1j]]
        south_east = [grid_dict[(ri + 0) + (ci + 0) * 1j],
                      grid_dict[(ri + 1) + (ci + 1) * 1j],
                      grid_dict[(ri + 2) + (ci + 2) * 1j],
                      grid_dict[(ri + 3) + (ci + 3) * 1j]]
        south = [grid_dict[(ri + 0) + (ci + 0) * 1j],
                 grid_dict[(ri + 1) + (ci + 0) * 1j],
                 grid_dict[(ri + 2) + (ci + 0) * 1j],
                 grid_dict[(ri + 3) + (ci + 0) * 1j]]
        south_west = [grid_dict[(ri + 0) + (ci + 0) * 1j],
                      grid_dict[(ri + 1) + (ci - 1) * 1j],
                      grid_dict[(ri + 2) + (ci - 2) * 1j],
                      grid_dict[(ri + 3) + (ci - 3) * 1j]]
        west = [grid_dict[(ri - 0) + (ci + 0) * 1j],
                grid_dict[(ri - 0) + (ci - 1) * 1j],
                grid_dict[(ri - 0) + (ci - 2) * 1j],
                grid_dict[(ri - 0) + (ci - 3) * 1j]]
        north_west = [grid_dict[(ri - 0) + (ci + 0) * 1j],
                      grid_dict[(ri - 1) + (ci - 1) * 1j],
                      grid_dict[(ri - 2) + (ci - 2) * 1j],
                      grid_dict[(ri - 3) + (ci - 3) * 1j]]

        finds = ["".join(north),
                 "".join(north_east),
                 "".join(east),
                 "".join(south_east),
                 "".join(south),
                 "".join(south_west),
                 "".join(west),
                 "".join(north_west)]

        for f in finds:
            if f == "XMAS":
                xmas_count += 1

        m_top = [grid_dict[(ri-1)+(ci-1) * 1j] == 'M',
                 grid_dict[(ri-1)+(ci+1) * 1j] == 'M',
                 grid_dict[(ri+1)+(ci-1) * 1j] == 'S',
                 grid_dict[(ri+1)+(ci+1) * 1j] == 'S',
                 grid_dict[ri+ci * 1j] == 'A']

        m_rgt = [grid_dict[(ri - 1) + (ci - 1) * 1j] == 'S',
                 grid_dict[(ri - 1) + (ci + 1) * 1j] == 'M',
                 grid_dict[(ri + 1) + (ci - 1) * 1j] == 'S',
                 grid_dict[(ri + 1) + (ci + 1) * 1j] == 'M',
                 grid_dict[ri + ci * 1j] == 'A']

        m_bot = [grid_dict[(ri - 1) + (ci - 1) * 1j] == 'S',
                 grid_dict[(ri - 1) + (ci + 1) * 1j] == 'S',
                 grid_dict[(ri + 1) + (ci - 1) * 1j] == 'M',
                 grid_dict[(ri + 1) + (ci + 1) * 1j] == 'M',
                 grid_dict[ri + ci * 1j] == 'A']

        m_lft = [grid_dict[(ri - 1) + (ci - 1) * 1j] == 'M',
                 grid_dict[(ri - 1) + (ci + 1) * 1j] == 'S',
                 grid_dict[(ri + 1) + (ci - 1) * 1j] == 'M',
                 grid_dict[(ri + 1) + (ci + 1) * 1j] == 'S',
                 grid_dict[ri + ci * 1j] == 'A']
        if all(m_top) or all(m_bot) or all(m_rgt) or all(m_lft):
            ecksmas_count += 1




print(xmas_count)
print(ecksmas_count)




