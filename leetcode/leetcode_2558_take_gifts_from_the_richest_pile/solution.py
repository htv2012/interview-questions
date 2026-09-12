import math


class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        for _ in range(k):
            largest = max(gifts)
            i = gifts.index(largest)
            gifts[i] = math.floor(math.sqrt(gifts[i]))

        return sum(gifts)
