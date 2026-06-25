import logging
import string

logger = logging.getLogger()


BASE = len(string.ascii_uppercase)


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        logger.debug(f"{columnNumber=}")
        letter = dict(zip(range(BASE), string.ascii_uppercase))
        stack = []

        while columnNumber > 0:
            columnNumber -= 1
            logger.debug(f"{columnNumber=}  # subtract 1 for zero-base look up")

            columnNumber, remainder = divmod(columnNumber, BASE)
            stack.append(letter[remainder])
            logger.debug(f"{columnNumber=}, {remainder=}, {stack=}")

        out = "".join(reversed(stack))
        logger.debug(f"{out=}")
        return out


#
# Just for fun, a function to do the reverse
#
def title_to_number(title: str) -> int:
    title = title.upper()
    num = dict(zip(string.ascii_uppercase, range(BASE)))
    out = 0

    for ch in title:
        out = (out * BASE) + num[ch] + 1
    return out
