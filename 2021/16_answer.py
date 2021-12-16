hex_string = open('16_input').read().splitlines()[0]


def hex_char_bin_four(ch):
    return format(int(ch, 16), '0>4b')


def hex_translate(h):
    return ''.join(map(hex_char_bin_four, list(h)))


def parse(bin_packet, version_sum):
    if '1' not in bin_packet:
        return '', version_sum
    else:
        v = bin_packet[0:3]
        version_sum += int(v, 2)
        t = bin_packet[3:6]
        if t == '100':
            prefix_index = 6
            literal_bin_string = ''
            while bin_packet[prefix_index] == '1':
                literal_bin_string += bin_packet[prefix_index + 1: prefix_index + 5]
                prefix_index += 5
            literal_bin_string += bin_packet[prefix_index + 1: prefix_index + 5]
            bin_packet = bin_packet[prefix_index + 5:]
        else:
            l_i = bin_packet[6]
            if l_i == '0':
                sub_packet_length_bit = bin_packet[7:22]
                sub_packet_length_int = int(sub_packet_length_bit, 2)
                sub_packet_data = bin_packet[22:22 + sub_packet_length_int]
                sub_sum = 0
                while sub_packet_data:
                    sub_packet_data, sub_sum = parse(sub_packet_data, sub_sum)
                version_sum += sub_sum
                bin_packet = bin_packet[22 + sub_packet_length_int:]
            elif l_i == '1':
                sub_packet_count_bit = bin_packet[7:18]
                sub_packet_count_int = int(sub_packet_count_bit, 2)
                bin_packet = bin_packet[18:]
                for i in range(sub_packet_count_int):
                    bin_packet, version_sum = parse(bin_packet, version_sum)
        bin_packet, version_sum = parse(bin_packet, version_sum)
        return bin_packet, version_sum


print("Part 1: ", parse(hex_translate(hex_string), 0)[1])
