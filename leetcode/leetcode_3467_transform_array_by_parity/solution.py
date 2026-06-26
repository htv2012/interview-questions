import logging
from typing import List

logger = logging.getLogger()


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        # count even numbers
        odd_count = sum(num % 2 for num in nums)
        even_count = len(nums) - odd_count
        logger.debug(f"{nums=}, {even_count=}, {odd_count=}")
        for i, _ in enumerate(nums):
            nums[i] = int(i >= even_count)

        return nums
