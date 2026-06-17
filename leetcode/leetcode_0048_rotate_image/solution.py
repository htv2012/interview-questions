from typing import List


def move(matrix: List[List[int]], row: int, col: int, value: int, size: int):
    new_row = col
    new_col = size - row
    hold = matrix[new_row][new_col]
    matrix[new_row][new_col] = value
    return new_row, new_col, hold


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix[0]) - 1
        already_moved = set()

        for row, row_obj in enumerate(matrix):
            for col, value in enumerate(row_obj):
                if (row, col) in already_moved:
                    continue

                for _ in range(4):
                    row, col, value = move(matrix, row, col, value, size)
                    already_moved.add((row, col))
