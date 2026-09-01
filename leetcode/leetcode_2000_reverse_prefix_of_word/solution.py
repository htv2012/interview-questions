import logging

logger = logging.getLogger("solution")


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Find index of ch
        try:
            ich = word.index(ch) + 1
            logger.debug(f"{ich = }")
        except ValueError:
            logger.debug(f"{ch} not found, return word as is")
            return word

        out = word[:ich][::-1] + word[ich:]
        return out
