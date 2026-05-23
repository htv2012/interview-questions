import logging
from typing import List

logger = logging.getLogger()


class Solution:
    def check(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums):
            if i == 0:
                continue
            if i < len(nums) - 1 and num > nums[i + 1]:
                break
        if i == len(nums) - 1:
            return True
        logger.debug(f"{nums=}, {i=}")
        for i in range(i + 1, len(nums)):
            try:
                next_num = nums[i + 1]
            except IndexError:
                next_num = nums[0]
            if nums[i] > next_num:
                return False
        return True
