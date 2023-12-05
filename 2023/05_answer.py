import re
from collections import defaultdict

map_sections = open('05_input').read().split('\n\n')


def in_source_range(search_num, source_start, range_length):
    return source_start <= search_num < source_start+range_length


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

# range_bounds = list(zip(seed_numbers[::2], seed_numbers[1::2]))
# unique_seeds = set()
# for rng in range_bounds:
#     for sd in range(rng[0], rng[0] + rng[1]):
#         unique_seeds.add(sd)

#seed_locas_2 = [(seed, seed_to_location(seed)) for seed in unique_seeds]
#seed_locas_2.sort(key=lambda tu: tu[1])
#print(seed_locas_2[0][1])
