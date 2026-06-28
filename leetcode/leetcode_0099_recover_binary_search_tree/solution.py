import logging
from typing import Dict, Optional

from tree import TreeNode

logger = logging.getLogger()

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def inorder_iter(root: Optional[TreeNode]):
    if root is None:
        return
    yield from inorder_iter(root.left)
    yield root
    yield from inorder_iter(root.right)


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def process_node(node: Optional[TreeNode]) -> int:
            nonlocal nodes
            nodes[node.val] = node
            return node.val

        nodes: Dict[int, TreeNode] = {}  # {value: node}
        values = [process_node(node) for node in inorder_iter(root)]
        logger.debug("values before fixing: %r", values)

        expected = sorted(values)
        for actual_val, expected_val in zip(values, expected):
            if actual_val != expected_val:
                actual_node = nodes[actual_val]
                expected_node = nodes[expected_val]
                logger.info("Swapping nodes %r and %r", actual_node, expected_node)
                actual_node.val, expected_node.val = expected_node.val, actual_node.val
                break
