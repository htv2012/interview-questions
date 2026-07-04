from typing import Optional

from tree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def search(root: Optional[TreeNode], key: int, parent, side):
    if root is None:
        return None, parent, side
    elif key == root.val:
        return root, parent, side
    elif key < root.val:
        return search(root.left, key, parent=root, side="left")
    else:
        return search(root.right, key, parent=root, side="right")


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent_of_root = TreeNode(-1, left=root)
        target, parent, side = search(root, key, parent=parent_of_root, side="left")
        if target is None:
            return root

        if target.left is None and target.right is None:
            setattr(parent, side, None)
        elif target.right is None:
            setattr(parent, side, target.left)
        elif target.left is None:
            setattr(parent, side, target.right)

        return parent_of_root.left
