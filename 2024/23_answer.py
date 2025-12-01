import networkx

G = networkx.Graph(map(lambda st: tuple(st.split('-')), open('23_input').read().splitlines()))
print(len([a for a in networkx.enumerate_all_cliques(G) if len(a) == 3 and any([n[0] == 't' for n in a])]))
print(','.join(sorted([a for a in networkx.enumerate_all_cliques(G)][-1])))
