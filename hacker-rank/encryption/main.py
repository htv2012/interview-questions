import itertools
import logging
import math

logger = logging.getLogger()


def encryption(s):
    no_space = s.replace(" ", "")
    row_count = math.floor(math.sqrt(len(no_space)))
    col_count = math.ceil(math.sqrt(len(no_space)))
    while row_count * col_count < len(no_space):
        row_count += 1

    it = iter(no_space)
    grid = [list(itertools.islice(it, col_count)) for _ in range(row_count)]
    for row in grid:
        logger.debug(row)

    encrypted_words = [
        "".join(word) for word in itertools.zip_longest(*grid, fillvalue="")
    ]
    logger.debug(f"{encrypted_words=}")
    encrypted_str = " ".join(encrypted_words)

    return encrypted_str
