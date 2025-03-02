from typing import Optional

from tree import TreeNode


def inorder_iter(node: Optional[TreeNode]):
    if node is None:
        return
    yield from inorder_iter(node.left)
    yield node
    yield from inorder_iter(node.right)


def gtt(root: Optional[TreeNode], extra: int = 0) -> Optional[TreeNode]:
    if root is None:
        return None

    right_tree = gtt(root.right)
    new_root = TreeNode(root.val + extra, right=right_tree)
    node = right_tree
    while node:
        new_root.val += node.val
        new_root.val -= right_tree.val
        node = node.left

    new_root.left = gtt(root.left, extra=new_root.val)

    return new_root


class Solution:
    def __init__(self):
        self.sum = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        self.convertBST(root.right)
        self.sum += root.val
        root.val = self.sum
        self.convertBST(root.left)
        return root
