import collections
from typing import List, Optional

from tree import TreeNode


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        queue = collections.deque([(root, tuple())])
        out = []

        while queue:
            node, path = queue.popleft()
            if node is None:
                continue

            path += (str(node.val),)
            if node.left is None and node.right is None:
                out.append("->".join(path))

            queue.append((node.left, path))
            queue.append((node.right, path))

        return out
