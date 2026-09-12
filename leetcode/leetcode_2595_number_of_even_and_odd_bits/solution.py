class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        out = [0, 0]
        i = 0

        while n != 0:
            out[i] += n & 1
            n >>= 1
            i = 1 - i

        return out
