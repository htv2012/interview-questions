#!/usr/bin/env python3
# https://leetcode.com/problems/sudoku-solver/
from typing import List

EMPTY = "."
DIGITS = "123456789"
b = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

b = [
    [".", "2", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "6", ".", ".", ".", ".", "3"],
    [".", "7", "4", ".", "8", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "2"],
    [".", "8", ".", ".", "4", ".", ".", "1", "."],
    ["6", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "1", ".", "7", "8", "."],
    ["5", ".", ".", ".", ".", "9", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "4", "."],
]


def neighbors(row, col):
    for row2 in range(9):
        if row2 != row:
            yield row2, col

    for col2 in range(9):
        if col2 != col:
            yield row, col2

    base_row = row // 3 * 3
    base_col = col // 3 * 3
    for row_offset in range(3):
        row2 = base_row + row_offset
        for col_offset in range(3):
            col2 = base_col + col_offset
            if (row2, col2) != (row, col):
                yield row2, col2


def conflicted(board, row, col, candidate):
    for r, c in neighbors(row, col):
        if board[r][c] == candidate:
            return True
    return False


def solve(board) -> bool:
    for row in range(9):
        for col in range(9):
            if board[row][col] != EMPTY:
                continue
            for candidate in DIGITS:
                if conflicted(board, row, col, candidate):
                    continue
                board[row][col] = candidate
                if solve(board):
                    return True
                board[row][col] = EMPTY
            # None of the candidates fits, puzzle is not solvable
            return False
    # No more empty cells: solved
    return True


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        return solve(board)
