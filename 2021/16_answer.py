from collections import deque
from numpy import prod

hex_string = open('16_input').read().splitlines()[0]


def hex_char_bin_four(ch):
    return format(int(ch, 16), '0>4b')


def hex_translate(h):
    return deque(''.join(map(hex_char_bin_four, list(h))))


def function_apply(f_type, sub_vals):
    res = None
    if f_type == 0:
        res = 0
        for v in sub_vals:
            res += v
    elif f_type == 1:
        res = 1
        for v in sub_vals:
            res *= v
    elif f_type == 2:
        res = min(sub_vals)
    elif f_type == 3:
        res = max(sub_vals)
    elif f_type == 5:
        if sub_vals[0] > sub_vals[1]:
            res = 1
        else:
            res = 0
    elif f_type == 6:
        if sub_vals[0] < sub_vals[1]:
            res = 1
        else:
            res = 0
    elif f_type == 7:
        if sub_vals[0] == sub_vals[1]:
            res = 1
        else:
            res = 0
    return res


def parse(packet, version_sum):
    # zero tail case
    if '1' not in packet:
        return '', version_sum, 0

    version = int(''.join([packet.popleft(), packet.popleft(), packet.popleft()]), 2)
    version_sum += version
    type_id = int(''.join([packet.popleft(), packet.popleft(), packet.popleft()]), 2)

    # literal case
    if type_id == 4:
        prefix_index = packet.popleft()
        literal_bin_string = ''
        while prefix_index == '1':
            literal_bin_string += ''.join([packet.popleft(), packet.popleft(), packet.popleft(), packet.popleft()])
            prefix_index = packet.popleft()
        literal_bin_string += ''.join([packet.popleft(), packet.popleft(), packet.popleft(), packet.popleft()])
        literal_int = int(literal_bin_string, 2)
        return packet, version_sum, literal_int

    # get length type
    sub_packet_type = packet.popleft()

    # length case
    if sub_packet_type == '0':
        sub_packet_length = int(''.join([packet.popleft() for _ in range(15)]), 2)
        sub_packet = deque(''.join([packet.popleft() for _ in range(sub_packet_length)]))
        sub_vals = []
        while sub_packet:
            _, version_sum, sub_res = parse(sub_packet, version_sum)
            sub_vals.append(sub_res)
        return packet, version_sum, function_apply(type_id, sub_vals)

    # count case
    if sub_packet_type == '1':
        sub_packet_count = int(''.join([packet.popleft() for _ in range(11)]), 2)
        sub_vals = []
        for i in range(sub_packet_count):
            packet, version_sum, sub_res = parse(packet, version_sum)
            sub_vals.append(sub_res)
        return packet, version_sum, function_apply(type_id, sub_vals)


_, one, two = parse(hex_translate(hex_string), 0)
print("Part 1: ", one)
print("Part 2: ", two)
