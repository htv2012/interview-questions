# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from tree import TreeNode


def max_depth(root: TreeNode | None, depth=0):
    if root is None:
        return depth
    left_depth = max_depth(root.left, depth=depth + 1)
    right_depth = max_depth(root.right, depth=depth + 1)
    return max(left_depth, right_depth)


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        return max_depth(root)
