from typing import List, Optional

from tree import TreeNode


def find_frequent_tree_sum(root: Optional[TreeNode], freq: dict):
    if root is None:
        return 0

    tree_sum = (
        root.val
        + find_frequent_tree_sum(root.left, freq)
        + find_frequent_tree_sum(root.right, freq)
    )
    freq.setdefault(tree_sum, 0)
    freq[tree_sum] += 1
    return tree_sum


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = {}
        find_frequent_tree_sum(root, freq)

        # TODO: Not done yet
        most_frequent = max(freq.values())
        return [k for k, v in freq.items() if v == most_frequent]
