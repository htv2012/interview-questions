#!/usr/bin/env python3
# https://leetcode.com/problems/mini-parser/description/

from nested_integer import NestedInteger


def tokenize(text: str) -> list:
    buf = ""
    for letter in text:
        if letter == ",":
            if buf:
                yield int(buf)
            buf = ""
        elif letter == "[":
            yield letter
        elif letter == "]":
            if buf:
                yield int(buf)
            buf = ""
            yield letter
        elif letter.isdigit():
            buf += letter
        elif letter == "-":
            buf += letter
        else:
            raise ValueError(f"Unknown char: {letter!r}")

    if buf:
        yield int(buf)


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = [NestedInteger()]
        for token in tokenize(s):
            if token == "[":
                new_list = NestedInteger()
                stack[-1].add(new_list)
                stack.append(new_list)
            elif token == "]":
                stack.pop()
            else:
                stack[-1].add(NestedInteger(token))

        dummy_list = stack[-1].getList()
        return dummy_list[0]
