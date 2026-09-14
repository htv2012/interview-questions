from collections import Counter


class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        out = []
        changed.sort()
        double = Counter()

        for value in changed:
            if double[value] > 0:
                double[value] -= 1
            else:
                out.append(value)
                double[value * 2] += 1

        if double.total() == 0:
            return out
        return []
