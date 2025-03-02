import itertools
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = []
        for i in range(numRows):
            if i == 0:
                out.append([1])
            elif i == 1:
                out.append([1, 1])
            else:
                row = [1] + [a + b for a, b in itertools.pairwise(out[-1])] + [1]
                out.append(row)
        return out
