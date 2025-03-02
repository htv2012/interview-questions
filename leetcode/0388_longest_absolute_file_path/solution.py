#!/usr/bin/env python3
# https://leetcode.com/problems/longest-absolute-file-path/description/


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        longest = 0

        for entry in input.splitlines():
            level = len(entry) - len(entry := entry.lstrip("\t"))

            while len(stack) <= level:
                stack.append(None)
            stack[level] = entry

            fullpath = "/".join(stack[:level] + [entry])
            if "." in fullpath:
                longest = max(longest, len(fullpath))

        return longest
