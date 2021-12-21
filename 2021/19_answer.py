raw_data = open('19_input').read().split("\n\n")

scanners = []
for scanner_block in raw_data:
    scanner_lines = scanner_block.splitlines()
    beacons = []
    for line in scanner_lines[1:]:
        x, y, z = list(map(int, line.split(',')))
        beacons.append((x, y, z))
    scanners.append(beacons)


def twenty_four_options(a, b, c, i):
    return [
        (a, b, c),
        (a, c, b),
        (b, a, c),
        (b, c, a),
        (c, a, b),
        (c, b, a),
        (a, b, -c),
        (a, c, -b),
        (b, a, -c),
        (b, c, -a),
        (c, a, -b),
        (c, b, -a),
        (a, -b, -c),
        (a, -c, -b),
        (b, -a, -c),
        (b, -c, -a),
        (c, -a, -b),
        (c, -b, -a),
        (-a, -b, -c),
        (-a, -c, -b),
        (-b, -a, -c),
        (-b, -c, -a),
        (-c, -a, -b),
        (-c, -b, -a)
    ][i]


def get_overlap(fixed_scanner, orientable_scanner):
