#!/usr/bin/env python3
# https://leetcode.com/problems/jump-game/description/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        furthest = 0
        for index, reach in enumerate(nums):
            if furthest >= target:
                break
            if furthest < index:
                return False
            furthest = max(furthest, index + reach)
        return True
