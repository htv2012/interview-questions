import logging
import string

logger = logging.getLogger("solution")

INVALID_FIRST_CHARS = set("-!,.")
HYPHEN = "-"
VALID_CHARS = set(string.ascii_lowercase + "-!,.")
PUNCTUATIONS = set("!,.")


def is_valid(word: str):
    # breakpoint()
    # Check: At most one hypen and it must be sourrounded by lowercase characters
    hypen_count = word.count(HYPHEN)
    if hypen_count > 1:
        logger.debug(f"Too many hypens: {word!r}")
        return 0
    elif hypen_count == 1:
        try:
            i = word.index(HYPHEN)
            assert (
                word[i - 1] in string.ascii_lowercase
                and word[i + 1] in string.ascii_lowercase
            )
        except (AssertionError, IndexError):
            logger.debug(f"Hypen not surrounded by lower case letter: {word!r}")
            return 0

    punctuations_count = 0
    last_index = len(word) - 1
    valid = 1

    for i, ch in enumerate(word):
        valid = 0
        if ch not in VALID_CHARS:
            logger.debug(f"Not a valid char: {ch!r}")
            break

        if i == 0 and i != last_index and ch in INVALID_FIRST_CHARS:
            logger.debug(f"Not a valid first char: {ch!r}")
            break

        if ch in PUNCTUATIONS:
            if i != last_index:
                logger.debug(f"Punctuation not at the end of word: {word!r}")
                break
            punctuations_count += 1
            if punctuations_count > 1:
                logger.debug(f"Too many punctuations, {punctuations_count=}, {i=}")
                break

        valid = 1

    logger.debug(f"{word = }, {valid = }")
    return valid


class Solution:
    def countValidWords(self, sentence: str) -> int:
        is_valid_count = sum(is_valid(token) for token in sentence.split())
        logger.debug(f"{sentence = }, {is_valid_count = }")
        return is_valid_count
