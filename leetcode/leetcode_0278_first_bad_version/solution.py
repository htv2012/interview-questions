import logging


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    raise NotImplementedError("To be supplied by leetcode")


def binary_search(lower: int, upper: int) -> int:
    while lower < upper:
        mid = (lower + upper) // 2
        is_bad = isBadVersion(mid)
        logging.debug(f"{lower = :14,} | {upper = :14,} | {mid = :14,} | {is_bad=}")

        if is_bad:
            upper = mid
        else:
            lower = mid + 1

    if isBadVersion(lower):
        logging.debug(f"First bad version is {lower:,}")
        return lower

    msg = "No first bad version found"
    logging.debug(msg)
    raise ValueError(msg)


def first_bad_version(n: int) -> int:
    return binary_search(1, n)


class Solution:
    def firstBadVersion(self, n: int) -> int:
        return first_bad_version(n)
