from typing import Optional

from tree import TreeNode


def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    left_depth = max_depth(root.left) + 1
    right_depth = max_depth(root.right) + 1
    return max(left_depth, right_depth)


def is_balance(root: Optional[TreeNode], depth: int = 0) -> tuple[bool, int]:
    if root is None:
        return True, depth

    left_balance, left_max_depth = is_balance(root.left, depth + 1)
    right_balance, right_max_depth = is_balance(root.right, depth + 1)
    balance = (
        left_balance and right_balance and abs(left_max_depth - right_max_depth) <= 1
    )
    max_depth = max(left_max_depth, right_max_depth)
    return balance, max_depth


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance, _ = is_balance(root)
        return balance
