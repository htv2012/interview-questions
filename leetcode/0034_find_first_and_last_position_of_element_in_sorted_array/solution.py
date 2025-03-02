import logging
from typing import List


def find_target(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def find_first(nums, target, left, right):
    while left < right:
        mid = (left + right) // 2
        logging.debug(
            "nums=%r, target=%r, left=%r, mid=%r, right=%r",
            nums,
            target,
            left,
            mid,
            right,
        )
        if nums[mid] == target:
            right = mid
        else:
            left = mid + 1
    return right


def find_last(nums, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        logging.debug("find_last: left=%r, mid=%r, right=%r", left, mid, right)
        if nums[mid] == target:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1


def search_range(nums: list[int], target: int, left: int, right: int) -> list:
    mid = find_target(nums, target)
    if mid == -1:
        return [-1, -1]
    first = find_first(nums, target, left, mid)
    last = find_last(nums, target, mid, right)
    return [first, last]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return search_range(nums, target, left=0, right=len(nums) - 1)
