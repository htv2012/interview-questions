from itertools import combinations


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out = {
            tuple(sorted(triplet))
            for triplet in combinations(nums, 3)
            if sum(triplet) == 0
        }
        out = [list(x) for x in out]
        return out
