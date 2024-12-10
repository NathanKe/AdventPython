from itertools import combinations
import random

comp_lines = open('25_input').read().splitlines()

adj = []
for line in comp_lines:
    lh, rh = line.split(': ')
    rhs = rh.split(' ')
    for rr in rhs:
        if lh < rr:
            adj.append((lh, rr))
        else:
            adj.append((rr, lh))


class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
        self.orig_adjacency_list = adjacency_list

    def neighbors(self, i_node):
        out_ngs = []
        for tu in self.adjacency_list:
            if tu[0] == i_node:
                out_ngs.append(tu[1])
            if tu[1] == i_node:
                out_ngs.append(tu[0])
        return out_ngs

    def karger_contract(self):
        rando_edge = random.choice(self.orig_adjacency_list)
        print(rando_edge)
        new_orig = self.orig_adjacency_list[::]
        new_orig.remove(rando_edge)
        matching_node_pair = [a for a in self.adjacency_list if (rando_edge[0] in a[0] and rando_edge[1] in a[1]) or (
                    rando_edge[0] in a[1] and rando_edge[1] in a[0])]
        print(len(self.adjacency_list))
        assert (len(matching_node_pair) == 1)
        left_contractee = matching_node_pair[0][0]
        right_contractee = matching_node_pair[0][1]
        for og_adj in new_orig:
            if (og_adj[0] in left_contractee and og_adj[1] in right_contractee) or (
                    og_adj[1] in left_contractee and og_adj[0] in right_contractee):
                new_orig.remove(og_adj)
        new_node_label = '|'.join([left_contractee, right_contractee])
        new_adj_list = self.adjacency_list[::]
        for c_adj in new_adj_list:
            if c_adj[0] in new_node_label:
                n_c_adj = (new_node_label, c_adj[1])
                new_adj_list.remove(c_adj)
                new_adj_list.append(n_c_adj)
            elif c_adj[1] in new_node_label:
                n_c_adj = (c_adj[0], new_node_label)
                new_adj_list.remove(c_adj)
                new_adj_list.append(n_c_adj)
        print(new_adj_list)
        self.orig_adjacency_list = new_orig
        self.adjacency_list = new_adj_list

    def multi_contract(self):
        while len(self.adjacency_list) >= 1:
            print(len(self.adjacency_list))
            self.karger_contract()
        print(self.adjacency_list)
        assert (len(self.adjacency_list) == 2)
        print(len(self.adjacency_list[0]) / 3 * len(self.adjacency_list[1] / 3))

    def remove_adjacency(self, i_adj_tu):
        assert (i_adj_tu[0] < i_adj_tu[1])
        if i_adj_tu in self.adjacency_list:
            self.adjacency_list.remove(i_adj_tu)
        else:
            return 0

    def bfs(self, i_node):
        frontier = [i_node]
        visited = []
        while frontier:
            cur = frontier.pop()
            visited.append(cur)
            ngs = self.neighbors(i_node)
            for ng in ngs:
                if ng not in visited and ng not in frontier:
                    frontier.append(ng)
        return visited

    # def decompose(self):
    #     sub_graphs = []
    #     unexplored_node_list = set(self.node_list[::])
    #     while unexplored_node_list:
    #         cur = unexplored_node_list.pop()
    #         cur_sub_graph = set(self.bfs(cur))
    #         sub_graphs.append(cur_sub_graph)
    #         unexplored_node_list.difference_update(cur_sub_graph)
    #     return sub_graphs
