from collections import Counter
from fractions import Fraction


class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        count = 0
        seen = Counter()

        for width, height in rectangles:
            ratio = Fraction(width, height)
            count += seen[ratio]
            seen[ratio] += 1

        return count
