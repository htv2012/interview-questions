from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = {0: 0, 1: 0, 2: 0}
        for num in nums:
            counter[num] += 1

        i = 0
        for num, count in counter.items():
            for _ in range(count):
                nums[i] = num
                i += 1
