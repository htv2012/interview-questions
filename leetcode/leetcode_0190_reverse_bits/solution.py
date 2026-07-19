class Solution:
    def reverseBits(self, n: int) -> int:
        bin_str = f"{n:032b}"
        rev_str = bin_str[::-1]
        out = int(rev_str, 2)
        return out
