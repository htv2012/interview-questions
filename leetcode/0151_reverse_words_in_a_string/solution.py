import logging

logger = logging.getLogger()


def easy_solution(text: str) -> str:
    return " ".join(word[::-1] for word in text[::-1].split())


def hard_solution(text: str) -> str:
    """For those languages that do not enjoy Python's advantages"""
    out = []
    word = ""
    for c in text:
        if c != " ":
            word = f"{c}{word}"
        elif word:
            if out:
                out.append(" ")
            logger.debug("word=%r", word)
            logger.debug("out=%r", out)
            out.extend(word)
            word = ""
    if word:
        if out:
            out.append(" ")
        out.extend(word)
    logger.debug("final out=%r", out)

    result = ""
    while out:
        result += out.pop()
    return result


class Solution:
    def reverseWords(self, s: str) -> str:
        # return easy_solution(s)
        return hard_solution(s)
