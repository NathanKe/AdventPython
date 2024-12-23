from collections import defaultdict
import networkx

connect_lines = open('23_input').read().splitlines()

edge_tuples = list(map(lambda st: tuple(st.split('-')), connect_lines))

connections = defaultdict(lambda: set())

for tu in edge_tuples:
    connections[tu[0]].add(tu[1])
    connections[tu[1]].add(tu[0])


def three_step_chains(i_origin):
    one_steps = list(connections[i_origin])
    out_chains = []
    for one in one_steps:
        two_steps = list(connections[one])
        for two in two_steps:
            three_steps = list(connections[two])
            for three in three_steps:
                out_chains.append([i_origin, one, two, three])

    return out_chains


def len_three_loops(i_origin):
    return set([''.join(sorted(ch[:-1])) for ch in three_step_chains(i_origin) if ch[3] == i_origin])


t_loop_sets = set()
for node in connections.keys():
    if node[0] == 't':
        t_loop_sets.update(len_three_loops(node))

print(len(t_loop_sets))

G = networkx.Graph()
G.add_edges_from(edge_tuples)

print(','.join(sorted([a for a in networkx.enumerate_all_cliques(G)][-1])))
