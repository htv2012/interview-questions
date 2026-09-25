import functools


class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        @functools.cache
        def play(left, right):
            if left >= right:
                return 0

            left_score = piles[left] - play(left + 1, right)
            right_score = piles[right] - play(left, right - 1)
            return max(left_score, right_score)

        return play(0, len(piles) - 1) > 0
