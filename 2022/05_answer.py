from collections import deque

stack_text, instr_text = map(lambda s: s.split('\n'), open('05_input').read().split('\n\n'))

stack_state_1 = []
stack_state_2 = []
for stack_id in range(0, 11):
    stack_state_1.append(deque())
    stack_state_2.append(deque())

for depth in reversed(range(0, 8)):
    for col_index in range(1, 34, 4):
        stack_id = 1 + col_index // 4
        crate = stack_text[depth][col_index]
        if crate != ' ':
            stack_state_1[stack_id].append(crate)
            stack_state_2[stack_id].append(crate)


for instr in instr_text:
    _, count, _, source, _, dest = instr.split(' ')
    count = int(count)
    source = int(source)
    dest = int(dest)

    stack_to_move = deque()
    for i in range(count):
        stack_state_1[dest].append(stack_state_1[source].pop())
        stack_to_move.appendleft(stack_state_2[source].pop())
    while stack_to_move:
        stack_state_2[dest].append(stack_to_move.popleft())


print("Part 1 ", "".join([stack_state_1[i][-1] for i in range(1, len(stack_state_1) - 1)]))
print("Part 2 ", "".join([stack_state_2[i][-1] for i in range(1, len(stack_state_2) - 1)]))
