from typing import List

EMPTY = "."
SHIP = "X"


def count_ship(board: List[List[str]], row_index: int, col_index: int) -> int:
    if board[row_index][col_index] == EMPTY:
        return 0

    board[row_index][col_index] = EMPTY
    for col in range(col_index + 1, len(board[0])):
        if board[row_index][col] == EMPTY:
            break
        board[row_index][col] = EMPTY
    for row in range(row_index + 1, len(board)):
        if board[row][col_index] == EMPTY:
            break
        board[row][col_index] = EMPTY

    return 1


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for row_index, row in enumerate(board):
            for col_index, _ in enumerate(row):
                count += count_ship(board, row_index, col_index)
        return count
