def next_n(n: int):
    new_n = 0
    while n > 0:
        n, remainder = divmod(n, 10)
        new_n += remainder * remainder
    return new_n


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            m = next_n(n)
            if m == 1:
                return True
            seen.add(n)
            n = m
        return False
