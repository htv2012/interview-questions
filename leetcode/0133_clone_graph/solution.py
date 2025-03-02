#!/usr/bin/env python3
# https://leetcode.com/problems/clone-graph/description/
from typing import Optional

from graph import Node


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        cloned = {}
        que = [node]
        original = node

        # Clone just the nodes' values. The neighbors still point to the original nodes
        while que:
            node = que.pop(0)
            if node in cloned:
                continue
            cloned[node] = Node(val=node.val, neighbors=node.neighbors)
            que.extend(node.neighbors)

        # Fix up the neighbors
        for node in cloned.values():
            node.neighbors = [cloned[nei] for nei in node.neighbors]

        return cloned[original]
