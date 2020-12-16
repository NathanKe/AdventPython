from numpy import prod

raw_data = open('16_input').read()

raw_rules, raw_my_ticket, raw_tickets = raw_data.split('\n\n')

rules_text = raw_rules.split('\n')
my_ticket_text = raw_my_ticket.split('\n')[1]
tickets_text = raw_tickets.split('\n')[1:]

rule_info = {}
validity_check_set = set()
for rule in rules_text:
    rule_name, rule_vals = rule.split(': ')
    rule_left, rule_right = rule_vals.split(' or ')
    rule_left_low, rule_left_high = map(int, rule_left.split('-'))
    rule_right_low, rule_right_high = map(int, rule_right.split('-'))

    rule_num_set = set()

    for i in range(rule_left_low, rule_left_high + 1):
        rule_num_set.add(i)
    for i in range(rule_right_low, rule_right_high + 1):
        rule_num_set.add(i)

    rule_info[rule_name] = rule_num_set
    validity_check_set |= rule_num_set

invalid_ticket_sum = 0
good_tickets = []
for tick in tickets_text:
    tick_nums = list(map(int, tick.split(',')))
    tick_diff = set(tick_nums) - validity_check_set
    for err in tick_diff:
        invalid_ticket_sum += err
    if not tick_diff:
        good_tickets.append(tick_nums)

good_transpose = list(map(list, zip(*good_tickets)))

position_rule_map = {}
for position, values in enumerate(good_transpose):
    valid_rules = []
    for rule in rule_info:
        if not set(values) - rule_info[rule]:
            valid_rules.append(rule)
    position_rule_map[position] = valid_rules

print('Part 1: ', invalid_ticket_sum)


def remove_rule(in_rule):
    for c_pos in position_rule_map:
        if len(position_rule_map[c_pos]) >= 2 and in_rule in position_rule_map[c_pos]:
            position_rule_map[c_pos].remove(in_rule)


while max(map(len, position_rule_map.values())) > 1:
    for pos in position_rule_map:
        if len(position_rule_map[pos]) == 1:
            remove_rule(position_rule_map[pos][0])

dept_positions = list(map(lambda tu: tu[0], filter(lambda tu: 'departure' in tu[1][0], position_rule_map.items())))

my_ticket_nums = list(map(int, my_ticket_text.split(',')))
my_dept_nums = [my_ticket_nums[i] for i in dept_positions]

print('Part 2: ', prod(my_dept_nums, dtype='int64'))
