"""
Intermediate values


old | new | code
--- | --- | ---
  0 |   0 | 100
  0 |   1 | 101
  1 |   0 | 110
  1 |   1 | 111
"""

import logging

logger = logging.getLogger("solution")

# from intermediate to old value
i2o = {0: 0, 1: 1, 100: 0, 101: 0, 110: 1, 111: 1}

# from intermediate to new value
i2n = {100: 0, 101: 1, 110: 0, 111: 1}


def count_live_neighbors(board: list[list[int]], row: int, col: int):
    live_count = 0

    for r in range(row - 1, row + 2):
        if not (0 <= r < len(board)):
            continue

        for c in range(col - 1, col + 2):
            if not (0 <= c < len(board[row])):
                continue
            if r == row and c == col:
                continue

            old_value = board[r][c]
            old_value = i2o[old_value]
            live_count += old_value

    return live_count


def log_board(board, msg: str):
    logger.info(msg)
    for row in board:
        logger.info("  " + (" ".join(str(cell) for cell in row)))


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        log_board(board, "Original Board")
        # Calculate the new lives
        for row, row_obj in enumerate(board):
            for col, cell in enumerate(row_obj):
                old = i2o[cell]
                live_count = count_live_neighbors(board, row, col)
                logger.debug(f"[{row}, {col}] {cell} -> {old}, {live_count=}")
                if old == 1:
                    if count_live_neighbors(board, row, col) in {2, 3}:
                        board[row][col] = 111
                    else:
                        board[row][col] = 110
                elif old == 0:
                    if count_live_neighbors(board, row, col) == 3:
                        board[row][col] = 101
                    else:
                        board[row][col] = 100

        log_board(board, "Intermediate Board")

        # Translate from intermediate to new values
        for row, row_obj in enumerate(board):
            for col, cell in enumerate(row_obj):
                board[row][col] = i2n[cell]

        log_board(board, "Final Board")
