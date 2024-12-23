import networkx as nx

connect_lines = open('23_input').read().splitlines()

edge_tuples = list(map(lambda st: tuple(st.split('-')), connect_lines))

G = nx.Graph()

G.
