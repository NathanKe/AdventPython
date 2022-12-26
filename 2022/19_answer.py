import re

input_blueprints = open('19_input').read().splitlines()

test_case = "Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian."


def text_parse_starter_bp(bp_line):
    params = list(map(int, re.findall("\d+", bp_line)))
    params.extend([0, 0, 0, 0, 1, 0, 0, 0, 24])
    return params


class BlueprintProcessing:
    def __init__(self, id, ooc, coc, oboc, obcc, goc, gobc, os, cs, obs, gs, oc, cc, obc, gc, tl):
        self.id = id
        self.ore_store = os
        self.clay_store = cs
        self.obs_store = obs
        self.geo_store = gs
        self.ore_bot_count = oc
        self.clay_bot_count = cc
        self.obs_bot_count = obc
        self.geo_bot_count = gc
        self.ore_bot_ore_cost = ooc
        self.clay_bot_ore_cost = coc
        self.obs_bot_ore_cost = oboc
        self.obs_bot_clay_cost = obcc
        self.geo_bot_ore_cost = goc
        self.geo_bot_obs_cost = gobc
        self.time_left = tl
        self.max_ore_per_minute_spend = max(self.ore_bot_ore_cost, self.clay_bot_ore_cost, self.obs_bot_ore_cost,
                                            self.geo_bot_ore_cost)

    def copy(self):
        new_version = BlueprintProcessing(self.id, self.ore_bot_ore_cost, self.clay_bot_ore_cost, self.obs_bot_ore_cost,
                                          self.obs_bot_clay_cost, self.geo_bot_ore_cost, self.geo_bot_obs_cost,
                                          self.ore_store, self.clay_store, self.obs_store, self.geo_store,
                                          self.ore_bot_count, self.clay_bot_count, self.obs_bot_count,
                                          self.geo_bot_count, self.time_left)
        return new_version

    def can_build_ore_bot(self):
        if self.ore_bot_count >= self.max_ore_per_minute_spend:
            return False
        return self.ore_bot_ore_cost <= self.ore_store

    def can_build_clay_bot(self):
        if self.clay_bot_count >= self.obs_bot_clay_cost:
            return False
        return self.clay_bot_ore_cost <= self.ore_store

    def can_build_obs_bot(self):
        if self.obs_bot_count >= self.geo_bot_obs_cost:
            return False
        return self.obs_bot_clay_cost <= self.clay_store and self.obs_bot_ore_cost <= self.ore_store

    def can_build_geo_bot(self):
        return self.geo_bot_obs_cost <= self.obs_store and self.geo_bot_ore_cost <= self.ore_store

    def collect_phase(self):
        self.ore_store += self.ore_bot_count
        self.clay_store += self.clay_bot_count
        self.obs_store += self.obs_bot_count
        self.geo_store += self.geo_bot_count

    def branch(self):

        build_options = ["NONE"]
        if self.can_build_ore_bot():
            build_options.append("ORE")
        if self.can_build_clay_bot():
            build_options.append("CLAY")
        if self.can_build_obs_bot():
            build_options.append("OBS")
        if self.can_build_geo_bot():
            build_options = ["GEO"]

        branches = []
        for build_option in build_options:
            branch = self.copy()
            if build_option == "NONE":
                branch.collect_phase()
                branch.time_left -= 1
                branches.append(branch)
            elif build_option == "ORE":
                branch.ore_store -= branch.ore_bot_ore_cost
                branch.collect_phase()
                branch.ore_bot_count += 1
                branch.time_left -= 1
                branches.append(branch)
            elif build_option == "CLAY":
                branch.ore_store -= branch.clay_bot_ore_cost
                branch.collect_phase()
                branch.clay_bot_count += 1
                branch.time_left -= 1
                branches.append(branch)
            elif build_option == "OBS":
                branch.ore_store -= branch.obs_bot_ore_cost
                branch.clay_store -= branch.obs_bot_clay_cost
                branch.collect_phase()
                branch.obs_bot_count += 1
                branch.time_left -= 1
                branches.append(branch)
            elif build_option == "GEO":
                branch.ore_store -= branch.geo_bot_ore_cost
                branch.obs_store -= branch.geo_bot_obs_cost
                branch.collect_phase()
                branch.geo_bot_count += 1
                branch.time_left -= 1
                branches.append(branch)
        return branches


def triangular(x):
    return (x * (x - 1)) / 2


def find_max_geodes(bp_string):
    params = text_parse_starter_bp(bp_string)

    bp_eval_stack = [BlueprintProcessing(*params)]

    max_geodes = 0

    while bp_eval_stack:
        cur_bp = bp_eval_stack.pop()
        if cur_bp.time_left == 0:
            if cur_bp.id * cur_bp.geo_store > max_geodes:
                max_geodes = cur_bp.id * cur_bp.geo_store
        # triangular number style - "if I build a Geo bot every turn, will I reach the max quality?"
        elif cur_bp.geo_store + cur_bp.geo_bot_count * cur_bp.time_left + triangular(cur_bp.time_left) < max_geodes:
            pass
        else:
            branch_res = cur_bp.branch()
            for b in branch_res:
                bp_eval_stack.append(b)

    return max_geodes


max_qual = 0
for bp in input_blueprints:
    cid = text_parse_starter_bp(bp)[0]
    print(cid)
    cgeo = find_max_geodes(bp)
    print(cid, cgeo)
    if cid * cgeo > max_qual:
        max_qual = cid * cgeo

print("Part 1: ", max_qual)
