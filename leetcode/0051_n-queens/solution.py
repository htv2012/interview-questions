import io
from typing import List

EMPTY = "."
QUEEN = "Q"


class Board:
    def __init__(self, size: int):
        self.size = size
        self.data = [[EMPTY for _ in range(size)] for _ in range(size)]

    def __repr__(self):
        return f"{self.__class__.__name__}(" f"size={self.size!r}" f")"

    def __str__(self):
        buffer = io.StringIO()
        top_line = "┌" + ("───┬" * len(self.data[0]))
        top_line = top_line[:-1] + "┐\n"
        mid_line = "├" + ("───┼" * len(self.data[0]))
        mid_line = mid_line[:-1] + "┤\n"
        bottom_line = "└" + ("───┴" * len(self.data[0]))
        bottom_line = bottom_line[:-1] + "┘\n"

        buffer.write(top_line)
        for row_number, row in enumerate(self.data):
            row_str = "│ " + " │ ".join(row) + " │\n"
            buffer.write(row_str)
            if row_number < len(self.data) - 1:
                buffer.write(mid_line)
        buffer.write(bottom_line)

        return buffer.getvalue()

    def __iter__(self):
        for row_index, row in enumerate(self.data):
            for col_index, _ in enumerate(row):
                yield row_index, col_index

    def __getitem__(self, key):
        row, col = key
        return self.data[row][col]

    def __setitem__(self, key, value):
        row, col = key
        self.data[row][col] = value

    def reach(self, row_index: int, col_index: int):
        for row, col in self:
            # Skip itself
            if row == row_index and col == col_index:
                continue

            # Vertical and horizontal
            if row == row_index or col == col_index:
                yield self[row, col]

            # Diagonal
            if abs(row - row_index) == abs(col - col_index):
                yield self[row, col]


def solve(board: Board):
    for row_index, col_index in board:
        if board[row_index, col_index] != EMPTY:
            continue

        if QUEEN in board.reach(row_index, col_index):
            continue

        board[row_index, col_index] = QUEEN


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        out = ""
        return out
