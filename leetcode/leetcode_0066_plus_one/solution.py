# https://leetcode.com/problems/plus-one/description/


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1
        out = []

        for digit in reversed(digits):
            carry, digit = divmod(carry + digit, 10)
            out.insert(0, digit)

        if carry:
            out.insert(0, carry)
        return out
