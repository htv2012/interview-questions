#!/usr/bin/env python3
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0
        bound = len(nums)

        while right < bound:
            # Number of duplicate elements
            count = 1
            while right + 1 < bound and nums[right] == nums[right + 1]:
                count += 1
                right += 1

            # Copy at most 2 elements
            for _ in range(min(2, count)):
                nums[left] = nums[right]
                left += 1

            right += 1

        return left
