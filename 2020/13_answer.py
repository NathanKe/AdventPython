dep_str, bus_str = open('13_input').read().splitlines()

dep = int(dep_str)
bus_ids = list(map(int, filter(lambda s: s.isnumeric(), bus_str.split(','))))

dep_options = sorted(list(map(lambda b: (b * (dep // b + 1) - dep, b), bus_ids)))

print('Part 1: ', dep_options[0][0] * dep_options[0][1])

samp1 = "17,x,13,19"
samp2 = "67,7,59,61"


def get_buses(data_str):
    ord_id_tuples = list(map(
        lambda tu: (tu[0], int(tu[1])),
        filter(lambda tux: tux[1].isnumeric(),
               [(i, data_str.split(',')[i]) for i in range(len(data_str.split(',')))]
               )
    )
    )
    return ord_id_tuples


stamp = 0
jump = 1
bus_ind = 0
bus_ord_id_tuples = get_buses(bus_str)

while True:
    cur_off = bus_ord_id_tuples[bus_ind][0]
    cur_bus = bus_ord_id_tuples[bus_ind][1]
    if (stamp + cur_off) % cur_bus == 0:
        jump *= cur_bus
        bus_ind += 1
        if bus_ind >= len(bus_ord_id_tuples):
            print('Part 2: ', stamp)
            break
    else:
        stamp += jump
