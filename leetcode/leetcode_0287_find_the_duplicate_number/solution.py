import logging

logger = logging.getLogger("solution")


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        logger.debug(f"{nums=}")

        # Find meet-up point
        fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            logger.debug(f"{slow=}")
            logger.debug(f"{fast=}")
            if fast == slow:
                logger.debug(f"fast and slow meet at {fast}")
                break

        # Find the entry to the loop, which is the duplicate value
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
            logger.debug(f"{slow=}")
            logger.debug(f"{fast=}")

        logger.debug(f"Entry at {fast}")
        return fast
