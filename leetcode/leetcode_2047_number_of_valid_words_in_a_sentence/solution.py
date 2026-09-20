import string

INVALID_FIRST_CHARS = set("-!,.")
HYPHEN = "-"
VALID_CHARS = set(string.ascii_lowercase + "-!,.")
PUNCTUATIONS = set("!,.")


def is_valid(word: str):
    last_index = len(word) - 1
    hypen_count = word.count(HYPHEN)

    # Check: At most one hypen and it must be sourrounded by lowercase characters
    if hypen_count > 1:
        return 0
    elif hypen_count == 1:
        i = word.index(HYPHEN)
        if (
            i == 0
            or i == last_index
            or word[i - 1] not in string.ascii_lowercase
            or word[i + 1] not in string.ascii_lowercase
        ):
            return 0

    # Check: Punctuations
    punctuations_count = 0

    for i, ch in enumerate(word):
        valid = 0
        if ch not in VALID_CHARS:
            break

        if i == 0 and i != last_index and ch in INVALID_FIRST_CHARS:
            break

        if ch in PUNCTUATIONS:
            if i != last_index:
                break
            punctuations_count += 1
            if punctuations_count > 1:
                break

        valid = 1

    return valid


class Solution:
    def countValidWords(self, sentence: str) -> int:
        is_valid_count = sum(is_valid(token) for token in sentence.split())
        return is_valid_count
