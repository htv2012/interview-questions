class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        return sorted(range(1, n + 1), key=str)
