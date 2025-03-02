import graph

g = graph.from_adj_list([[2, 4], [1, 3], [2, 4], [1, 3]])
s = graph.serialize(g)
print(s)
