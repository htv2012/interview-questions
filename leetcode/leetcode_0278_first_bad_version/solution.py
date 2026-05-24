import json
import logging


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    with open("/tmp/bad.json") as stream:
        bad_version = json.load(stream)
    return version <= bad_version


def binary_search(lower: int, upper: int) -> int:
    logging.debug(f"{lower=}, {upper=}")
    if lower == upper and isBadVersion(lower):
        return lower
    elif lower > upper:
        raise ValueError(f"{lower=}, {upper=}")

    mid = (lower + upper) // 2
    if isBadVersion(mid):
        return binary_search(lower, mid)
    else:
        return binary_search(mid, upper)


def first_bad_version(n: int) -> int:
    """Binary search for the bad version"""
    return binary_search(1, n)


class Solution:
    def firstBadVersion(self, n: int) -> int:
        return first_bad_version(n)
