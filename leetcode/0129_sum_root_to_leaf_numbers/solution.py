import collections
from typing import Optional

from tree import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        out = 0
        queue = collections.deque([(root, 0)])

        while queue:
            node, number = queue.popleft()
            if node is None:
                continue

            number = number * 10 + node.val
            if node.left is None and node.right is None:
                out += number

            queue.append((node.left, number))
            queue.append((node.right, number))

        return out
