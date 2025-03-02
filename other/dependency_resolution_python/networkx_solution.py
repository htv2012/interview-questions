#!/usr/bin/env python
import networkx as nx

# List of (dependence, independence)
# (a , b) means a depends on b
raw_dependency = [
    ('a', 'b'),
    ('a', 'c'),
    ('d', 'e'),
    ('d', 'b'),
    ('b', 'e'),
    ('c', 'e'),
    ('f', 'g'),
]
print 'Raw data:', raw_dependency

# Create a directed graph, which goes from the independence node to the
# dependence node
g = nx.DiGraph()
g.add_edges_from((i, d) for d, i in raw_dependency)

if nx.is_directed_acyclic_graph(g):
    print 'Build order:', nx.topological_sort(g)
else:
    print 'Circular dependency:', list(nx.simple_cycles(g))
