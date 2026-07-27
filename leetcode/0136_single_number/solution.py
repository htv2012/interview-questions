class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        seen = set()
        for number in nums:
            if number in seen:
                seen.discard(number)
            else:
                seen.add(number)
        return seen.pop()
