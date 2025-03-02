#!/usr/bin/env python3
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/?envType=daily-question&envId=2024-04-04
import logging


class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = depth = 0
        for c in s:
            if c == "(":
                depth += 1
                max_depth = max(max_depth, depth)
                logging.debug("Open: depth=%r, max=%r", depth, max_depth)
            elif c == ")":
                depth -= 1
                logging.debug("Close: depth=%r, max=%r", depth, max_depth)
        return max_depth
