# https://leetcode.com/problems/path-sum/

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
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        return [path for path in all_paths(root) if sum(path) == targetSum]
