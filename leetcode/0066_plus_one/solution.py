#!/usr/bin/env python3
# https://leetcode.com/problems/plus-one/description/
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        out = []

        for digit in reversed(digits):
            carry, digit = divmod(carry + digit, 10)
            out.insert(0, digit)

        if carry:
            out.insert(0, carry)
        return out
