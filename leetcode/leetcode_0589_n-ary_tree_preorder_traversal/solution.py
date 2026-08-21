import collections

from nary_tree import Node


class Solution:
    def preorder(self, root: "Node") -> list[int]:
        if root is None:
            return

        queue = collections.deque()
        queue.append(root)
        out = []

        while queue:
            node = queue.popleft()
            out.append(node.val)
            queue.extendleft(reversed(node.children or []))

        return out
