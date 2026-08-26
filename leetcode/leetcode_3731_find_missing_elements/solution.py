class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        smallest = min(nums)
        largest = max(nums)
        all_values = set(range(smallest, largest + 1))
        presence = set(nums)
        missing = all_values - presence
        missing = sorted(missing)
        return missing
