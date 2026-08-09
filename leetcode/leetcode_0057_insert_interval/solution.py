import bisect
import logging

logger = logging.getLogger()


def is_overlapped(interval1, interval2):
    return not (interval1[1] < interval2[0] or interval2[1] < interval1[0])


class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        # Find the insertion point
        ip = bisect.bisect(intervals, newInterval[0], key=lambda x: x[0])

        # Search left
        left = ip
        while left > 0 and is_overlapped(intervals[left - 1], newInterval):
            left -= 1

        # Search right
        right = left
        while right < len(intervals) and is_overlapped(intervals[right], newInterval):
            right += 1
        right = max(right - 1, 0)

        logger.debug(f"{intervals=}")
        logger.debug(f"{newInterval=}")
        logger.debug(f"Replace indices [{left}, {right}]: {intervals[left:right]}")
        return f"{left}, {ip}, {right}"
        # Replace
        # Return
