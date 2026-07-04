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


def inorder_iter(root: Optional[TreeNode], parent: Optional[TreeNode] = None):
    if root is None:
        return

    yield from inorder_iter(root.left, root)
    yield root, parent
    yield from inorder_iter(root.right, root)


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        # TODO: case delete root

        it = inorder_iter(root)
        for node, parent in it:
            logger.debug(f"{node=}, {parent=}")
            if node.val == key:
                # Found it. Is it a leaf node?
                if node.left is None and node.right is None:
                    if node is root:
                        return None
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                    return root

                successor, successor_parent = next(it)
                logger.debug(f"{successor=}, {successor_parent=}")

                # Remove the successor
                if successor_parent.left is successor:
                    successor_parent.left = None
                else:
                    successor_parent.right = None

                # Remove the node
                if parent.left is node:
                    parent.left = successor
                else:
                    parent.right = successor

            # TODO: Return new root
        logger.debug(f"{key=} is not found in {root=}")
