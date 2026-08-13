import bisect
import logging

logger = logging.getLogger()


def is_overlapped(interval1, interval2):
    return not (interval1[1] < interval2[0] or interval2[1] < interval1[0])


class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        logger.debug("------------------------------------------------------------")
        # Find the insertion point
        logger.debug(f"{intervals=}")
        logger.debug(f"{newInterval=}")
        ip = bisect.bisect(intervals, newInterval[0], key=lambda x: x[0])
        logger.debug(f"insertion point, {ip=}")
        intervals.insert(ip, newInterval)
        logger.debug(f"{intervals=}")

        # Search left
        left = ip
        while left > 0 and is_overlapped(intervals[left - 1], newInterval):
            left -= 1

        # Search right
        right = left
        while right < len(intervals) and is_overlapped(intervals[right], newInterval):
            right += 1

        # Replace
        segment = intervals[left:right]
        logger.debug(f"Replace indices [{left}, {right}]: {segment}")

        start = min(i[0] for i in segment)
        end = max(i[1] for i in segment)
        merged = [start, end]
        logger.debug(f"{merged=}")

        intervals[left:right] = [merged]
        logger.debug(f"after replacement: {intervals=}")
        return intervals
