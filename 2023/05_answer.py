import re
from collections import defaultdict
from itertools import chain

map_sections = open('05_input').read().split('\n\n')


def in_source_range(search_num, source_start, range_length):
    return source_start <= search_num < source_start + range_length


def source_to_dest(search_num, list_of_range_tuples):
    for range_tuple in list_of_range_tuples:
        if in_source_range(search_num, range_tuple[1], range_tuple[2]):
            return range_tuple[0] + search_num - range_tuple[1]
    return search_num


def text_num_block_to_tuples(text_num_block):
    out_tuples = []
    for line in text_num_block:
        cur_tuple = tuple(list(map(int, re.findall(r"\d+", line))))
        out_tuples.append(cur_tuple)
    return out_tuples


seed_numbers = list(map(int, re.findall(r"\d+", map_sections[0])))
seed_to_soil = text_num_block_to_tuples(map_sections[1].splitlines()[1:])
soil_to_fertilizer = text_num_block_to_tuples(map_sections[2].splitlines()[1:])
fertilizer_to_water = text_num_block_to_tuples(map_sections[3].splitlines()[1:])
water_to_light = text_num_block_to_tuples(map_sections[4].splitlines()[1:])
light_to_temperature = text_num_block_to_tuples(map_sections[5].splitlines()[1:])
temperature_to_humidity = text_num_block_to_tuples(map_sections[6].splitlines()[1:])
humidity_to_location = text_num_block_to_tuples(map_sections[7].splitlines()[1:])


def seed_to_location(seed):
    soil = source_to_dest(seed, seed_to_soil)
    fert = source_to_dest(soil, soil_to_fertilizer)
    wate = source_to_dest(fert, fertilizer_to_water)
    ligt = source_to_dest(wate, water_to_light)
    temp = source_to_dest(ligt, light_to_temperature)
    humd = source_to_dest(temp, temperature_to_humidity)
    loca = source_to_dest(humd, humidity_to_location)
    return loca


seed_locas = [(seed, seed_to_location(seed)) for seed in seed_numbers]
seed_locas.sort(key=lambda tu: tu[1])
print(seed_locas[0][1])

seed_to_soil.sort(key=lambda tu: tu[1])
soil_to_fertilizer.sort(key=lambda tu: tu[1])
fertilizer_to_water.sort(key=lambda tu: tu[1])
water_to_light.sort(key=lambda tu: tu[1])
light_to_temperature.sort(key=lambda tu: tu[1])
temperature_to_humidity.sort(key=lambda tu: tu[1])
humidity_to_location.sort(key=lambda tu: tu[1])

seed_zip = list(zip(seed_numbers[::2], seed_numbers[1::2]))
nothing_to_seed = list(map(lambda tu: (0, tu[0], tu[1]), seed_zip))

map_depth_chart = [nothing_to_seed, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light,
                   light_to_temperature, temperature_to_humidity, humidity_to_location]


def split_forward(depth, start, length):
    next_data = map_depth_chart[depth + 1]
    out_ranges = []
    tup_ind = 0
    while length:
        # beyond next data, push through unchanged
        if tup_ind >= len(next_data):
            out_ranges.append((depth + 1, start, length))
            length = 0
        else:
            next_dest_start = next_data[tup_ind][0]
            next_start = next_data[tup_ind][1]
            next_length = next_data[tup_ind][2]

            # underlaps left
            if start < next_start:
                # complete underlap, push through unchanged
                if start + length <= next_start:
                    out_ranges.append((depth + 1, start, length))
                    length = 0
                # partial underlap, push through partial
                else:
                    used_length = next_start - start

                    out_ranges.append((depth + 1, start, used_length))
                    length -= used_length
                    start += used_length
            # beyond right
            elif start >= next_start + next_length:
                tup_ind += 1
            # full contain
            elif start >= next_start and start + length <= next_start + next_length:
                offset = start - next_start
                # consumed
                out_ranges.append((depth + 1, next_dest_start + offset, length))
                length = 0
            # consume partial
            else:
                used_length = next_start + next_length - start
                offset = start - next_start
                out_ranges.append((depth + 1, next_dest_start + offset, used_length))

                length -= used_length
                start += used_length
                tup_ind += 1

    return out_ranges


soil_ranges = list(chain(*map(lambda rng: split_forward(*rng), nothing_to_seed)))
fert_ranges = list(chain(*map(lambda rng: split_forward(*rng), soil_ranges)))
wate_ranges = list(chain(*map(lambda rng: split_forward(*rng), fert_ranges)))
ligt_ranges = list(chain(*map(lambda rng: split_forward(*rng), wate_ranges)))
temp_ranges = list(chain(*map(lambda rng: split_forward(*rng), ligt_ranges)))
humd_ranges = list(chain(*map(lambda rng: split_forward(*rng), temp_ranges)))
loca_ranges = list(chain(*map(lambda rng: split_forward(*rng), humd_ranges)))

print(min(map(lambda tu: tu[1], loca_ranges)))
