mirror_text = open('16_input').read().splitlines()

# real row
# imag column

mirror_dict = {}

for r_n, r_v in enumerate(mirror_text):
    for c_n, c_v in enumerate(r_v):
        cur_loc = r_n + 1j * c_n
        mirror_dict[cur_loc] = c_v

MAX_COL = max(map(lambda cn: cn.imag, mirror_dict.keys()))
MAX_ROW = max(map(lambda cn: cn.real, mirror_dict.keys()))


# starts should be "outside", that is, value types of:
#
#
def energize_count(start_loc, start_dir):
    energize_dict = {}
    visited = set()
    beams = [(start_loc, start_dir)]
    while beams:
        beam = beams.pop()
        energize_dict[beam[0]] = True
        if beam not in visited:
            visited.add(beam)
            next_beam = (beam[0] + beam[1], beam[1])

            if 0 <= next_beam[0].real <= MAX_ROW and 0 <= next_beam[0].imag <= MAX_COL:
                next_action = mirror_dict[next_beam[0]]
                if next_action == '.':
                    beams.append(next_beam)
                elif next_action == '/':
                    if beam[1].imag:
                        next_beam = (next_beam[0], 1j * next_beam[1])
                    else:
                        next_beam = (next_beam[0], -1j * next_beam[1])
                    beams.append(next_beam)
                elif next_action == '\\':
                    if beam[1].imag:
                        next_beam = (next_beam[0], -1j * next_beam[1])
                    else:
                        next_beam = (next_beam[0], 1j * next_beam[1])
                    beams.append(next_beam)
                elif next_action == '-':
                    if beam[1].imag:
                        # passing through from left to right
                        beams.append(next_beam)
                    else:
                        beams.append((next_beam[0], -1j))
                        beams.append((next_beam[0], 1j))
                elif next_action == '|':
                    if beam[1].real:
                        # passing through from top to bottom
                        beams.append(next_beam)
                    else:
                        beams.append((next_beam[0], 1))
                        beams.append((next_beam[0], -1))
            else:
                # beam off grid, it dies
                pass

    return len([a for a in energize_dict.values() if a]) - 1


print(energize_count(0 - 1j, 1j))

max_energy = 0
for i in range(int(MAX_COL) + 1):
    down_from_top = energize_count(-1 + i * 1j, 1)
    up_from_bottom = energize_count(MAX_ROW + 1 + i * 1j, -1)
    if down_from_top > max_energy:
        max_energy = down_from_top
    if up_from_bottom > max_energy:
        max_energy = - up_from_bottom

for i in range(int(MAX_ROW) + 1):
    right_from_left = energize_count(i - 1j, 1j)
    left_from_right = energize_count(i + 1j * MAX_COL + 1j, -1j)
    if left_from_right > max_energy:
        max_energy = left_from_right
    if right_from_left > max_energy:
        max_energy = right_from_left

print(max_energy)
