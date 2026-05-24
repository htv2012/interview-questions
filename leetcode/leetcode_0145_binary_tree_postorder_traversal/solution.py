from typing import List, Optional

from tree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def post_order(root: Optional[TreeNode]) -> List[int]:
    out = []
    stack = [(root, False)]  # [(node, ready)]

    while stack:
        node, ready = stack.pop()
        if node is None:
            continue

        if ready:
            out.append(node.val)
        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))

    return out


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return post_order(root)
