#!/usr/bin/env python3
# https://leetcode.com/problems/simplify-path/description/


class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split("/")
        out = []
        for token in tokens:
            if token == "." or token == "":
                continue
            elif token == "..":
                try:
                    out.pop()
                except IndexError:
                    pass
            else:
                out.append(token)

        return f"/{'/'.join(out)}"
