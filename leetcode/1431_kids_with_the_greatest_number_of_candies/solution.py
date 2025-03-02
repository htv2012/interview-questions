from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        original_max = max(candies)
        result = [count + extraCandies >= original_max for count in candies]
        return result
