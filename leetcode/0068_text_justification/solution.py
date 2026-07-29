import itertools
import logging

logger = logging.getLogger()


def split_lines(words: list, maxWidth: int):
    out = []
    line = []

    for word in words:
        if line:
            line.append(" ")
        line.append(word)
        if len("".join(line)) > maxWidth:
            line.pop()  # Remove last word
            line.pop()  # Remove space
            out.append(line)
            line = [word]
    if line:
        out.append(line)

    logger.debug("out=%r", out)
    logger.debug("line=%r", line)
    return out


def justify_line(line: list, maxWidth: int):
    line = line[:]
    if len(line) == 1:
        spaces_indices = [0]
    else:
        spaces_indices = [index for index, word in enumerate(line) if word == " "]
    logger.debug("line=%r", line)
    logger.debug("spaces_indices=%r", spaces_indices)

    for index in itertools.cycle(spaces_indices):
        line_as_text = "".join(line)
        logger.debug("line_as_text=%r", line_as_text)
        if len(line_as_text) == maxWidth:
            logger.debug("Return %r", line_as_text)
            return line_as_text
        elif len(line_as_text) > maxWidth:
            raise ValueError()
        line[index] += " "


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        lines = split_lines(words, maxWidth)
        out = [justify_line(line, maxWidth) for line in lines]
        out[-1] = "".join(lines[-1]).ljust(maxWidth)
        return out
