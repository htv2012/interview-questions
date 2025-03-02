#!/usr/bin/env python3
# https://leetcode.com/problems/evaluate-division/
import collections
import contextlib
import functools
import operator
from typing import List


def find_path_weight(graph, src, dest):
    if src not in graph:
        return []
    if src == dest:
        return [1.0]

    seen = set()

    def bfs(src, dest):
        nonlocal graph, seen

        with contextlib.suppress(KeyError):
            return [graph[src][dest]]

        seen.add(src)
        for intermediate in graph[src]:
            if intermediate in seen:
                continue
            if found := bfs(intermediate, dest):
                return [graph[src][intermediate]] + found

        return []

    return bfs(src, dest)


def calculate(graph, src, dest):
    if path := find_path_weight(graph, src, dest):
        return functools.reduce(operator.mul, path)
    return -1.0


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        # Create a graph: {'src': {'dest': src/dest}}
        graph = collections.defaultdict(dict)
        for (src, dest), weight in zip(equations, values):
            graph[src][dest] = weight
            graph[dest][src] = 1.0 / weight

        result = [calculate(graph, src, dest) for src, dest in queries]
        return result
