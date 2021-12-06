data = open('06_input').read().splitlines()[0]


child_tracking_hash = {}


def child_count(days_to_spawn, days_remaining):
    if (days_to_spawn, days_remaining) in child_tracking_hash.keys():
        return child_tracking_hash[(days_to_spawn, days_remaining)]
    elif days_remaining == -1:
        child_tracking_hash[(days_to_spawn, days_remaining)] = 1
        return 1
    elif days_to_spawn >= 0:
        new_days_remaining = days_remaining - days_to_spawn - 1
        return child_count(-1, new_days_remaining)
    else:

        child_one = child_count(6, days_remaining)
        child_two = child_count(8, days_remaining)
        child_tracking_hash[(6, days_remaining)] = child_one
        child_tracking_hash[(8, days_remaining)] = child_two
        return child_one + child_two


# class LanternFish:
#     def __init__(self, in_days_to_spawn, in_days_remaining):
#         self.days_to_spawn = in_days_to_spawn
#         self.days_remaining = in_days_remaining
#
#     def age_one_day(self):
#         self.days_to_spawn -= 1
#         self.days_remaining -= 1
#         return self.days_to_spawn
#
#     def child_count(self):
#         if self.days_remaining == -1:
#             return 1
#         elif self.days_to_spawn >= 0:
#             self.age_one_day()
#             return self.child_count()
#         else:
#             child_one = LanternFish(6, self.days_remaining)
#             child_two = LanternFish(8, self.days_remaining)
#             return child_one.child_count() + child_two.child_count()
#
#
# class LanternSchool:
#     def __init__(self, input_string, in_total_days):
#         self.fish_list = []
#         self.total_days = in_total_days
#         for fish in map(int, input_string.split(',')):
#             self.fish_list.append(LanternFish(fish, in_total_days))
#
#     def total_fish(self):
#         return sum(map(lambda f: f.child_count(), self.fish_list))

total_fish = sum(map(lambda f: child_count(f,80), map(int, data.split(','))))
print("Part 1: ", total_fish())


# school = LanternSchool(data)
# for i in range(256):
#     #print(list(map(lambda x: x.days_to_spawn, school.fish_list)))
#     school.age_school()
# print("Part 1: ", len(school.fish_list))
