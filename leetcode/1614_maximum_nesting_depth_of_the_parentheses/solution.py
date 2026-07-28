# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/?envType=daily-question&envId=2024-04-04
import logging

logger = logging.getLogger()


class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = depth = 0
        for c in s:
            if c == "(":
                depth += 1
                max_depth = max(max_depth, depth)
                logger.debug("Open: depth=%r, max=%r", depth, max_depth)
            elif c == ")":
                depth -= 1
                logger.debug("Close: depth=%r, max=%r", depth, max_depth)
        return max_depth
