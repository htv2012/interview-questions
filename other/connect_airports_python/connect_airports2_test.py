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
BGI,CDG,DEL,DOH,DSM,EWR,EYW,HND,ICN,JFK,LGA,LHR,ORD,SAN,SFO,SIN,TLV,BUD
DSM,ORD
ORD,BGI
BGI,LGA
SIN,CDG
CDG,SIN
CDG,BUD
DEL,DOH
DEL,CDG
TLV,DEL
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
# raw = """
# X
# I,J
# E,I
# A,B
# B,C
# D,E
# D,F
# D,G
# X,H
# """.strip()

lines = iter(raw.splitlines())
hub = next(lines)
reader = csv.reader(lines)
nodes = next(reader)
# data = list(reader)

print(f"Hub: {hub}")
print(f"Airports: {nodes}")
routes = {hub: set()}

# Create a reverse digraph
for start, dest in reader:
    routes.setdefault(start, set())
    routes.setdefault(dest, set()).add(start)
print("Routes:")
pprint(routes)

existing_conn = {dest for dest, src in routes.items() if hub in src}
new_conn = set()
stop_conn = set()
print(f"Existing: {existing_conn}")

for dest, src in routes.items():
    print(f"dest={dest}, src={src}")
    if dest == hub:
        print("  dest is hub, skip")
        continue
    if dest in existing_conn:
        print(f"  dest {dest} in existing_conn {existing_conn}, skip")
        continue
    if dest in new_conn:
        print(f"  dest {dest} in new_conn {new_conn}, skip")
        continue
    if dest in stop_conn:
        print(f"  dest {dest} in stop_conn {stop_conn}, skip")
        continue
    if src:
        stop_conn.add(dest)
        for node in src:
            if not (node in new_conn or node in stop_conn):
                new_conn.add(node)
        print(f"  dest {dest} reachable from {src}, new_conn={new_conn}, stop_conn={stop_conn}")
    else:
        new_conn.add(dest)
        print(f"  dest {dest} not reachable from hub, add to new_conn -> {new_conn}")

print("---")
print(f"existing_conn={existing_conn}")
print(f"new_conn={new_conn}")
print(f"stop_conn={stop_conn}")

# Remove duplicates
new_conn = {
    node
    for node in new_conn
    if not (routes[node].intersection(new_conn))
}

print("---")
print(f"existing_conn={existing_conn}")
print(f"new_conn={new_conn}")
# print(f"stop_conn={stop_conn}")
print(f"The answer is the length of new_conn, {len(new_conn)}")
print("CDG is wrong because TLV -> DEL -> CDG, how can we remove it?")
