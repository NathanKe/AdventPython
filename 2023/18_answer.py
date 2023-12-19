from collections import defaultdict

dig_instrs = open('18_input').read().splitlines()

hole_map = defaultdict(lambda: False)
hole_map[0] = True
digger_loc = 0

for dig_instr in dig_instrs:
    dir_t, val_t, hex_t = dig_instr.split(" ")
    val_i = int(val_t)

    for i in range(val_i):
