import logging


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    raise NotImplementedError("To be supplied by leetcode")


def binary_search(lower: int, upper: int) -> int:
    if lower == upper:
        if isBadVersion(lower):
            return lower
        return -1

    mid = (lower + upper) // 2
    is_bad = isBadVersion(mid)
    logging.debug(f"{lower=}, {upper=}, {mid=}, {is_bad=}")

    if is_bad:
        return binary_search(lower, mid)
    else:
        return binary_search(mid + 1, upper)


def first_bad_version(n: int) -> int:
    """Binary search for the bad version"""
    return binary_search(1, n)


class Solution:
    def firstBadVersion(self, n: int) -> int:
        return first_bad_version(n)
