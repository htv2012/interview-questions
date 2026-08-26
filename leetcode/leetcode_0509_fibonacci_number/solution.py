cache = {0: 0, 1: 1}


class Solution:
    def fib(self, n: int) -> int:
        try:
            return cache[n]
        except KeyError:
            pass

        out = self.fib(n - 1) + self.fib(n - 2)
        cache[n] = out
        return out
