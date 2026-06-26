import logging
from typing import List

logger = logging.getLogger()


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odd_count = sum(num % 2 for num in nums)
        even_count = len(nums) - odd_count
        logger.debug(f"{nums=}, {even_count=}, {odd_count=}")

        nums[:even_count] = [0] * even_count
        nums[even_count:] = [1] * odd_count

        return nums
