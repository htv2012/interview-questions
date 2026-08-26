NULL = "#"


def is_valid(tokens: list[str]) -> bool:
    stack = []
    for token in tokens:
        stack.append(token)
        while (
            len(stack) > 2
            and stack[-1] == NULL
            and stack[-2] == NULL
            and stack[-3] != NULL
        ):
            stack[-3:] = [NULL]

    return stack == [NULL]


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        tokens = preorder.split(",")
        return is_valid(tokens)
