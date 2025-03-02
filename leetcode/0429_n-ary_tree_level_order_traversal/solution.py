import collections
from typing import List

from nary_tree import Node


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        queue = collections.deque()
        queue.append((root, 0))
        out = []

        while queue:
            node, level = queue.popleft()
            if node is None:
                continue

            # Pad the output
            while len(out) <= level:
                out.append([])

            # Process this node
            out[level].append(node.val)

            # Enqueue the children
            for child in node.children or []:
                queue.append((child, level + 1))

        return out
