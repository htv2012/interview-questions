#!/usr/bin/env python3
# https://leetcode.com/problems/valid-sudoku/description/
import logging
from typing import List


def iter_board(board: List[List[str]]):
    # Rows
    for row_number, row_number in enumerate(board):
        yield row_number, f"Row {row_number}"

    # Columns
    for col_number in range(9):
        yield [row[col_number] for row in board], f"Column {col_number}"

    # Grids
    for row_number in [0, 3, 6]:
        for col_number in [0, 3, 6]:
            grid = [
                board[row_number + r][col_number + c]
                for r in range(3)
                for c in range(3)
            ]
            yield grid, f"Grid {row_number}, {col_number}"


def valid(seq, label):
    seen = set()
    for value in seq:
        if not (value == "." or ("0" <= value <= "9")):
            logging.debug("%s: Invalid value from %r", label, seq)
            return False
        if value in seen and value != ".":
            logging.debug("%s: Duplicate value %r from %r", label, value, seq)
            return False
        seen.add(value)
    return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return all(valid(*group) for group in iter_board(board))
