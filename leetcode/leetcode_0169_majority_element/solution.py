from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter = Counter(nums)
        element, _ = counter.most_common(1)[0]
        return element
