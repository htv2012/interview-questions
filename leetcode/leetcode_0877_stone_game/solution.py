import functools


class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        @functools.lru_cache
        def play(left, right, total):
            if left == right:
                return piles[left]
            elif left + 1 == right:
                return max(piles[left], piles[right])
            else:
                path1 = total - play(left + 1, right, total - piles[left])
                if path1 > threshold:
                    return path1
                path2 = total - play(left, right - 1, total - piles[right])
                if path2 > threshold:
                    return path2
                return max(path1, path2)

        max_score = sum(piles)
        threshold = max_score // 2
        return play(0, len(piles) - 1, max_score) > threshold
