
from tree import TreeNode


def inorder_iter(node: TreeNode | None):
    if node is None:
        return
    yield from inorder_iter(node.left)
    yield node
    yield from inorder_iter(node.right)


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        for count, node in enumerate(inorder_iter(root), 1):
            if count == k:
                return node.val
        raise ValueError()
