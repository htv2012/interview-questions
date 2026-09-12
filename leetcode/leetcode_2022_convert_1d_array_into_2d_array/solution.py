class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if n * m != len(original):
            return []

        it = iter(original)
        return [[next(it) for _col in range(n)] for _row in range(m)]
