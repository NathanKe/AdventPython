data_stream = open('06_input').read()


# assumes such substring exists
def first_n_length_distinct_substring(string, n):
    for i in range(len(string)):
        if len(set(string[i:i + n])) == n:
            return i + n


print("Part 1: ", first_n_length_distinct_substring(data_stream, 4))
print("Part 1: ", first_n_length_distinct_substring(data_stream, 14))

# less readable, but maybe faster single loop version
# p1found = False
# for i in range(0, len(data_stream)):
#    if not p1found and len(set(data_stream[i:i+4])) == 4:
#        print("Part 1: ", i + 4)
#        p1found = True
#    if len(set(data_stream[i:i + 14])) == 14:
#        print("Part 2: ", i + 14)
#        break
