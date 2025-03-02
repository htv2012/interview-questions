import collections
from typing import Optional

from tree import TreeNode


def breadth_first_iter(node: TreeNode, level: int = 0):
    queue = collections.deque([(node, level)])
    while queue:
        node, level = queue.popleft()
        if node is None:
            continue
        yield node, level
        queue.append((node.left, level + 1))
        queue.append((node.right, level + 1))


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        out = None
        last_level = -1

        for node, level in breadth_first_iter(root):
            if level > last_level:
                out = node.val
            last_level = level

        return out
