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
            # by definition, the successor might has right child, but not left
            succ, succ_parent, succ_side = get_inorder_successor(target)
            logger.debug(f"{succ=} {succ_parent=} {succ_side=}, {succ.right=}")

            # successor to take over the target's children
            succ.left = target.left
            right_most = succ  # right-most of successor
            logger.debug(f"{right_most=}, {right_most.right=}")
            while right_most.right is not None:
                right_most = right_most.right
                logger.debug(f"{right_most=}, {right_most.right=}")
            right_most.right = target.right
            logger.debug(
                f"After fixing the right_most.right, {succ=}, {succ.right=}, {right_most=}, {right_most.right=}"
            )

            # disconnect the link between successor and its parent
            setattr(succ_parent, succ_side, None)

            # fix up the link to the target node
            setattr(parent, side, succ)

            logger.debug(f"{parent=}")
            logger.debug(f"{root=}")
            logger.debug(f"{target=}")
            logger.debug(f"{succ=}")
            logger.debug(f"{succ_parent=}")

        return parent_of_root.left
