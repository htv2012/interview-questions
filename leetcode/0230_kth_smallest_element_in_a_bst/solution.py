from typing import Optional

from tree import TreeNode


def inorder_iter(node: Optional[TreeNode]):
    if node is None:
        return
    yield from inorder_iter(node.left)
    yield node
    yield from inorder_iter(node.right)


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        for count, node in enumerate(inorder_iter(root), 1):
            if count == k:
                return node.val
        raise ValueError()
