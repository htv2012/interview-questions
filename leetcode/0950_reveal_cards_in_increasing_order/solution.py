import heapq
from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        heapq.heapify(deck)
        size = len(deck)
        idx = deque(range(size))
        out = size * [None]

        while idx:
            index = idx.popleft()
            out[index] = heapq.heappop(deck)
            idx.rotate(-1)

        return out
