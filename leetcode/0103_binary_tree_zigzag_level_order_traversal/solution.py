#!/usr/bin/env python3
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
from typing import List, Optional

from tree import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        queue = [(root, 0)]

        while queue:
            node, level = queue.pop(0)
            if node is None:
                continue

            while len(out) <= level:
                out.append([])

            if level % 2 == 0:
                out[level].append(node.val)
            else:
                out[level].insert(0, node.val)

            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

        return out
