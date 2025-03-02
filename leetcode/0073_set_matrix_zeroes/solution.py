from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Record where the original zeros are
        rows = set()
        cols = set()
        for row_index, row in enumerate(matrix):
            for col_index, cell in enumerate(row):
                if cell == 0:
                    rows.add(row_index)
                    cols.add(col_index)

        # Place zeros in rows
        for row_index in rows:
            for col_index, _ in enumerate(matrix[row_index]):
                matrix[row_index][col_index] = 0

        # Place zeros in columns
        for col_index in cols:
            for row in matrix:
                row[col_index] = 0
