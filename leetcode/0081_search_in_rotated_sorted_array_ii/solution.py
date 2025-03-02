#!/usr/bin/env python3
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
from typing import List


class Solution:
    def search_forward(self, nums: List[int], target: int) -> bool:
        last = nums[0]
        for index in range(1, len(nums)):
            if nums[index] == target:
                return True
            elif nums[index] == last:
                continue

            if not (last < nums[index] < target):
                return False
            last = nums[index]
        return False

    def search_backward(self, nums: List[int], target: int) -> bool:
        last = nums[0]
        for index in range(len(nums) - 1, -1, -1):
            if nums[index] == target:
                return True
            elif nums[index] == last:
                continue

            if not (target < nums[index] < last):
                return False
            last = nums[index]
        return False

    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        if nums[0] == target:
            return True
        elif nums[0] < target:
            return self.search_forward(nums, target)
        else:
            return self.search_backward(nums, target)
