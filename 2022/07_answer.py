from collections import defaultdict
commands = open('07_input').read().splitlines()


class Directory:
    def __init__(self, in_parent):
        self.direct_files = []
        self.child_directory_ids = []
        self.parent_directory_id = in_parent


directory_dict = {'/': Directory(None)}

cur_dir = "/"
for (i, cmd) in enumerate(commands[1:]):
    if cmd[0:4] == "$ cd":
        dir_target = cmd.split(" ")[-1]
        if dir_target == "..":
            cur_dir = directory_dict[cur_dir].parent_directory_id
        else:
            cur_dir = cur_dir + "/" + dir_target

    elif cmd == "$ ls":
        pass
    else:
        left, right = cmd.split(" ")
        if left == "dir":
            new_dir = (cur_dir + "/" + right)
            directory_dict[cur_dir].child_directory_ids.append(new_dir)
            directory_dict[new_dir] = Directory(cur_dir)
        else:
            directory_dict[cur_dir].direct_files.append((right, int(left)))


def directory_size(in_dir):
    direct_file_sizes = sum(map(lambda tu: tu[1], directory_dict[in_dir].direct_files))
    child_directory_sizes = sum(map(directory_size, directory_dict[in_dir].child_directory_ids))
    return direct_file_sizes + child_directory_sizes


dir_sizes = []
for dir_id in directory_dict.keys():
    cur_sum = directory_size(dir_id)
    dir_sizes.append(cur_sum)
dir_sizes.sort()


AVAIL_SIZE = 70000000
SPACE_NEEDED = 30000000

total_size = directory_size("/")

size_to_delete = SPACE_NEEDED - (AVAIL_SIZE - total_size)

print("Part 1: ", sum([size for size in dir_sizes if size < 100000]))
print("Part 2: ", [size for size in dir_sizes if size >= size_to_delete][0])

