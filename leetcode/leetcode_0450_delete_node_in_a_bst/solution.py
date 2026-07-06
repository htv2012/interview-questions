import logging
from typing import Optional

from tree import TreeNode

logger = logging.getLogger()


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


def get_inorder_successor(root: Optional[TreeNode]):
    if root is None:
        return None, None, None

    parent = root
    node = root.right
    side = "right"
    while node and node.left:
        parent = node
        node = parent.left
        side = "left"

    return node, parent, side


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent_of_root = TreeNode(-1, left=root)
        target, parent, side = search(root, key, parent=parent_of_root, side="left")
        logger.debug(f"{target=}, {parent=}, {side=}")
        if target is None:
            return root

        logger.debug(f"{target.left=}, {target.right=}")
        if target.left is None and target.right is None:
            setattr(parent, side, None)
        elif target.right is None:
            setattr(parent, side, target.left)
        elif target.left is None:
            logger.debug(f"{target.left=}, {target.right=}")
            setattr(parent, side, target.right)
        else:
            # succ, succ_parent, succ_side = get_inorder_successor(target)
            pass

        return parent_of_root.left
