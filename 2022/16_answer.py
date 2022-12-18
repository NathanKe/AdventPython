import re
from collections import deque

data_lines = open('16_input').read().splitlines()

edges = []
valve_flow_map = {}
adjacency_map = {}
initial_valve_state = {}

for line in data_lines:
    regex_parse = re.match(r"Valve (\w{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)$", line)
    cur_valve = regex_parse.group(1)
    cur_flow = int(regex_parse.group(2))
    cur_connections = regex_parse.group(3).split(", ")
    valve_flow_map[cur_valve] = cur_flow
    for conn in cur_connections:
        if cur_valve in adjacency_map.keys():
            adjacency_map[cur_valve].add(conn)
        else:
            adjacency_map[cur_valve] = {conn}
            initial_valve_state[cur_valve] = "CLOSED"
        edges.append((cur_valve, conn))


def bfs(start, end):
    return bfs_proc(deque([[start]]), end)


def bfs_proc(paths, end):
    while paths:
        path = paths.pop()
        next_steps = adjacency_map[path[-1]]
        if next_steps:
            if end in next_steps:
                path.append(end)
                return path
            else:
                for step in next_steps:
                    if step not in path:
                        n_p = path[:]
                        n_p.append(step)
                        paths.appendleft(n_p)
    return "No Solution"


# cur_loc = 'AA'
# # for room in valve_flow_map.keys():
# #     print(room)
# #     bfs_res = bfs(cur_loc, room)
# #     print(bfs_res)
# #     print((30 - len(bfs_res))*valve_flow_map[room])


class TunnelState:
    def __init__(self, in_steps_remaining, in_valve_state, in_cur_loc, in_wpm, in_tot_flow):
        self.steps_remaining = in_steps_remaining
        self.valve_state = in_valve_state
        self.cur_loc = in_cur_loc
        self.wpm = in_wpm
        self.total_flow_actual = in_tot_flow
        self.theoretic_total_flow = self.calc_theoretic_max_flow()

    def calc_theoretic_max_flow(self):
        decreasing_order_remaining_closed_valve_flows = sorted(
            [valve_flow_map[vi] for vi in self.valve_state if self.valve_state[vi] == "CLOSED"], reverse=True)
        rem_valve_count = len(decreasing_order_remaining_closed_valve_flows)
        theo = 0
        r_steps = self.steps_remaining
        v_ix = 0
        # one step to magically go to next largest valve, one step to open it.
        # remaining steps times corresponding valve flow added to theory
        while r_steps >= 2:
            r_steps -= 2
            if v_ix < rem_valve_count:
                theo += r_steps * decreasing_order_remaining_closed_valve_flows[v_ix]
            v_ix += 1
        return self.total_flow_actual + theo

    def get_child_options(self):
        if self.steps_remaining == 0:
            return []
        elif "CLOSED" not in self.valve_state.values():
            return [TunnelState(self.steps_remaining - 1, self.valve_state, self.cur_loc, self.wpm,
                                self.total_flow_actual + self.wpm)]
        else:
            options = []
            for adj in adjacency_map[self.cur_loc]:
                options.append(TunnelState(self.steps_remaining - 1, self.valve_state, adj, self.wpm,
                                           self.total_flow_actual + self.wpm))
            if self.valve_state[self.cur_loc] == "CLOSED":
                new_valve_state = self.valve_state.copy()
                new_valve_state[self.cur_loc] = "OPEN"
                options.append(TunnelState(self.steps_remaining - 1, new_valve_state, self.cur_loc,
                                           self.wpm + valve_flow_map[self.cur_loc], self.total_flow_actual + self.wpm))
            return options


BEST_KNOWN_TOTAL_FLOW = 0
incomplete_states = deque([TunnelState(30, initial_valve_state, 'AA', 0, 0)])
complete_states = []
while incomplete_states:
    print(len(incomplete_states), BEST_KNOWN_TOTAL_FLOW)
    cur_state = incomplete_states.pop()
    # update best found
    if cur_state.total_flow_actual >= BEST_KNOWN_TOTAL_FLOW:
        BEST_KNOWN_TOTAL_FLOW = cur_state.total_flow_actual

    # prune impossible, prune complete, expand incomplete
    if cur_state.theoretic_total_flow < BEST_KNOWN_TOTAL_FLOW:
        # prune it
        pass
    elif cur_state.steps_remaining == 0:
        complete_states.append(cur_state)
    else:
        child_states = cur_state.get_child_options()
        for child in child_states:
            incomplete_states.append(child)

print("Done!")
# calculate a "theoretical maximum" flow total.  That is, if you could step to the largest remaining closed
# rooms in order and open each - what would your total flow be?
#
# Keep track of a "Largest Known Possible Flow Total".  Prune all branches whose theory is less than this actual
