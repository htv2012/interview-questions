import functools


@functools.cache
def digit_mul(num: tuple[int], digit: int):
    if digit == 0:
        return 0
    total = 0
    factor = 1
    for digit2 in num:
        total += factor * digit * digit2
        factor *= 10

    return total


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = tuple(int(d) for d in reversed(num1))
        total = 0
        factor = 1
        for digit in reversed(num2):
            total += factor * digit_mul(num1, int(digit))
            factor *= 10

        return str(total)
