from collections import deque

item_assignments = deque([(0, 79), (0, 98), (1, 54), (1, 65), (1, 75), (1, 74), (2, 79), (2, 60), (2, 97), (3, 74)])

m0c = 0
m1c = 0
m2c = 0
m3c = 0

for r in range(10000):
    # monkey 0
    for m in range(len(item_assignments)):
        owner, cur_item = item_assignments.popleft()
        if owner == 0:
            m0c += 1
            nv = (cur_item * 19)
            if nv % 23 == 0:
                item_assignments.append((2, nv % 96577))
            else:
                item_assignments.append((3, nv % 96577))
        else:
            item_assignments.append((owner, cur_item))
    # monkey 1
    for m in range(len(item_assignments)):
        owner, cur_item = item_assignments.popleft()
        if owner == 1:
            m1c += 1
            nv = (cur_item + 6)
            if nv % 19 == 0:
                item_assignments.append((2, nv % 96577))
            else:
                item_assignments.append((0, nv % 96577))
        else:
            item_assignments.append((owner, cur_item))
    # monkey 2
    for m in range(len(item_assignments)):
        owner, cur_item = item_assignments.popleft()
        if owner == 2:
            m2c += 1
            nv = (cur_item * cur_item)
            if nv % 13 == 0:
                item_assignments.append((1, nv % 96577))
            else:
                item_assignments.append((3, nv % 96577))
        else:
            item_assignments.append((owner, cur_item))
    # monkey 3
    for m in range(len(item_assignments)):
        owner, cur_item = item_assignments.popleft()
        if owner == 3:
            m3c += 1
            nv = (cur_item + 3)
            if nv % 17 == 0:
                item_assignments.append((0, nv % 96577))
            else:
                item_assignments.append((1, nv % 96577))
        else:
            item_assignments.append((owner, cur_item))

print(m0c, m1c, m2c, m3c)
