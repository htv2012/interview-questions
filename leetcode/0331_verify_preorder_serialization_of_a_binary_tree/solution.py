import collections


def validate(stream: collections.deque):
    value = stream.popleft()
    if value == "#":
        return

    left = stream.popleft()
    if left != "#":
        stream.appendleft(left)
        validate(stream)

    right = stream.popleft()
    if right != "#":
        stream.appendleft(right)
        validate(stream)


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        tokens = collections.deque(preorder.split(","))
        stack = [[]]
        while tokens:
            value = tokens.popleft()
            if value == "#":
                break
            stack.push(("value"))
