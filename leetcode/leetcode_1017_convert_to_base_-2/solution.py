import collections


class Solution:
    def baseNeg2(self, n: int) -> str:
        out = collections.deque()

        while n != 0:
            out.appendleft(str(n & 1))
            n = -(n >> 1)

        return "".join(out) if out else "0"
