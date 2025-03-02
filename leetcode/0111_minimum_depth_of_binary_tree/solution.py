from typing import Optional

from tree import TreeNode


def inorder_iter(node: Optional[TreeNode], level: int = 1):
    if node is None:
        return
    yield from inorder_iter(node.left, level + 1)
    yield node, level
    yield from inorder_iter(node.right, level + 1)


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = None
        for node, depth in inorder_iter(root):
            if node.left is None and node.right is None:
                if min_depth is None:
                    min_depth = depth
                min_depth = min(min_depth, depth)
        return min_depth or 0
