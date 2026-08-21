# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

from tree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if nums == []:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 :])
        return root
