import itertools
from typing import List



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = itertools.cycle(
            [
                (0, 1),  # go right
                (1, 0),  # go down
                (0, -1),  # go left
                (-1, 0),  # go up
            ]
        )
        row_delta, col_delta = next(directions)
        done = set()
        row_count = len(matrix)
        col_count = len(matrix[0])
        out = []
        row, col = 0, 0

        for _ in range(row_count * col_count):
            # Collect the value and mark this cell as done
            out.append(matrix[row][col])
            done.add((row, col))

            # Advance to the next cell
            new_row, new_col = row + row_delta, col + col_delta
            if (
                (new_row, new_col) in done  # hit a cell that is done
                or not (0 <= new_row < row_count)  # hit a row boundary
                or not (0 <= new_col < col_count)  # hit a col boundary
            ):
                # Change direction
                row_delta, col_delta = next(directions)
                new_row, new_col = row + row_delta, col + col_delta
            row, col = new_row, new_col

        return out
