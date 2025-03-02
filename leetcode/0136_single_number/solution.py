from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for number in nums:
            if number in seen:
                seen.discard(number)
            else:
                seen.add(number)
        return seen.pop()
