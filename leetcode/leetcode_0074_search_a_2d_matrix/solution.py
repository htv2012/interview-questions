import logging
from typing import List

logger = logging.getLogger()


def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
        else:
            break
    return mid


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search to pinpoint which row might contain target
        row_index = binary_search([r[0] for r in matrix], target)
        if matrix[row_index][0] == target:
            return True
        elif matrix[row_index][0] > target:
            row_index -= 1
        logger.debug(f"{row_index=}")

        # binary search the row to find the target
        col_index = binary_search(matrix[row_index], target)
        logger.debug(f"{col_index=}")
        return matrix[row_index][col_index] == target
