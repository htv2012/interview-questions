import collections
from typing import Optional

from tree import TreeNode


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        elif root1 is None:
            return root2
        elif root2 is None:
            return root1

        root3 = TreeNode(None)
        queue = collections.deque([(root1, root2, root3)])

        while queue:
            node1, node2, result = queue.popleft()
            if node1 is None and node2 is None:
                continue
            result.val = node1.val + node2.val

            if node1.left or node2.left:
                result.left = TreeNode(0)
                queue.append(
                    (node1.left or TreeNode(0), node2.left or TreeNode(0), result.left)
                )

            if node1.right or node2.right:
                result.right = TreeNode(0)
                queue.append(
                    (
                        node1.right or TreeNode(0),
                        node2.right or TreeNode(0),
                        result.right,
                    )
                )

        return None if root3.val is None else root3
