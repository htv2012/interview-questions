import logging

logger = logging.getLogger("solution")


def cap(word: str) -> str:
    out = word.lower() if len(word) <= 2 else word.title()
    logger.debug(f"cap {word!r} -> {out!r}")
    return out


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        start, end = 0, None
        out = []

        while start < len(title):
            try:
                end = title.index(" ", start)
            except ValueError:
                # no more spaces
                end = len(title)
            out.append(cap(title[start:end]))
            while end < len(title) and title[end] == " ":
                out.append(title[end])
                end += 1
            start = end

        logger.debug(f"exit while, {out = }")
        return "".join(out)
