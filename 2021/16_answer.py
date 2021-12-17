hex_string = open('16_input').read().splitlines()[0]


def hex_char_bin_four(ch):
    return format(int(ch, 16), '0>4b')


def hex_translate(h):
    return ''.join(map(hex_char_bin_four, list(h)))


def function_apply(f_type_bin, sub_vals):
    f_type = int(f_type_bin, 2)

    if type(sub_vals) == int:
        sub_vals = [sub_vals]

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


def parse(bin_packet, version_sum, packet_result):
    print(bin_packet, version_sum, packet_result)
    if '1' not in bin_packet:
        return '', version_sum, packet_result
    else:
        v = bin_packet[0:3]
        version_sum += int(v, 2)
        t = bin_packet[3:6]
        if t == '100':
            prefix_index = 6
            literal_val = 0
            while bin_packet[prefix_index] == '1':
                literal_val *= 10
                literal_val += int(bin_packet[prefix_index + 1: prefix_index + 5], 2)
                prefix_index += 5
            literal_val += int(bin_packet[prefix_index + 1: prefix_index + 5])
            bin_packet = bin_packet[prefix_index + 5:]
            packet_result = literal_val
            bin_packet, version_sum, packet_result = parse(bin_packet, version_sum, packet_result)
        else:
            l_i = bin_packet[6]
            # length defined
            if l_i == '0':
                sub_packet_length_bit = bin_packet[7:22]
                sub_packet_length_int = int(sub_packet_length_bit, 2)
                sub_packet_data = bin_packet[22:22 + sub_packet_length_int]
                sub_sum = 0
                sub_packet_results = []
                while sub_packet_data:
                    sub_packet_data, sub_sum, x_res = parse(sub_packet_data, sub_sum, packet_result)
                    sub_packet_results.append(x_res)
                version_sum += sub_sum
                sub_res = [function_apply(t, e) for e in sub_packet_results]
                packet_result = function_apply(t, [packet_result, sub_res])
                bin_packet = bin_packet[22 + sub_packet_length_int:]
                bin_packet, version_sum, packet_result = parse(bin_packet, version_sum, packet_result)
            # count defined
            elif l_i == '1':
                sub_packet_count_bit = bin_packet[7:18]
                sub_packet_count_int = int(sub_packet_count_bit, 2)
                bin_packet = bin_packet[18:]
                sub_packet_results = []
                for i in range(sub_packet_count_int):
                    bin_packet, version_sum, x_res = parse(bin_packet, version_sum, packet_result)
                    sub_packet_results.append(x_res)
                sub_res = [function_apply(t, e) for e in sub_packet_results]
                packet_result = function_apply(t, [packet_result, sub_res])
                bin_packet, version_sum, packet_result = parse(bin_packet, version_sum, packet_result)
        return bin_packet, version_sum, packet_result


a = parse(hex_translate(hex_string), 0, 0)
print("Part 1: ", a)
#print("Part 2: ", res)
