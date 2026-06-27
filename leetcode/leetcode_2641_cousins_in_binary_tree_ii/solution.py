import collections
from typing import Optional

from tree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def children_values(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    out = 0
    if root.left:
        out += root.left.val
    if root.right:
        out += root.right.val
    return out


def dfs(root: Optional[TreeNode]):
    stack = collections.deque()  # queue of (node, parent, level)
    stack.append((root, None, 0))
    done = {None}  # is this node processed?

    while stack:
        node, parent, level = stack.pop()
        if node in done:
            continue

        if node.left in done and node.right in done:
            yield node, parent, level
            done.add(node)
        else:
            stack.append((node, parent, level))
            stack.append((node.right, node, level + 1))
            stack.append((node.left, node, level + 1))


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sum = collections.Counter()
        sibblings_sum = {}  # {node: sum of my sibbling's value and mine}

        for node, parent, level in dfs(root):
            level_sum[level] += node.val
            sibblings_sum[node] = children_values(parent)

        for node, _, level in dfs(root):
            if level == 0:
                node.val = 0
            else:
                node.val = level_sum[level] - sibblings_sum[node]

        return root
