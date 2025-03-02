#!/usr/bin/env python3
# https://leetcode.com/problems/rle-iterator/description/
from typing import List


class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.it = self.decode(encoding)

    def decode(self, encoding):
        while encoding:
            count = encoding.pop(0)
            value = encoding.pop(0)
            for _ in range(count):
                yield value

    def next(self, n: int) -> int:
        value = None
        for _ in range(n):
            try:
                value = next(self.it)
            except StopIteration:
                return -1
        return value


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
