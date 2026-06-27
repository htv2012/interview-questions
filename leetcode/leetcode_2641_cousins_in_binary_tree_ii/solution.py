import collections
from typing import Optional

from tree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def bfs(root: Optional[TreeNode]):
    que = collections.deque()  # queue of (node, parent, level)
    que.append((root, None, 0))

    while que:
        node, parent, level = que.popleft()
        if node is None:
            continue

        yield node, parent, level

        que.append((node.left, node, level + 1))
        que.append((node.right, node, level + 1))


def children_values(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    out = 0
    if root.left:
        out += root.left.val
    if root.right:
        out += root.right.val
    return out


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sum = collections.Counter()
        sibblings_sum = {}  # {node: sum for the sibbling and me}

        for node, parent, level in bfs(root):
            if level == 0:
                continue
            level_sum[level] += node.val
            sibblings_sum[node] = children_values(parent)

        for node, _, level in bfs(root):
            if level == 0:
                node.val = 0

            node.val = level_sum[level] - sibblings_sum[node]

        return root
