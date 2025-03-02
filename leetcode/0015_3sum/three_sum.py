#!/usr/bin/env python3
from itertools import combinations
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set(
            tuple(sorted(triplet))
            for triplet in combinations(nums, 3)
            if sum(triplet) == 0
        )
        out = [list(x) for x in out]
        return out
