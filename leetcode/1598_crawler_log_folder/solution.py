from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for name in logs:
            if name == "../":
                depth = max(0, depth - 1)
            elif name == "./":
                pass
            else:
                depth += 1
        return depth
