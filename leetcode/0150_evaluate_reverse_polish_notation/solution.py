#!/usr/bin/env python3
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
import operator
from typing import List


def div(left, right):
    """truediv and floordiv cannot do what this does"""
    result = left / right
    return int(result)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        binary_operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": div,
        }

        stack = []
        for token in tokens:
            binop = binary_operators.get(token)
            if binop is not None:
                right = stack.pop()
                left = stack.pop()
                result = binop(left, right)
                stack.append(result)
            else:
                result = int(token)
                stack.append(result)

        result = stack.pop()
        return result
