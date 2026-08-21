import functools


@functools.cache
def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


class Solution:
    def tribonacci(self, n: int) -> int:
        return tribonacci(n)
