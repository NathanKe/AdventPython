from collections import deque

long_string = open('09_input').read()

disk_map = list(map(int, "2333133121414131402"))  # long_string
# disk_map = list(map(int, long_string))  #long_string

files = [v for (ix, v) in enumerate(disk_map) if ix % 2 == 0]
blanks = deque([v for (ix, v) in enumerate(disk_map) if ix % 2 != 0])

files_count_id = deque(zip(files, range(len(files))))

out_deque = deque()

operation = "FILE"
while files_count_id:
    if operation == "FILE":
        cur_count_id = files_count_id.popleft()
        for i in range(cur_count_id[0]):
            out_deque.append(cur_count_id[1])
        operation = "BLANK"
    elif operation == "BLANK":
        cur_blank_run = blanks.popleft()
        if cur_blank_run > 0:
            end_pull = files_count_id.pop()

            while cur_blank_run > 0:
                if cur_blank_run > end_pull[0] and files_count_id:
                    for i in range(end_pull[0]):
                        out_deque.append(end_pull[1])
                    cur_blank_run -= end_pull[0]
                    end_pull = files_count_id.pop()
                elif cur_blank_run >= end_pull[0]:
                    for i in range(end_pull[0]):
                        out_deque.append(end_pull[1])
                    cur_blank_run = 0
                else:
                    for i in range(cur_blank_run):
                        out_deque.append(end_pull[1])
                    diminished_tail = (end_pull[0] - cur_blank_run, end_pull[1])
                    files_count_id.append(diminished_tail)
                    cur_blank_run = 0
        operation = "FILE"
    else:
        print("Something Went Wrong")

checksum = sum(map(lambda tu: tu[0] * tu[1], enumerate(out_deque)))

print(checksum)

blanks = deque([v for (ix, v) in enumerate(disk_map) if ix % 2 != 0])
files_count_id = deque(zip(files, range(len(files))))

full_list = []
blank_space_avail = 0
operation = "FILE"

while files_count_id:
    cur_count_id = files_count_id.popleft()
    for _ in range(cur_count_id[0]):
        full_list.append(cur_count_id[1])
    if blanks:
        cur_blank_run = blanks.popleft()
        for _ in range(cur_blank_run):
            full_list.append('.')


def ix_of_earliest_blank_run_of_size(i_sz):
    for ix in range(len(full_list) - i_sz):
        if full_list[ix] == '.':
            test_sub = full_list[ix:ix + i_sz]
            if all([x == '.' for x in test_sub]):
                return ix
    return False


search_item = full_list[-1]
search_len = 0

for rev_trav_ix in range(len(full_list))[::-1]:
    if full_list[rev_trav_ix] == search_item:
        search_len += 1
    else:
        space_res = ix_of_earliest_blank_run_of_size(search_len)
        if space_res:
            for swap_ix in range(search_len):
                full_list[space_res + swap_ix] = search_item
                full_list[rev_trav_ix + swap_ix] = '.'

        if full_list[rev_trav_ix] != '.':
            search_item = full_list[rev_trav_ix]
            search_len = 1
