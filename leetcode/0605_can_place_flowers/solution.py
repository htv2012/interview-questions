from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        bound = len(flowerbed) - 1

        for i, e in enumerate(flowerbed):
            left = 0 if i == 0 else flowerbed[i - 1]
            right = 0 if i == bound else flowerbed[i + 1]
            if (left, e, right) == (0, 0, 0):
                count += 1
                flowerbed[i] = 1
        return count >= n
