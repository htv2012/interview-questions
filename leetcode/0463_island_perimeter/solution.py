from typing import List


def count_land_neighbors(g: list[list[int]], row, col):
    count = 0
    if row > 0:
        count += g[row - 1][col]  # North
    if col > 0:
        count += g[row][col - 1]  # West
    if col < len(g[0]) - 1:
        count += g[row][col + 1]  # East
    if row < len(g) - 1:
        count += g[row + 1][col]  # South
    return count


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        for row_index, row in enumerate(grid):
            for col_index, cell in enumerate(row):
                if cell == 0:
                    continue
                perimeter += 4
                perimeter -= count_land_neighbors(grid, row_index, col_index)

        return perimeter
