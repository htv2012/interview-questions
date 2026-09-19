import logging
import string

logger = logging.getLogger("solution")

INVALID_FIRST_CHARS = set("-!,.")
DASH = "-"
VALID_CHARS = set(string.ascii_lowercase + "-!,.")
PUNCTUATIONS = set("!,.")


def is_valid(word: str):
    counter = {}
    last_index = len(word) - 1
    for i, ch in enumerate(word):
        valid = 0
        if ch not in VALID_CHARS:
            break

        if i == 0 and ch in INVALID_FIRST_CHARS:
            break

        counter[ch] = counter.setdefault(ch, 0) + 1
        if ch in PUNCTUATIONS and counter[ch] > 1:
            break

        if ch == DASH and (counter[ch] > 1 or i == 0 or i == last_index):
            break

        valid = 1

    logger.debug(f"{word = }, {valid = }")
    return valid


class Solution:
    def countValidWords(self, sentence: str) -> int:
        is_valid_count = sum(is_valid(token) for token in sentence.split())
        logger.debug(f"{sentence = }, {is_valid_count = }")
        return is_valid_count
