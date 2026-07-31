import logging

logger = logging.getLogger()


NULL = "#"


def is_valid(tokens: list[str]) -> bool:
    logger.debug(f"is_valid({tokens})")

    stack = []
    for token in tokens:
        stack.append(token)
        logger.debug(f"{stack=}")
        while (
            len(stack) > 2
            and stack[-1] == NULL
            and stack[-2] == NULL
            and stack[-3] != NULL
        ):
            logger.debug(f"Leaf found: {stack}")
            stack[-3:] = [NULL]
            logger.debug(f"  stack becomes {stack}")

    return stack == [NULL]


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        tokens = preorder.split(",")
        return is_valid(tokens)
