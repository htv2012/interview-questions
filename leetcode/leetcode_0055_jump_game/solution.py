# https://leetcode.com/problems/jump-game/description/


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        target = len(nums) - 1
        furthest = 0
        for index, reach in enumerate(nums):
            if furthest >= target:
                break
            if furthest < index:
                return False
            furthest = max(furthest, index + reach)
        return True
