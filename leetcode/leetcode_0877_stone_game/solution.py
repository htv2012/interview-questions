class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        def play(left, right):
            if left == right:
                return piles[left]
            elif left + 1 == right:
                return max(piles[left], piles[right])
            else:
                path1 = (
                    piles[left]
                    + sum(piles[left + 1 : right + 1])
                    - play(left + 1, right)
                )
                path2 = piles[right] + sum(piles[left:right]) - play(left, right - 1)
                return max(path1, path2)

        threshold = sum(piles) // 2
        return play(0, len(piles) - 1) > threshold
