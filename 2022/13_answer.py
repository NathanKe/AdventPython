packet_pairs = [(eval(a), eval(b)) for a, b in map(lambda s: s.splitlines(), open('13_input').read().split("\n\n"))]


def packet_compare(left, right):
    # left ran out, right still non empty
    if not left and not right:
        return "WTF?!"
    if not left and right:
        return "SHORT_CIRCUIT_TRUE"
    if left and not right:
        return "SHORT_CIRCUIT_FALSE"
    else:
        left_type = type(left)
        right_type = type(right)
        if left_type == int and right_type == int:
            if left < right:
                return "SHORT_CIRCUIT_TRUE"
            elif right < left:
                return "SHORT_CIRCUIT_FALSE"
            else:
                return "INDETERMINATE"
        elif left_type == list and right_type == list:
            len_left = len(left)
            len_right = len(right)
            min_len = min(len_left, len_right)
            for ix in range(min_len):
                recur_res = packet_compare(left[ix], right[ix])
                if recur_res == "SHORT_CIRCUIT_TRUE" or recur_res == "SHORT_CIRCUIT_FALSE":
                    return recur_res
            # all common items passed, so check who is longer
            if len_left > len_right:
                # right ran out first
                return "SHORT_CIRCUIT_FALSE"
            elif len_right > len_left:
                # left ran out first
                return "SHORT_CIRCUIT_TRUE"
            else:
                return "HOPELESSLY INDETERMINATE"
        else:
            if left_type == int:
                left = [left]
            else:
                right = [right]
            return packet_compare(left, right)


correct_order_index_sum = 0
for ix, cur_pair in enumerate(packet_pairs):
    if packet_compare(*cur_pair) == "SHORT_CIRCUIT_TRUE":
        correct_order_index_sum += (ix + 1)

print("Part 1: ", correct_order_index_sum)


flat_packets = [eval(a) for a in open('13_input').read().splitlines() if a]
flat_packets.append([[2]])
flat_packets.append([[6]])

ordered = False
while not ordered:
    ordered = True
    for ix in range(len(flat_packets) - 1):
        cur_ord_res = packet_compare(flat_packets[ix], flat_packets[ix + 1])
        if cur_ord_res == "SHORT_CIRCUIT_FALSE":
            ordered = False
            temp = flat_packets[ix]
            flat_packets[ix] = flat_packets[ix + 1]
            flat_packets[ix + 1] = temp

decoder_key = (flat_packets.index([[2]]) + 1) * (flat_packets.index([[6]]) + 1)
print("Part 2: ", decoder_key)
