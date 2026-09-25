import functools


class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        @functools.cache
        def play(left, right, total):
            if left == right:
                return piles[left]

            left_score = total - play(left + 1, right, total - piles[left])
            if left_score > threshold:
                return left_score

            right_score = total - play(left, right - 1, total - piles[right])
            if right_score > threshold:
                return right_score

            return max(left_score, right_score)

        max_score = sum(piles)
        threshold = max_score // 2
        return play(0, len(piles) - 1, max_score) > threshold
