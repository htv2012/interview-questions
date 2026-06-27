import collections
from typing import Optional

from tree import TreeNode


def breadth_first_iter(root: Optional[TreeNode]):
    que = collections.deque()
    que.append((root, 0))
    while que:
        node, level = que.popleft()
        if node is None:
            continue

        yield node, level

        que.append((node.left, level + 1))
        que.append((node.right, level + 1))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parent = {}  # child_value: parent_value
        level = {}  # value: level

        for node, node_level in breadth_first_iter(root):
            if node.left:
                parent[node.left.val] = node.val
            if node.right:
                parent[node.right.val] = node.val

            level[node.val] = node_level
            if x in level and y in level:
                break

        return (level[x] == level[y]) and (parent[x] != parent[y])
