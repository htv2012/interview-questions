import heapq
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        heapq.heapify(deck)
        size = len(deck)
        idx = deque(range(size))
        out = size * [None]

        while idx:
            index = idx.popleft()
            out[index] = heapq.heappop(deck)
            idx.rotate(-1)

        return out
