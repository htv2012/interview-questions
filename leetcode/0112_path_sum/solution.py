#!/usr/bin/env python3
# https://leetcode.com/problems/path-sum/
from typing import Optional

from tree import TreeNode


def all_paths(root, path=None):
    if root is None:
        return

    path = (path or []) + [root.val]

    if root.left is None and root.right is None:
        yield path

    yield from all_paths(root.left, path)
    yield from all_paths(root.right, path)


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return any(sum(path) == targetSum for path in all_paths(root))
