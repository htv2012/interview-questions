import itertools
import logging

logger = logging.getLogger("solution")


class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        out = {
            num
            for hun, ten, one in itertools.permutations(digits, 3)
            if one % 2 == 0 and (num := hun * 100 + ten * 10 + one) > 99
        }
        out = sorted(out)
        logger.debug(f"{out = }")
        return out
