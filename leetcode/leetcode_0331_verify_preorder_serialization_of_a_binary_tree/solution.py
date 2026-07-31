import logging

logger = logging.getLogger()


NULL = "#"


def is_valid(tokens: list[str]) -> bool:
    logger.debug(f"is_valid({tokens})")
    if tokens == [NULL]:
        return True
    elif len(tokens) == 2:
        return False

    que = []
    for token in tokens:
        que.append(token)
        logger.debug(f"{que=}")
        if len(que) > 2 and que[-1] == NULL and que[-2] == NULL and que[-3] != NULL:
            logger.debug(f"Leaf found: {que}")
            que[-3:] = [NULL]
            logger.debug(f"  que becomes {que}")

    return is_valid(que)


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        tokens = preorder.split(",")
        return is_valid(tokens)
