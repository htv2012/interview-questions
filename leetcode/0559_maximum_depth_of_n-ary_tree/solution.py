from queue import SimpleQueue

from nary_tree import Node


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if root is None:
            return 0
        max_depth = 1
        queue = SimpleQueue()
        queue.put((root, 1))

        while not queue.empty():
            node, depth = queue.get()
            max_depth = max(max_depth, depth)
            for child in node.children or []:
                queue.put((child, depth + 1))

        return max_depth
