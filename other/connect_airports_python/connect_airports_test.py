#!/usr/bin/env python3
"""
# Problem

Given: 

- A list of airport codes, e.g. DSM, ORD, BGI, LGA ...
- A list of one-way connections: [[DSN, ORD], [ORD, BGI]]
- A starting airport, e.g. LGA

We want to be able to travel from the start airport to any of the
airports in the list. What is the minimum number of new connections
we have to create for this to happen?

# Discussion

First, we need to discuss the data structure to express the problem.
The most natural structure is a directed graph or a digraph. Since
most interviewers don't allow to use packages such as networkx, we
are going to use a dictionary to represent a graph. Each key will
represent an airport, and each value will represent a list of
destination airports.
"""
import collections
import csv
from pprint import pprint

raw = """
LGA
DSM,ORD
ORD,BGI
BGI,LGA
SIN,CDG
CDG,SIN
CDG,BUD
TLV,DEL
DEL,DOH
EWR,HND
HND,ICN
HND,JFK
ICN,JFK
JFK,LGA
EYW,LHR
LHR,SFO
SFO,SAN
SFO,DSM
SAN,EYW
""".strip()
raw = """
X
A,B
B,C
D,E
D,F
D,G
""".strip()

lines = iter(raw.splitlines())
hub = next(lines)
data = list(csv.reader(lines))

print(f"Hub: {hub}")
routes = {hub: set()}
for start, dest in data:
    routes.setdefault(start, set()).add(dest)
    routes.setdefault(dest, set())
print("Routes:")
pprint(routes)

# Calculate the existing coverage. A coverage is a set of destinations
# which the hub can reach
coverage = set()
queue = routes[hub].copy()
while queue:
    node = queue.pop()
    if node in coverage:
        continue
    coverage.add(node)
    queue.update(routes[node])
print(f"Original coverage: {coverage}")


# Add connections
new_connections = set()
count = 0
for node, dest in routes.items():
    if node == hub or node in coverage or node in new_connections:
        continue
    # coverage.add(node)
    new_connections.add(node)
    count += 1
    print(f"node: {node}, dest: {dest}, count: {count}")
    for subnode in dest:
        print(f"  subnode: {subnode}, new_connections: {new_connections}")
        new_connections.add(subnode)
        if subnode in coverage:
            count -= 1
    print(f"node: {node}, dest: {dest}, count: {count}")
    print()

print(f"New connections: {new_connections}, {count}")
