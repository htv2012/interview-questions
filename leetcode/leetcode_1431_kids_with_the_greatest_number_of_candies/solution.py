

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        original_max = max(candies)
        result = [count + extraCandies >= original_max for count in candies]
        return result
