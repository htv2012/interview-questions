from typing import List, Optional

from tree import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        out = []

        while stack:
            node = stack.pop()
            if node is None:
                continue
            out.append(node.val)
            stack.append(node.right)
            stack.append(node.left)

        return out
