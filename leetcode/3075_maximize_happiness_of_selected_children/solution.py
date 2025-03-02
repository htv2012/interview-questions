import heapq
from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        """
        Algorithm:
        1. Sort the array, due to large size, use heapq instead of sort()
        2. Get the largest n elements
        3. For each element, subtract: 0 for the first, 1 for second, 2 for the third, ...
        4. Sum up
        """
        heapq.heapify(happiness)
        selected = heapq.nlargest(k, happiness)
        out = sum(max(value - index, 0) for index, value in enumerate(selected))
        return out
